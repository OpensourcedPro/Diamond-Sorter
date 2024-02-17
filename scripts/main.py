import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class ConfigApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('domain_sorter.ui', self)
        # Remove this line: self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = ConfigApp()
    config.show()
    sys.exit(app.exec_())