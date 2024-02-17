import sys
import typing
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget,QListWidgetItem,QListWidget,QAction
from PyQt5.QtCore import QRegExp,pyqtSignal, pyqtProperty, Qt,pyqtSlot
from PyQt5.QtGui import QRegExpValidator,QPainter,  QCloseEvent,QPixmap
import resources_rc
from ui.Ui_MainContactsPanel import Ui_MainContactsPanel
from ChatItemWidget import ChatItemWidget
from ContactItemWidget import ContactItemWidget
from qfluentwidgets import FluentIcon,Theme,MessageBoxBase,SubtitleLabel,LineEdit
from utils import *
from Threads import *
import DataManager
import base64
from RequestInfoWidget import RequestInfoWidget

class AddFriendMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = SubtitleLabel('Add a friend', self)
        self.usernameLineEdit = LineEdit(self)

        self.usernameLineEdit.setPlaceholderText('Enter your friends username or ID (not nickname)')
        self.usernameLineEdit.setClearButtonEnabled(True)

        reg = QRegExp("^[A-Za-z0-9_]+$")
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.usernameLineEdit.setValidator(validator)
        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.usernameLineEdit)

        # change the text of button
        self.yesButton.setText('Send Request')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        self.yesButton.setDisabled(True)
        self.usernameLineEdit.textChanged.connect(self.checkUsername)
        
    def checkUsername(self):
        if self.usernameLineEdit.text():
            self.yesButton.setDisabled(False)
        else:
            self.yesButton.setDisabled(True)
        print("self.widget.size()",self.widget.size())
    def add_friend_error(self,data):
        # json_data = json.loads(data.decode("utf8"))
        print("in add_friend_error")
        json_data = data
        QMessageBox.warning(self,"Request Failed",json_data["message"])
        self.yesButton.setDisabled(False)
        DataManager.dataManager.websocket_thread.add_friend_error.disconnect(self.add_friend_error)
        DataManager.dataManager.websocket_thread.add_friend_request_success.disconnect(self.add_friend_request_success)
    def add_friend_request_success(self,data):
        print("in add_friend_request_success")
        QMessageBox.information(self,"Request successful","Successful Sent Request！")
        DataManager.dataManager.websocket_thread.add_friend_error.disconnect(self.add_friend_error)
        DataManager.dataManager.websocket_thread.add_friend_request_success.disconnect(self.add_friend_request_success)
        self.close()
    def accept(self) -> None:
        def f():
            DataManager.dataManager.WebSocketSend(ServerEvent.request_add_friend.name,data={"user_username":DataManager.dataManager.username,"friend_username":self.usernameLineEdit.text()})
        DataManager.dataManager.websocket_thread.add_friend_error.connect(self.add_friend_error)
        DataManager.dataManager.websocket_thread.add_friend_request_success.connect(self.add_friend_request_success)
        QThreadPool.globalInstance().start(f)
        self.yesButton.setDisabled(True)
        
class AddGroupMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = SubtitleLabel('Join a group', self)
        self.groupIDLineEdit = LineEdit(self)

        self.groupIDLineEdit.setPlaceholderText('Enter the group ID')
        self.groupIDLineEdit.setClearButtonEnabled(True)

        reg = QRegExp("^[0-9]+$")
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        self.groupIDLineEdit.setValidator(validator)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.groupIDLineEdit)


        self.yesButton.setText('Send Request')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        self.yesButton.setDisabled(True)
        self.groupIDLineEdit.textChanged.connect(self.checkUsername)
        
    def checkUsername(self):
        if self.groupIDLineEdit.text():
            self.yesButton.setDisabled(False)
        else:
            self.yesButton.setDisabled(True)
        print("self.widget.size()",self.widget.size())
    def join_group_error(self,data):
        # json_data = json.loads(data.decode("utf8"))
        json_data = data
        QMessageBox.warning(self,"Request Failed",json_data["message"])
        self.yesButton.setDisabled(False)
        self.yesButton.setText("Send Request")
        DataManager.dataManager.websocket_thread.join_group_error.connect(self.join_group_error)
        DataManager.dataManager.websocket_thread.join_group_request_success.connect(self.join_group_request_success)
    def join_group_request_success(self,data):
        QMessageBox.information(self,"Request successful","Successful Sent Request！")
        DataManager.dataManager.websocket_thread.join_group_error.connect(self.join_group_error)
        DataManager.dataManager.websocket_thread.join_group_request_success.connect(self.join_group_request_success)
        self.close()
    def accept(self) -> None:
        def f():
            DataManager.dataManager.WebSocketSend(ServerEvent.request_join_group.name,data={"username":DataManager.dataManager.username,"group_id":str(int(self.groupIDLineEdit.text()))})
        DataManager.dataManager.websocket_thread.join_group_error.connect(self.join_group_error)
        DataManager.dataManager.websocket_thread.join_group_request_success.connect(self.join_group_request_success)
        QThreadPool.globalInstance().start(f)
        self.yesButton.setDisabled(True)
        self.yesButton.setText("Send Request...")
class CreateGroupMessageBox(MessageBoxBase):
    """ Custom message box """
    CreateGroupSuccess = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = SubtitleLabel('Create Group', self)
        self.groupNameLineEdit = LineEdit(self)

        self.groupNameLineEdit.setPlaceholderText('Enter the name of the group you are creating')
        self.groupNameLineEdit.setClearButtonEnabled(True)
        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.groupNameLineEdit)

        # change the text of button
        self.yesButton.setText('Send Request')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        self.yesButton.setDisabled(True)
        self.groupNameLineEdit.textChanged.connect(self.checkUsername)
        
    def checkUsername(self):
        if self.groupNameLineEdit.text():
            self.yesButton.setDisabled(False)
        else:
            self.yesButton.setDisabled(True)
        print("self.widget.size()",self.widget.size())
    def create_group_error(self,data):
        # json_data = json.loads(data.decode("utf8"))
        json_data = data
        QMessageBox.warning(self,"Request Failed",json_data["message"])
        self.yesButton.setDisabled(False)
        DataManager.dataManager.websocket_thread.create_group_error.disconnect(self.create_group_error)
        DataManager.dataManager.websocket_thread.create_group_success.disconnect(self.create_group_success)
        self.yesButton.setText("Send Request")
    def create_group_success(self,data):
        QMessageBox.information(self,"Request successful","Successful Sent Request！")
        self.CreateGroupSuccess.emit(data)
        DataManager.dataManager.websocket_thread.create_group_error.disconnect(self.create_group_error)
        DataManager.dataManager.websocket_thread.create_group_success.disconnect(self.create_group_success)
        self.close()
    def accept(self) -> None:
        def f():
            DataManager.dataManager.WebSocketSend(ServerEvent.create_group.name,data={"username":DataManager.dataManager.username,"group_name":str(self.groupNameLineEdit.text())})
        DataManager.dataManager.websocket_thread.create_group_error.connect(self.create_group_error)
        DataManager.dataManager.websocket_thread.create_group_success.connect(self.create_group_success)
        QThreadPool.globalInstance().start(f)
        self.yesButton.setDisabled(True)
        self.yesButton.setText("Send Request...")
class MainContactsWidget(Ui_MainContactsPanel,QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._initUI()
        self.RequestInfoIsShow = False
        self.requestInfoWidget = None
        self.friends = {}
        self.groups = {}
        DataManager.dataManager.websocket_thread.get_contacts_info.connect(self._init_contacts_info)
        DataManager.dataManager.websocket_thread.friend_request.connect(self._init_friend_requests)
        DataManager.dataManager.websocket_thread.group_request_all.connect(self._init_group_requests)
        DataManager.dataManager.websocket_thread.get_friend_accept.connect(self._init_friend_accept)
        DataManager.dataManager.websocket_thread.get_group_request_accepted.connect(self._accept_group_request)
        DataManager.dataManager.websocket_thread.get_friend_request.connect(self.receiveFriendRequest)
        DataManager.dataManager.websocket_thread.get_group_request.connect(self.receiveGroupRequest)
        # DataManager.dataManager.websocket_thread.receive_message.connect(self.receiveMessage)
    # def receiveMessage(self,data):
    #     json_data = data
    #     if "group_id" in json_data:
    #         if json_data["group_id"] in self.groups:
    #             contactItem,chatItem = self.groups[json_data["group_id"]]
    #             chatItem.setMessage(json_data["content"])
    #             chatItem.setTime(json_data["timestamp"])
    #             chatItem.increaseCount()
    #             # if contactItem.chatWindow:
    #             #     contactItem.chatWindow.addMessage(json_data["username"],json_data["content"],json_data["nickname"],
    #             #                                       json_data["timestamp"],json_data["username"]==DataManager.dataManager.username,isReverseInsert=False,isReceive=True)
    #     else:
    #         if json_data["username"] in self.friends:
    #             contactItem,chatItem = self.friends[json_data["username"]]
    #             chatItem.setMessage(json_data["content"])
    #             chatItem.setTime(json_data["timestamp"])
    #             chatItem.increaseCount()
    #             # if contactItem.chatWindow:
    #             #     contactItem.chatWindow.addMessage(json_data["username"],json_data["content"],json_data["nickname"],
    #             #                                       json_data["timestamp"],json_data["username"]==DataManager.dataManager.username,isReverseInsert=False,isReceive=True)
    def _initUI(self):
        self.setupUi(self)
        
        self.addSubInterface(self.page_nowChatting,"page_nowChatting","chats")
        self.addSubInterface(self.page_friends,"page_contacts","contacts")
        self.addSubInterface(self.page_groups,"page_groups","group chat")
        self.addSubInterface(self.page_groups,"page_groups","content")
        self.addSubInterface(self.page_groups,"page_groups","link resources")
        self.stackedWidget.setStyleSheet("QStackedWidget { background-color:rgba(255,255,255,128); }")
        self.navigation.setCurrentItem("page_nowChatting")
        self.lv_nowChatting.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lv_nowChatting.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lv_nowChatting.setResizeMode(QListWidget.Adjust)
        self.lv_friends.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lv_friends.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lv_friends.setResizeMode(QListWidget.Adjust)
        self.lv_groups.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lv_groups.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lv_groups.setResizeMode(QListWidget.Adjust)
        self.add_button = MyDropDownToolButton(FluentIcon.ADD.icon(Theme.LIGHT),self)
        self.add_button_menu = MyRoundMenu(self)
        addfriend_action = QAction(FluentIcon.PEOPLE.icon(), 'add a friend')
        addfriend_action.triggered.connect(self.showAddFriendMessageBox)
        self.add_button_menu.addAction(addfriend_action)
        add_group_action = QAction(FluentIcon.IOT.icon(), 'add a group')
        add_group_action.triggered.connect(self.showAddGroupMessageBox)
        self.add_button_menu.addAction(add_group_action)
        request_info_action = QAction(FluentIcon.FEEDBACK.icon(), 'Friends & Groups Application')
        self.badgeWidget = BadgeWidget()
        self.badgeWidget.valueChanged.connect(self.add_button.setBadgeValue)
        request_info_action.triggered.connect(self.showRequestInfo)
        self.add_button_menu.addWidget(self.badgeWidget,request_info_action)
        create_group_action = QAction(FluentIcon.LABEL.icon(), 'Create Group')
        create_group_action.triggered.connect(self.showCreateGroupMessageBox)
        self.add_button_menu.addAction(create_group_action)
        self.add_button.setMenu(self.add_button_menu)
        self.add_button.setMaximumWidth(40)
        self.add_button.show()
        self.lb_username = QLabel()
        self.lb_username.setText(f"(ID:{DataManager.dataManager.username})")
        self.lb_username.setStyleSheet("color:rgb(240,240,240);")



    def setUserInfo(self):
        self.lb_nickname.setText(DataManager.dataManager.nickname)
        self.lb_username.setText(f"(ID:{DataManager.dataManager.username})")
        self.lb_nickname.setStyleSheet("color:rgb(240,240,240);")
        self.lb_username.setStyleSheet("color:rgb(240,240,240);")
        if isinstance(DataManager.dataManager.avatar,bytes):
            pixmap = QPixmap()
            if pixmap.loadFromData(DataManager.dataManager.avatar):
                self.img_avatar.setPixmap(pixmap.scaled(80,80,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            self.img_avatar.setPixmap(QPixmap(DataManager.dataManager.avatar).scaled(80,80,Qt.KeepAspectRatio,Qt.SmoothTransformation))
    def _accept_group_request(self,data):
        print("in _accept_group_request")
        json_data = data

        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.add_group(json_data["group_name"],json_data["manager_username"], json_data["group_id"],json_data["members"])))
    def _create_group(self,data):
        print("in _create_group")
        json_data = data

        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.add_group(json_data["group_name"],DataManager.dataManager.username, json_data["group_id"],json_data["members"])))
    def groupChatItemClicked(self,groupID):
        if int(groupID) in self.groups:
            contactItem,_ = self.groups[int(groupID)]
            if contactItem:
                contactItem.openChatWindow()
        else:
            print("error groupChatItemClicked")
    def FriendItemClicked(self,username):
        if username in self.friends:
            contactItem,_ = self.friends[username]
            if contactItem:
                contactItem.openChatWindow()
        else:
            print("error FriendItemClicked")
    def _init_friend_accept(self,data):
        print("in _init_friend_accept")
        json_data = data
        encoded_bytes = json_data["avatar"].encode('utf-8')
        avatar = base64.b64decode(encoded_bytes)
        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.add_friend(json_data["username"],json_data["nickname"],avatar)))
    def _init_contacts_info(self,data):
        print("in _init_contacts_info")
        json_data = data
        for friend in json_data["friends_list"]:
            if "avatar" in json_data:
                encoded_bytes = json_data["avatar"].encode('utf-8')
                avatar = base64.b64decode(encoded_bytes)
            else:
                avatar = None
            DataManager.db_manager.add_friend(friend["username"],friend["nickname"],avatar)
            if friend["messages"]:
                for message in friend["messages"]:
                    DataManager.db_manager.add_friend_message(message["content"],message["username"],friend["username"],message["timestamp"])
        for group_id in json_data["group_info"]:
            if "avatar" in json_data["group_info"][group_id]:
                encoded_bytes = json_data["group_info"][group_id]["avatar"].encode('utf-8')
                avatar = base64.b64decode(encoded_bytes)
            else:
                avatar = DEFAULT_GROUP_AVATAR
            DataManager.db_manager.add_group(json_data["group_info"][group_id]["name"],json_data["group_info"][group_id]["manager_username"],group_id,json_data["group_info"][group_id]["members"])
            groupMembers = {x[0]:x for x in DataManager.db_manager.get_group_members(group_id)}
            group = json_data["group_info"][group_id]
            for member in group["members"]:
                if member["username"] not in groupMembers:
                    DataManager.db_manager.set_user_info(member["username"],member["nickname"],None)
                    DataManager.db_manager.addGroupMember(group_id,member["username"],member["nickname"],None)
                else:
                    groupMembers.pop(member["username"])
            for member in groupMembers:
                DataManager.db_manager.removeGroupMember(group_id,member)
            group = json_data["group_info"][group_id]
            if group["messages"]:
                def f(group1,group_id1):
                    for message in group1["messages"]:
                        DataManager.db_manager.add_group_message(message["content"],message["username"],group_id1,message["timestamp"])
                
                    print("receive message",message["content"],message["username"],group_id,message["timestamp"])
                QThreadPool.globalInstance().start(Task(f,group,group_id))      
    def _init_friend_requests(self,data):
        print("in _init_friend_requests")
        json_data = data
        for friend_request in json_data["friend_requests"]:
            self.receiveFriendRequest(friend_request)
    def _init_group_requests(self,data):
        print("in _init_group_requests")
        json_data = data
        for group_request in json_data["group_requests"]:
            self.receiveGroupRequest(group_request)
    def receiveFriendRequest(self,data):
        print("in receiveRequest")
        # json_data = json.loads(data.decode("utf8"))
        json_data = data
        if "avatar" in json_data:
            encoded_bytes = json_data["avatar"].encode('utf-8')
            avatar = base64.b64decode(encoded_bytes)
        else:
            avatar = None

        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.setFriendRequest(json_data["username"],json_data["nickname"],avatar)))
        if self.RequestInfoIsShow:
            self.requestInfoWidget.addFriendRequest(json_data["username"],json_data["nickname"],avatar,False,False)
        else:
            self.badgeWidget.increaseBadge()
        
    def receiveGroupRequest(self,data):
        print("in receiveGroupRequest")
        json_data = data
        if "avatar" in json_data:
            encoded_bytes = json_data["avatar"].encode('utf-8')
            avatar = base64.b64decode(encoded_bytes)
        else:
            avatar = None

        QThreadPool.globalInstance().start(Task(lambda :DataManager.db_manager.setGroupRequest(json_data["group_id"],json_data["username"],json_data["nickname"],avatar)))
        if self.RequestInfoIsShow:
            self.requestInfoWidget.addGroupRequest(json_data["group_id"],json_data["group_name"],json_data["username"],json_data["nickname"],avatar,False,False)
        else:
            self.badgeWidget.increaseBadge()
    def showAddFriendMessageBox(self):
        print("in showAddFriendMessageBox")
        window = FramelessWindow()
        w = AddFriendMessageBox(window)

        w.layout().setContentsMargins(0,0,0,0)
        w.layout().setSpacing(0)
        w.adjustSize()
        window.resize(max(w.widget.width(),w.widget.sizeHint().width()),max(w.widget.sizeHint().height(),w.widget.height()))
        window.show()
        if w.exec():
            print(w.usernameLineEdit.text())
    def showAddGroupMessageBox(self):
        print("in showAddGroupMessageBox")
        window = FramelessWindow()
        w = AddGroupMessageBox(window)

        w.layout().setContentsMargins(0,0,0,0)
        w.layout().setSpacing(0)
        w.adjustSize()
        window.resize(max(w.widget.width(),w.widget.sizeHint().width()),max(w.widget.sizeHint().height(),w.widget.height()))
        window.show()
        if w.exec():
            print(w.groupIDLineEdit.text())
    def showCreateGroupMessageBox(self):
        print("in showCreateGroupMessageBox")
        window = FramelessWindow()
        w = CreateGroupMessageBox(window)

        w.layout().setContentsMargins(0,0,0,0)
        w.layout().setSpacing(0)
        w.adjustSize()
        w.CreateGroupSuccess.connect(self._create_group)
        window.resize(max(w.widget.width(),w.widget.sizeHint().width()),max(w.widget.sizeHint().height(),w.widget.height()))
        window.show()
        if w.exec():
            print(w.groupNameLineEdit.text())
    def RequestInfoWidgetClosed(self):
        print("in RequestInfoWidgetClosed")
        self.RequestInfoIsShow = False
        if self.requestInfoWidget:
            self.requestInfoWidget.deleteLater()
        self.requestInfoWidget = None



    def showRequestInfo(self):
        print("in showRequestInfo")
        self.badgeWidget.clearBadge()
        if not self.RequestInfoIsShow:
            self.RequestInfoIsShow = True
            self.requestInfoWidget = RequestInfoWidget()
            self.requestInfoWidget.closed.connect(self.RequestInfoWidgetClosed)
            self.requestInfoWidget.show()
        else:
            self.requestInfoWidget.activateWindow()








    def addSubInterface(self, widget, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.navigation.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )










    def AddFriend(self,json_data):
        print("in AddFriend")
        contactItem = ContactItemWidget()
        contactItem.setAvatar(json_data["avatar"])
        contactItem.setNickname(json_data["nickname"])
        contactItem.setUsername(json_data["username"])
        self.addContactItem(contactItem)
        chatItem = ChatItemWidget()
        chatItem.setAvatar(json_data["avatar"])
        chatItem.setName(f'{json_data["nickname"]} (ID:{json_data["username"]})')
        message = DataManager.db_manager.get_messages_with_friend_by_countDESC(json_data["username"],1)
        if message:
            chatItem.setMessage(message[0][0])
            chatItem.setTime(message[0][1])
        else:
            chatItem.setMessage("A friend has been added，Chat history is available")
        self.addChatItem(chatItem)
        self.friends[json_data["username"]] = (contactItem,chatItem)
        chatItem.doubleclicked.connect(lambda :self.FriendItemClicked(json_data["username"]))







    def AddGroup(self,json_data):
        print("in AddGroup")
        contactItem = ContactItemWidget()
        contactItem.setAvatar(DEFAULT_GROUP_AVATAR)
        contactItem.setGroupID(json_data["group_id"])
        contactItem.setGroupName(json_data["group_name"])
        self.addGroupItem(contactItem)
        chatItem = ChatItemWidget(None,True)
        chatItem.setAvatar(DEFAULT_GROUP_AVATAR)
        chatItem.setName(f'{json_data["group_name"]} (ID:{json_data["group_id"]})')
        message = DataManager.db_manager.get_latest_group_messages(json_data["group_id"],1)
        if message:
            chatItem.setMessage(message[0][0])
            chatItem.setTime(message[0][1])
        else:
            chatItem.setMessage("alreadyJoin a group")
        self.addChatItem(chatItem)
        self.groups[int(json_data["group_id"])] = (contactItem,chatItem)
        chatItem.doubleclicked.connect(lambda :self.groupChatItemClicked(json_data["group_id"]))







    def deleteFriend(self,data):
        print("in deleteFriend")
        json_data = data
        if json_data["username"] in self.friends:
            contactItem,chatItem = self.friends[json_data["username"]]
            self.lv_friends.takeItem(self.lv_friends.row(contactItem))
            self.lv_nowChatting.takeItem(self.lv_nowChatting.row(chatItem))
            self.friends.pop(json_data["username"])



    def deleteGroup(self,data):
        print("in deleteGroup")
        json_data = data
        if int(json_data["group_id"]) in self.groups:
            contactItem,chatItem = self.groups[int(json_data["group_id"])]
            self.lv_groups.takeItem(self.lv_groups.row(contactItem))
            self.lv_nowChatting.takeItem(self.lv_nowChatting.row(chatItem))
            self.groups.pop(int(json_data["group_id"]))



    def addChatItem(self,widget :ChatItemWidget):
        item = QListWidgetItem(self.lv_nowChatting)
        item.setSizeHint(widget.sizeHint())
        self.lv_nowChatting.addItem(item)
        self.lv_nowChatting.setItemWidget(item,widget)




    def addContactItem(self,widget :ContactItemWidget):
        item = QListWidgetItem(self.lv_friends)
        item.setSizeHint(widget.sizeHint())
        self.lv_friends.addItem(item)
        self.lv_friends.setItemWidget(item,widget)


    def addGroupItem(self,widget :ContactItemWidget):
        item = QListWidgetItem(self.lv_groups)
        item.setSizeHint(widget.sizeHint())
        self.lv_groups.addItem(item)
        self.lv_groups.setItemWidget(item,widget)




    def paintEvent(self, a0) -> None:
        painter = QPainter(self)
        painter.drawPixmap(self.rect(),QPixmap(":/images/ContactsPanelBackground.jpg").scaled(self.size(),Qt.KeepAspectRatioByExpanding))
        self.add_button.move(15,self.height()-self.navigation.height()-self.add_button.height()-20)
        return super().paintEvent(a0)


    def event(self, event: QtCore.QEvent):
        if event.type() == ReceiveMessageEvent.EventType:
            if isinstance(event, ReceiveMessageEvent):
                data = event.data
                if event.fromGroup:
                    if int(data["group_id"]) in self.groups:
                        contactItem,chatItem = self.groups[int(data["group_id"])]
                        chatItem.setMessage(data["content"])
                        chatItem.setTime(data["timestamp"])
                        chatItem.increaseCount()
                else:
                    if data["friend_username"] in self.friends:
                        contactItem,chatItem = self.friends[data["friend_username"]]
                        chatItem.setMessage(data["content"])
                        chatItem.setTime(data["timestamp"])
                        chatItem.increaseCount()
            else:
                print("event.type() == ReceiveMessageEvent.EventType but not isinstance(event, ReceiveMessageEvent)")
            event.accept()
            return True
        return super().event(event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainContactsWidget()
    widget.addChatItem(ChatItemWidget())
    widget.addContactItem(ContactItemWidget())
    widget.addGroupItem(ContactItemWidget())
    widget.show()
    def print_visible_windows(event :QCloseEvent):
        for a in app.topLevelWidgets():
            if a.isVisible() and isinstance(a, QWidget):
                print(f"Visible window: {a.windowTitle()}")
                a.close()
        event.accept()
    widget.closeEvent = print_visible_windows
    sys.exit(app.exec_())