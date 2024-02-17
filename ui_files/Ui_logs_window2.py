import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout, QMenu, QAction, QTabBar
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QLineEdit
import datetime
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("💎 Diamond Sorter - Log Hunter")
        MainWindow.resize(1288, 653)
        MainWindow.setStyleSheet("/*\n"
"Material Dark Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Inspired on https://github.com/jxfwinter/qt-material-stylesheet\n"
"Company: GTRONICK\n"
"Last updated: 04/12/2018, 15:00.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#007b50;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #37efba;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #808086;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #a9b7c6;\n"
"    background:#1e1d23;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #04b97f;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #04b97f;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(9, 9, 1001, 141))
        self.tab_widget.setStyleSheet("QLineEdit,\n"
"QComboBox,\n"
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox {\n"
"  color: #1de9b6;\n"
"  background-color: #31363b;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;\n"
"}\n"
"\n"
"QWidget {\n"
"  background-color: #232629;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox,\n"
"QFrame {\n"
"  background-color: #232629;\n"
"  border: 2px solid #4f5b62;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QRadioButton::indicator,\n"
"QCheckBox::indicator {\n"
"  width: 16px;\n"
"  height: 16px;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 0;\n"
"  transform: rotate(45deg);\n"
"  transform-origin: center;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QCheckBox::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover,\n"
"QCheckBox::indicator:hover {\n"
"  border-color: rgba(29, 233, 182, 0.8);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #1de9b6;\n"
"}")
        self.tab_widget.setObjectName("tab_widget")
        self.main_data_widget = QtWidgets.QTabWidget(self.tab_widget)
        self.main_data_widget.setGeometry(QtCore.QRect(9, 9, 991, 131))
        self.main_data_widget.setStyleSheet("")
        self.main_data_widget.setObjectName("main_data_widget")
        self.data_tab_widget_1 = QtWidgets.QWidget()
        self.data_tab_widget_1.setObjectName("data_tab_widget_1")
        self.grab_data_button = QtWidgets.QPushButton(self.data_tab_widget_1)
        self.grab_data_button.setGeometry(QtCore.QRect(650, 10, 91, 34))
        self.grab_data_button.setObjectName("grab_data_button")
        self.toolButton = QtWidgets.QToolButton(self.data_tab_widget_1)
        self.toolButton.setGeometry(QtCore.QRect(950, 70, 23, 23))
        self.toolButton.setObjectName("toolButton")
        self.frame_stats_1 = QtWidgets.QFrame(self.data_tab_widget_1)
        self.frame_stats_1.setGeometry(QtCore.QRect(20, 10, 201, 80))
        self.frame_stats_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stats_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_stats_1.setObjectName("frame_stats_1")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_stats_1)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 201, 81))
        self.textBrowser.setSearchPaths([])
        self.textBrowser.setObjectName("textBrowser")
        self.frame_stats_2 = QtWidgets.QFrame(self.data_tab_widget_1)
        self.frame_stats_2.setGeometry(QtCore.QRect(230, 10, 201, 80))
        self.frame_stats_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stats_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_stats_2.setObjectName("frame_stats_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_stats_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 201, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.frame_stats_3 = QtWidgets.QFrame(self.data_tab_widget_1)
        self.frame_stats_3.setGeometry(QtCore.QRect(440, 10, 201, 80))
        self.frame_stats_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stats_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_stats_3.setObjectName("frame_stats_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_stats_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 201, 81))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.request_data_button = QtWidgets.QPushButton(self.data_tab_widget_1)
        self.request_data_button.setGeometry(QtCore.QRect(650, 40, 91, 34))
        self.request_data_button.setObjectName("request_data_button")
        self.request_data_combobox = QtWidgets.QComboBox(self.data_tab_widget_1)
        self.request_data_combobox.setGeometry(QtCore.QRect(750, 10, 221, 38))
        self.request_data_combobox.setEditable(True)
        self.request_data_combobox.setObjectName("request_data_combobox")
        self.data_request_text = QtWidgets.QTextEdit(self.data_tab_widget_1)
        self.data_request_text.setGeometry(QtCore.QRect(750, 40, 221, 26))
        self.data_request_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.data_request_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.data_request_text.setObjectName("data_request_text")
        self.add_request_to_db_button = QtWidgets.QPushButton(self.data_tab_widget_1)
        self.add_request_to_db_button.setGeometry(QtCore.QRect(800, 70, 111, 34))
        self.add_request_to_db_button.setObjectName("add_request_to_db_button")
        self.main_data_widget.addTab(self.data_tab_widget_1, "")
        self.community_request_tab = QtWidgets.QWidget()
        self.community_request_tab.setObjectName("community_request_tab")
        self.label = QtWidgets.QLabel(self.community_request_tab)
        self.label.setGeometry(QtCore.QRect(360, 20, 241, 51))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(10)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.main_data_widget.addTab(self.community_request_tab, "")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(20, 390, 1001, 210))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 991, 192))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 160, 991, 210))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.domain_tree_page_1 = QtWidgets.QWidget()
        self.domain_tree_page_1.setObjectName("domain_tree_page_1")
        self.domain_tree_widget = QtWidgets.QTreeWidget(self.domain_tree_page_1)
        self.domain_tree_widget.setEnabled(True)
        self.domain_tree_widget.setGeometry(QtCore.QRect(9, 9, 981, 192))
        self.domain_tree_widget.setAlternatingRowColors(True)
        self.domain_tree_widget.setObjectName("domain_tree_widget")
        item_0 = QtWidgets.QTreeWidgetItem(self.domain_tree_widget)
        font = QtGui.QFont()
        font.setBold(True)
        item_0.setFont(0, font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/website.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/cookiemonster.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon1)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setItalic(True)
        item_1.setFont(0, font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/icons8-genealogy-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon2)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/website-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_2.setIcon(0, icon3)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.domain_tree_widget.header().setHighlightSections(True)
        self.stackedWidget.addWidget(self.domain_tree_page_1)
        self.domain_tree_widget_2 = QtWidgets.QWidget()
        self.domain_tree_widget_2.setObjectName("domain_tree_widget_2")
        self.stackedWidget.addWidget(self.domain_tree_widget_2)
        self.console_text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.console_text_browser.setGeometry(QtCore.QRect(1020, 20, 256, 561))
        self.console_text_browser.setStyleSheet("/*\n"
"Material Dark Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Inspired on https://github.com/jxfwinter/qt-material-stylesheet\n"
"Company: GTRONICK\n"
"Last updated: 04/12/2018, 15:00.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#007b50;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #37efba;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #808086;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #a9b7c6;\n"
"    background:#1e1d23;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #04b97f;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #04b97f;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}")
        self.console_text_browser.setObjectName("console_text_browser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1288, 18))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuCommunity_Stats = QtWidgets.QMenu(self.menubar)
        self.menuCommunity_Stats.setObjectName("menuCommunity_Stats")
        self.menuGroups_Channels = QtWidgets.QMenu(self.menubar)
        self.menuGroups_Channels.setObjectName("menuGroups_Channels")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_To_Database = QtWidgets.QAction(MainWindow)
        self.actionAdd_To_Database.setObjectName("actionAdd_To_Database")
        self.actionOpen_Saved_Dictionary = QtWidgets.QAction(MainWindow)
        self.actionOpen_Saved_Dictionary.setObjectName("actionOpen_Saved_Dictionary")
        self.actionHomepage = QtWidgets.QAction(MainWindow)
        self.actionHomepage.setObjectName("actionHomepage")
        self.actionTelegram_Community = QtWidgets.QAction(MainWindow)
        self.actionTelegram_Community.setObjectName("actionTelegram_Community")
        self.menuMenu.addAction(self.actionAdd_To_Database)
        self.menuMenu.addAction(self.actionOpen_Saved_Dictionary)
        self.menuCommunity_Stats.addAction(self.actionHomepage)
        self.menuCommunity_Stats.addAction(self.actionTelegram_Community)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuCommunity_Stats.menuAction())
        self.menubar.addAction(self.menuGroups_Channels.menuAction())

        self.retranslateUi(MainWindow)
        self.main_data_widget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grab_data_button.setText(_translate("MainWindow", "Grab Data"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Domains In Database                                                        Cookies In Database                                                  Sub Domains In Database"))
        self.textBrowser_2.setPlaceholderText(_translate("MainWindow", "                  Your Request Data                      Domains:                                            Cookies:                                                             Subdomains:"))
        self.textBrowser_3.setPlaceholderText(_translate("MainWindow", "            Community  Stats"))
        self.request_data_button.setText(_translate("MainWindow", "Request Data"))
        self.add_request_to_db_button.setText(_translate("MainWindow", "Add To Database"))
        self.main_data_widget.setTabText(self.main_data_widget.indexOf(self.data_tab_widget_1), _translate("MainWindow", "Data Tab 1"))
        self.label.setText(_translate("MainWindow", "Comming Soon"))
        self.main_data_widget.setTabText(self.main_data_widget.indexOf(self.community_request_tab), _translate("MainWindow", "Community Request Tab"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Domain"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL  "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cookie_Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cookie_ID   "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cookie Description"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Duration   "))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Type"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.domain_tree_widget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.domain_tree_widget.headerItem().setText(1, _translate("MainWindow", "2"))
        self.domain_tree_widget.headerItem().setText(2, _translate("MainWindow", "3"))
        __sortingEnabled = self.domain_tree_widget.isSortingEnabled()
        self.domain_tree_widget.setSortingEnabled(False)
        self.domain_tree_widget.topLevelItem(0).setText(0, _translate("MainWindow", "url"))
        self.domain_tree_widget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "cookie_name"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "cookie_id"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(1).setText(0, _translate("MainWindow", "url"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(2).setText(0, _translate("MainWindow", "duration"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(3).setText(0, _translate("MainWindow", "type"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(4).setText(0, _translate("MainWindow", "storage_type"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(5).setText(0, _translate("MainWindow", "Description"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(6).setText(0, _translate("MainWindow", "category_id"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(7).setText(0, _translate("MainWindow", "script_id"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(8).setText(0, _translate("MainWindow", "category"))
        self.domain_tree_widget.topLevelItem(0).child(0).child(9).setText(0, _translate("MainWindow", "category_desc"))
        self.domain_tree_widget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "SubDomains"))
        self.domain_tree_widget.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "Subdomain"))
        self.domain_tree_widget.topLevelItem(0).child(1).child(1).setText(0, _translate("MainWindow", "Script Path"))
        self.domain_tree_widget.topLevelItem(0).child(1).child(2).setText(0, _translate("MainWindow", "Relitive Path"))
        self.domain_tree_widget.setSortingEnabled(__sortingEnabled)
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuCommunity_Stats.setTitle(_translate("MainWindow", "Community Stats"))
        self.menuGroups_Channels.setTitle(_translate("MainWindow", "Groups & Channels"))
        self.actionAdd_To_Database.setText(_translate("MainWindow", "Add To Database"))
        self.actionOpen_Saved_Dictionary.setText(_translate("MainWindow", "Open Saved Dictionary"))
        self.actionHomepage.setText(_translate("MainWindow", "Homepage"))
        self.actionTelegram_Community.setText(_translate("MainWindow", "Telegram Community"))



        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.grab_data_button.clicked.connect(self.grabData)
        self.request_data_button.clicked.connect(self.handle_data_request)
        self.add_request_to_db_button

    def show_context_menu(self, pos):
        # Get the position relative to the widget
        global_pos = self.tree_widget.viewport().mapToGlobal(pos)
    
        # Create the context menu with the parent set to the main window
        context_menu = QMenu(self.tree_widget)
    
        # Add actions to the context menu
        action1 = QAction("Action 1", context_menu)
        action2 = QAction("Action 2", context_menu)
        context_menu.addAction(action1)
        context_menu.addAction(action2)
    
        # Show the context menu at the specified position
        context_menu.exec_(global_pos)
        
    def populateTableWidget(self):
        # Connect to the database
        conn = sqlite3.connect('cookies_data.db')
        cursor = conn.cursor()
    
        # Retrieve the data from the cookies table
        cursor.execute("SELECT domain, URL, Cookie_name, cookie_ID, description FROM cookies")
        results = cursor.fetchall()
    
        # Set the table headers
        headers = ["Domain", "URL", "Cookie Name", "Cookie ID", "Cookie Description"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
    
        # Populate the tableWidget with the data
        self.tableWidget.setRowCount(len(results))
        for row, result in enumerate(results):
            for col, value in enumerate(result):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
    
        # Close the database connection
        conn.close()



    def display_stats(self):
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()

        # Retrieve the statistics data from the database
        cursor.execute("SELECT COUNT(*), MIN(column), MAX(column) FROM cookies")
        result = cursor.fetchone()
        count = result[0]
        min_value = result[1]
        max_value = result[2]

        # Update the labels in the frames with the statistics data
        self.frame_stats_1.setText(f"Count: {count}")
        self.label_stats_2.setText(f"Min Value: {min_value}")
        self.label_stats_3.setText(f"Max Value: {max_value}")

        # Close the database connection
        conn.close()


    def grabData(self):
        # Connect to the database
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()
        
        # Create the cookies table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cookies (
                request_datetime TEXT,
                domain TEXT,
                URL TEXT,
                Cookie_name TEXT,
                cookie_ID TEXT,
                description TEXT,
                duration TEXT,
                type TEXT,
                storage_type TEXT
            )
        """)
        
        # Commit the changes and close the connection
        conn.commit()
        # Retrieve the data from the database
        cursor.execute("SELECT * FROM cookies")
        results = cursor.fetchall()
    
        # Retrieve the count of unique values for domains
        cursor.execute("SELECT COUNT(DISTINCT domain) FROM cookies")
        domain_count = cursor.fetchone()[0]
    
        # Retrieve the count of unique values for cookie names
        cursor.execute("SELECT COUNT(DISTINCT Cookie_name) FROM cookies")
        cookie_name_count = cursor.fetchone()[0]
    
        # Retrieve the count of unique values for cookie IDs
        cursor.execute("SELECT COUNT(DISTINCT cookie_ID) FROM cookies")
        cookie_id_count = cursor.fetchone()[0]
    
        # Retrieve the count of unique values for cookie types
        cursor.execute("SELECT COUNT(DISTINCT type) FROM cookies")
        cookie_type_count = cursor.fetchone()[0]
    
        # Display the counts in the textBrowser
        self.textBrowser.setPlainText("Data Numbers:\n\n")
        self.textBrowser.append(f"Domains: {domain_count}")
        self.textBrowser.append(f"Cookie Names: {cookie_name_count}")
        self.textBrowser.append(f"Cookie ID: {cookie_id_count}")
        self.textBrowser.append(f"Cookie Types: {cookie_type_count}")
    
        # Close the database connection
        conn.close()
    
        # Auto-resize the columns to fit the content
        self.tableWidget.resizeColumnsToContents()
    
        # Populate the request_data_combobox with unique URLs
        urls = set(result[2] for result in results)
        self.request_data_combobox.clear()
        self.request_data_combobox.addItems(urls)


    def handle_data_request(self):
        # Get the selected URL from the data_request_text field
        selected_url = self.data_request_text.toPlainText()
    
        # Connect to the database
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()
    
        # Retrieve the results for the selected URL from the database
        cursor.execute("SELECT * FROM cookies WHERE URL = ? LIMIT 10", (selected_url,))
        results = cursor.fetchall()
    
        # Clear the tableWidget
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
    
        # Populate the tableWidget with the data
        for row, result in enumerate(results):
            self.tableWidget.insertRow(row)
            for col, data in enumerate(result):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, col, item)
    
        # Close the database connection
        conn.close()
    # Allow context menu on the tableWidget
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.show_context_menu)


    
    
    def open_action_triggered(self):
        selected_item = self.tableWidget.currentItem()
        if selected_item:
            # Perform the open action for the selected item
            pass
    
    def copy_action_triggered(self):
        selected_item = self.tableWidget.currentItem()
        if selected_item:
            # Perform the copy action for the selected item
            pass
    
    def clear_action_triggered(self):
        # Clear the tableWidget
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
    
    def get_favicon(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            favicon_link = soup.find('link', rel='icon')
            if favicon_link:
                favicon_url = favicon_link['href']
                if not favicon_url.startswith('http'):
                    parsed_url = urlparse(url)
                    favicon_url = f"{parsed_url.scheme}://{parsed_url.netloc}{favicon_url}"
                return favicon_url
        except requests.exceptions.RequestException:
            return None
      

    def display_results(self, results):
        # Set the table dimensions
        self.table_widget.setRowCount(len(results))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Website", "Number of Cookies", "Min Age", "Max Age"])

        # Populate the table with results
        for row, result in enumerate(results):
            domain, num_cookies, min_age, max_age = result
            self.table_widget.setItem(row, 0, QTableWidgetItem(domain))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(num_cookies)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(min_age)))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(max_age)))

    def fetch_results(self, url):
        # Define your logic to fetch the results here
        # Replace this with your actual code to fetch the results from the specified URL

        results = [
            ("2022-01-01 10:00:00", "Type 1", "example.com", "Cookie 1", "123", "Description 1", "1 day", "LocalStorage", url),
            ("2022-01-01 10:00:00", "Type 2", "example.com", "Cookie 2", "456", "Description 2", "2 days", "SessionStorage", url),
        ]

        return results

    def actionAdd_To_Database_selected(self):
        # Establish a connection to the SQLite database
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()
        website = self.data_request_text.toPlainText()
        url = f"https://api.cookieserve.com/get_scan_result?url={website}"
        response = requests.get(url)
    
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response data as JSON
            data = response.json()
    
            # Create a table if it doesn't exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS cookies
                            (url TEXT, domain TEXT, cookie_name TEXT, cookie_id TEXT, duration TEXT, type TEXT, storage_type TEXT, description TEXT, request_datetime TEXT)''')
    
            # Insert the data into the table
            for category, cookies_list in data.items():
                for cookie in cookies_list:
                    cookie_name = cookie.get("cookie_name")
                    cookie_id = cookie.get("cookie_id")
                    url = cookie.get("url")
                    duration = cookie.get("duration")
                    cookie_type = cookie.get("type")
                    storage_type = cookie.get("storage_type")
                    description = cookie.get("description")
                    request_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cursor.execute("INSERT INTO cookies (url, domain, cookie_name, cookie_id, duration, type, storage_type, description, request_datetime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                    (url, website, cookie_name, cookie_id, duration, cookie_type, storage_type, description, request_datetime))
    
            conn.commit()
    
            print(f"Data stored for {website} successfully.")
        else:
            print(f"Error occurred while retrieving data for {website}.")
    
        conn.close()
    
        display_results(domain_tree_widget)
            
            

        def url_exists_in_database(self, url):
            # Connect to the SQLite database
            conn = sqlite3.connect('cookies_data.db')
            cursor = conn.cursor()
    
            # Execute a query to check if the URL exists in the cookies table
            cursor.execute("SELECT EXISTS(SELECT 1 FROM cookies WHERE url = ? LIMIT 1)", (url,))
            result = cursor.fetchone()[0]
    
            # Close the database connection
            conn.close()
    
            return result == 1
    
        def show_submit_another_request_dialog(self):
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Question)
            dialog.setWindowTitle("Submit Another Request?")
            dialog.setText("Would you like to submit another request?")
            dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            return dialog.exec_()





    def show_update_dialog(self):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Warning)
        dialog.setWindowTitle("Caution")
        dialog.setText("The URL that you have just requested is already exists in the database.")
        dialog.setInformativeText("Do you want to continue and update the current data?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return dialog.exec_()

    def update_results(self, url):
        # Perform the update logic here
        print("Updating results for URL:", url)

    def retrieve_results(self, url):
        # Perform the retrieval logic here
        print("Retrieving results for URL:", url)










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
