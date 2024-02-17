from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtProperty, Qt, QSize
from PyQt5.QtGui import QPixmap, QFontMetrics
import resources_rc
import sys
from ui.Ui_ContactItemWidget import Ui_ContactItemWidget
from FriendChatWindow import FriendChatWindow
from GroupChatWindow import GroupChatWindow
import DataManager

class ContactItemWidget(Ui_ContactItemWidget, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Rest of the code...

    def setAvatar(self, avatar):
        self.AvatarWidget.setPixmap(avatar.scaled(65, 65, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    @pyqtProperty(QPixmap)
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        self._avatar = avatar
        self.setAvatar(avatar)

    @pyqtProperty(str)
    def groupID(self):
        return self.groupID

    @groupID.setter
    def groupID(self, groupID):
        self.groupID = groupID
        if self.groupID:
            self.setGroupID(groupID)

    @pyqtProperty(str)
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        self.username = username
        if self.username:
            self.setUsername(username)

    @pyqtProperty(str)
    def groupName(self):
        return self.groupName

    @groupName.setter
    def groupName(self, groupName):
        self.groupName = groupName
        if self.groupName:
            self.setGroupName(groupName)

    @pyqtProperty(str)
    def nickname(self):
        return self.nickname

    @nickname.setter
    def nickname(self, nickname):
        self.nickname = nickname
        if self.nickname:
            self.setNickname(nickname)

    def setGroupID(self, groupID):
        text = f"(ID: {groupID})"
        elidfont = QFontMetrics(self.username_or_groupID.font())
        elidedText = elidfont.elidedText(text, Qt.ElideRight, self.width() - self.AvatarWidget.width() - 5)
        self.username_or_groupID.setText(elidedText)
        self.groupID = groupID
        self.username = None

    def setGroupName(self, groupName):
        text = groupName
        elidfont = QFontMetrics(self.nickname_or_groupName.font())
        elidedText = elidfont.elidedText(text, Qt.ElideRight, self.width() - self.AvatarWidget.width() - 5)
        self.nickname_or_groupName.setText(elidedText)
        self.groupName = groupName
        self.nickname = None

    def sizeHint(self):
        return QSize(super().sizeHint().width(), self.minimumHeight())

    def resizeEvent(self, event):
        ret = super().resizeEvent(event)
        if self.groupID:
            self.setGroupID(self.groupID)
        elif self.username:
            self.setUsername(self.username)
        if self.groupName:
            self.setGroupName(self.groupName)
        elif self.nickname:
            self.setNickname(self.nickname)
        return ret

    def mouseDoubleClickEvent(self, event):
        ret = super().mouseDoubleClickEvent(event)
        self.openChatWindow()
        if self.username:
            print("ContactItemWidget: mouseDoubleClickEvent: username:", self.username)
            avatar = DataManager.db_manager.getAvatarByUsername(self.username)
            if avatar and self._avatar != avatar:
                self.setAvatar(avatar)
        return ret

    def openChatWindow(self):
        if self.groupID is not None and self.groupName is not None:
            if self.chatWindow is None:
                self.chatWindow = GroupChatWindow(None, self.groupID, self.groupName)
                self.chatWindow.closed.connect(lambda: setattr(self, "chatWindow", None))
                self.chatWindow.show()
            else:
                self.chatWindow.show()
        elif self.username is not None and self.nickname is not None:
            if self.chatWindow is None:
                self.chatWindow = FriendChatWindow(None, self.username, self.nickname)
                self.chatWindow.closed.connect(lambda: setattr(self, "chatWindow", None))
                self.chatWindow.show()
            else:
                self.chatWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    widget = ContactItemWidget(window)
    window.show()
    sys.exit(app.exec_())