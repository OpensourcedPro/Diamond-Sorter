from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest,QNetworkReply
from PyQt5.QtCore import QUrl
import json
from config import *
from PyQt5.QtCore import QThreadPool, QRunnable
class Task(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Task, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """Your code goes here."""
        self.fn(*self.args, **self.kwargs)
class loginProcessThread(QThread):
    loginSuccess = pyqtSignal(bytes)
    loginFailed = pyqtSignal(bytes)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.username = None
        self.password = None
        self.session_id = None
        self.is_running = True
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.on_finished)
        self.network_manager.moveToThread(self)
    def setLoginInfo(self,username,password,session_id=None):
        self.username = username
        self.password = password
        self.session_id = session_id
    def clearLoginInfo(self):
        self.username = None
        self.password = None
    def run(self):
        
        while self.is_running:
            if self.username is not None:
                if self.session_id is not None:
                    data = {
                        "username": self.username,
                        "session_id": self.session_id
                    }
                elif self.password is not None:
                    data = {
                        "username": self.username,
                        "password": self.password
                    }
                print("data:",data)
                self.network_manager.clearConnectionCache()
                self.network_manager.clearAccessCache()
                request = QNetworkRequest(QUrl(f"{SERVER_URL}/login"))
                request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
                self.network_manager.post(request, json.dumps(data).encode('utf-8'))
                self.clearLoginInfo()
                self.exec_()
                print("finish post request")
                break
    @pyqtSlot(QNetworkReply)
    def on_finished(self, reply:QNetworkReply):
        self.is_running = False
        if reply.error() == QNetworkReply.NoError:
            response = json.loads(reply.readAll().data().decode('utf-8'))
            self.loginSuccess.emit(json.dumps(response).encode('utf-8'))
        else:
            mapping = {QNetworkReply.NetworkError.NoError : "NoError",
            QNetworkReply.NetworkError.ConnectionRefusedError : "ConnectionRefusedError",
            QNetworkReply.NetworkError.RemoteHostClosedError : "RemoteHostClosedError",
            QNetworkReply.NetworkError.HostNotFoundError : "HostNotFoundError",
            QNetworkReply.NetworkError.TimeoutError : "TimeoutError",
            QNetworkReply.NetworkError.OperationCanceledError : "OperationCanceledError",
            QNetworkReply.NetworkError.SslHandshakeFailedError : "SslHandshakeFailedError",
            QNetworkReply.NetworkError.UnknownNetworkError : "UnknownNetworkError",
            QNetworkReply.NetworkError.ProxyConnectionRefusedError : "ProxyConnectionRefusedError",
            QNetworkReply.NetworkError.ProxyConnectionClosedError : "ProxyConnectionClosedError",
            QNetworkReply.NetworkError.ProxyNotFoundError : "ProxyNotFoundError",
            QNetworkReply.NetworkError.ProxyTimeoutError : "ProxyTimeoutError",
            QNetworkReply.NetworkError.ProxyAuthenticationRequiredError : "ProxyAuthenticationRequiredError",
            QNetworkReply.NetworkError.UnknownProxyError : "UnknownProxyError",
            QNetworkReply.NetworkError.ContentAccessDenied : "ContentAccessDenied",
            QNetworkReply.NetworkError.ContentOperationNotPermittedError : "ContentOperationNotPermittedError",
            QNetworkReply.NetworkError.ContentNotFoundError : "ContentNotFoundError",
            QNetworkReply.NetworkError.AuthenticationRequiredError : "AuthenticationRequiredError",
            QNetworkReply.NetworkError.UnknownContentError : "UnknownContentError",
            QNetworkReply.NetworkError.ProtocolUnknownError : "ProtocolUnknownError",
            QNetworkReply.NetworkError.ProtocolInvalidOperationError : "ProtocolInvalidOperationError",
            QNetworkReply.NetworkError.ProtocolFailure : "ProtocolFailure",
            QNetworkReply.NetworkError.ContentReSendError : "ContentReSendError",
            QNetworkReply.NetworkError.TemporaryNetworkFailureError : "TemporaryNetworkFailureError",
            QNetworkReply.NetworkError.NetworkSessionFailedError : "NetworkSessionFailedError",
            QNetworkReply.NetworkError.BackgroundRequestNotAllowedError : "BackgroundRequestNotAllowedError",
            QNetworkReply.NetworkError.ContentConflictError : "ContentConflictError",
            QNetworkReply.NetworkError.ContentGoneError : "ContentGoneError",
            QNetworkReply.NetworkError.InternalServerError : "InternalServerError",
            QNetworkReply.NetworkError.OperationNotImplementedError : "OperationNotImplementedError",
            QNetworkReply.NetworkError.ServiceUnavailableError : "ServiceUnavailableError",
            QNetworkReply.NetworkError.UnknownServerError : "UnknownServerError",
            QNetworkReply.NetworkError.TooManyRedirectsError : "TooManyRedirectsError",
            QNetworkReply.NetworkError.InsecureRedirectError : "InsecureRedirectError"}
            try:
                response = json.loads(reply.readAll().data().decode('utf-8'))
                self.loginFailed.emit(json.dumps(response).encode('utf-8'))
            except:
                self.loginFailed.emit(json.dumps({"message":mapping[reply.error()],"status":Status.ERROR.value}).encode('utf-8'))
            
    def stop(self):
        self.is_running = False
        self.network_manager.deleteLater()
        self.quit()
        self.exit()
class RegisterProcessThread(QThread):
    registerSuccess = pyqtSignal(bytes)
    registerFailed = pyqtSignal(bytes)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.username = None
        self.password = None
        self.nickname = None
        self.is_running = True
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.on_finished)
        self.network_manager.moveToThread(self)
    def setLoginInfo(self,username,password,nickname=None):
        self.username = username
        self.password = password
        self.nickname = nickname
    def clearLoginInfo(self):
        self.username = None
        self.password = None
        self.nickname = None
    def run(self):
        
        while self.is_running:
            if self.username is not None and self.password is not None:
                if self.nickname is None:
                    data = {
                        "username": self.username,
                        "password": self.password
                    }
                else:
                    data = {
                        "username": self.username,
                        "password": self.password,
                        "nickname": self.nickname
                    }
                request = QNetworkRequest(QUrl(f"{SERVER_URL}/register"))
                request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
                self.network_manager.post(request, json.dumps(data).encode('utf-8'))
                self.exec_()
                break
    @pyqtSlot(QNetworkReply)
    def on_finished(self, reply:QNetworkReply):
        self.is_running = False
        if reply.error() == QNetworkReply.NoError:
            response = json.loads(reply.readAll().data().decode('utf-8'))
            self.registerSuccess.emit(json.dumps(response).encode('utf-8'))
        else:
            mapping = {QNetworkReply.NetworkError.NoError : "NoError",
            QNetworkReply.NetworkError.ConnectionRefusedError : "ConnectionRefusedError",
            QNetworkReply.NetworkError.RemoteHostClosedError : "RemoteHostClosedError",
            QNetworkReply.NetworkError.HostNotFoundError : "HostNotFoundError",
            QNetworkReply.NetworkError.TimeoutError : "TimeoutError",
            QNetworkReply.NetworkError.OperationCanceledError : "OperationCanceledError",
            QNetworkReply.NetworkError.SslHandshakeFailedError : "SslHandshakeFailedError",
            QNetworkReply.NetworkError.UnknownNetworkError : "UnknownNetworkError",
            QNetworkReply.NetworkError.ProxyConnectionRefusedError : "ProxyConnectionRefusedError",
            QNetworkReply.NetworkError.ProxyConnectionClosedError : "ProxyConnectionClosedError",
            QNetworkReply.NetworkError.ProxyNotFoundError : "ProxyNotFoundError",
            QNetworkReply.NetworkError.ProxyTimeoutError : "ProxyTimeoutError",
            QNetworkReply.NetworkError.ProxyAuthenticationRequiredError : "ProxyAuthenticationRequiredError",
            QNetworkReply.NetworkError.UnknownProxyError : "UnknownProxyError",
            QNetworkReply.NetworkError.ContentAccessDenied : "ContentAccessDenied",
            QNetworkReply.NetworkError.ContentOperationNotPermittedError : "ContentOperationNotPermittedError",
            QNetworkReply.NetworkError.ContentNotFoundError : "ContentNotFoundError",
            QNetworkReply.NetworkError.AuthenticationRequiredError : "AuthenticationRequiredError",
            QNetworkReply.NetworkError.UnknownContentError : "UnknownContentError",
            QNetworkReply.NetworkError.ProtocolUnknownError : "ProtocolUnknownError",
            QNetworkReply.NetworkError.ProtocolInvalidOperationError : "ProtocolInvalidOperationError",
            QNetworkReply.NetworkError.ProtocolFailure : "ProtocolFailure",
            QNetworkReply.NetworkError.ContentReSendError : "ContentReSendError",
            QNetworkReply.NetworkError.TemporaryNetworkFailureError : "TemporaryNetworkFailureError",
            QNetworkReply.NetworkError.NetworkSessionFailedError : "NetworkSessionFailedError",
            QNetworkReply.NetworkError.BackgroundRequestNotAllowedError : "BackgroundRequestNotAllowedError",
            QNetworkReply.NetworkError.ContentConflictError : "ContentConflictError",
            QNetworkReply.NetworkError.ContentGoneError : "ContentGoneError",
            QNetworkReply.NetworkError.InternalServerError : "InternalServerError",
            QNetworkReply.NetworkError.OperationNotImplementedError : "OperationNotImplementedError",
            QNetworkReply.NetworkError.ServiceUnavailableError : "ServiceUnavailableError",
            QNetworkReply.NetworkError.UnknownServerError : "UnknownServerError",
            QNetworkReply.NetworkError.TooManyRedirectsError : "TooManyRedirectsError",
            QNetworkReply.NetworkError.InsecureRedirectError : "InsecureRedirectError"}
            try:
                response = json.loads(reply.readAll().data().decode('utf-8'))
                self.registerFailed.emit(json.dumps(response).encode('utf-8'))
            except:
                self.registerFailed.emit(json.dumps({"message":mapping[reply.error()],"status":Status.ERROR.value}).encode('utf-8'))
            
    def stop(self):
        self.is_running = False
        self.network_manager.deleteLater()
        self.quit()
class GetAvatarThread(QThread):
    getAvatarSuccess = pyqtSignal(bytes)
    getAvatarFailed = pyqtSignal(bytes)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.username = None
        self.session_id = None
        self.query_username  = None
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.on_finished)
        self.network_manager.moveToThread(self)
        self.is_running=True
    def setQueryInfo(self,username,session_id,query_username):
        self.username = username
        self.session_id = session_id
        self.query_username  =query_username
    def run(self):
        
        while self.is_running:
            if self.username is not None and self.session_id is not None:
                data = {
                        "username": self.username,
                        "mysessionid": self.session_id,
                        "queryusername": self.query_username
                    }
                request = QNetworkRequest(QUrl(f"{SERVER_URL}/getAvatar"))
                request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
                self.network_manager.post(request, json.dumps(data).encode('utf-8'))
                self.exec_()
                break
    @pyqtSlot(QNetworkReply)
    def on_finished(self, reply:QNetworkReply):
        self.is_running = False
        if reply.error() == QNetworkReply.NetworkError.NoError:
            response = json.loads(reply.readAll().data().decode('utf-8'))
            
            self.getAvatarSuccess.emit(json.dumps(response).encode('utf-8'))
        else:
            response = json.loads(reply.readAll().data().decode('utf-8'))
            self.getAvatarFailed.emit(json.dumps(response).encode('utf-8'))
    def stop(self):
        self.is_running = False
        self.network_manager.deleteLater()
        self.quit()

    
import socketio
class WebSocketThread(QThread):
    connected = pyqtSignal()  # 定义一个信号
    get_contacts_info = pyqtSignal(dict)
    friend_request = pyqtSignal(dict)
    login_error = pyqtSignal(dict)
    add_friend_error = pyqtSignal(dict)
    add_friend_request_success = pyqtSignal(dict)
    get_friend_request = pyqtSignal(dict)
    accept_friend_request_error = pyqtSignal(dict)
    accept_friend_request_success = pyqtSignal(dict)
    get_friend_accept = pyqtSignal(dict)
    create_group_success = pyqtSignal(dict)
    create_group_error = pyqtSignal(dict)
    join_group_request_success = pyqtSignal(dict)
    join_group_error = pyqtSignal(dict)
    group_request_all = pyqtSignal(dict)
    get_group_request_accepted = pyqtSignal(dict)
    accept_group_request_error = pyqtSignal(dict)
    accept_group_request_success = pyqtSignal(dict)
    send_message_success = pyqtSignal(dict)
    send_message_error = pyqtSignal(dict)
    receive_message = pyqtSignal(dict)
    get_group_request = pyqtSignal(dict)
    get_group_info = pyqtSignal(dict)
    new_user_join_group = pyqtSignal(dict)
    def __init__(self, parent=None,username=None,session_id=None,timestamp=None):
        super().__init__(parent)
        self.sio_client = None
        self.username = username
        self.session_id = session_id
        self.timestamp = timestamp
    def run(self):
        self.sio_client = socketio.Client(logger=True,engineio_logger=True)

        @self.sio_client.event
        def connect():
            print("Connected to server")
            self.connected.emit()  # 当连接成功时发射信号

        @self.sio_client.event
        def disconnect():
            print("Disconnected from server")
        @self.sio_client.on(ClientEvent.get_contacts_info.name)
        def get_contacts_info(data):
            self.get_contacts_info.emit(data)
            print("get_contacts_info",data)
        @self.sio_client.on(ClientEvent.friend_request.name)
        def friend_request(data):
            self.friend_request.emit(data)
            print("friend_request",data)
        @self.sio_client.on(ClientEvent.login_error.name)
        def login_error(data):
            self.login_error.emit(data)
            print("login_error",data)
        @self.sio_client.on(ClientEvent.add_friend_error.name)
        def add_friend_error(data):
            self.add_friend_error.emit(data)
            print("add_friend_error",data)
        @self.sio_client.on(ClientEvent.add_friend_request_success.name)
        def add_friend_request_success(data):
            print("add_friend_request_success",data)
            self.add_friend_request_success.emit(data)
            
        @self.sio_client.on(ClientEvent.get_friend_request.name)
        def get_friend_request(data):
            self.get_friend_request.emit(data)
            print("get_friend_request",data)
        @self.sio_client.on(ClientEvent.accept_friend_request_error.name)
        def accept_friend_request_error(data):
            self.accept_friend_request_error.emit(data)
            print("accept_friend_request_error",data)
        @self.sio_client.on(ClientEvent.accept_friend_request_success.name)
        def accept_friend_request_success(data):
            self.accept_friend_request_success.emit(data)
            print("accept_friend_request_success",data)
        @self.sio_client.on(ClientEvent.get_friend_accept.name)
        def get_friend_accept(data):
            self.get_friend_accept.emit(data)
            print("get_friend_accept",data)
        @self.sio_client.on(ClientEvent.create_group_success.name)
        def create_group_success(data):
            self.create_group_success.emit(data)
            print("create_group_success",data)
        @self.sio_client.on(ClientEvent.create_group_error.name)
        def create_group_error(data):
            self.create_group_error.emit(data)
            print("create_group_error",data)
        @self.sio_client.on(ClientEvent.join_group_request_success.name)
        def join_group_request_success(data):
            self.join_group_request_success.emit(data)
            print("join_group_request_success",data)
        @self.sio_client.on(ClientEvent.join_group_error.name)
        def join_group_error(data):
            self.join_group_error.emit(data)
            print("join_group_error",data)
        @self.sio_client.on(ClientEvent.group_request_all.name)
        def group_request_all(data):
            self.group_request_all.emit(data)
            print("group_request_all",data)
        @self.sio_client.on(ClientEvent.get_group_request.name)
        def get_group_request(data):
            self.get_group_request.emit(data)
            print("get_group_request",data)
        @self.sio_client.on(ClientEvent.get_group_request_accepted.name)
        def get_group_request_accepted(data):
            self.get_group_request_accepted.emit(data)
            print("get_group_request_accepted",data)
        @self.sio_client.on(ClientEvent.accept_group_request_error.name)
        def accept_group_request_error(data):
            self.accept_group_request_error.emit(data)
            print("accept_group_request_error",data)
        @self.sio_client.on(ClientEvent.accept_group_request_success.name)
        def accept_group_request_success(data):
            self.accept_group_request_success.emit(data)
            print("accept_group_request_success",data)
        @self.sio_client.on(ClientEvent.send_message_success.name)
        def send_message_success(data):
            self.send_message_success.emit(data)
            print("send_message_success",data)
        @self.sio_client.on(ClientEvent.send_message_error.name)
        def send_message_error(data):
            self.send_message_error.emit(data)
            print("send_message_error",data)
        @self.sio_client.on(ClientEvent.receive_message.name)
        def receive_message(data):
            self.receive_message.emit(data)
            print("receive_message",data)
        @self.sio_client.on(ClientEvent.get_group_info.name)
        def get_group_info(data):
            self.get_group_info.emit(data)
            print("get_group_info",data)
        @self.sio_client.on(ClientEvent.new_user_join_group.name)
        def new_user_join_group(data):
            self.new_user_join_group.emit(data)
            print("new_user_join_group",data)
        print("start websocket",self.username,self.session_id,self.timestamp)
        self.sio_client.connect(SERVER_URL, headers={'username': self.username, 'mysessionid': self.session_id, 'mytimestamp': self.timestamp})
        self.sio_client.wait()
    def setLoginInfo(self,username,session_id,timestamp):
        self.username = str(username)
        self.session_id = str(session_id)
        self.timestamp = str(timestamp)
    def getWebSocketClient(self):
        return self.sio_client

    