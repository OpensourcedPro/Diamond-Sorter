from ui.Ui_MessageItemWidget import Ui_MessageItemWidget
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QSpacerItem,QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import resources_rc
from qfluentwidgets import InfoLevel
class MessageItemWidget(Ui_MessageItemWidget,QWidget):
    def __init__(self, parent = None,isRight=False) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.avatar.setPixmap(QPixmap(":/images/DefaultContactAvatar.png").scaled(40,40,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        self.groupID = None
        self.username = None
        self.groupName = None
        self.nickname = None
        self.content = None
        self.iconIsSendSuccess.setLevel(InfoLevel.INFOAMTION)
        self.document = self.te_content.document()
        self.te_content.setLineWrapMode(QTextEdit.NoWrap)
        self.te_content.document().contentsChanged.connect(self.textAreaChange)
        if isRight:
            self.moveToRight()
    def textAreaChange(self):
        self.document.adjustSize()
 
        newWidth = self.document.size().width() + 20
        newHeight = self.document.size().height() + 20
        if newWidth != self.te_content.width():
            self.te_content.setMaximumWidth(newWidth)
        if newHeight != self.te_content.height():
            self.te_content.setMaximumHeight(newHeight)
        self.adjustSize()
    def setAvatar(self,avatar):
        if isinstance(avatar,bytes):
            pixmap = QPixmap()
            if pixmap.loadFromData(avatar):
                self.avatar.setPixmap(pixmap.scaled(40,40,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            self.avatar.setPixmap(QPixmap(avatar).scaled(40,40,Qt.KeepAspectRatio,Qt.SmoothTransformation))
    def setUsername(self,username):
        self.username = username
        self.groupID = None
        self.updateName()
    def setNickname(self,nickname):
        self.nickname = nickname
        self.groupName = None
        self.updateName()
    def setGroupID(self,groupID):
        self.groupID = groupID
        self.username = None
        self.updateName()
    def setGroupName(self,groupName):
        self.groupName = groupName
        self.nickname = None
        self.updateName()
    def updateName(self):
        text = f"{self.nickname if self.nickname else self.groupName} (ID: {self.username if self.username else self.groupID})"
        self.lb_name.setText(text)
    def setContent(self,content):
        self.te_content.setHtml(content)
    def setSendSuccess(self,isSuccess):
        if isSuccess:
            self.iconIsSendSuccess.setLevel(InfoLevel.SUCCESS)
        else:
            self.iconIsSendSuccess.setLevel(InfoLevel.ERROR)
    def moveToRight(self):
        self.horizontalLayout_2.removeItem(self.horizontalLayout_2.itemAt(1))
        self.horizontalLayout_2.removeItem(self.horizontalLayout_2.itemAt(0))
        self.verticalLayout_2.removeItem(self.verticalLayout_2.itemAt(2))
        self.verticalLayout_2.removeItem(self.verticalLayout_2.itemAt(1))
        self.verticalLayout_2.removeItem(self.verticalLayout_2.itemAt(0))
        self.verticalLayout.removeWidget(self.lb_name)
        self.verticalLayout.removeWidget(self.te_content)
        self.verticalLayout.insertWidget(0,self.lb_name,0,Qt.AlignRight)
        self.verticalLayout.insertWidget(1,self.te_content,0,Qt.AlignRight)
        spacerItem2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addWidget(self.avatar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0,1)
        self.horizontalLayout_2.setStretch(1,0)
        self.horizontalLayout_2.activate()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # a = MessageItemWidget()
    # a.setUsername("lgl")
    # a.setNickname("mono")
    # a.setContent("你好呀！宝贝！")
    # a.setSendSuccess(False)
    # a.show()
    b = MessageItemWidget(None,True)
    b.setUsername("lgl")
    b.setNickname("mono")
    b.setContent("Hello baby!")
    b.setSendSuccess(False)
    b.show()
    sys.exit(app.exec_())