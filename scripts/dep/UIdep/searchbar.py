from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
import os

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

back_png = current_dir+'/UIres/back.png'
forward_png = current_dir+'/UIres/arrow-right.png'
reload_png = current_dir+'/UIres/reload.png'
home_png = current_dir+'/UIres/diamond.png'
settings_png = current_dir+'/UIres/settings.png'
close_png = current_dir+'/UIres/close.png'


AutoCompleteWords = [
    "github.com", "youtube.com", "twitch.tv", "reddit.com", "spotify.com", "github.com/cookie0o", "facebook.com", "wikipedia.com", "amazon.com", "instagram.com", "yahoo.com", "twitter.com",
    "naver.com", "bit.ly", "vk.com", "live.com", "gmail.com", "google.com", "duckduckgo.com"
]


class CheckableComboBox(QtWidgets.QComboBox):
	def __init__(self):
		super().__init__()
		self._changed = False

		self.view().pressed.connect(self.handleItemPressed)

	def setItemChecked(self, index, checked=False):
		item = self.model().item(index, self.modelColumn()) # QStandardItem object

		if checked:
			item.setCheckState(QtCore.Qt.Checked)
		else:
			item.setCheckState(QtCore.Qt.Unchecked)

	def handleItemPressed(self, index):
		item = self.model().itemFromIndex(index)

		if item.checkState() == QtCore.Qt.Checked:
			item.setCheckState(QtCore.Qt.Unchecked)
		else:
			item.setCheckState(QtCore.Qt.Checked)
		self._changed = True


	def hidePopup(self):
		if not self._changed:
			super().hidePopup()
		self._changed = False

	def itemChecked(self, index):
		item = self.model().item(index, self.modelColumn())
		return item.checkState() == QtCore.Qt.Checked

# select everything in the search bar when selected
class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)
        self.readyToEdit = True

    def mousePressEvent(self, e, Parent=None):
        super(LineEdit, self).mousePressEvent(e) #required to deselect on 2e click
        if self.readyToEdit:
            self.selectAll()
            self.readyToEdit = False

    def focusOutEvent(self, e):
        super(LineEdit, self).focusOutEvent(e) #required to remove cursor on focusOut
        self.readyToEdit = True


class Ui_searchbar(object):
    def setupUi(self, wpWidget):
        wpWidget.setObjectName("wpWidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wpWidget.sizePolicy().hasHeightForWidth())
        wpWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(wpWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wpWidget_2 = QtWidgets.QWidget(wpWidget)
        self.wpWidget_2.setObjectName("wpWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wpWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wpWidget_3 = QtWidgets.QWidget(self.wpWidget_2)
        self.wpWidget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.wpWidget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.wpWidget_3.setStyleSheet("QWidget#wpWidget_3{\n"
"    background-color:rgb(35, 34, 39);\n"
"}")
        self.wpWidget_3.setObjectName("wpWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wpWidget_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wpWidget_5 = QtWidgets.QWidget(self.wpWidget_3)
        self.wpWidget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.wpWidget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.wpWidget_5.setObjectName("wpWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wpWidget_5)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.back_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.back_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.back_PushButton.setIcon(QtGui.QIcon(back_png))
        self.back_PushButton.setObjectName("back_PushButton")
        self.horizontalLayout.addWidget(self.back_PushButton)
        self.forward_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.forward_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.forward_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.forward_PushButton.setIcon(QtGui.QIcon(forward_png))
        self.forward_PushButton.setObjectName("forward_PushButton")
        self.horizontalLayout.addWidget(self.forward_PushButton)
        self.reload_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.reload_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.reload_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.reload_PushButton.setIcon(QtGui.QIcon(reload_png))
        self.reload_PushButton.setObjectName("reload_PushButton")
        self.horizontalLayout.addWidget(self.reload_PushButton)
        self.settings_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.settings_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.settings_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.settings_PushButton.setIcon(QtGui.QIcon(settings_png))
        self.settings_PushButton.setObjectName("settings_PushButton")
        # self.horizontalLayout.addWidget(self.settings_PushButton)
        self.home_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.home_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.home_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.home_PushButton.setIcon(QtGui.QIcon(home_png))
        self.home_PushButton.setObjectName("home_PushButton")
        self.horizontalLayout.addWidget(self.home_PushButton)
        self.horizontalLayout_2.addWidget(self.wpWidget_5)

        self.urlbar = LineEdit(self.wpWidget_3)
        self.urlbar.setMinimumSize(QtCore.QSize(300, 28))
        self.urlbar.setMaximumSize(QtCore.QSize(16777215, 28))
        self.urlbar.setStyleSheet("QLineEdit{\n"
"    margin-right: 5px;\n"
"    background-color:rgb(27, 27, 27);\n"
"    border-radius:12px;\n"
"    color:rgb(240, 240, 240);\n"
"    padding-left:15px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgba(99, 173, 229, 150);\n"
"}")
        self.urlbar.setObjectName("urlbar")


        self.horizontalLayout_2.addWidget(self.urlbar)
        self.horizontalLayout_2.addWidget(self.settings_PushButton)
        self.verticalLayout_2.addWidget(self.wpWidget_3)
        self.wpWidget_4 = QtWidgets.QWidget(self.wpWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wpWidget_4.sizePolicy().hasHeightForWidth())
        self.wpWidget_4.setSizePolicy(sizePolicy)
        self.wpWidget_4.setObjectName("wpWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wpWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.wpWidget_4)
        self.verticalLayout.addWidget(self.wpWidget_2)

        self.wpWidget_2.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    font-size:17px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(144, 144, 144, 30);\n"
"    border-radius:5px;\n"
"}")     
        
        # set auto completer for the url bar
        completer = QCompleter(AutoCompleteWords)
        self.urlbar.setCompleter(completer)

        QtCore.QMetaObject.connectSlotsByName(wpWidget)

        # set universal style
        self.setStyleSheet("""
            QLineEdit { color: rgb(255, 255, 255); }
            QCheckBox { color: rgb(255, 255, 255); }
            QPlainTextEdit { color: rgb(255, 255, 255); }
            QLabel { color: rgb(255, 255, 255); }
            QComboBox { color: rgb(255, 255, 255); }
            QListView { color: rgb(255, 255, 255); }
            QPushButton { color: rgb(255, 255, 255); }
        """)

        # set tooltips
        self.settings_PushButton.setToolTip('Open Settings Window')  
        self.home_PushButton.setToolTip("return to Homepage")
        self.reload_PushButton.setToolTip("reload current page")
        self.back_PushButton.setToolTip("back")
        self.forward_PushButton.setToolTip("forward")

        # set tooltip duration and style
        self.setToolTipDuration(50)