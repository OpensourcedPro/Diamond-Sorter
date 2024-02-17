from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QHBoxLayout, QLabel, QWidget, QSizePolicy,QSpacerItem
from PyQt5.QtCore import pyqtSignal, pyqtProperty, Qt,pyqtSlot,QSize
from PyQt5.QtGui import QTextCursor,QTextDocument, QPixmap,QFont,QFontMetrics
from ui.Ui_ChatItemWidget import Ui_ChatItemWidget
import resources_rc
import sys
from datetime import datetime, timedelta
from config import *
import DataManager
from Threads import GetAvatarThread
class MessageTimeLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Arial Unicode MS", 10))
        self.setFixedHeight(10)
        self.setWordWrap(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred , QSizePolicy.Policy.Preferred )
        self.setSizePolicy(sizePolicy)
    
        self.setText("")
        self.adjustSize()
        
    def setTime(self, timestamp):
        message_time = datetime.fromtimestamp(timestamp)
        current_time = datetime.now()
        delta = current_time - message_time
        if message_time.date() == current_time.date():
            self.setText(message_time.strftime("%H:%M"))
        elif message_time.date() == current_time.date() - timedelta(days=1):
            self.setText("yesterday")
        else:
            self.setText(message_time.strftime("%m-%d"))
        self.adjustSize()
class MessageCountLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("")
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Arial Unicode MS", 10))
        self.setFixedHeight(15)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred , QSizePolicy.Policy.Preferred)
        self.setSizePolicy(sizePolicy)
        # 根据文本内容调整大小
        self.adjustSize()
        
        # 设置样式以得到椭圆形的背景和边框
        self.setStyleSheet("""MessageCountLabel { 
                border: 0px solid gray;
                border-radius: 5px;
                background-color: transparent;
                padding: 0px;
                }
        """)
    def setCount(self,count):
        if count>99:
            self.setText("99+")
            self.setStyleSheet("""MessageCountLabel { 
                border: 0px solid gray;
                border-radius: 5px;
                background-color: lightgray;
                padding: 0px;
                }
        """)
        elif count>0:
            self.setText(str(count))
            self.setStyleSheet("""MessageCountLabel { 
                border: 0px solid gray;
                border-radius: 5px;
                background-color: lightgray;
                padding: 0px;
                }
        """)
        else:
            self.setText("")
            self.setStyleSheet("""MessageCountLabel { 
                border: 0px solid gray;
                border-radius: 5px;
                background-color: transparent;
                padding: 0px;
                }
        """)
class ChatItemWidget(Ui_ChatItemWidget,QWidget):
    doubleclicked = pyqtSignal()
    def __init__(self, parent=None,isgroup=False) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.AvatarWidget.setPixmap(QPixmap(":/images/DefaultGroupAvatar.png").scaled(65, 65, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.AvatarWidget.setStyleSheet("margin: 0px; padding: 0px;")  # 移除按钮的外边距和内边距
        self.verticalLayout.setSpacing(0)  # 移除控件间的间距
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)  # 移除布局边距
        self.horizontalLayout.setSpacing(0)  # 移除控件间的间距
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)  # 移除布局边距
        self.lb_name.setStyleSheet("margin: 0px; padding: 0px;")  # 移除按钮的外边距和内边距
        self.lb_message.setStyleSheet("margin: 0px; padding: 0px;")  # 移除按钮的外边距和内边距
        self.setStyleSheet("ChatItemWidget { margin: 0px; padding: 0px;background-color: transparent; }")  # 移除按钮的外边距和内边距
        self.message_info = QWidget(self)
        self.message_info.setFixedHeight(self.height()*0.5)
        message_info_layout = QVBoxLayout()
        self.latest_message_time = MessageTimeLabel()
        self.message_count = MessageCountLabel()
        horizontal_layout = QHBoxLayout()
        spacer = QSpacerItem(1, 1, QSizePolicy.Policy.Expanding , QSizePolicy.Policy.Expanding )
        horizontal_layout.addSpacerItem(spacer)
        message_info_layout.addWidget(self.latest_message_time)
        message_info_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Expanding , QSizePolicy.Policy.Expanding ))
        message_info_layout.addWidget(self.message_count)
        horizontal_layout.addLayout(message_info_layout)
        self.message_info.setLayout(horizontal_layout)
        parent_width = self.width()
        floating_width = self.message_info.width()
        new_x = parent_width - floating_width
        self.message_info.move(new_x, 20)
        self._message = None
        self._name = None
        self.avatarThread = None
        self.count = 0
        self._avatar = None
        self.isgroup = isgroup
        
    def resizeEvent(self, event):
        # 获取父控件的当前宽度
        ret = super().resizeEvent(event)
        parent_width = self.width()
        # 获取浮动控件的宽度
        floating_width = self.message_info.width()
        # 计算浮动控件新的 x 坐标位置
        new_x = parent_width - floating_width
        # 移动浮动控件到父控件的最右侧
        self.message_info.move(new_x, self.message_info.y())
        if self._message:
            self.setMessage(self._message)
        if self._name:
            self.setName(self._name)
        return ret
    def setAvatar(self,avatar):
        self._avatar = avatar
        if isinstance(avatar,bytes):
            pixmap = QPixmap()
            if pixmap.loadFromData(avatar):
                self.AvatarWidget.setPixmap(pixmap.scaled(65,65,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            self.AvatarWidget.setPixmap(QPixmap(avatar).scaled(65,65,Qt.KeepAspectRatio,Qt.SmoothTransformation))
    def setName(self,name):
        elidfont = QFontMetrics(self.lb_name.font())
        elidedText = elidfont.elidedText(name, Qt.ElideRight, self.width()-self.AvatarWidget.width()-5)
        self.lb_name.setText(elidedText)
        self._name = name
    def setMessage(self,message):
        self._message = message
        doc = QTextDocument()
        doc.setHtml(message)
        doc.setDefaultFont(self.lb_message.font())

        # 使用 QFontMetrics 计算文本的宽度
        metrics = QFontMetrics(self.lb_message.font())
        cursor = QTextCursor(doc)
        cursor.movePosition(QTextCursor.Start)
        plainText = ""
        position = 0
        isend = True
        # 遍历文档字符
        while not cursor.atEnd():
            cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            char = cursor.selectedText()
            if metrics.width(plainText+char) <= self.width()-self.AvatarWidget.width()-5:
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
        self.lb_message.setText(cursor.selection().toHtml())

        # elidfont = QFontMetrics(self.lb_message.font())
        # elidedText = elidfont.elidedText(message, Qt.ElideRight, self.width()-self.AvatarWidget.width()-5)
        # self.lb_message.setText(elidedText)
        # self._message = message
    def setTime(self,timestamp):
        self.latest_message_time.setTime(timestamp)
    def setCount(self,count):
        if self.count !=count:
            self.count = count
            self.message_count.setCount(count)
    def increaseCount(self):
        self.setCount(self.count+1)
    def clearCount(self):
        self.setCount(0)
    def sizeHint(self):
        return QSize(super().sizeHint().width(),self.minimumHeight())
    def mouseDoubleClickEvent(self, a0) -> None:
        self.doubleclicked.emit()
        self.clearCount()
        if self._name:
            if not self.isgroup:
                avatar = DataManager.db_manager.getAvatarByUsername(self._name[self._name.rfind('(')+4:self._name.rfind(')')])
                if avatar==DEFAULT_CONTACT_AVATAR:
                    t =  GetAvatarThread()
                    import json
                    import base64
                    t.setQueryInfo(DataManager.dataManager.username,DataManager.dataManager.session_id,self._name[self._name.rfind('(')+4:self._name.rfind(')')])
                    def success(data):
                        json_data = json.loads(data.decode("utf8"))
                        encoded_bytes = json_data["avatar"].encode('utf-8')
                        avatar = base64.b64decode(encoded_bytes)
                        DataManager.db_manager.setAvatarByUsername(self._name[self._name.rfind('(')+4:self._name.rfind(')')],avatar)
                        t.stop()
                        self.setAvatar(avatar)
                        print("get avatar success!")
                    def fail(data):
                        t.stop()
                        print("getavatar fail!",data.decode("utf8"))
                    t.getAvatarSuccess.connect(success)
                    t.getAvatarFailed.connect(fail)
                    t.start()
                elif avatar and self._avatar!=avatar:
                    self.setAvatar(avatar)
            else:
                avatar = DEFAULT_GROUP_AVATAR
                self.setAvatar(avatar)
        return super().mouseDoubleClickEvent(a0)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setLayout(QVBoxLayout())
    window.layout().addWidget(ChatItemWidget())
    window.show()
    sys.exit(app.exec_())