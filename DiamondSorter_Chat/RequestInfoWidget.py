import sys
import typing
from PyQt5 import QtCore

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox,QWidget, QScrollArea,QStackedWidget, QVBoxLayout, QLabel,QSizePolicy,QSpacerItem
from PyQt5.QtGui import QFontMetrics, QPixmap,QTextDocument,QTextCursor
from ui.Ui_RequestItem import Ui_RequestItem
from qfluentwidgets import Pivot
from PyQt5.QtCore import  Qt

from PyQt5.QtWidgets import QWidget

from utils import *
import DataManager
from Threads import *


class RequestItem(Ui_RequestItem,QWidget):
    def __init__(self, parent=None,groupID=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._nickname = None
        self._username = None
        self._body = None
        self.groupID = groupID
        self.box = None
        self.isProcess = False
        self.isAccepted = False
        self.chosenIsAccepted = None
    def checkIsMine(self,data):
        json_data = json.loads(data.decode("utf8"))
        if json_data["username"]==self._username:
            if "group_id" not in json_data or ("group_id" in json_data and json_data["group_id"]==str(self.groupID)):
                return True,json_data
        return False,None

    def sendAcceptedRequestFail(self,data):
        # isMine,json_data = self.checkIsMine(data)
        isMine,json_data = True,data
        if json_data["status"] == Status.DUPLICATE.value:
            if isMine:
                self.box.yesButton.setText("Agreed")
                if self.groupID:
                    QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.updateGroupRequest(self.groupID,self._username,True)))
                else:
                    QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.updateFriendRequest(self._username,True)))
        else:
            if isMine:
                self.box.showCancelButton()
                self.box.yesButton.setText("agree")
                self.box.yesButton.setDisabled(False)
                self.chosenIsAccepted = None
                QMessageBox.warning(self,"Send Request failed",json_data["message"])
    def sendAcceptedRequestSuccess(self,data):
        if self.chosenIsAccepted is None:
            return lambda data:print(f"username:{self._username},groupID:{self.groupID},sendAcceptedRequestSuccess error")
        if "group_id" in data and data["group_id"]!=str(self.groupID):
            print(f"username:{self._username},groupID:{self.groupID},data:{data},sendAcceptedRequestSuccess error")
            return
        if self.chosenIsAccepted:
            def f(data):
                # isMine,json_data = self.checkIsMine(data)
                isMine,json_data = True,data
                if isMine:
                    self.box.yesButton.setText("Agreed")
                    if self.groupID:
                        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.updateGroupRequest(self.groupID,self._username,True)))
                    else:
                        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.updateFriendRequest(self._username,True)))
                        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.add_friend(self._username,self._nickname)))
            return f
            DataManager.dataManager.websocket_thread.accept_friend_request_success.connect(f)
        else:
            def f(data):
                # isMine,json_data = self.checkIsMine(data)
                isMine,json_data = True,data
                if isMine:
                    self.box.yesButton.setText("Rejected")
                    if self.groupID:
                        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.updateGroupRequest(self.groupID,self._username,False)))
                    else:
                        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.updateFriendRequest(self._username,False)))
            return f
            DataManager.dataManager.websocket_thread.accept_friend_request_success.connect(f)
    def setAvatar(self,avatar):
        if isinstance(avatar,bytes):
            pixmap = QPixmap()
            if pixmap.loadFromData(avatar):
                self.avatar.setPixmap(pixmap.scaled(60,60,Qt.KeepAspectRatioByExpanding))
        else:
            self.avatar.setPixmap(QPixmap(avatar).scaled(60,60,Qt.KeepAspectRatioByExpanding))
    def setGroupID(self,groupID):
        self.groupID = groupID
    def setNickname(self,nickname):
        elidfont = QFontMetrics(self.lb_nickname.font())
        elidedText = elidfont.elidedText(nickname, Qt.TextElideMode.ElideMiddle, self.width()-self.avatar.width()-25)
        self.lb_nickname.setText(elidedText)
        self._nickname = nickname
    def setUsername(self,username):
        text  = f"(ID:{username})"
        elidfont = QFontMetrics(self.lb_username.font())
        elidedText = elidfont.elidedText(text, Qt.ElideRight, self.width()-self.avatar.width()-self.lb_nickname.width()-5)
        self.lb_username.setText(elidedText)
        self._username = username
    def setRequestText(self,html):
        self._body = html
        doc = QTextDocument()
        doc.setHtml(html)
        doc.setDefaultFont(self.lb_body.font())

        metrics = QFontMetrics(self.lb_body.font())
        cursor = QTextCursor(doc)
        cursor.movePosition(QTextCursor.Start)
        plainText = ""
        position = 0
        isend = True
        while not cursor.atEnd():
            cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            char = cursor.selectedText()
            if metrics.width(plainText+char) <= self.width()-self.avatar.width()-20:
                plainText += char
                position = cursor.position()
            else:
                plainText += "..."
                isend = False
                break
            cursor.clearSelection()
        cursor.setPosition(position)
        if not isend:
            cursor.insertHtml("...")
        position = cursor.position()
        cursor.setPosition(0)
        cursor.setPosition(position, QTextCursor.KeepAnchor)
        self.lb_body.setText(cursor.selection().toHtml())
    def setIsProcess(self,isProcess,isAccepted):
        self.isProcess = isProcess
        self.isAccepted = isAccepted
    def resizeEvent(self, event):

        ret = super().resizeEvent(event)
        if self.box:
            self.box.resize(event.size())
        if self._nickname:
            self.setNickname(self._nickname)
        if self._username:
            self.setUsername(self._username)
        if self._body:
            self.setRequestText(self._body)   
        return ret
    def acceptRequest(self,isaccepted):
        self.box.hideCancelButton()
        self.box.yesButton.setDisabled(True)
        self.box.yesButton.setText("Sending...")
        self.chosenIsAccepted = isaccepted
        if self.groupID:
            QThreadPool.globalInstance().start(Task(lambda :DataManager.dataManager.WebSocketSend(ServerEvent.accept_group_request.name,{"username":self._username,"group_id":self.groupID,"isaccepted":isaccepted})))
        else:
            QThreadPool.globalInstance().start(Task(lambda :DataManager.dataManager.WebSocketSend(ServerEvent.accept_friend_request.name,{"username":DataManager.dataManager.username,"friend_username":self._username,"isaccepted":isaccepted})))
    def enterEvent(self, event) -> None:
        ret = super().enterEvent(event)
        if self._username and self._nickname and self._body:
            if not self.box:
                self.box = ModifiedMessageBoxBase(self)
                if not self.isProcess:
                    self.box.yesButton.setText("agree")
                    self.box.cancelButton.setText("refuse")
                    self.box.yesButton.clicked.connect(lambda :self.acceptRequest(True))
                    self.box.cancelButton.clicked.connect(lambda : self.acceptRequest(False))
                else:
                    if self.isAccepted:
                        self.box.yesButton.setText("Agreed")
                    else:
                        self.box.yesButton.setText("Rejected")
                    self.box.hideCancelButton()
                    self.box.yesButton.setDisabled(True)
                self.box.show()
            else:
                self.box.show()
        return ret
    def leaveEvent(self, event) -> None:
        ret = super().leaveEvent(event)
        if self._username and self._nickname and self._body:
            if self.box:
                self.box.hide()
        return ret
class RequestInfoWidget(QWidget):
    closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setStyleSheet("""
            RequestInfoWidget{background: white}
            QLabel{
                font: 20px 'Segoe UI';
                background: rgb(242,242,242);
                border-radius: 8px;
            }
        """)
        self.resize(400, 400)

        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.FriendInterface = QWidget(self)
        self.FriendScroll_Area = QScrollArea(self)
        self.FriendScroll_Area.setWidgetResizable(True)
        self.friendLayout = QVBoxLayout(self.FriendInterface)
        self.friendLayout.addSpacerItem(QSpacerItem(0,0,QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.FriendInterface.setLayout(self.friendLayout)
        self.FriendScroll_Area.setWidget(self.FriendInterface)
        self.FriendScroll_Area.setStyleSheet("border:none;")
        self.GroupInterface = QWidget(self)
        self.GroupScroll_Area = QScrollArea(self)
        self.GroupScroll_Area.setStyleSheet("border:none;")
        self.GroupScroll_Area.setWidgetResizable(True)
        self.groupLayout = QVBoxLayout(self.GroupInterface)
        self.groupLayout.addSpacerItem(QSpacerItem(0,0,QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.GroupInterface.setLayout(self.groupLayout)
        self.GroupScroll_Area.setWidget(self.GroupInterface)
        # add items to pivot
        self.addSubInterface(self.FriendScroll_Area, 'FriendInterface', 'Friend application')
        self.addSubInterface(self.GroupScroll_Area, 'GroupInterface', 'Group application')

        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(30, 0, 30, 30)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.FriendScroll_Area)
        self.pivot.setCurrentItem(self.FriendScroll_Area.objectName())
        self.friend_requests = {}
        self.group_request = {}
        self._initData()
        DataManager.dataManager.websocket_thread.accept_friend_request_success.connect(self.dispatchSuccessMessage)
        DataManager.dataManager.websocket_thread.accept_friend_request_error.connect(self.dispatchErrorMessage)
        DataManager.dataManager.websocket_thread.accept_group_request_success.connect(self.dispatchSuccessMessage)
        DataManager.dataManager.websocket_thread.accept_group_request_error.connect(self.dispatchErrorMessage)
    def __del__(self):
        DataManager.dataManager.websocket_thread.accept_friend_request_success.disconnect(self.dispatchSuccessMessage)
        DataManager.dataManager.websocket_thread.accept_friend_request_error.disconnect(self.dispatchErrorMessage)
        DataManager.dataManager.websocket_thread.accept_group_request_success.disconnect(self.dispatchSuccessMessage)
        DataManager.dataManager.websocket_thread.accept_group_request_error.disconnect(self.dispatchErrorMessage)
    def _initData(self):
        friend_data = DataManager.db_manager.getFriendRequest()
        for friend_request in friend_data:
            self.addFriendRequest(friend_request[0],friend_request[1],friend_request[2],False,False)
        group_data = DataManager.db_manager.getGroupRequest()
        for group_request in group_data:
            self.addGroupRequest(group_request[0],group_request[1],group_request[2],group_request[3],group_request[4],False,False)
    def dispatchErrorMessage(self,data):
        # json_data = json.loads(data.decode("uft8"))
        print("dispatchErrorMessage:data",data)
        print("dispatchErrorMessage:self.friend_requests",self.friend_requests)
        print("dispatchErrorMessage:self.group_request",self.group_request)
        json_data = data
        if "group_id" in json_data and 'username' in json_data:
            self.group_request[f"{json_data['group_id']}_{json_data['username']}"].sendAcceptedRequestFail(json_data)
        elif 'username' in json_data:
            self.friend_requests[f"{json_data['username']}"].sendAcceptedRequestFail(json_data)
        else:
            print(f"error:{json_data}")
    def dispatchSuccessMessage(self,data):
        """"""
        # json_data = json.loads(data.decode("uft8"))
        json_data = data
        print("dispatchSuccessMessage:self.friend_requests",self.friend_requests)
        print("dispatchSuccessMessage:self.group_request",self.group_request)
        print("dispatchSuccessMessage,data:",data)
        if "group_id" in json_data and 'username' in json_data:
            self.group_request[f"{json_data['group_id']}_{json_data['username']}"].sendAcceptedRequestSuccess(json_data)(json_data)
        elif 'username' in json_data:
            self.friend_requests[f"{json_data['username']}"].sendAcceptedRequestSuccess(json_data)(json_data)
        else:
            print(f"error:{json_data}")
    def addFriendRequest(self, username, nickname, avatar,isProcess,isAccepted):
        widget = RequestItem(self)
        widget.setAvatar(avatar)
        widget.setNickname(nickname)
        widget.setUsername(username)
        widget.setRequestText("This user wants to add you as a friend")
        widget.setIsProcess(isProcess,isAccepted)
        self.friend_requests[f"{username}"] = widget
        self.friendLayout.insertWidget(0,widget)
    def addGroupRequest(self,group_id, group_name, username, nickname, avatar,isProcess,isAccepted):
        widget = RequestItem(self)
        widget.setAvatar(avatar)
        widget.setNickname(nickname)
        widget.setUsername(username)
        widget.setGroupID(group_id)
        widget.setRequestText(f"Group application：<b>{group_name}</b><i>(ID:{group_id})</i>")
        widget.setIsProcess(isProcess,isAccepted)
        self.group_request[f"{group_id}_{username}"] = widget
        self.groupLayout.insertWidget(0,widget)
    def addSubInterface(self, widget: QLabel, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())
    def closeEvent(self, a0) -> None:
        self.closed.emit()
        return super().closeEvent(a0)

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = RequestInfoWidget()
    w.addFriendRequest("yllgertytryl","msdrgergono","avatar/0.png",False,False)
    w.addGroupRequest('56546848',"天下第一ertggerg","ertyhtgxyllgl","mowefw4no","avatar/1.png",False,False)
    w.show()
    app.exec_()