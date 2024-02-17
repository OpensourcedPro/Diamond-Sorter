import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox, QWidget
from PyQt5.QtCore import QRegExp,pyqtSignal, pyqtProperty,pyqtSlot
from PyQt5.QtGui import QRegExpValidator
from ui.Ui_RegisterWidget import Ui_RegisterWidget
from Threads import RegisterProcessThread
import json
class RegisterWidget(Ui_RegisterWidget,QWidget):
    closed = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bt_ok.clicked.connect(self.on_btn_register_clicked)
        self.bt_cancel.clicked.connect(self.on_btn_cancel_clicked)
        self.registerThread = RegisterProcessThread(self)
        self.registerThread.registerSuccess.connect(self.registerSuccess)
        self.registerThread.registerFailed.connect(self.registerFailed)
        regex = QRegExp("^[A-Za-z0-9_]+$")
        validator = QRegExpValidator(regex)
        self.le_username.setValidator(validator)
    def on_btn_register_clicked(self):
        username = self.le_username.text()
        password = self.le_password.text()
        if username == "" or password == "":
            QMessageBox.critical(self,"incorrect","User name, password can not be empty")
            return
        doublecheck_password = self.le_doublecheck.text()
        if password != doublecheck_password:
            QMessageBox.critical(self,"incorrect","Inconsistent passwords entered twice")
            return
        nickname = self.le_nickname.text()
        if nickname == "":
            self.registerThread.setLoginInfo(username,password)
        else:
            self.registerThread.setLoginInfo(username,password,nickname)
        self.registerThread.start()
    @pyqtSlot(bytes)
    def registerSuccess(self,response):
        print("Register Success")
        QMessageBox.information(self,"successes","Successful Registration")
        self.registerThread.stop()
        self.close()
    @pyqtSlot(bytes)
    def registerFailed(self,response):
        print("register failed")
        QMessageBox.critical(self,"incorrect","Registration Failure\nmessage:"+json.loads(response.decode('utf-8'))["message"])
        self.registerThread.stop()
        self.registerThread.deleteLater()
        self.registerThread = RegisterProcessThread()
        self.registerThread.registerSuccess.connect(self.registerSuccess)
        self.registerThread.registerFailed.connect(self.registerFailed)
    def on_btn_cancel_clicked(self):
        self.close()
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.registerThread.stop()
        self.registerThread.deleteLater()
        self.closed.emit()
        return super().closeEvent(event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterWidget()

    window.show()
    sys.exit(app.exec_())