from PyQt5.QtCore import QObject, pyqtSignal
import sqlite3
import threading
from Threads import WebSocketThread
import hashlib
import os
from config import CACHE_DIR
import time
class ChatAppDBManager(QObject):
    add_friend_signal = pyqtSignal(dict)
    add_group_signal = pyqtSignal(dict)
    add_group_message_signal = pyqtSignal(dict)
    add_friend_message_signal = pyqtSignal(dict)
    delete_friend_signal = pyqtSignal(dict)
    delete_group_signal = pyqtSignal(dict)
    add_group_member_signal = pyqtSignal(dict)
    delete_group_member_signal = pyqtSignal(dict)

    def __init__(self, db_path):
        super().__init__()
        self.lock = threading.Lock()
        self.db_path = db_path

    def create_tables(self,isLogginDB=True):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            if not isLogginDB:
                cursor.execute("""CREATE TABLE IF NOT EXISTS chat_group (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        manager_username TEXT NOT NULL,
                                        group_id TEXT UNIQUE NOT NULL,
                                        FOREIGN KEY (manager_username) REFERENCES user(username)
                                    );""")

                cursor.execute("""CREATE TABLE IF NOT EXISTS group_members (
                                        id INTEGER PRIMARY KEY,
                                        user_id INTEGER NOT NULL,
                                        group_id INTEGER NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES user(id),
                                        FOREIGN KEY (group_id) REFERENCES chat_group(group_id) ON DELETE CASCADE
                                    );""")
                cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_groupID_user_id
                                    ON group_members (user_id, group_id);""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS friendship (
                                        id INTEGER PRIMARY KEY,
                                        user_id INTEGER NOT NULL,
                                        UNIQUE(user_id),
                                        FOREIGN KEY (user_id) REFERENCES user(id)
                                    );""")

                cursor.execute("""CREATE TABLE IF NOT EXISTS message (
                                    id INTEGER PRIMARY KEY,
                                    content TEXT NOT NULL,
                                    timestamp INTEGER DEFAULT (strftime('%s', 'now')),
                                    author_id INTEGER NOT NULL,
                                    group_id INTEGER,
                                    friendship_id INTEGER,
                                    FOREIGN KEY (author_id) REFERENCES user(id),
                                    FOREIGN KEY (group_id) REFERENCES chat_group(group_id) ON DELETE CASCADE,
                                    FOREIGN KEY (friendship_id) REFERENCES friendship(id) ON DELETE CASCADE,
                                    CHECK ((group_id IS NULL AND friendship_id IS NOT NULL) OR (group_id IS NOT NULL AND friendship_id IS NULL))
                                );""")
                cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_timestamp_author_id_groupID_friendship_id
                                    ON message (timestamp, author_id, group_id, friendship_id);""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS friend_request (
                                        id INTEGER PRIMARY KEY,
                                        timestamp INTEGER DEFAULT (strftime('%s', 'now')),
                                        username TEXT UNIQUE NOT NULL,
                                        nickname TEXT,
                                        avatar TEXT,
                                        isProcess BOOLEAN DEFAULT FALSE,
                                        isAccepted BOOLEAN DEFAULT FALSE
                                    );
                                    """)
                cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_username_on_isProcess_false 
                                    ON friend_request (username) 
                                    WHERE isProcess = FALSE;""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS group_request (
                                        id INTEGER PRIMARY KEY,
                                        timestamp INTEGER DEFAULT (strftime('%s', 'now')),
                                        groupID TEXT NOT NULL,
                                        username TEXT NOT NULL,
                                        nickname TEXT,
                                        avatar TEXT,
                                        isProcess BOOLEAN DEFAULT FALSE,
                                        isAccepted BOOLEAN DEFAULT FALSE
                                    );
                                    """)
                cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_groupID_username_on_isProcess_false 
                                    ON group_request (groupID, username) 
                                    WHERE isProcess = FALSE;""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                                            id INTEGER PRIMARY KEY,
                                            username TEXT UNIQUE NOT NULL,
                                            nickname TEXT,
                                            avatar TEXT
                                        );""")
            else:
                cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                                        id INTEGER PRIMARY KEY,
                                        username TEXT UNIQUE NOT NULL,
                                        nickname TEXT,
                                        avatar TEXT
                                    );""")
                cursor.execute("""CREATE TABLE IF NOT EXISTS user_session (
                                        id INTEGER PRIMARY KEY,
                                        username TEXT UNIQUE NOT NULL,
                                        session_id TEXT,
                                        is_remember_password BOOLEAN DEFAULT FALSE
                                    );""")
            connection.commit()
        finally:
            connection.close()
    def get_user_info(self, username):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT username, nickname, avatar FROM user WHERE username = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
        finally:
            connection.close()
        return result
    def set_user_info(self,username,nickname,avatar=None):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "INSERT INTO user (username, nickname, avatar) VALUES (?, ?, ?)"

            if avatar is None:
                save_path = DEFAULT_CONTACT_AVATAR
                tmp = self.getAvatarByUsername(username)
                if tmp:
                    print("set_user_info,tmp:",tmp)
                    save_path = tmp
                    return
            elif isinstance(avatar,bytes):
                tmp = hashlib.md5(avatar)
                save_path = os.path.join(CACHE_DIR,f"{tmp.hexdigest()}.png")
                if not os.path.exists(save_path):
                    with open(save_path,'wb') as f:
                        f.write(avatar)
            elif isinstance(avatar,str):
                if avatar==DEFAULT_CONTACT_AVATAR:
                    save_path = avatar
                else:
                    if os.path.exists(avatar):
                        pass
                    else:
                        print(f"avatar:{avatar} not exist!")
                        save_path = DEFAULT_CONTACT_AVATAR
            if self._get_user_id(username) is not None:
                query = "UPDATE user SET nickname = ?, avatar = ? WHERE username = ?"
                cursor.execute(query, (nickname,save_path,username))
            else:
                cursor.execute(query, (username,nickname,save_path))
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
    def get_user_session(self, username):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT session_id FROM user_session WHERE username = ? AND is_remember_password = TRUE"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                result = result[0]
        finally:
            connection.close()
        return result
    def set_user_remember_password(self, username, is_remember_password):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "INSERT OR REPLACE INTO user_session (username, is_remember_password) VALUES (?, ?)"
            cursor.execute(query, (username,is_remember_password))
            connection.commit()
        finally:
            connection.close()
    def get_all_saved_users(self):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM user_session"
            cursor.execute(query)
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def set_user_session(self, username, session_id):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = """
                INSERT OR REPLACE INTO user_session (username, session_id,is_remember_password) 
                VALUES (?, ?, TRUE)
                """
            cursor.execute(query, (username, session_id))
            connection.commit()
        finally:
            connection.close()
    def get_latest_timestamp(self):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query_message = "SELECT MAX(timestamp) FROM message"
            query_operation = "SELECT MAX(timestamp) FROM friend_request"

            cursor.execute(query_message)
            latest_message_time = cursor.fetchone()
            if latest_message_time:
                latest_message_time = latest_message_time[0]
            cursor.execute(query_operation)
            latest_operation_time = cursor.fetchone()
            if latest_operation_time:
                latest_operation_time = latest_operation_time[0]
            query_operation = "SELECT MAX(timestamp) FROM group_request"
            cursor.execute(query_operation)
            latest_group_time = cursor.fetchone()
            if latest_group_time:
                latest_group_time = latest_group_time[0]
            
            result = max((latest_group_time if latest_group_time is not None else 0),(latest_message_time if latest_message_time is not None else 0), (latest_operation_time if latest_operation_time is not None else 0))+1
        finally:
            connection.close()
        result = 0 if result is None else result
        return result

    def get_group_members(self, group_id):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = """
                SELECT u.username, u.avatar, u.nickname 
                FROM user u 
                JOIN group_members gm ON u.id = gm.user_id 
                WHERE gm.group_id = ?
                """
            cursor.execute(query, (group_id,))
            result = cursor.fetchall()
            print("get_group_members:",result)
        finally:
            connection.close()
        return result

    def get_latest_group_messages(self, group_id, n):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = """
                SELECT m.content, m.timestamp, u.username, u.avatar, u.nickname 
                FROM message m
                JOIN user u ON m.author_id = u.id
                WHERE m.group_id = ?
                ORDER BY m.timestamp DESC
                LIMIT ?
                """
            cursor.execute(query, (group_id, n))
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def get_messages_fromGroup_by_timestampAndcountDESC(self, group_id, before_timestamp, n):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = """
                SELECT m.content, m.timestamp, u.username, u.avatar, u.nickname 
                FROM message m
                JOIN user u ON m.author_id = u.id
                WHERE m.group_id = ? AND m.timestamp <= ?
                ORDER BY m.timestamp DESC
                LIMIT ?
                """
            cursor.execute(query, (group_id, before_timestamp,n))
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def get_messages_fromGroup_by_countDESC(self, group_id, n,offset=0):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = """
                SELECT m.content, m.timestamp, u.username, u.avatar, u.nickname 
                FROM message m
                JOIN user u ON m.author_id = u.id
                WHERE m.group_id = ?
                ORDER BY m.timestamp DESC
                LIMIT ? OFFSET ?
                """
            cursor.execute(query, (group_id, n, offset))
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def get_messages_with_friend_by_timestampAndcountDESC(self, friend_username, before_timestamp, n):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            friendship_id = self._get_friendship_id(friend_username)
            query = """
                SELECT m.content, m.timestamp, u.username, u.avatar, u.nickname
                FROM message m
                JOIN user u ON m.author_id = u.id
                WHERE m.friendship_id = ? AND m.timestamp <= ?
                ORDER BY m.timestamp DESC
                LIMIT ?
                """
            cursor.execute(query, (friendship_id, before_timestamp,n))
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def get_messages_with_friend_by_countDESC(self, friend_username, n,offset=0):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            friendship_id = self._get_friendship_id(friend_username)
            query = """
                SELECT m.content, m.timestamp, u.username, u.avatar, u.nickname
                FROM message m
                JOIN user u ON m.author_id = u.id
                WHERE m.friendship_id = ?
                ORDER BY m.timestamp DESC
                LIMIT ? OFFSET ?
                """
            cursor.execute(query, (friendship_id, n, offset))
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def _get_user_id(self, username):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT id FROM user WHERE username = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            print("in _get_user_id:",result)
            if result:
                result = result[0]
        finally:
            connection.close()
        return result
    def _get_friendship_id(self, friend_username):
        result = None
        friend_id = self._get_user_id(friend_username)
        if friend_id:
            connection = sqlite3.connect(self.db_path, check_same_thread=False)
            try:
                cursor = connection.cursor()
                query = "SELECT id FROM friendship WHERE  user_id = ?"
                cursor.execute(query, (friend_id,))
                result = cursor.fetchone()
                if result:
                    result = result[0]
            finally:
                connection.close()
            return result
        else:
            print("One or both users not found")
            return None
    def _get_group_id(self, group_id):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM chat_group WHERE group_id = ?"
            cursor.execute(query, (group_id,))
            result = cursor.fetchone()
            if result:
                result = result[0]
        finally:
            connection.close()
        return result
    def add_friend(self, friend_username,nickname,avatar=None):
        friend_id = self._get_user_id(friend_username)

        if friend_id:
            connection = sqlite3.connect(self.db_path, check_same_thread=False)
            try:
                cursor = connection.cursor()
                if self._get_friendship_id(friend_username):
                    info = self.get_user_info(friend_username)
                    print("emit add_friend_signal signal")
                    self.add_friend_signal.emit({"username":friend_username,"nickname":info[1],"avatar":info[2]})
                else:
                    query = "INSERT INTO friendship (user_id) VALUES (?)"
                    cursor.execute(query, (friend_id,))
                    print("commit:INSERT INTO friendship (user_id) VALUES (?)")
                    connection.commit()
                    info = self.get_user_info(friend_username)
                    print("emit add_friend_signal signal")
                    self.add_friend_signal.emit({"username":friend_username,"nickname":info[1],"avatar":info[2]})
            except Exception as e:
                print(e)
            finally:
                connection.close()
        else:
            connection = sqlite3.connect(self.db_path, check_same_thread=False)
            try:
                cursor = connection.cursor()
                self.set_user_info(friend_username,nickname,avatar)
                friend_id = self._get_user_id(friend_username)
                query = "INSERT INTO friendship (user_id) VALUES (?)"
                cursor.execute(query, (friend_id,))
                connection.commit()
                info = self.get_user_info(friend_username)
                print("emit add_friend_signal signal")
                self.add_friend_signal.emit({"username":friend_username,"nickname":info[1],"avatar":info[2]})
            except Exception as e:
                print(e)
            finally:
                connection.close()
            # print("One or both users not found")

    def delete_friend(self, friend_username):
        friend_id = self._get_user_id(friend_username)
        if friend_id:
            connection = sqlite3.connect(self.db_path, check_same_thread=False)
            try:
                cursor = connection.cursor()
                delete_messages_query = "DELETE FROM message WHERE friendship_id IN (SELECT id FROM friendship WHERE user_id = ?)"
                delete_friendship_query = "DELETE FROM friendship WHERE user_id = ?"
                cursor.execute(delete_messages_query, (friend_id,))
                cursor.execute(delete_friendship_query, (friend_id,))
                connection.commit()
                self.delete_friend_signal.emit({"username":friend_username})
            finally:
                connection.close()

    def add_group(self, name, manager_username,group_id,members):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            if self._get_group_id(group_id) is not None:
                print("group_id already exist")
                self.add_group_signal.emit({"group_id":group_id,"group_name":name,"manager_username":manager_username,"timestamp":int(time.time())})
                return
            query = "INSERT INTO chat_group (name, manager_username,group_id) VALUES (?, ?, ?)"
            cursor.execute(query, (name, manager_username,group_id))
            connection.commit()
            for member in members:
                self.set_user_info(member["username"],member["nickname"],member.get("avatar",None))
            connection.commit()
            for member in members:
                print("member:",member)
                print("self._get_user_id(member['username']):",self._get_user_id(member["username"]))
                query = "INSERT INTO group_members (user_id, group_id) VALUES (?, ?)"
                cursor.execute(query, (self._get_user_id(member["username"]), group_id))
                connection.commit()
            self.add_group_signal.emit({"group_id":group_id,"group_name":name,"manager_username":manager_username,"timestamp":int(time.time())})
        finally:
            connection.close()

    def delete_group(self, group_id):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "DELETE FROM chat_group WHERE group_id = ?"
            cursor.execute(query, (group_id,))
            connection.commit()
            self.delete_group_signal.emit({"group_id":group_id})
        finally:
            connection.close()
        

    def add_group_message(self, content, username, group_id,timestamp=None):
        user_id = self._get_user_id(username)
        try:
            connection = sqlite3.connect(self.db_path, check_same_thread=False)
            cursor = connection.cursor()
            query = "INSERT INTO message (content, author_id, group_id, timestamp) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (content, user_id, group_id,timestamp if timestamp else int(time.time())))
            connection.commit()
            info = self.get_user_info(username)
            self.add_group_message_signal.emit({"username":username,"nickname":info[1],"avatar":info[2],"content":content,"group_id":group_id,"timestamp":timestamp if timestamp else int(time.time())})
        finally:
            connection.close()

    def add_friend_message(self, content,sender_username,friend_username,timestamp=None):
        friendship_id = self._get_friendship_id(friend_username)
        author_id = self._get_user_id(sender_username)
        try:
            connection = sqlite3.connect(self.db_path, check_same_thread=False)
            cursor = connection.cursor()
            query = "INSERT INTO message (content, author_id, friendship_id, timestamp) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (content, author_id, friendship_id,timestamp if timestamp else int(time.time())))
            connection.commit()
            info = self.get_user_info(sender_username)
            print("emit add_friend_message_signal signal",{"username":sender_username,"nickname":info[1],"avatar":info[2],"content":content,"friend_username":friend_username,"timestamp":timestamp if timestamp else int(time.time())})
            self.add_friend_message_signal.emit({"username":sender_username,"nickname":info[1],"avatar":info[2],"content":content,"friend_username":friend_username,"timestamp":timestamp if timestamp else int(time.time())})
        except Exception as e:
            print(e)
        finally:
            connection.close()
    def setFriendRequest(self,username,nickname,avatar=None):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            user_id = self._get_user_id(username)
            
            if user_id:
                if avatar is not None and avatar!=DEFAULT_CONTACT_AVATAR:
                    self.set_user_info(username,nickname,avatar)
                user = self.get_user_info(username)
                query = "INSERT OR REPLACE INTO friend_request (username,nickname,avatar) VALUES (?,?,?)"
                cursor.execute(query, (user[0],user[1],user[2]))
                connection.commit()
            else:
                self.set_user_info(username,nickname,avatar)
                user = self.get_user_info(username)
                query = "INSERT OR REPLACE INTO friend_request (username,nickname,avatar) VALUES (?,?,?)"
                cursor.execute(query, (user[0],user[1],user[2]))
                connection.commit()
        finally:
            connection.close()
    def setGroupRequest(self,group_id,username,nickname,avatar):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            user_id = self._get_user_id(username)
            
            if user_id:
                if avatar is not None and avatar!=DEFAULT_CONTACT_AVATAR:
                    self.set_user_info(username,nickname,avatar)
                user = self.get_user_info(username)
                query = "INSERT OR REPLACE INTO group_request (groupID,username,nickname,avatar) VALUES (?,?,?,?)"
                cursor.execute(query, (group_id,user[0],user[1],user[2]))
                connection.commit()
            else:
                self.set_user_info(username,nickname,avatar)
                user = self.get_user_info(username)
                query = "INSERT OR REPLACE INTO group_request (groupID,username,nickname,avatar) VALUES (?,?,?,?)"
                cursor.execute(query, (group_id,user[0],user[1],user[2]))
                connection.commit()
        finally:
            connection.close()
    def updateFriendRequest(self,username,isAccepted):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "UPDATE friend_request SET isProcess = TRUE,isAccepted = ? WHERE username = ? AND isProcess = FALSE"
            cursor.execute(query, (isAccepted,username))
            connection.commit()
        finally:
            connection.close()
    def updateGroupRequest(self,group_id,username,isAccepted):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "UPDATE group_request SET isProcess = TRUE,isAccepted = ? WHERE groupID = ? AND username = ? AND isProcess = FALSE"
            cursor.execute(query, (isAccepted,group_id,username))
            connection.commit()
        finally:
            connection.close()
    def getFriendRequest(self):
        result = []
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT username,nickname,avatar FROM friend_request WHERE isProcess = FALSE"
            cursor.execute(query)
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def getFriendRequestByUsername(self,username):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM friend_request WHERE username = ? ORDER BY timestamp DESC LIMIT 1 "
            cursor.execute(query,(username,))
            result = cursor.fetchone()
        finally:
            connection.close()
        return result
    def getGroupRequest(self):
        result = []
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()

            query = "SELECT g.groupID,cg.name,g.username,g.nickname,g.avatar FROM group_request g JOIN chat_group cg ON cg.group_id = g.groupID WHERE g.isProcess = FALSE"
            cursor.execute(query)
            result = cursor.fetchall()
        finally:
            connection.close()
        return result
    def getGroupRequestByUsernameAndGroupID(self):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT g.groupID,cg.name,g.username,g.nickname,g.avatar,g.isProcess,g.isAccepted FROM group_request g JOIN chat_group cg ON cg.group_id = g.groupID WHERE g.groupID = ? AND g.username = ?"
            cursor.execute(query)
            result = cursor.fetchone()
        finally:
            connection.close()
        return result
    def addGroupMember(self,group_id,username,nickname,avatar=None):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            user_id = self._get_user_id(username)
            if user_id:
                if self.IsGroupMember(group_id,username):
                    return
                query = "INSERT INTO group_members (user_id,group_id) VALUES (?,?)"
                cursor.execute(query, (user_id,group_id))
                connection.commit()
                info = self.get_user_info(username)
                self.add_group_member_signal.emit({"group_id":group_id,"username":username,"nickname":nickname,"avatar":info[2]})
            else:
                self.set_user_info(username,nickname,avatar)
                user_id = self._get_user_id(username)
                query = "INSERT INTO group_members (user_id,group_id) VALUES (?,?)"
                cursor.execute(query, (user_id,group_id))
                connection.commit()
                info = self.get_user_info(username)
                self.add_group_member_signal.emit({"group_id":group_id,"username":username,"nickname":nickname,"avatar":info[2]})
        finally:
            connection.close()
    def removeGroupMember(self,group_id,username):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "DELETE FROM group_members WHERE user_id = ? AND group_id = ?"
            cursor.execute(query, (self._get_user_id(username),group_id))
            self.delete_group_member_signal.emit({"group_id":group_id,"username":username})
            connection.commit()
        finally:
            connection.close()
    def IsGroupMember(self,group_id,username):
        result = False
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM group_members WHERE user_id = ? AND group_id = ?"
            cursor.execute(query, (self._get_user_id(username),group_id))
            result = cursor.fetchone()
        finally:
            connection.close()
        return result
    def getAvatarByUsername(self,username):
        result = None
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = "SELECT avatar FROM user WHERE username = ?"
            print("in getAvatarByUsername: username:",username)
            cursor.execute(query, (str(username.strip()),))
            result = cursor.fetchone()
            print("in getAvatarByUsername:",result)
            if result:
                result = result[0]
            else:
                result = None
        finally:
            connection.close()
        return result
    def setAvatarByUsername(self,username,avatar):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            tmp = hashlib.md5(avatar)
            save_path = os.path.join(CACHE_DIR,f"{tmp.hexdigest()}.png")
            if not os.path.exists(save_path):
                with open(save_path,'wb') as f:
                    f.write(avatar)
            else:
                return
            query = "UPDATE user SET avatar = ? WHERE username = ?"
            cursor.execute(query, (save_path,username))
            connection.commit()
        finally:
            connection.close()
    def set_user_info_without_avatar(self,username,nickname):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            cursor = connection.cursor()
            query = f"INSERT INTO user (nickname,username,avatar) VALUES (?,?,'{DEFAULT_CONTACT_AVATAR}')"
            cursor.execute(query, (nickname,username))
            connection.commit()
        finally:
            connection.close()
from Threads import *
class DataManager(QObject):
    websocketConnected = pyqtSignal()
    setUserInfoSuccess = pyqtSignal()
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.username = None
        self.nickname = None
        self.avatar = None
        self.session_id = None
        self.websocket_thread = WebSocketThread()
        self.websocket_thread.connected.connect(lambda :self.websocketConnected.emit())
        self.thread_pool = QThreadPool.globalInstance()
    def setUserInfo(self,username,nickname,avatar,session_id):
        self.username = username
        self.nickname = nickname
        self.avatar = avatar
        self.session_id = session_id
        global db_manager
        db_manager = ChatAppDBManager(f"{self.username}.db")
        db_manager.create_tables(isLogginDB=False)
        timestamp = db_manager.get_latest_timestamp()
        db_manager.set_user_info(self.username,self.nickname,self.avatar)
        print("username:",self.username,"session_id:",self.session_id,"timestamp:",timestamp)
        self.websocket_thread.setLoginInfo(self.username,self.session_id,timestamp)
        self.setUserInfoSuccess.emit()
        print("emit setUserInfoSuccess")
        self.websocket_thread.start()
    def WebSocketSend(self,event_name,data):
        return self.websocket_thread.getWebSocketClient().emit(event_name,data=data)
db_manager = ChatAppDBManager("chatapp.db")
db_manager.create_tables()
dataManager = DataManager()