from flask import Flask, request, jsonify
from serverDatabase import User, Friendship, ChatGroup, GroupMembers, Message,Database,Operation,OperationType
from flask_socketio import SocketIO
from flask_socketio import join_room,disconnect,close_room,leave_room
import uuid
import base64
import random
from config import ClientEvent,Status,ServerEvent
from sqlalchemy import and_,or_,desc
import os
import logging
import time
logging.basicConfig(level=logging.DEBUG)
IMAGE_PATH = "./avatar"
app = Flask(__name__)
socketio = SocketIO(app,logger=True, engineio_logger=True)
db_url = 'postgresql://vultradmin:AVNS_pdhyuBiAurlhAN8FDQ5@vultr-prod-2b48bc65-37f2-4cee-a7e4-0336fd12066a-vultr-prod-613a.vultrdb.com:16751/defaultdb'
db = Database(db_url)
db.create_table()
class myLoggedDict:
    def __init__(self) -> None:
        self.map1to2 = {}
        self.map2to1 = {}
    def __getitem__(self, key):
        if key in self.map1to2:
            return self.map1to2[key]
        elif key in self.map2to1:
            return self.map2to1[key]
    def __setitem__(self, key, value):
        if key in self.map1to2:
            del self.map2to1[self.map1to2[key]]
        self.map1to2[key] = value
        self.map2to1[value] = key
    def __delitem__(self, key):
        if key in self.map1to2:
            del self.map2to1[self.map1to2[key]]
            del self.map1to2[key]
        elif key in self.map2to1:
            del self.map1to2[self.map2to1[key]]
            del self.map2to1[key]
    def __contains__(self,key):
        return key in self.map1to2 or key in self.map2to1
logged_in_users = {}
logged_in_users_session_id = myLoggedDict()
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    nickname = request.json.get('nickname',"mono")
    if username == "":
        return jsonify({"message":"Username cannot be empty!","status":Status.ERROR.value}), 400
    elif db.query(User,username=username):
        return jsonify({"message":"Username already exists!","status":Status.ERROR.value}), 400
    elif db.insert(User,username=username, password=password, nickname=nickname,avatar="{}.png".format(random.randint(0, 178))):
        return jsonify({"message":"User registered successfully!","status":Status.SUCCESS.value}),200
    else:
        return jsonify({"message":"User registered failed!","status":Status.ERROR.value}),400  
@app.route('/getAvatar', methods=['POST'])
def getAvatar():
    username = request.json.get('username')
    query_username = request.json.get('queryusername')
    session_id = request.json.get('mysessionid')
    print("username:",username,"query_username",query_username,"session_id",session_id)
    print("in memory:",logged_in_users)
    if session_id:
        userid = db.query(User,username=username)[0].id
        if userid in logged_in_users and logged_in_users[userid] == session_id:
            user = db.query(User, username=query_username)[0]
            with open(os.path.join(IMAGE_PATH, user.avatar), 'rb') as f:
                avatar = base64.b64encode(f.read()).decode('utf-8')
            return jsonify({"message":"get Avatar successful!","status":Status.SUCCESS.value,"avatar":avatar}), 200
        else:
            return jsonify({"message":"Invalid session ID!","status":Status.OUTDATED.value}), 401
    else:
        return jsonify({"message":"session ID not provide!","status":Status.ERROR.value}), 404
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    session_id = request.json.get('session_id')
    if session_id:
        userid = db.query(User,username=username)[0].id
        if userid in logged_in_users and logged_in_users[userid] == session_id:
            user = db.query(User, username=username)[0]

            return jsonify({"message":"Login successful!","status":Status.SUCCESS.value, "session_id":session_id,"user_id":user.id,"username":user.username,"nickname":user.nickname,"avatar":avatar}), 200
        else:
            return jsonify({"message":"Invalid session ID!","status":Status.OUTDATED.value}), 401
    # 检查用户名和密码是否为空
    if not username or not password:
        return jsonify({"message":"Username and password cannot be empty!","status":Status.ERROR.value}), 400

    # 查询用户
    user_list = db.query(User, username=username)
    if user_list:
        user = user_list[0]
        if user.verify_password(password):
            session_id = str(uuid.uuid4())
            if user.id in logged_in_users:
                if user.id in logged_in_users_session_id:
                    socketio.emit(ClientEvent.logout.name, {"message":"You have been logged out!","status":Status.SUCCESS.value}, to=logged_in_users_session_id[user.id])
                    disconnect(logged_in_users_session_id[user.id])
                    del logged_in_users_session_id[user.id]
                del logged_in_users[user.id]
            logged_in_users[user.id] = session_id
            with open(os.path.join(IMAGE_PATH, user.avatar), 'rb') as f:
                avatar = base64.b64encode(f.read()).decode('utf-8')
            print("in login:",session_id)
            print("in login memory:",logged_in_users)
            return jsonify({"message":"Login successful!","status":Status.SUCCESS.value, "session_id":session_id,"user_id":user.id,"username":user.username,"nickname":user.nickname,"avatar":avatar}), 200
        else:
            return jsonify({"message":"Invalid credentials!","status":Status.ERROR.value}), 401
    else:
        return jsonify({"message":"User not found!","status":Status.ERROR.value}), 404


@socketio.on('connect')
def connect():
    print("connect")
    username = request.headers.get('username')
    print("get username:",username)
    session_id = request.headers.get('mysessionid')
    print("get session_id:",session_id)
    timestamp = request.headers.get('mytimestamp',0)
    print("get timestamp:",timestamp)
    timestamp = int(timestamp)
    user_list = db.query(User, username=username)
    if user_list:
        user_id = user_list[0].id
        if user_id in logged_in_users:
            print("in connect:",session_id)
            print("in connect memory:",logged_in_users)
            if logged_in_users[user_id] == session_id:
                if db.update(User, dict(id=user_id), lastip=request.remote_addr,last_online=int(time.time())):
                    friends_list, group_info = get_friends_and_groups(user_id,timestamp)
                    logged_in_users_session_id[user_id] = request.sid
                    socketio.emit(ClientEvent.get_contacts_info.name, {"friends_list": friends_list, "group_info": group_info},to=request.sid)
                    current_timestamp = int(time.time())  # 当前 Unix 时间戳
                    # 计算 180 天前的 Unix 时间戳
                    timestamp_180_days_ago = current_timestamp - 180 * 24 * 60 * 60
                    def getAvatar(user_id):
                        user = db.query(User, id=user_id)[0]
                        with open(os.path.join(IMAGE_PATH, user.avatar), 'rb') as f:
                            avatar = base64.b64encode(f.read()).decode('utf-8')
                        return avatar
                    friend_requests = db.query(Operation,Operation.friend_id==user_id,Operation.type==OperationType.ADD_FRIEND,Operation.timestamp>=max(timestamp,timestamp_180_days_ago),Operation.isProcess==False)
                    socketio.emit(ClientEvent.friend_request.name, {"friend_requests": [{"avatar":getAvatar(friend_request.author_id),"username":db.query(User,id=friend_request.author_id)[0].username,"nickname":db.query(User,id=friend_request.author_id)[0].nickname} for friend_request in friend_requests]},to=request.sid)
                    managed_groups = db.query(ChatGroup,manager_id=user_id)
                    group_requests = [db.query(Operation,Operation.group_id==managed_group.id,Operation.type==OperationType.JOIN_GROUP,Operation.timestamp>=max(timestamp,timestamp_180_days_ago),Operation.isProcess==False) for managed_group in managed_groups]
                    request_users = []
                    for group_request in group_requests:
                        request_users.extend([(db.query(User,id=tmp.author_id)[0],tmp.group_id) for tmp in group_request])
                    socketio.emit(ClientEvent.group_request_all.name,{"group_requests":[{"user_id":user.id,"username":user.username,"nickname":user.nickname,"group_id":group_id,"group_name":db.query(ChatGroup,id=int(group_id))[0].name} for (user,group_id) in request_users]},to=request.sid)
                    for group_id in group_info.keys():
                        join_room(int(group_id),request.sid)
                else:
                    socketio.emit(ClientEvent.login_error.name, {"message":"Failed to connect! Database Error!","status":Status.ERROR.value},to=request.sid)
                    disconnect(request.sid)
            else:
                socketio.emit(ClientEvent.login_error.name, {"message":"Invalid session ID!","status":Status.ERROR.value},to=request.sid)
                disconnect(request.sid)
        else:
            socketio.emit(ClientEvent.login_error.name, {"message":"User not logged in!","status":Status.ERROR.value},to=request.sid)
            disconnect(request.sid)
    else:
        socketio.emit(ClientEvent.login_error.name, {"message":"User not found!","status":Status.ERROR.value},to=request.sid)
        disconnect(request.sid)
@socketio.on('disconnect')
def my_disconnect():
    del logged_in_users_session_id[request.sid]
@socketio.on(ServerEvent.request_add_friend.name)
def request_add_friend(data):
    user_username = data.get('user_username', None)
    friend_username = data.get('friend_username', None)
    assert user_username and friend_username, "Either user_username and friend_username must be provided!"
    user_id = db.query(User, username=user_username)[0].id
    if friend_username:
        friend = db.query(User, username=friend_username)
    if friend:
        friend = friend[0]
        friend_id = friend.id
        
        if db.query(Friendship, user1_id=user_id, user2_id=friend_id) or db.query(Friendship, user1_id=friend_id, user2_id=user_id):
            socketio.emit(ClientEvent.add_friend_error.name, {"message":"Friend already exists!","status":Status.ERROR.value},to=request.sid)
        elif user_id == friend_id:
            socketio.emit(ClientEvent.add_friend_error.name, {"message":"Cannot add yourself as a friend!","status":Status.ERROR.value},to=request.sid)
        else:
            isFirstInsert = True
            if db.query(Operation,type=OperationType.ADD_FRIEND,author_id=user_id,friend_id=friend_id,isProcess=False):
                isFirstInsert = False
            else:
                db.insert(Operation,type=OperationType.ADD_FRIEND,author_id=user_id,friend_id=friend_id)
            try:
                socketio.emit(ClientEvent.add_friend_request_success.name, {"message":"send request success!","status":Status.SUCCESS.value},to=request.sid)
            except Exception as e:
                print(e)
            if isFirstInsert:
                if friend_id in logged_in_users_session_id:
                    user = db.query(User, id=user_id)[0]
                    with open(os.path.join(IMAGE_PATH, user.avatar), 'rb') as f:
                        avatar = base64.b64encode(f.read()).decode('utf-8')
                    socketio.emit(ClientEvent.get_friend_request.name, {"message":"new friend request!","status":Status.SUCCESS.value, "user_id": user_id, "username": user.username, "nickname": user.nickname,"avatar":avatar}, to=logged_in_users_session_id[friend_id])
                else:
                    print("insert operation error")
    else:
        socketio.emit(ClientEvent.add_friend_error.name, {"message":"Friend does not exist!","status":Status.ERROR.value},to=request.sid)
def get_friends_and_groups(user_id,timestamp=None):
    # 获取朋友列表
    # 假设 Friendship 模型包含用户间的朋友关系
    if not timestamp:
        timestamp_180_days_ago = int(time.time()) - 180 * 24 * 60 * 60
        timestamp = timestamp_180_days_ago
    friend_ids = [(friendship.user2_id,friendship.id) for friendship in db.query(Friendship, user1_id=user_id)] + \
                 [(friendship.user1_id,friendship.id) for friendship in db.query(Friendship, user2_id=user_id)]
    friends = [(db.query(User, id=friend_id)[0],friendship_id) for (friend_id,friendship_id) in friend_ids]

    # 格式化朋友列表为所需结构
    friends_list = [{"nickname": friend.nickname, "user_id": friend.id, "username": friend.username,"messages":
    list(map(lambda x:{"content":x.content,"username":(friend.username if x.author_id==friend.id else None),"timestamp":x.timestamp},db.query(Message,Message.friendship_id==friendship_id,Message.timestamp>=timestamp,order_by=Message.timestamp)))} for (friend,friendship_id) in friends if friend]
    # 获取群组信息
    # 假设 GroupMembers 模型包含用户和群组的关系，ChatGroup 模型表示聊天群组
    group_memberships = db.query(GroupMembers, user_id=user_id)
    group_info = {}
    for membership in group_memberships:
        group = db.query(ChatGroup, id=membership.group_id)[0]
        if group:
            member_ids = [member.user_id for member in db.query(GroupMembers, group_id=group.id)]
            members = [db.query(User, id=member_id)[0] for member_id in member_ids]
            mapping = {member.id:member for member in members}
            group_info[group.id] = {
                "name": group.name,"manager_username":db.query(User,id=group.manager_id)[0].username,
                "members": [{"user_id": member.id, "nickname": member.nickname, "username": member.username} for member in members if member],
        "messages":list(map(lambda x:{"content":x.content,"username":(mapping[x.author_id].username if x.author_id in mapping else None),"timestamp":x.timestamp},db.query(Message,Message.group_id==group.id,Message.timestamp>=timestamp,order_by=Message.timestamp)))
            }
    return friends_list, group_info
@socketio.on(ServerEvent.getGroupInfo.name)
def get_groupInfo(data):
    username = data.get('username', None)
    group_id = data.get('group_id', None)
    timestamp = data.get('mytimestamp', None)
    assert username and group_id, "Both user_id and group_id must be provided!"
    user_id = db.query(User, username=username)[0].id
    group = db.query(ChatGroup, id=group_id)[0]
    if group:
        if db.query(GroupMembers, user_id=user_id, group_id=group.id):
            member_ids = [member.user_id for member in db.query(GroupMembers, group_id=group.id)]
            members = [db.query(User, id=member_id)[0] for member_id in member_ids]
            mapping = {member.id:member for member in members}
            socketio.emit(ClientEvent.get_group_info.name,  {"group_id":group_id,
                "name": group.name,"manager_username":db.query(User,id=group.manager_id)[0].username,
                "members": [{"nickname": member.nickname, "username": member.username} for member in members if member],
        "messages":list(map(lambda x:{"content":x.content,"username":(mapping[x.author_id].username if x.author_id in mapping else None),"timestamp":x.timestamp},db.query(Message,Message.group_id==group.id,Message.timestamp>=timestamp,order_by=Message.timestamp)))
            },to=request.sid)
        else:
            print(f"get_groupInfo error:{username} is not a member of the group(ID:{group_id})!")
            # socketio.emit(ClientEvent.login_error.name, {"message":"You are not a member of the group!","status":Status.ERROR.value},to=request.sid)
    else:
        print("get_groupInfo error:not found group")
@socketio.on(ServerEvent.accept_friend_request.name)
def accept_friend_request(data):
    username = data.get('username', None)
    friend_username = data.get('friend_username', None)
    isaccepted = data.get('isaccepted', None)
    assert username and friend_username, "Both user_id and friend_id must be provided!"
    user_id = db.query(User, username=username)[0].id
    friend_id = db.query(User, username=friend_username)[0].id
    if db.query(Friendship, user1_id=user_id, user2_id=friend_id) or db.query(Friendship, user1_id=friend_id, user2_id=user_id):
        db.update(Operation,dict(author_id=friend_id,type=OperationType.ADD_FRIEND,friend_id=user_id),isProcess=True)
        socketio.emit(ClientEvent.accept_friend_request_error.name, {"message":"Friend already exists!","status":Status.DUPLICATE.value,"username":friend_username},to=request.sid)
    elif user_id == friend_id:
        socketio.emit(ClientEvent.accept_friend_request_error.name, {"message":"Cannot add yourself as a friend!","status":Status.ERROR.value,"username":friend_username},to=request.sid)
    else:
        if isaccepted:
            if db.insert(Friendship,user1_id=user_id,user2_id=friend_id):
                socketio.emit(ClientEvent.accept_friend_request_success.name, {"message":"Accept friend request success!","status":Status.SUCCESS.value,"username":friend_username},to=request.sid)
                db.update(Operation,dict(author_id=friend_id,type=OperationType.ADD_FRIEND,friend_id=user_id),isProcess=True)
                if friend_id in logged_in_users_session_id:
                    user = db.query(User, id=user_id)[0]
                    with open(os.path.join(IMAGE_PATH, user.avatar), 'rb') as f:
                        avatar = base64.b64encode(f.read()).decode('utf-8')
                    socketio.emit(ClientEvent.get_friend_accept.name, {"message":"Friend request accepted!","status":Status.SUCCESS.value, "user_id": user_id, "username": user.username, "nickname": user.nickname,"avatar":avatar}, to=logged_in_users_session_id[friend_id])
            else:
                socketio.emit(ClientEvent.accept_friend_request_error.name, {"message":"Server Error when add friend!","status":Status.ERROR.value,"username":friend_username},to=request.sid)
        else:
            socketio.emit(ClientEvent.accept_friend_request_success.name, {"message":"Friend request rejected!","status":Status.REJECTED.value,"username":friend_username},to=request.sid)
            db.update(Operation,dict(author_id=user_id,type=OperationType.ADD_FRIEND,friend_id=friend_id),isProcess=True)
@socketio.on(ServerEvent.create_group.name)
def create_group(data):
    username = data.get('username', None)
    group_name = data.get('group_name', None)
    assert username and group_name, "Both user_id and group_name must be provided!"
    user_id = db.query(User, username=username)[0].id
    if db.insert(ChatGroup,name=group_name,manager_id=user_id):
        group = db.query(ChatGroup,name=group_name,manager_id=user_id,order_by=desc(ChatGroup.id))[0]
        if not db.query(GroupMembers,user_id=user_id,group_id=group.id):
            if db.insert(GroupMembers,user_id=user_id,group_id=group.id):
                members = [db.query(User, id=member.user_id)[0] for member in db.query(GroupMembers, group_id=group.id)]
                join_room(int(group.id),request.sid)
                socketio.emit(ClientEvent.create_group_success.name, {"message":"Create group success!","status":Status.SUCCESS.value,"group_id":group.id,"group_name":group.name,"members":[{"username":member.username,"nickname":member.nickname} for member in members]},to=request.sid)
            else:
                socketio.emit(ClientEvent.create_group_error.name, {"message":"insert groupMember database error!","status":Status.ERROR.value},to=request.sid)
        else:
            socketio.emit(ClientEvent.create_group_error.name, {"message":"is already a member!","status":Status.DUPLICATE.value},to=request.sid)
    else:
        socketio.emit(ClientEvent.create_group_error.name, {"message":"insert group database error!","status":Status.ERROR.value},to=request.sid)
@socketio.on(ServerEvent.request_join_group.name)
def request_join_group(data):
    username = data.get('username', None)
    group_id = data.get('group_id', None)
    assert username and group_id, "must Provided user_id and group_id in request_join_group"
    group = db.query(ChatGroup, id=group_id)
    user_id = db.query(User, username=username)
    if not user_id:
        socketio.emit(ClientEvent.join_group_error.name, {"message":"username does not exist!","status":Status.ERROR.value},to=request.sid)
    else:
        user_id = user_id[0].id
    if group:
        group = group[0]
        # 检查用户是否已经是群组成员
        if db.query(GroupMembers, user_id=user_id, group_id=group.id):
            socketio.emit(ClientEvent.join_group_error.name, {"message":"Already a member of the group!","status":Status.ERROR.value},to=request.sid)
        else:
            # 发送加入群组请求给管理员
            group_manager_id = group.manager_id
            user = db.query(User,id=user_id)[0]
            if group_manager_id in logged_in_users_session_id:
                # 假设管理员在线，发送请求
                with open(os.path.join(IMAGE_PATH, user.avatar), 'rb') as f:
                    avatar = base64.b64encode(f.read()).decode('utf-8')
                socketio.emit(ClientEvent.get_group_request.name, 
                              {"message":"New join request!","status":Status.SUCCESS.value, "user_id": user.id, "group_id": group.id,"username":user.username,"nickname":user.nickname,"avatar":avatar},
                              to=logged_in_users_session_id[group_manager_id])
            if db.insert(Operation,type=OperationType.JOIN_GROUP,author_id=user_id,group_id=group_id):
                socketio.emit(ClientEvent.join_group_request_success.name, {"message":"Join request sent to the group manager!","status":Status.SUCCESS.value},to=request.sid)
    else:
        # 群组不存在的情况
        socketio.emit(ClientEvent.join_group_error.name, {"message":"Group does not exist!","status":Status.ERROR.value},to=request.sid)
@socketio.on(ServerEvent.accept_group_request.name)
def accept_group_request(data):
    username = data.get('username', None)
    group_id = data.get('group_id', None)
    isaccepted = data.get('isaccepted', None)
    assert username and group_id, "Both user_id and group_id must be provided!"
    # 检查用户是否是群组管理员
    group = db.query(ChatGroup, id=group_id)
    user_id = db.query(User, username=username)
    if not user_id:
        socketio.emit(ClientEvent.accept_group_request_error.name, {"message":"username does not exist!","status":Status.ERROR.value},to=request.sid)
    else:
        user_id = user_id[0].id
    if group:
        group = group[0]
        if group.manager_id == logged_in_users_session_id[request.sid]:
            # 检查用户是否之前有申请加入群组
            if db.query(Operation,type=OperationType.JOIN_GROUP,author_id=user_id,group_id=group_id,isProcess=False):
                if isaccepted:
                    if db.insert(GroupMembers,user_id=user_id,group_id=group_id):
                        socketio.emit(ClientEvent.accept_group_request_success.name, {"message":"Group request accepted!","status":Status.SUCCESS.value,"group_id":group_id,"username":username},to=request.sid)
                        db.update(Operation,dict(author_id=user_id,type=OperationType.JOIN_GROUP,group_id=group_id),isProcess=True)
                        socketio.emit(ClientEvent.new_user_join_group.name,{"message":"New user joined the group!","status":Status.SUCCESS.value,"group_id":group_id,"username":username,"nickname":db.query(User,id=user_id)[0].nickname},to=int(group_id))
                        if user_id in logged_in_users_session_id:
                            members = [db.query(User, id=member.user_id)[0] for member in db.query(GroupMembers, group_id=group.id)]
                            join_room(int(group.id),logged_in_users_session_id[user_id])
                            socketio.emit(ClientEvent.get_group_request_accepted.name, {"message":"Group request accepted!","status":Status.SUCCESS.value, "group_id": group_id,"group_name":group.name,"timestamp":int(time.time()),"manager_username":db.query(User,id=group.manager_id)[0].username,"members":[{"username":member.username,"nickname":member.nickname} for member in members]}, to=logged_in_users_session_id[user_id])
                    else:
                        socketio.emit(ClientEvent.accept_group_request_error.name, {"message":"insert groupMember database error!","status":Status.ERROR.value,"group_id":group_id,"username":username},to=request.sid)
                else:
                    socketio.emit(ClientEvent.accept_group_request_success.name, {"message":"Group request rejected!","status":Status.REJECTED.value,"group_id":group_id,"username":username},to=request.sid)
                    db.update(Operation,dict(author_id=user_id,type=OperationType.JOIN_GROUP,group_id=group_id),isProcess=True)
            else:
                socketio.emit(ClientEvent.accept_group_request_error.name, {"message":"No join request found!","status":Status.ERROR.value,"group_id":group_id,"username":username},to=request.sid)
        else:
            socketio.emit(ClientEvent.accept_group_request_error.name, {"message":"User is not the group manager!","status":Status.ERROR.value,"group_id":group_id,"username":username},to=request.sid)
    else:
        socketio.emit(ClientEvent.accept_group_request_error.name, {"message":"Group does not exist!","status":Status.ERROR.value,"group_id":group_id,"username":username},to=request.sid)
@socketio.on(ServerEvent.send_message.name)
def send_message(data):
    username = data.get('username', None)
    content = data.get('content', None)
    group_id = data.get('group_id', None)
    friend_username = data.get('friend_username', None)
    md5 = data.get('md5', None)
    assert md5, "md5 must be provided!"
    assert username and content, "Both user_id and content must be provided!"
    assert (group_id is None and friend_username is not None) or (group_id is not None and friend_username is None), "group_id and friendship_id can only provided one"
    user_id = db.query(User, username=username)[0].id
    if group_id:
        if db.query(GroupMembers, user_id=user_id, group_id=group_id):
            if db.insert(Message,author_id=user_id,content=content,group_id=group_id):
                socketio.emit(ClientEvent.send_message_success.name, {"message":"Message sent successfully!","status":Status.SUCCESS.value,"md5":md5},to=request.sid)
                message = db.query(Message,order_by=desc(Message.timestamp),author_id=user_id,content=content,group_id=group_id)[0]
                socketio.emit(ClientEvent.receive_message.name,{"timestamp":message.timestamp,"username":username,"content":content,"group_id":group_id,"nickname":db.query(User,id=user_id)[0].nickname},to=int(group_id),include_self=False)
            else:
                socketio.emit(ClientEvent.send_message_error.name, {"message":"Message sent failed!","status":Status.ERROR.value,"md5":md5},to=request.sid)
        else:
            socketio.emit(ClientEvent.send_message_error.name, {"message":"User is not a member of the group!","status":Status.ERROR.value,"md5":md5},to=request.sid)
    elif friend_username:
        friend_id = db.query(User, username=friend_username)[0].id
        friendship =  db.query(Friendship,or_(and_(Friendship.user1_id==user_id,Friendship.user2_id==friend_id),and_(Friendship.user1_id==friend_id,Friendship.user2_id==user_id)))
        if friendship:
            friendship = friendship[0]
            if db.insert(Message,author_id=user_id,content=content,friendship_id=friendship.id):
                socketio.emit(ClientEvent.send_message_success.name, {"message":"Message sent successfully!","status":Status.SUCCESS.value,"md5":md5},to=request.sid)
                if friend_id in logged_in_users_session_id:
                    user = db.query(User, id=user_id)[0]
                    message = db.query(Message,order_by=desc(Message.timestamp),author_id=user_id,content=content,friendship_id=friendship.id)[0]
                    socketio.emit(ClientEvent.receive_message.name,{"timestamp":message.timestamp,"content":content,"username":user.username,"nickname":user.nickname},to=logged_in_users_session_id[friend_id])
            else:
                socketio.emit(ClientEvent.send_message_error.name, {"message":"Message sent failed!","status":Status.ERROR.value,"md5":md5},to=request.sid)
        else:
            socketio.emit(ClientEvent.send_message_error.name, {"message":"Friend does not exist!","status":Status.ERROR.value,"md5":md5},to=request.sid)
@socketio.on(ServerEvent.delete_friend.name)
def delete_friend(data):
    username = data.get('username', None)
    friend_username = data.get('friend_username', None)
    assert username and friend_username, "Both user_id and friend_id must be provided!"
    user_id = db.query(User, username=username)[0].id
    friend_id = db.query(User, username=friend_username)[0].id
    friendship = db.query(Friendship,or_(and_(Friendship.user1_id==user_id,Friendship.user2_id==friend_id),and_(Friendship.user1_id==friend_id,Friendship.user2_id==user_id)))
    if friendship:
        friendship = friendship[0]
        if db.delete(Friendship,id=friendship.id):
            socketio.emit(ClientEvent.send_message_success.name, {"message":"Delete friend successfully!","status":Status.SUCCESS.value},to=request.sid)
        else:
            socketio.emit(ClientEvent.send_message_error.name, {"message":"Delete friend failed!","status":Status.ERROR.value},to=request.sid)
    else:
        socketio.emit(ClientEvent.send_message_error.name, {"message":"Friend does not exist!","status":Status.ERROR.value},to=request.sid)
@socketio.on(ServerEvent.delete_group.name)
def delete_group(data):
    username = data.get('username', None)
    group_id = data.get('group_id', None)
    assert username and group_id, "Both user_id and group_id must be provided!"
    user_id = db.query(User, username=username)[0].id
    group = db.query(ChatGroup, id=group_id)[0]
    if group:
        if group.manager_id == user_id:
            if db.delete(ChatGroup,id=group.id):
                close_room(int(group.id))
                socketio.emit(ClientEvent.send_message_success.name, {"message":"Delete group successfully!","status":Status.SUCCESS.value},to=request.sid)
            else:
                socketio.emit(ClientEvent.send_message_error.name, {"message":"Delete group failed!","status":Status.ERROR.value},to=request.sid)
        else:
            socketio.emit(ClientEvent.send_message_error.name, {"message":"User is not the group manager!","status":Status.ERROR.value},to=request.sid)
    else:
        socketio.emit(ClientEvent.send_message_error.name, {"message":"Group does not exist!","status":Status.ERROR.value},to=request.sid)
@socketio.on(ServerEvent.leave_group.name)
def leave_group(data):
    username = data.get('username', None)
    group_id = data.get('group_id', None)
    assert username and group_id, "Both user_id and group_id must be provided!"
    user_id = db.query(User, username=username)[0].id
    group = db.query(ChatGroup, id=group_id)[0]
    if group:
        if db.delete(GroupMembers,user_id=user_id,group_id=group.id):
            socketio.emit(ClientEvent.send_message_success.name, {"message":"Leave group successfully!","status":Status.SUCCESS.value},to=request.sid)
            leave_room(int(group_id),request.sid)
        else:
            socketio.emit(ClientEvent.send_message_error.name, {"message":"Leave group failed!","status":Status.ERROR.value},to=request.sid)
    else:
        socketio.emit(ClientEvent.send_message_error.name, {"message":"Group does not exist!","status":Status.ERROR.value},to=request.sid)
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',debug=True,log_output=True)
    # app.run(host='0.0.0.0',debug=True)
