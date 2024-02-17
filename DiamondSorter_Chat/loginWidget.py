from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtCore import QRegExp,QPropertyAnimation, pyqtProperty, Qt,QPoint,pyqtSlot
from PyQt5.QtGui import QRegExpValidator,QPainter, QLinearGradient, QPixmap, QColor,QRadialGradient,QBrush,QIcon
import math
from resource.resources_rc import *
from flask import request
from flask import jsonify
from flask import jsonify, current_app
from PyQt5.QtWidgets import QMessageBox, QWidget, QPushButton

def rectangle_path(value, width, height):
    # 计算周长
    perimeter = 5 * (width + height)
    value = value/4
    # 计算每个部分的比例长度
    bottom_top_ratio = width / perimeter
    left_right_ratio = height / perimeter

    # 根据比例和 value 计算坐标
    if value < bottom_top_ratio:
        # 从 (0,0) 到 (width,0)
        return (value / bottom_top_ratio * width, 0)
    elif value < bottom_top_ratio + left_right_ratio:
        # 从 (width,0) 到 (width,height)
        return (width, (value - bottom_top_ratio) / left_right_ratio * height)
    elif value < 2 * bottom_top_ratio + left_right_ratio:
        # 从 (width,height) 到 (0,height)
        return ((1 - (value - bottom_top_ratio - left_right_ratio) / bottom_top_ratio) * width, height)
    else:
        # 从 (0,height) 到 (0,0)
        return (0, (1 - (value - 2 * bottom_top_ratio - left_right_ratio) / left_right_ratio) * height)
def cycle_path(t, width, height):
    t = t/4
    x = ((1+math.sin(t * 2 * math.pi))/2)*width
    y = ((1+math.sin(t * 4 * math.pi))/2)*height
    return (float(x),float(y))
    
    
    
class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Other initialization code...

        self.quick_signin_button = QPushButton("Quick Sign In", self)
        self.quick_signin_button.setObjectName("quick_signin_button")
        self.quick_signin_button.clicked.connect(self.quick_signin)
        
    @pyqtSlot()
    def quick_signin(self):
        username = self.comb_username.currentText()
        if not username:
            QMessageBox.warning(self, "Warning", "Please enter a username.")
            return
        
        # Perform the login process with the provided username
        response = self.login_with_username(username)
        
        # Handle the login response
        if response.status_code == 200:
            # Login successful
            data = response.json()
            # Perform additional actions after successful login
            print(f"Login successful! User ID: {data['user_id']}")
            # Proceed to the chat interface
            self.open_chat_interface()
        else:
            # Login failed
            error_message = response.json().get('message', 'Unknown error')
            # Handle the error and display an appropriate message to the user
            print(f"Login failed: {error_message}")

    def login_with_username(self, username):
        # Implement the login logic with the provided username.
        # Return the response from the server.
        # You can replace the following code with your actual implementation.
        # This is just a placeholder.
        return jsonify({
            "message": "Login successful!",
            "status": 200,
            "user_id": 1
        })

    def open_chat_interface(self):
        # Implement the code to open the chat interface.
        # This is a placeholder. Replace it with your own implementation.
        print("Opening chat interface...")
        

@pyqtSlot(bytes)
class BackgroundWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._gradient_shift = 0
        # self.setMinimumSize(800, 600)
        self.gradient1 = QLinearGradient(0, 0, self.width(), self.height())
        self.gradient1.setColorAt(0, QColor('#5ee7df'))  # 深蓝
        self.gradient1.setColorAt(0.5, QColor('#02A7A7')) # 橙色
        self.gradient1.setColorAt(1, QColor('#b490ca'))  # 黄色
        self.gradient2 = QRadialGradient(QPoint(self.width()//2, self.height()//2), max(self.height()//2, self.width()//2))
        self.gradient2.setColorAt(0, QColor('#667eea'))  # 深海蓝
        self.gradient2.setColorAt(0.5, QColor('#fff1eb')) # 中等海蓝
        self.gradient2.setColorAt(1, QColor('#764ba2'))  # 浅海水蓝
        self.gradient3 = QLinearGradient(0, 0, self.width(), self.height())
        self.gradient3.setColorAt(0, QColor('#E0BBE4'))  # 浅紫色
        self.gradient3.setColorAt(0.5, QColor('#957DAD')) # 粉红色
        self.gradient3.setColorAt(1, QColor('#D291BC'))  # 鲜绿色
        self.animation = QPropertyAnimation(self, b"gradient_shift")
        self.animation.setDuration(5000)  # 15 seconds
        self.animation.setStartValue(0)
        self.animation.setEndValue(4)
        self.animation.setLoopCount(-1)  # Infinite loop
        self.animation.start()
    @pyqtProperty(float)
    def gradient_shift(self):
        return self._gradient_shift

    @gradient_shift.setter
    def gradient_shift(self, value):
        self._gradient_shift = value
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        start_point = rectangle_path(self._gradient_shift%4, self.width(), self.height())
        end_point = rectangle_path((self._gradient_shift + 2)%4, self.width(), self.height())
        self.gradient1.setStart(*start_point)
        self.gradient1.setFinalStop(*end_point)
        start_point = rectangle_path((self._gradient_shift*2)%4, self.width(), self.height())
        end_point = rectangle_path(((self._gradient_shift)*2+2)%4, self.width(), self.height())
        self.gradient3.setStart(*start_point)
        self.gradient3.setFinalStop(*end_point)
        (x,y) = cycle_path(self._gradient_shift, self.width(), self.height())
        self.gradient2.setCenter(x,y)
        self.gradient2.setRadius(min(self.width(),self.height()))
        self.gradient2.setFocalPoint(x,y)
        painter.setBrush(QBrush(self.gradient1))
        painter.setOpacity(0.5)
        painter.drawRect(0, 0, self.width(), self.height())
        painter.setBrush(QBrush(self.gradient2))
        painter.setOpacity(0.5)
        painter.drawRect(0, 0, self.width(), self.height())
        # painter.setBrush(QBrush(self.gradient3))
        # painter.setOpacity(0.33)
        # painter.drawRect(0, 0, self.width(), self.height())
from ui.Ui_loginPanel import Ui_LoginPanel
from Threads import loginProcessThread
import json
from RegisterWidget import RegisterWidget
import DataManager
from Threads import *
from utils import AvatarFromEncodedText
class LoginWidget(Ui_LoginPanel,BackgroundWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._opacity = 1
        self.setGeometry(0, 0, 1 * self.width(), 1 * self.height())
        self.setWindowTitle("Diamond Sorter - Online Chat")

        pixmap = QPixmap(':/images/logo.png')
        smaller_pixmap = pixmap.scaled(216, 72, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.imgLB_logo.setImage(smaller_pixmap)
        pixmap = QPixmap(':/images/qr-code.png')
        smaller_pixmap = pixmap.scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.bt_QRcode.setIcon(QIcon(smaller_pixmap))
        self.bt_QRcode.clicked.connect(self.on_img_QRcode_clicked)
        self.bt_login.clicked.connect(self.on_bt_login_clicked)
        self.loginThread = loginProcessThread(self)
        self.loginThread.loginSuccess.connect(self.loginSuccess)
        self.loginThread.loginFailed.connect(self.loginFailed)
        self.fade_out_animation = None
        self.registerWidgetisShow = False
        regex = QRegExp("^[A-Za-z0-9_]+$")
        validator = QRegExpValidator(regex)
        self.isclosed = False
        self.comb_username.setValidator(validator)
        users = DataManager.db_manager.get_all_saved_users()
        print(users)
        if users:
            for user in users:
                self.comb_username.addItem(user[1])
            self.comb_username.setCurrentIndex(0)
        if DataManager.db_manager.get_user_session(self.comb_username.currentText()):
            self.PasswordLineEdit.setText("123456")
            self.cb_rememberPassword.setChecked(True)
        self.comb_username.selectionChanged.connect(self.on_comb_username_selectionChanged)

                
            
        
        
        
    def on_comb_username_selectionChanged(self):
        session_id = DataManager.db_manager.get_user_session(self.comb_username.currentText())
        if session_id:
            self.PasswordLineEdit.setText("123456")
            self.cb_rememberPassword.setChecked(True)
        else:
            self.PasswordLineEdit.setText("")
            self.cb_rememberPassword.setChecked(False)
            
            
            
            
            
    def resetLoginThread(self):
        self.loginThread.stop()
        self.loginThread.deleteLater()
        self.loginThread = loginProcessThread(self)
        self.loginThread.loginSuccess.connect(self.loginSuccess)
        self.loginThread.loginFailed.connect(self.loginFailed)
        
        
        
        
        
        
        
    def start_fade_out(self):
        self.fade_out_animation = QPropertyAnimation(self, b"opacity")
        self.fade_out_animation.setDuration(500)  # 动画时长 2000 毫秒
        self.fade_out_animation.setStartValue(1)   # 开始时的透明度
        self.fade_out_animation.setEndValue(0)     # 结束时的透明度
        self.fade_out_animation.finished.connect(self.close)  # 动画完成后关闭窗口
        self.fade_out_animation.start()
        
        
        
    @pyqtProperty(float)
    def opacity(self):
        return self._opacity
        
        
        
    @opacity.setter
    def opacity(self, opacity):
        self._opacity = opacity
        self.setWindowOpacity(opacity)
        
        
        
    @pyqtSlot()
    def on_bt_login_clicked(self):
        self.bt_login.setDisabled(False)
        self.stackedWidget_login.setCurrentIndex(1)
        session_id = DataManager.db_manager.get_user_session(self.comb_username.currentText())
        if session_id:
            self.loginThread.setLoginInfo(self.comb_username.currentText(),self.PasswordLineEdit.text(),session_id)
        else:
            self.loginThread.setLoginInfo(self.comb_username.currentText(),self.PasswordLineEdit.text())
        self.loginThread.start()
        
        
    @pyqtSlot(bytes)
    def loginSuccess(self,data):
        self.bt_login.setDisabled(False)
        self.stackedWidget_login.setCurrentIndex(0)
        json_data = json.loads(data.decode('utf-8'))
        self.resetLoginThread()
        
        print("loginSuccess")
        print(json_data)
        if self.cb_rememberPassword.isChecked():
            if not DataManager.db_manager.get_user_session(json_data["username"]):
                with DataManager.db_manager.lock:
                    DataManager.db_manager.set_user_session(json_data["username"], json_data["session_id"])      
        else:
            with DataManager.db_manager.lock:
                DataManager.db_manager.set_user_remember_password(json_data["username"],False)
        
        
        DataManager.dataManager.setUserInfo(json_data["username"],json_data["nickname"],AvatarFromEncodedText(json_data["avatar"]),json_data["session_id"])
    @pyqtSlot(bytes)
    
    
    
    
    def loginFailed(self,data):
        self.bt_login.setDisabled(False)
        self.stackedWidget_login.setCurrentIndex(0)
        json_data = json.loads(data.decode('utf-8'))
        self.resetLoginThread()
        if json_data["status"] == Status.OUTDATED.value:
            QMessageBox.warning(self, "warnings", "Remember password has expired，Please re-enter your password")
            self.cb_rememberPassword.setChecked(False)
            DataManager.db_manager.set_user_remember_password(self.comb_username.currentText(),False)
            self.PasswordLineEdit.setText("")
        else:
            QMessageBox.warning(self, "warnings", f"Login Failure，{json_data['message']}")
        print("loginFailed")
        print(json_data)
        
        
        
        
    #处理注册回调函数
    
    @pyqtSlot()
    def on_lb_register_clicked(self):
        if self.registerWidgetisShow:
            self.registerWidget.activateWindow()
            return
        self.registerWidgetisShow = True
        self.registerWidget = RegisterWidget()
        self.registerWidget.closed.connect(self.registerWidgetClosed)
        self.registerWidget.show()
        
        
        
    @pyqtSlot()
    def registerWidgetClosed(self):
        self.registerWidgetisShow = False
        self.registerWidget.deleteLater()
        self.registerWidget = None
        
        
        
        
    #Handling the retrieve password callback function
    @pyqtSlot()
    def on_lb_findPassword_clicked(self):
        pass


    @pyqtSlot()
    def on_img_QRcode_clicked(self):
        print("on_img_QRcode_clicked")
        self.imgLB_logo.setScaledContents(True)
        self.imgLB_logo.setFixedSize(self.imgLB_logo.width() * 5, self.imgLB_logo.height() * 5)
    
        # Load the image using QPixmap
        image_path = r"\resource\images\qr-code.png"
        pixmap = QPixmap(image_path)
    
        # Display the image in the QLabel
        self.imgLB_logo.setPixmap(pixmap)
        
       
        
    def closeEvent(self, event) -> None:
        if self.isclosed:
            return super().closeEvent(event)
        else:
            self.isclosed = True
            self.start_fade_out()
            event.ignore()


