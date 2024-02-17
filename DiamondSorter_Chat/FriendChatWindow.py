from ui.Ui_FriendChatWindow import Ui_FriendChatWindow
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import  Qt, QRectF, pyqtSignal, pyqtProperty
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtWidgets import QApplication,  QWidget,QListWidgetItem
from qfluentwidgets import themeColor,FluentIcon
import DataManager
from MessageItemWidget import MessageItemWidget
from Threads import *
import base64
from utils import TimeHorizontalSeparator
import time
import hashlib
from utils import *
from qfluentwidgets import TextEdit
class FriendChatWindow(Ui_FriendChatWindow,QWidget):
    closed = pyqtSignal()
    def __init__(self,parent=None,username=None,nickname=None):
        super().__init__(parent=parent)
        self.username = username
        self.nickname = nickname
        self.oldMaximum = 0
        self.minimumOfTimestamp = float("inf")
        self.maximumOfTimestamp = 0
        self.scrollValue = 0
        self.isReverseInsert = False
        self.setupUi(self)
        self._initUI()
        self._initData()
    def setUsername(self,username):
        if self.username is None:
            self.username = username
            self._initData()
    def setNickname(self,nickname):
        if self.nickname is None:
            self.nickname = nickname
            self._initData()
    def updateWindowName(self):
        self.setWindowTitle(f"💎 Chats Window{self.nickname}(ID:{self.username})")
        self.lb_username.setText(f"(ID:{self.username})")
        self.lb_nickname.setText(self.nickname)
    def _initData(self):
        if self.username is None:
            return
        if self.nickname is None:
            return
        self.updateWindowName()
        messages = DataManager.db_manager.get_messages_with_friend_by_countDESC(self.username,100)
        if messages:
            for message in reversed(messages):
                """m.content, m.timestamp, u.username, u.avatar, u.nickname"""
                self.addMessage(message[2],message[0],message[4],message[1],isMe=message[2]==DataManager.dataManager.username,isReverseInsert=False,isReceive=True)
    def _initUI(self):
        self.setStyleSheet("background-color: #e6e6e6; border: none;")
        self.widget.setStyleSheet("background-color: white; border: none;")
        self.te_inputText.setStyleSheet("""TextEdit {
            color: black;
            background-color: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(0, 0, 0, 13);
            border-top: 1px solid rgba(0, 0, 0, 100);
            border-radius: 5px;
            /* font: 14px "Segoe UI", "Microsoft YaHei"; */
            padding: 0px 10px;
            selection-background-color: --ThemeColorLight1;
        }

        TextEdit {
            padding: 2px 3px 2px 8px;
        }

        TextEdit:hover{
            background-color: rgba(249, 249, 249, 0.5);
            border: 1px solid rgba(0, 0, 0, 13);
            border-top: 1px solid rgba(0, 0, 0, 100);
        }
        TextEdit:focus
        {
            border-top: 1px solid --ThemeColorPrimary;
            background-color: white;
        }

        TextEdit:disabled{
            color: rgba(0, 0, 0, 150);
            background-color: rgba(249, 249, 249, 0.3);
            border: 1px solid rgba(0, 0, 0, 13);
            border-top: 1px solid rgba(0, 0, 0, 13);
        }

                                        """)
        def f(selfa, e):
            if not selfa.parent().hasFocus():
                return

            painter = QPainter(selfa)
            painter.setRenderHints(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)

            m = selfa.contentsMargins()
            path = QPainterPath()
            w, h = selfa.width()-m.left()-m.right(), selfa.height()
            path.addRoundedRect(QRectF(m.left(), 0, w, 10), 5, 5)

            rectPath = QPainterPath()
            rectPath.addRect(m.left(), 2.5, w, 10)
            path = path.subtracted(rectPath)

            painter.fillPath(path, themeColor())
        self.te_inputText.layer.paintEvent = lambda e: f(self.te_inputText.layer, e)
        self.addToolButton(self.page_chat, FluentIcon.CHAT.icon())
        self.addToolButton(self.page_file, FluentIcon.FOLDER.icon())
        self.SendButton.clicked.connect(self.sendMessage)
        def f2(selfb, event):
            if event.key() == Qt.Key_Return and event.modifiers() == Qt.NoModifier:
                self.sendMessage()
            else:
                super(TextEdit,selfb).keyPressEvent(event)
        self.te_inputText.keyPressEvent = lambda e: f2(self.te_inputText, e)
        self.lw_message.verticalScrollBar().rangeChanged.connect(self.moveScrollBarToPreviousPosition)
        self.lw_message.verticalScrollBar().valueChanged.connect(self.onScroll)
        
    def moveScrollBarToPreviousPosition(self):
        if self.isReverseInsert:
            self.lw_message.verticalScrollBar().setValue(self.scrollValue+self.lw_message.verticalScrollBar().maximum()-self.oldMaximum)
        else:
            if self.scrollValue == self.oldMaximum:
                self.lw_message.verticalScrollBar().setValue(self.lw_message.verticalScrollBar().maximum())
            else:
                self.lw_message.verticalScrollBar().setValue(self.scrollValue)
        self.oldMaximum = self.lw_message.verticalScrollBar().maximum()
    def onScroll(self, value):

        self.scrollValue = value
        if value == self.lw_message.verticalScrollBar().minimum():
            self.loadMoreMessages()
    def loadMoreMessages(self):
        if self.minimumOfTimestamp is None:
            messages = DataManager.db_manager.get_messages_with_friend_by_countDESC(self.username,100)
        else:
            messages = DataManager.db_manager.get_messages_with_friend_by_timestampAndcountDESC(self.username,self.minimumOfTimestamp-1,100)
        if messages:
            for message in messages:
                """m.content, m.timestamp, u.username, u.avatar, u.nickname"""
                self.addMessage(message[2],message[0],message[4],message[1],isMe=message[2]==DataManager.dataManager.username,isReverseInsert=True,isReceive=True)
    def addToolButton(self, widget:QWidget,icon):
        self.toolButtons.addItem(
            routeKey=widget.objectName(),
            icon=icon,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )
    def addMessage(self, username, content, nickname,timestamp=None, isMe=False,isReverseInsert=False,isReceive=True):
        def innerAddMessage():
            if isMe or username == DataManager.dataManager.username:
                messageItem = MessageItemWidget(None,True)
                messageItem.setAvatar(DataManager.dataManager.avatar)
                messageItem.setNickname(nickname)
                messageItem.setUsername(username)
                messageItem.setContent(content)
                if isReceive:
                    messageItem.setSendSuccess(True)
                else:
                    md5 = hashlib.md5(f"{username}{content}{int(time.time())}".encode("utf8")).hexdigest()
                    def sendsuccess(data):
                        if data["md5"]==md5:
                            print("send success!")
                            messageItem.setSendSuccess(True)
                            DataManager.db_manager.add_friend_message(content,username,self.username,int(time.time()))
                            DataManager.dataManager.websocket_thread.send_message_success.disconnect(sendsuccess)
                            DataManager.dataManager.websocket_thread.send_message_error.disconnect(sendfail)
                    def sendfail(data):
                        if data["md5"]==md5:
                            messageItem.setSendSuccess(False)
                            DataManager.dataManager.websocket_thread.send_message_success.disconnect(sendsuccess)
                            DataManager.dataManager.websocket_thread.send_message_error.disconnect(sendfail)
                    DataManager.dataManager.websocket_thread.send_message_success.connect(sendsuccess)
                    DataManager.dataManager.websocket_thread.send_message_error.connect(sendfail)
                    DataManager.dataManager.WebSocketSend(ServerEvent.send_message.name,{"username":DataManager.dataManager.username,"content":content,"friend_username":self.username,"md5":md5})
                item = QListWidgetItem(self.lw_message)

                size = messageItem.sizeHint()
                item.setSizeHint(size)

                if isReverseInsert:
                    self.lw_message.insertItem(0,item)
                    self.lw_message.setItemWidget(item, messageItem)
                else:
                    self.lw_message.addItem(item)
                    self.lw_message.setItemWidget(item, messageItem)
            else:
                messageItem = MessageItemWidget()
                print("FriendChatWindow, messageItem: username:",username)
                avatar = DataManager.db_manager.getAvatarByUsername(username)
                if avatar and avatar!=DEFAULT_CONTACT_AVATAR:
                    messageItem.setAvatar(avatar)
                else:
                    messageItem.setAvatar(DEFAULT_CONTACT_AVATAR)
                    t =  GetAvatarThread()
                    t.setQueryInfo(DataManager.dataManager.username,DataManager.dataManager.session_id,username)
                    def success(data):
                        json_data = json.loads(data.decode("utf8"))
                        encoded_bytes = json_data["avatar"].encode('utf-8')
                        avatar = base64.b64decode(encoded_bytes)
                        DataManager.db_manager.setAvatarByUsername(username,avatar)
                        messageItem.setAvatar(avatar)
                        t.stop()
                        print("get avatar success!")
                    def fail(data):
                        t.stop()
                        print("getavatar fail!",data.decode("utf8"))
                    t.getAvatarSuccess.connect(success)
                    t.getAvatarFailed.connect(fail)
                    t.start()
                messageItem.setUsername(username)
                messageItem.setNickname(nickname)
                messageItem.setContent(content)
                if isReceive:
                    messageItem.setSendSuccess(True)
                else:
                    md5 = hashlib.md5(f"{username}{content}{int(time.time())}".encode("utf8")).hexdigest()
                    def sendsuccess(data):
                        if data["md5"]==md5:
                            messageItem.setSendSuccess(True)
                            DataManager.dataManager.websocket_thread.send_message_success.disconnect(sendsuccess)
                            DataManager.dataManager.websocket_thread.send_message_error.disconnect(sendfail)
                    def sendfail(data):
                        if data["md5"]==md5:
                            messageItem.setSendSuccess(False)
                            DataManager.dataManager.websocket_thread.send_message_success.disconnect(sendsuccess)
                            DataManager.dataManager.websocket_thread.send_message_error.disconnect(sendfail)
                    DataManager.dataManager.websocket_thread.send_message_success.connect(sendsuccess)
                    DataManager.dataManager.websocket_thread.send_message_error.connect(sendfail)
                    DataManager.dataManager.WebSocketSend(ServerEvent.send_message.name,{"username":DataManager.dataManager.username,"content":content,"friend_username":self.username,"md5":md5})
                    

                item = QListWidgetItem(self.lw_message)

                size = messageItem.sizeHint()
                item.setSizeHint(size)

                if isReverseInsert:
                    self.lw_message.insertItem(0,item)
                    self.lw_message.setItemWidget(item, messageItem)
                else:
                    self.lw_message.addItem(item)
                    self.lw_message.setItemWidget(item, messageItem)
        def innerAddTime():
            timeItem = TimeHorizontalSeparator()
            timeItem.setTimeStamp(timestamp)
            item = QListWidgetItem(self.lw_message)

            size = timeItem.sizeHint()
            item.setSizeHint(size)

            if isReverseInsert:
                if abs(timestamp-self.minimumOfTimestamp)>=60:
                    self.lw_message.insertItem(0,item)
                    self.lw_message.setItemWidget(item, timeItem)
            else:
                if abs(timestamp-self.maximumOfTimestamp)>=60:
                    self.lw_message.addItem(item)
                    self.lw_message.setItemWidget(item, timeItem)
            if self.minimumOfTimestamp is None:
                self.minimumOfTimestamp = timestamp
            else:
                self.minimumOfTimestamp = min(self.minimumOfTimestamp,timestamp)
            if self.maximumOfTimestamp is None:
                self.maximumOfTimestamp = timestamp
            else:
                self.maximumOfTimestamp = max(self.maximumOfTimestamp,timestamp)
        self.isReverseInsert = isReverseInsert
        if isReverseInsert:
            innerAddMessage()
            if timestamp:
                innerAddTime()
        else:
            if timestamp:
                innerAddTime()
            innerAddMessage()
    def sendMessage(self):
        text = self.te_inputText.toHtml()
        self.te_inputText.clear()
        if text:
            self.addMessage(DataManager.dataManager.username,text,DataManager.dataManager.nickname,int(time.time()),isMe=True,isReceive=False)
    def closeEvent(self, a0) -> None:
        self.closed.emit()
        return super().closeEvent(a0)
    def event(self, event: QtCore.QEvent):
        if event.type() == ReceiveMessageEvent.EventType:
            data  = event.data
            if not event.fromGroup and data["friend_username"]==self.username and data["username"]!=DataManager.dataManager.username:
                self.addMessage(data['username'],data["content"],data["nickname"],data["timestamp"],data["username"]==DataManager.dataManager.username,isReverseInsert=False,isReceive=True)
            event.accept()
            return True
        return super().event(event)
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    mainWin = FriendChatWindow()
    mainWin.show()
    sys.exit(app.exec_())