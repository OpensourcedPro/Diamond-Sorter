import enum
SERVER_URL = "http://104.156.244.168:5000"
class ClientEvent(enum.Enum):
    logout = 0 #{"message", "status"}
    get_contacts_info = 1 #{"friend_list":[{"nickname", "user_id", "username","messages":[{"content","username"(me:None),"timestamp"}]}],"group_info":{group_id:{"name","manager_username","members": [{"user_id", "nickname", "username"}],"messages":[{"content","username"(me:None),"timestamp"}]}}}
    friend_request = 2 #{"friend_requests": [{"user_id","username","nickname"}]}
    login_error = 3 #"message","status"
    add_friend_error = 4 #"message","status"
    add_friend_request_success = 5#"message","status"
    get_friend_request = 6#"message","status", "user_id", "username", "nickname","avatar"
    accept_friend_request_error = 7#"message","status","username"
    accept_friend_request_success = 8#"message","status","username"
    get_friend_accept = 9#"message","status", "user_id", "username", "nickname","avatar"
    create_group_success = 10#"message","status","group_id","group_name","members":[{"username","nickname"}]
    create_group_error = 11 #"message","status"
    join_group_request_success = 12#"message","status"
    join_group_error = 13#"message","status"
    group_request_all  = 14 #{"group_requests":[{"user_id","username","nickname","group_id","group_name"}]}
    get_group_request_accepted = 15#"message","status", "group_id","group_name","timestamp","manager_username"
    accept_group_request_error = 16#"message","status","group_id","username"
    accept_group_request_success = 17#"message","status","group_id","username"
    send_message_success = 18#"message","status","md5"
    send_message_error = 19#"message","status","md5"
    receive_message = 20#"username","content","nickname","timestamp",("group_id")
    get_group_request = 21 #"message","status", "user_id","group_id","username","nickname","avatar"
    get_group_info = 22 #"message","status", "group_id","group_name","manager_username","members":[{"user_id","username","nickname"}],"messages":[{"content","username"(me:None),"timestamp"}]
    new_user_join_group = 23 #"message","status", "group_id","group_name","user_id","username","nickname"


class ServerEvent(enum.Enum):
    "/login"#json "message","status",状态码 ("session_id","user_id","username","nickname") 
    "/register"#json "message","status",状态码
    "connect"#websocket  username, session_id, timestamp
    "disconnect"#websocket
    request_add_friend = 0 #user_username, friend_username
    accept_friend_request = 1 #username, friend_username, isaccepted
    create_group = 2 #username, group_name
    request_join_group = 3 #username, group_id
    accept_group_request = 4 #username, group_id, isaccepted
    send_message = 5 #username, content, group_id, friend_username, md5
    delete_friend = 6 #username, friend_username
    delete_group = 7 #username, group_id
    leave_group = 8  #username, group_id
    getGroupInfo = 9 #username, group_id

class Status(enum.Enum):
    SUCCESS = 0
    REJECTED = 1
    ERROR = 2
    OUTDATED = 3
    DUPLICATE = 4
from PyQt5.QtCore import QStandardPaths
CACHE_DIR = QStandardPaths.writableLocation(QStandardPaths.CacheLocation)
DEFAULT_CONTACT_AVATAR = ":/images/DefaultContactAvatar.png"
DEFAULT_GROUP_AVATAR = ":/images/DefaultGroupAvatar.png"