import json
import os
import re
import random
import string
import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QUrl, Qt, QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QPlainTextEdit, QLCDNumber, QMainWindow, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout
import hashlib
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices, QColor, QTextCharFormat, QIcon
import binascii
import json as jsond
import platform
import subprocess
import time
from datetime import datetime
from time import sleep
import shutil
from collections import Counter
from urllib.parse import urlparse
from multiprocessing import Process
import os
import hashlib
from time import sleep
from subprocess import Popen
import requests

### UI Imports
import ui_form 
INSTALLER_MODE = True # CHANGE THIS LINE WHEN COMPILE
if INSTALLER_MODE:
    top_classes = [QtWidgets.QMainWindow, ui_form.Ui_DiamondSorter]
else:
    top_classes = [QtWidgets.QMainWindow]
    
def calc_lines(txt, remove_empty_lines = True):
    if not txt.strip():
        return 0
    all_lines = txt.strip().split('\n')
    if not remove_empty_lines:
        return len(all_lines)
    else:
        return len([i for i in all_lines if bool(i.strip())])

class Ui_DiamondSorter(object):
    def setupUi(self, DiamondSorter):
        DiamondSorter.setObjectName("DiamondSorter")
        DiamondSorter.resize(843, 807)
        DiamondSorter.setMaximumSize(QtCore.QSize(882, 810))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        DiamondSorter.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        DiamondSorter.setFont(font)
        DiamondSorter.setAutoFillBackground(False)
        DiamondSorter.setStyleSheet("QWidget {\n"
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
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTreeView,\n"
"QListView,\n"
"QLineEdit,\n"
"QComboBox {\n"
"  color: #1de9b6;\n"
"  background-color: #31363b;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;\n"
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
"QRadioButton::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
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
        DiamondSorter.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(DiamondSorter)
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setEnabled(True)
        self.tab_widget.setGeometry(QtCore.QRect(0, 430, 841, 241))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.tab_widget.setFont(font)
        self.tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_widget.setStyleSheet("tool.Optionswidget")
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab_widget.setUsesScrollButtons(True)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setMovable(False)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName("tab_widget")
        self.formatOptionsTab = QtWidgets.QWidget()
        self.formatOptionsTab.setObjectName("formatOptionsTab")
        self.deleate_after_sorting_checkbox = QtWidgets.QCheckBox(self.formatOptionsTab)
        self.deleate_after_sorting_checkbox.setEnabled(False)
        self.deleate_after_sorting_checkbox.setGeometry(QtCore.QRect(610, 180, 181, 22))
        self.deleate_after_sorting_checkbox.setObjectName("deleate_after_sorting_checkbox")
        self.file_type_or_format_for_the_search_label = QtWidgets.QTextEdit(self.formatOptionsTab)
        self.file_type_or_format_for_the_search_label.setEnabled(True)
        self.file_type_or_format_for_the_search_label.setGeometry(QtCore.QRect(20, 100, 171, 31))
        self.file_type_or_format_for_the_search_label.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_type_or_format_for_the_search_label.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_type_or_format_for_the_search_label.setDocumentTitle("")
        self.file_type_or_format_for_the_search_label.setObjectName("file_type_or_format_for_the_search_label")
        self.stealer_log_format_label = QtWidgets.QLabel(self.formatOptionsTab)
        self.stealer_log_format_label.setGeometry(QtCore.QRect(20, 5, 161, 21))
        self.stealer_log_format_label.setObjectName("stealer_log_format_label")
        self.file_type_or_format_label = QtWidgets.QLabel(self.formatOptionsTab)
        self.file_type_or_format_label.setGeometry(QtCore.QRect(10, 70, 191, 20))
        self.file_type_or_format_label.setObjectName("file_type_or_format_label")
        self.stealer_log_format_combo = QtWidgets.QComboBox(self.formatOptionsTab)
        self.stealer_log_format_combo.setEnabled(True)
        self.stealer_log_format_combo.setGeometry(QtCore.QRect(30, 30, 141, 24))
        self.stealer_log_format_combo.setObjectName("stealer_log_format_combo")
        self.stealer_log_format_combo.addItem("")
        self.stealer_log_format_combo.setItemText(0, "")
        self.stealer_log_format_combo.addItem("")
        self.stealer_log_format_combo.addItem("")
        self.stealer_log_format_combo.addItem("")
        self.stealer_log_format_combo.addItem("")
        self.stealer_log_format_combo.addItem("")
        self.file_structure_frame = QtWidgets.QFrame(self.formatOptionsTab)
        self.file_structure_frame.setGeometry(QtCore.QRect(220, 10, 261, 191))
        self.file_structure_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_structure_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_structure_frame.setObjectName("file_structure_frame")
        self.label = QtWidgets.QLabel(self.file_structure_frame)
        self.label.setGeometry(QtCore.QRect(80, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.redline_file_structure_text_browser = QtWidgets.QTextBrowser(self.file_structure_frame)
        self.redline_file_structure_text_browser.setEnabled(True)
        self.redline_file_structure_text_browser.setGeometry(QtCore.QRect(0, 30, 261, 161))
        self.redline_file_structure_text_browser.setOpenLinks(False)
        self.redline_file_structure_text_browser.setObjectName("redline_file_structure_text_browser")
        self.racoon_file_structure_text_browser = QtWidgets.QTextBrowser(self.file_structure_frame)
        self.racoon_file_structure_text_browser.setEnabled(True)
        self.racoon_file_structure_text_browser.setGeometry(QtCore.QRect(0, 30, 261, 161))
        self.racoon_file_structure_text_browser.setOpenLinks(False)
        self.racoon_file_structure_text_browser.setObjectName("racoon_file_structure_text_browser")
        self.titan_file_structure_text_browser = QtWidgets.QTextBrowser(self.file_structure_frame)
        self.titan_file_structure_text_browser.setEnabled(True)
        self.titan_file_structure_text_browser.setGeometry(QtCore.QRect(0, 30, 261, 161))
        self.titan_file_structure_text_browser.setOpenLinks(False)
        self.titan_file_structure_text_browser.setObjectName("titan_file_structure_text_browser")
        self.worldwind_file_structure_text_browser = QtWidgets.QTextBrowser(self.file_structure_frame)
        self.worldwind_file_structure_text_browser.setEnabled(True)
        self.worldwind_file_structure_text_browser.setGeometry(QtCore.QRect(0, 30, 261, 161))
        self.worldwind_file_structure_text_browser.setOpenLinks(False)
        self.worldwind_file_structure_text_browser.setObjectName("worldwind_file_structure_text_browser")
        self.whitesnake_file_structure_text_browser = QtWidgets.QTextBrowser(self.file_structure_frame)
        self.whitesnake_file_structure_text_browser.setEnabled(True)
        self.whitesnake_file_structure_text_browser.setGeometry(QtCore.QRect(0, 30, 261, 161))
        self.whitesnake_file_structure_text_browser.setOpenLinks(False)
        self.whitesnake_file_structure_text_browser.setObjectName("whitesnake_file_structure_text_browser")
        self.label.raise_()
        self.whitesnake_file_structure_text_browser.raise_()
        self.titan_file_structure_text_browser.raise_()
        self.worldwind_file_structure_text_browser.raise_()
        self.racoon_file_structure_text_browser.raise_()
        self.redline_file_structure_text_browser.raise_()
        self.domain_managerButton = QtWidgets.QPushButton(self.formatOptionsTab)
        self.domain_managerButton.setEnabled(True)
        self.domain_managerButton.setGeometry(QtCore.QRect(710, 100, 111, 61))
        self.domain_managerButton.setObjectName("domain_managerButton")
        self.tab_widget.addTab(self.formatOptionsTab, "")
        self.generalComboOptionsTab = QtWidgets.QWidget()
        self.generalComboOptionsTab.setObjectName("generalComboOptionsTab")
        self.pasteButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.pasteButton.setGeometry(QtCore.QRect(20, 10, 80, 24))
        self.pasteButton.setObjectName("pasteButton")
        self.removeLinksButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.removeLinksButton.setGeometry(QtCore.QRect(640, 100, 81, 24))
        self.removeLinksButton.setObjectName("removeLinksButton")
        self.copyButton_2 = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.copyButton_2.setGeometry(QtCore.QRect(120, 10, 80, 24))
        self.copyButton_2.setObjectName("copyButton_2")
        self.removeEndingPunctuationButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.removeEndingPunctuationButton.setGeometry(QtCore.QRect(650, 40, 171, 24))
        self.removeEndingPunctuationButton.setObjectName("removeEndingPunctuationButton")
        self.remove_domainsButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.remove_domainsButton.setGeometry(QtCore.QRect(520, 40, 91, 24))
        self.remove_domainsButton.setObjectName("remove_domainsButton")
        self.removeDuplicatesButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.removeDuplicatesButton.setGeometry(QtCore.QRect(730, 100, 91, 24))
        self.removeDuplicatesButton.setObjectName("removeDuplicatesButton")
        self.extract_md5Button = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.extract_md5Button.setGeometry(QtCore.QRect(20, 70, 80, 24))
        self.extract_md5Button.setObjectName("extract_md5Button")
        self.removeSpecialCharacterButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.removeSpecialCharacterButton.setGeometry(QtCore.QRect(650, 10, 171, 24))
        self.removeSpecialCharacterButton.setObjectName("removeSpecialCharacterButton")
        self.organizeLinesButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.organizeLinesButton.setGeometry(QtCore.QRect(120, 40, 81, 24))
        self.organizeLinesButton.setObjectName("organizeLinesButton")
        self.remove_trash_button = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.remove_trash_button.setGeometry(QtCore.QRect(520, 160, 101, 24))
        self.remove_trash_button.setObjectName("remove_trash_button")
        self.remove_capturesButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.remove_capturesButton.setGeometry(QtCore.QRect(520, 70, 91, 24))
        self.remove_capturesButton.setObjectName("remove_capturesButton")
        self.split_by_linesButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.split_by_linesButton.setGeometry(QtCore.QRect(120, 70, 81, 24))
        self.split_by_linesButton.setObjectName("split_by_linesButton")
        self.removeAfterSpace = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.removeAfterSpace.setGeometry(QtCore.QRect(510, 10, 111, 24))
        self.removeAfterSpace.setObjectName("removeAfterSpace")
        self.removeAfter_Tab_Space = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.removeAfter_Tab_Space.setGeometry(QtCore.QRect(520, 130, 101, 24))
        self.removeAfter_Tab_Space.setObjectName("removeAfter_Tab_Space")
        self.remove_inbetween_two_variablesButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.remove_inbetween_two_variablesButton.setGeometry(QtCore.QRect(650, 70, 171, 24))
        self.remove_inbetween_two_variablesButton.setObjectName("remove_inbetween_two_variablesButton")
        self.sort_remove_similarButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.sort_remove_similarButton.setGeometry(QtCore.QRect(510, 100, 111, 24))
        self.sort_remove_similarButton.setObjectName("sort_remove_similarButton")
        self.replace_linesButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.replace_linesButton.setGeometry(QtCore.QRect(20, 40, 80, 24))
        self.replace_linesButton.setObjectName("replace_linesButton")
        self.extract_ip_addressButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.extract_ip_addressButton.setGeometry(QtCore.QRect(120, 100, 91, 24))
        self.extract_ip_addressButton.setObjectName("extract_ip_addressButton")
        self.extract_phone_numberButton = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.extract_phone_numberButton.setGeometry(QtCore.QRect(10, 100, 91, 24))
        self.extract_phone_numberButton.setObjectName("extract_phone_numberButton")
        self.format_request_textedit = QtWidgets.QTextEdit(self.generalComboOptionsTab)
        self.format_request_textedit.setGeometry(QtCore.QRect(200, 169, 311, 31))
        self.format_request_textedit.setObjectName("format_request_textedit")
        self.remove_new_lines = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.remove_new_lines.setGeometry(QtCore.QRect(640, 130, 181, 41))
        self.remove_new_lines.setObjectName("remove_new_lines")
        self.consecutive_digits_button = QtWidgets.QPushButton(self.generalComboOptionsTab)
        self.consecutive_digits_button.setGeometry(QtCore.QRect(210, 10, 111, 24))
        self.consecutive_digits_button.setObjectName("consecutive_digits_button")
        self.tab_widget.addTab(self.generalComboOptionsTab, "")
        self.password_format_tab = QtWidgets.QWidget()
        self.password_format_tab.setObjectName("password_format_tab")
        self.emailPasswordButton = QtWidgets.QPushButton(self.password_format_tab)
        self.emailPasswordButton.setEnabled(True)
        self.emailPasswordButton.setGeometry(QtCore.QRect(10, 50, 121, 24))
        self.emailPasswordButton.setObjectName("emailPasswordButton")
        self.usernamePasswordButton = QtWidgets.QPushButton(self.password_format_tab)
        self.usernamePasswordButton.setEnabled(True)
        self.usernamePasswordButton.setGeometry(QtCore.QRect(170, 50, 111, 24))
        self.usernamePasswordButton.setObjectName("usernamePasswordButton")
        self.memberIDPINButton = QtWidgets.QPushButton(self.password_format_tab)
        self.memberIDPINButton.setEnabled(True)
        self.memberIDPINButton.setGeometry(QtCore.QRect(450, 50, 101, 24))
        self.memberIDPINButton.setObjectName("memberIDPINButton")
        self.numberPasswordButton = QtWidgets.QPushButton(self.password_format_tab)
        self.numberPasswordButton.setEnabled(True)
        self.numberPasswordButton.setGeometry(QtCore.QRect(310, 50, 111, 24))
        self.numberPasswordButton.setObjectName("numberPasswordButton")
        self.wordpress_finder_button = QtWidgets.QPushButton(self.password_format_tab)
        self.wordpress_finder_button.setEnabled(True)
        self.wordpress_finder_button.setGeometry(QtCore.QRect(10, 110, 121, 24))
        self.wordpress_finder_button.setObjectName("wordpress_finder_button")
        self.business_emailfinder_button = QtWidgets.QPushButton(self.password_format_tab)
        self.business_emailfinder_button.setEnabled(True)
        self.business_emailfinder_button.setGeometry(QtCore.QRect(10, 140, 121, 24))
        self.business_emailfinder_button.setObjectName("business_emailfinder_button")
        self.governmentDomainsButton = QtWidgets.QPushButton(self.password_format_tab)
        self.governmentDomainsButton.setEnabled(True)
        self.governmentDomainsButton.setGeometry(QtCore.QRect(170, 140, 111, 24))
        self.governmentDomainsButton.setObjectName("governmentDomainsButton")
        self.server_information_button = QtWidgets.QPushButton(self.password_format_tab)
        self.server_information_button.setEnabled(True)
        self.server_information_button.setGeometry(QtCore.QRect(450, 140, 101, 24))
        self.server_information_button.setObjectName("server_information_button")
        self.cpanel_account_button = QtWidgets.QPushButton(self.password_format_tab)
        self.cpanel_account_button.setEnabled(True)
        self.cpanel_account_button.setGeometry(QtCore.QRect(170, 110, 111, 24))
        self.cpanel_account_button.setObjectName("cpanel_account_button")
        self.mailBoxesOptions_ComboButton = QtWidgets.QPushButton(self.password_format_tab)
        self.mailBoxesOptions_ComboButton.setEnabled(True)
        self.mailBoxesOptions_ComboButton.setGeometry(QtCore.QRect(560, 110, 21, 21))
        self.mailBoxesOptions_ComboButton.setObjectName("mailBoxesOptions_ComboButton")
        self.advertisingButton = QtWidgets.QPushButton(self.password_format_tab)
        self.advertisingButton.setEnabled(True)
        self.advertisingButton.setGeometry(QtCore.QRect(450, 80, 101, 24))
        self.advertisingButton.setObjectName("advertisingButton")
        self.socialForumsButton = QtWidgets.QPushButton(self.password_format_tab)
        self.socialForumsButton.setEnabled(True)
        self.socialForumsButton.setGeometry(QtCore.QRect(310, 110, 111, 24))
        self.socialForumsButton.setObjectName("socialForumsButton")
        self.mailbox_options_combo = QtWidgets.QComboBox(self.password_format_tab)
        self.mailbox_options_combo.setEnabled(True)
        self.mailbox_options_combo.setGeometry(QtCore.QRect(450, 110, 101, 24))
        self.mailbox_options_combo.setObjectName("mailbox_options_combo")
        self.mailbox_options_combo.addItem("")
        self.mailbox_options_combo.addItem("")
        self.mailbox_options_combo.addItem("")
        self.password_working_function_combo = QtWidgets.QComboBox(self.password_format_tab)
        self.password_working_function_combo.setEnabled(True)
        self.password_working_function_combo.setGeometry(QtCore.QRect(600, 10, 191, 24))
        self.password_working_function_combo.setObjectName("password_working_function_combo")
        self.password_working_function_combo.addItem("")
        self.password_working_function_combo.setItemText(0, "")
        self.password_working_function_combo.addItem("")
        self.password_working_function_combo.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.password_format_tab)
        self.frame_2.setGeometry(QtCore.QRect(590, 50, 221, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.variables_label_2 = QtWidgets.QLabel(self.frame_2)
        self.variables_label_2.setGeometry(QtCore.QRect(70, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.variables_label_2.setFont(font)
        self.variables_label_2.setObjectName("variables_label_2")
        self.url_variable_label_2 = QtWidgets.QLabel(self.frame_2)
        self.url_variable_label_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.url_variable_label_2.setObjectName("url_variable_label_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_20 = QtWidgets.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(120, 20, 81, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(120, 40, 91, 16))
        self.label_22.setObjectName("label_22")
        self.creditcard_variable_label_2 = QtWidgets.QLabel(self.frame_2)
        self.creditcard_variable_label_2.setGeometry(QtCore.QRect(120, 60, 101, 16))
        self.creditcard_variable_label_2.setObjectName("creditcard_variable_label_2")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(120, 80, 91, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(120, 100, 91, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_2)
        self.label_27.setGeometry(QtCore.QRect(10, 120, 101, 16))
        self.label_27.setObjectName("label_27")
        self.create_username_list_button = QtWidgets.QPushButton(self.password_format_tab)
        self.create_username_list_button.setEnabled(True)
        self.create_username_list_button.setGeometry(QtCore.QRect(10, 80, 121, 24))
        self.create_username_list_button.setObjectName("create_username_list_button")
        self.create_password_list = QtWidgets.QPushButton(self.password_format_tab)
        self.create_password_list.setEnabled(True)
        self.create_password_list.setGeometry(QtCore.QRect(170, 80, 111, 24))
        self.create_password_list.setObjectName("create_password_list")
        self.create_number_list = QtWidgets.QPushButton(self.password_format_tab)
        self.create_number_list.setEnabled(True)
        self.create_number_list.setGeometry(QtCore.QRect(310, 80, 111, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.create_number_list.setFont(font)
        self.create_number_list.setObjectName("create_number_list")
        self.copyButton = QtWidgets.QPushButton(self.password_format_tab)
        self.copyButton.setEnabled(True)
        self.copyButton.setGeometry(QtCore.QRect(120, 10, 80, 24))
        self.copyButton.setObjectName("copyButton")
        self.tab2_pasteButton = QtWidgets.QPushButton(self.password_format_tab)
        self.tab2_pasteButton.setEnabled(True)
        self.tab2_pasteButton.setGeometry(QtCore.QRect(20, 10, 80, 24))
        self.tab2_pasteButton.setObjectName("tab2_pasteButton")
        icon = QtGui.QIcon.fromTheme("address-book-new")
        self.tab_widget.addTab(self.password_format_tab, icon, "")
        self.sortingLogsTab = QtWidgets.QWidget()
        self.sortingLogsTab.setObjectName("sortingLogsTab")
        self.sort_by_cap_dateButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_by_cap_dateButton.setEnabled(True)
        self.sort_by_cap_dateButton.setGeometry(QtCore.QRect(130, 10, 121, 24))
        self.sort_by_cap_dateButton.setObjectName("sort_by_cap_dateButton")
        self.sort_password_by_weightButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_password_by_weightButton.setEnabled(True)
        self.sort_password_by_weightButton.setGeometry(QtCore.QRect(380, 10, 141, 24))
        self.sort_password_by_weightButton.setObjectName("sort_password_by_weightButton")
        self.remove_duplicatesButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.remove_duplicatesButton.setEnabled(True)
        self.remove_duplicatesButton.setGeometry(QtCore.QRect(20, 40, 111, 24))
        self.remove_duplicatesButton.setObjectName("remove_duplicatesButton")
        self.sort_by_file_capturesButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_by_file_capturesButton.setEnabled(True)
        self.sort_by_file_capturesButton.setGeometry(QtCore.QRect(270, 40, 121, 24))
        self.sort_by_file_capturesButton.setObjectName("sort_by_file_capturesButton")
        self.sort_stealer_typeButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_stealer_typeButton.setEnabled(True)
        self.sort_stealer_typeButton.setGeometry(QtCore.QRect(530, 10, 121, 24))
        self.sort_stealer_typeButton.setObjectName("sort_stealer_typeButton")
        self.sort_by_geoButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_by_geoButton.setEnabled(True)
        self.sort_by_geoButton.setGeometry(QtCore.QRect(260, 10, 111, 24))
        self.sort_by_geoButton.setObjectName("sort_by_geoButton")
        self.remove_skinnyButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.remove_skinnyButton.setEnabled(True)
        self.remove_skinnyButton.setGeometry(QtCore.QRect(140, 40, 121, 24))
        self.remove_skinnyButton.setObjectName("remove_skinnyButton")
        self.sort_tg_groupButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_tg_groupButton.setEnabled(True)
        self.sort_tg_groupButton.setGeometry(QtCore.QRect(20, 10, 101, 24))
        self.sort_tg_groupButton.setObjectName("sort_tg_groupButton")
        self.sort_by_ads_logsButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_by_ads_logsButton.setEnabled(True)
        self.sort_by_ads_logsButton.setGeometry(QtCore.QRect(400, 40, 121, 24))
        self.sort_by_ads_logsButton.setObjectName("sort_by_ads_logsButton")
        self.sort_by_business_capturesButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_by_business_capturesButton.setEnabled(True)
        self.sort_by_business_capturesButton.setGeometry(QtCore.QRect(660, 10, 151, 24))
        self.sort_by_business_capturesButton.setObjectName("sort_by_business_capturesButton")
        self.create_a_file_tree_sortinglogsButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.create_a_file_tree_sortinglogsButton.setEnabled(True)
        self.create_a_file_tree_sortinglogsButton.setGeometry(QtCore.QRect(530, 40, 121, 24))
        self.create_a_file_tree_sortinglogsButton.setObjectName("create_a_file_tree_sortinglogsButton")
        self.sort_email_domainsButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_email_domainsButton.setEnabled(True)
        self.sort_email_domainsButton.setGeometry(QtCore.QRect(670, 40, 111, 24))
        self.sort_email_domainsButton.setObjectName("sort_email_domainsButton")
        self.variable_text_edit_path = QtWidgets.QTextEdit(self.sortingLogsTab)
        self.variable_text_edit_path.setGeometry(QtCore.QRect(360, 160, 301, 31))
        self.variable_text_edit_path.setAutoFillBackground(False)
        self.variable_text_edit_path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.variable_text_edit_path.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.variable_text_edit_path.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.variable_text_edit_path.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.variable_text_edit_path.setMarkdown("")
        self.variable_text_edit_path.setObjectName("variable_text_edit_path")
        self.extractBySearchButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.extractBySearchButton.setGeometry(QtCore.QRect(670, 160, 131, 31))
        self.extractBySearchButton.setObjectName("extractBySearchButton")
        self.sort_passwords_textButton = QtWidgets.QPushButton(self.sortingLogsTab)
        self.sort_passwords_textButton.setEnabled(True)
        self.sort_passwords_textButton.setGeometry(QtCore.QRect(10, 70, 141, 24))
        self.sort_passwords_textButton.setObjectName("sort_passwords_textButton")
        self.tab_widget.addTab(self.sortingLogsTab, "")
        self.sortingFilesTab = QtWidgets.QWidget()
        self.sortingFilesTab.setObjectName("sortingFilesTab")
        self.telegram_folder_sorting_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.telegram_folder_sorting_button.setEnabled(True)
        self.telegram_folder_sorting_button.setGeometry(QtCore.QRect(420, 80, 111, 24))
        self.telegram_folder_sorting_button.setObjectName("telegram_folder_sorting_button")
        self.authy_desktop_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.authy_desktop_button.setEnabled(True)
        self.authy_desktop_button.setGeometry(QtCore.QRect(150, 20, 111, 24))
        self.authy_desktop_button.setObjectName("authy_desktop_button")
        self.chrome_extensions_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.chrome_extensions_button.setEnabled(True)
        self.chrome_extensions_button.setGeometry(QtCore.QRect(420, 20, 111, 24))
        self.chrome_extensions_button.setObjectName("chrome_extensions_button")
        self.desktop_wallet_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.desktop_wallet_button.setEnabled(True)
        self.desktop_wallet_button.setGeometry(QtCore.QRect(550, 20, 111, 24))
        self.desktop_wallet_button.setObjectName("desktop_wallet_button")
        self.browser_wallet_sort_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.browser_wallet_sort_button.setEnabled(True)
        self.browser_wallet_sort_button.setGeometry(QtCore.QRect(550, 50, 111, 24))
        self.browser_wallet_sort_button.setObjectName("browser_wallet_sort_button")
        self.browser_2fa_extension_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.browser_2fa_extension_button.setEnabled(True)
        self.browser_2fa_extension_button.setGeometry(QtCore.QRect(420, 50, 111, 24))
        self.browser_2fa_extension_button.setObjectName("browser_2fa_extension_button")
        self.newtextdocuments_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.newtextdocuments_button.setEnabled(True)
        self.newtextdocuments_button.setGeometry(QtCore.QRect(280, 20, 121, 24))
        self.newtextdocuments_button.setObjectName("newtextdocuments_button")
        self.text_named_sorting_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.text_named_sorting_button.setEnabled(True)
        self.text_named_sorting_button.setGeometry(QtCore.QRect(280, 50, 121, 24))
        self.text_named_sorting_button.setObjectName("text_named_sorting_button")
        self.pgp_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.pgp_button.setEnabled(True)
        self.pgp_button.setGeometry(QtCore.QRect(150, 50, 111, 24))
        self.pgp_button.setObjectName("pgp_button")
        self.encryption_keys_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.encryption_keys_button.setEnabled(True)
        self.encryption_keys_button.setGeometry(QtCore.QRect(150, 80, 111, 24))
        self.encryption_keys_button.setObjectName("encryption_keys_button")
        self.auth_files_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.auth_files_button.setEnabled(True)
        self.auth_files_button.setGeometry(QtCore.QRect(20, 50, 111, 24))
        self.auth_files_button.setObjectName("auth_files_button")
        self.sort_by_cookies_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.sort_by_cookies_button.setEnabled(True)
        self.sort_by_cookies_button.setGeometry(QtCore.QRect(20, 20, 111, 24))
        self.sort_by_cookies_button.setObjectName("sort_by_cookies_button")
        self.remote_desktop_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.remote_desktop_button.setEnabled(True)
        self.remote_desktop_button.setGeometry(QtCore.QRect(20, 80, 111, 24))
        self.remote_desktop_button.setObjectName("remote_desktop_button")
        self.discord_sorting_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.discord_sorting_button.setEnabled(True)
        self.discord_sorting_button.setGeometry(QtCore.QRect(550, 80, 111, 24))
        self.discord_sorting_button.setObjectName("discord_sorting_button")
        self.control_panels_sort_button = QtWidgets.QPushButton(self.sortingFilesTab)
        self.control_panels_sort_button.setEnabled(True)
        self.control_panels_sort_button.setGeometry(QtCore.QRect(280, 80, 121, 24))
        self.control_panels_sort_button.setObjectName("control_panels_sort_button")
        self.button_scrape_keys = QtWidgets.QPushButton(self.sortingFilesTab)
        self.button_scrape_keys.setEnabled(True)
        self.button_scrape_keys.setGeometry(QtCore.QRect(20, 170, 71, 24))
        self.button_scrape_keys.setObjectName("button_scrape_keys")
        self.button_scrape_banking_data = QtWidgets.QPushButton(self.sortingFilesTab)
        self.button_scrape_banking_data.setEnabled(True)
        self.button_scrape_banking_data.setGeometry(QtCore.QRect(100, 170, 121, 24))
        self.button_scrape_banking_data.setObjectName("button_scrape_banking_data")
        self.button_scrape_backup_codes = QtWidgets.QPushButton(self.sortingFilesTab)
        self.button_scrape_backup_codes.setEnabled(True)
        self.button_scrape_backup_codes.setGeometry(QtCore.QRect(230, 170, 121, 24))
        self.button_scrape_backup_codes.setObjectName("button_scrape_backup_codes")
        self.button_scrape_security_data = QtWidgets.QPushButton(self.sortingFilesTab)
        self.button_scrape_security_data.setEnabled(True)
        self.button_scrape_security_data.setGeometry(QtCore.QRect(360, 170, 151, 24))
        self.button_scrape_security_data.setObjectName("button_scrape_security_data")
        self.tab_widget.addTab(self.sortingFilesTab, "")
        self.sortingCookiesTab = QtWidgets.QWidget()
        self.sortingCookiesTab.setObjectName("sortingCookiesTab")
        self.sorting_cookies_sort_by_domain = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_sort_by_domain.setEnabled(True)
        self.sorting_cookies_sort_by_domain.setGeometry(QtCore.QRect(20, 20, 111, 24))
        self.sorting_cookies_sort_by_domain.setObjectName("sorting_cookies_sort_by_domain")
        self.sorting_cookies_sort_by_quantity = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_sort_by_quantity.setEnabled(True)
        self.sorting_cookies_sort_by_quantity.setGeometry(QtCore.QRect(150, 20, 111, 24))
        self.sorting_cookies_sort_by_quantity.setObjectName("sorting_cookies_sort_by_quantity")
        self.sorting_cookies_sort_by_values_button = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_sort_by_values_button.setEnabled(True)
        self.sorting_cookies_sort_by_values_button.setGeometry(QtCore.QRect(280, 20, 111, 24))
        self.sorting_cookies_sort_by_values_button.setObjectName("sorting_cookies_sort_by_values_button")
        self.sorting_cookies_keywords_button = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_keywords_button.setEnabled(True)
        self.sorting_cookies_keywords_button.setGeometry(QtCore.QRect(550, 20, 111, 24))
        self.sorting_cookies_keywords_button.setObjectName("sorting_cookies_keywords_button")
        self.sorting_cookies_netscape_to_json_button = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_netscape_to_json_button.setEnabled(True)
        self.sorting_cookies_netscape_to_json_button.setGeometry(QtCore.QRect(20, 50, 111, 24))
        self.sorting_cookies_netscape_to_json_button.setObjectName("sorting_cookies_netscape_to_json_button")
        self.sorting_cookies_json_to_netscape_button = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_json_to_netscape_button.setEnabled(True)
        self.sorting_cookies_json_to_netscape_button.setGeometry(QtCore.QRect(150, 50, 111, 24))
        self.sorting_cookies_json_to_netscape_button.setObjectName("sorting_cookies_json_to_netscape_button")
        self.sorting_cookies_save_password_checkbox = QtWidgets.QCheckBox(self.sortingCookiesTab)
        self.sorting_cookies_save_password_checkbox.setGeometry(QtCore.QRect(630, 180, 171, 22))
        self.sorting_cookies_save_password_checkbox.setObjectName("sorting_cookies_save_password_checkbox")
        self.sorting_cookies_save_login_cookie_capture_checkbox = QtWidgets.QCheckBox(self.sortingCookiesTab)
        self.sorting_cookies_save_login_cookie_capture_checkbox.setGeometry(QtCore.QRect(630, 160, 181, 22))
        self.sorting_cookies_save_login_cookie_capture_checkbox.setObjectName("sorting_cookies_save_login_cookie_capture_checkbox")
        self.sorting_cookies_save_autofill_data_button = QtWidgets.QCheckBox(self.sortingCookiesTab)
        self.sorting_cookies_save_autofill_data_button.setGeometry(QtCore.QRect(630, 140, 151, 22))
        self.sorting_cookies_save_autofill_data_button.setObjectName("sorting_cookies_save_autofill_data_button")
        self.sorting_cookies_fix_cookie_misprintButton = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_fix_cookie_misprintButton.setEnabled(True)
        self.sorting_cookies_fix_cookie_misprintButton.setGeometry(QtCore.QRect(280, 50, 111, 24))
        self.sorting_cookies_fix_cookie_misprintButton.setObjectName("sorting_cookies_fix_cookie_misprintButton")
        self.sorting_cookies_count_total_values = QtWidgets.QPushButton(self.sortingCookiesTab)
        self.sorting_cookies_count_total_values.setEnabled(True)
        self.sorting_cookies_count_total_values.setGeometry(QtCore.QRect(410, 20, 111, 24))
        self.sorting_cookies_count_total_values.setObjectName("sorting_cookies_count_total_values")
        self.tab_widget.addTab(self.sortingCookiesTab, "")
        self.bankingFeaturesTab = QtWidgets.QWidget()
        self.bankingFeaturesTab.setObjectName("bankingFeaturesTab")
        self.capture_security_quest_answer_button = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.capture_security_quest_answer_button.setEnabled(True)
        self.capture_security_quest_answer_button.setGeometry(QtCore.QRect(10, 20, 141, 24))
        self.capture_security_quest_answer_button.setObjectName("capture_security_quest_answer_button")
        self.capture_all_banking_logs_button = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.capture_all_banking_logs_button.setEnabled(True)
        self.capture_all_banking_logs_button.setGeometry(QtCore.QRect(160, 20, 141, 24))
        self.capture_all_banking_logs_button.setObjectName("capture_all_banking_logs_button")
        self.parse_fulls_button = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.parse_fulls_button.setEnabled(True)
        self.parse_fulls_button.setGeometry(QtCore.QRect(420, 20, 111, 24))
        self.parse_fulls_button.setObjectName("parse_fulls_button")
        self.sort_cc_dataButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.sort_cc_dataButton.setEnabled(True)
        self.sort_cc_dataButton.setGeometry(QtCore.QRect(560, 20, 91, 24))
        self.sort_cc_dataButton.setObjectName("sort_cc_dataButton")
        self.sort_cc_data_with_cvcButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.sort_cc_data_with_cvcButton.setEnabled(True)
        self.sort_cc_data_with_cvcButton.setGeometry(QtCore.QRect(670, 20, 131, 24))
        self.sort_cc_data_with_cvcButton.setObjectName("sort_cc_data_with_cvcButton")
        self.sort_by_remitliesButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.sort_by_remitliesButton.setEnabled(True)
        self.sort_by_remitliesButton.setGeometry(QtCore.QRect(310, 20, 101, 24))
        self.sort_by_remitliesButton.setObjectName("sort_by_remitliesButton")
        self.sort_by_remetliescookiesButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.sort_by_remetliescookiesButton.setEnabled(True)
        self.sort_by_remetliescookiesButton.setGeometry(QtCore.QRect(10, 50, 141, 24))
        self.sort_by_remetliescookiesButton.setObjectName("sort_by_remetliescookiesButton")
        self.search_inside_new_text_docs = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.search_inside_new_text_docs.setEnabled(True)
        self.search_inside_new_text_docs.setGeometry(QtCore.QRect(340, 50, 161, 24))
        self.search_inside_new_text_docs.setObjectName("search_inside_new_text_docs")
        self.capture_2fa_files_bypassButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.capture_2fa_files_bypassButton.setEnabled(True)
        self.capture_2fa_files_bypassButton.setGeometry(QtCore.QRect(680, 50, 121, 24))
        self.capture_2fa_files_bypassButton.setObjectName("capture_2fa_files_bypassButton")
        self.banking_leads_emailButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.banking_leads_emailButton.setEnabled(True)
        self.banking_leads_emailButton.setGeometry(QtCore.QRect(10, 80, 141, 24))
        self.banking_leads_emailButton.setObjectName("banking_leads_emailButton")
        self.banking_leads_phoneButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.banking_leads_phoneButton.setEnabled(True)
        self.banking_leads_phoneButton.setGeometry(QtCore.QRect(170, 50, 141, 24))
        self.banking_leads_phoneButton.setObjectName("banking_leads_phoneButton")
        self.scan_potental_phishersButton = QtWidgets.QPushButton(self.bankingFeaturesTab)
        self.scan_potental_phishersButton.setEnabled(True)
        self.scan_potental_phishersButton.setGeometry(QtCore.QRect(520, 50, 141, 24))
        self.scan_potental_phishersButton.setObjectName("scan_potental_phishersButton")
        self.tab_widget.addTab(self.bankingFeaturesTab, "")
        self.requestedOptionsTab = QtWidgets.QWidget()
        self.requestedOptionsTab.setObjectName("requestedOptionsTab")
        self.columnView = QtWidgets.QColumnView(self.requestedOptionsTab)
        self.columnView.setGeometry(QtCore.QRect(540, 10, 256, 192))
        self.columnView.setObjectName("columnView")
        self.pushButton = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 80, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 10, 80, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 10, 80, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 50, 80, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 50, 80, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 50, 80, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 50, 80, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 90, 80, 24))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 90, 80, 24))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setGeometry(QtCore.QRect(190, 90, 80, 24))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.requestedOptionsTab)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(100, 90, 80, 24))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tab_widget.addTab(self.requestedOptionsTab, "")
        self.requestedOptionsTab2 = QtWidgets.QWidget()
        self.requestedOptionsTab2.setObjectName("requestedOptionsTab2")
        self.removeAfterSpace_2 = QtWidgets.QPushButton(self.requestedOptionsTab2)
        self.removeAfterSpace_2.setEnabled(False)
        self.removeAfterSpace_2.setGeometry(QtCore.QRect(290, 80, 171, 24))
        self.removeAfterSpace_2.setObjectName("removeAfterSpace_2")
        self.tab_widget.addTab(self.requestedOptionsTab2, "")
        self.savedResultsTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.savedResultsTextBox.setGeometry(QtCore.QRect(120, 30, 241, 31))
        self.savedResultsTextBox.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.savedResultsTextBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.savedResultsTextBox.setLineWidth(3)
        self.savedResultsTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.savedResultsTextBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.savedResultsTextBox.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.savedResultsTextBox.setObjectName("savedResultsTextBox")
        self.thread_box = QtWidgets.QSpinBox(self.centralwidget)
        self.thread_box.setGeometry(QtCore.QRect(750, 20, 71, 25))
        self.thread_box.setFrame(True)
        self.thread_box.setMinimum(1)
        self.thread_box.setObjectName("thread_box")
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(10, 110, 171, 281))
        self.input_text.setWhatsThis("")
        self.input_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input_text.setDocumentTitle("")
        self.input_text.setMarkdown("")
        self.input_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.input_text.setObjectName("input_text")
        self.variable_frame = QtWidgets.QFrame(self.centralwidget)
        self.variable_frame.setGeometry(QtCore.QRect(600, 250, 221, 131))
        self.variable_frame.setAutoFillBackground(False)
        self.variable_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variable_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.variable_frame.setObjectName("variable_frame")
        self.variables_label = QtWidgets.QLabel(self.variable_frame)
        self.variables_label.setGeometry(QtCore.QRect(70, 0, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.variables_label.setFont(font)
        self.variables_label.setObjectName("variables_label")
        self.url_variable_label = QtWidgets.QLabel(self.variable_frame)
        self.url_variable_label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.url_variable_label.setObjectName("url_variable_label")
        self.variable_text_username = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_username.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.variable_text_username.setObjectName("variable_text_username")
        self.variable_text_password = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_password.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.variable_text_password.setObjectName("variable_text_password")
        self.variable_text_email = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_email.setGeometry(QtCore.QRect(120, 20, 111, 16))
        self.variable_text_email.setObjectName("variable_text_email")
        self.variable_text_ip = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_ip.setGeometry(QtCore.QRect(120, 40, 81, 16))
        self.variable_text_ip.setObjectName("variable_text_ip")
        self.creditcard_variable_label = QtWidgets.QLabel(self.variable_frame)
        self.creditcard_variable_label.setGeometry(QtCore.QRect(120, 60, 101, 16))
        self.creditcard_variable_label.setObjectName("creditcard_variable_label")
        self.variable_text_cvc = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_cvc.setGeometry(QtCore.QRect(120, 80, 91, 16))
        self.variable_text_cvc.setObjectName("variable_text_cvc")
        self.variable_text_anrn = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_anrn.setGeometry(QtCore.QRect(120, 100, 101, 16))
        self.variable_text_anrn.setObjectName("variable_text_anrn")
        self.variable_text_fullz = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_fullz.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.variable_text_fullz.setObjectName("variable_text_fullz")
        self.variable_text_phone = QtWidgets.QLabel(self.variable_frame)
        self.variable_text_phone.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.variable_text_phone.setObjectName("variable_text_phone")
        self.directory_path_label_main = QtWidgets.QLabel(self.centralwidget)
        self.directory_path_label_main.setGeometry(QtCore.QRect(10, 0, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.directory_path_label_main.setFont(font)
        self.directory_path_label_main.setObjectName("directory_path_label_main")
        self.directory_path_label_main_2 = QtWidgets.QLabel(self.centralwidget)
        self.directory_path_label_main_2.setGeometry(QtCore.QRect(20, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.directory_path_label_main_2.setFont(font)
        self.directory_path_label_main_2.setObjectName("directory_path_label_main_2")
        self.set_directory_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_directory_path_button.setGeometry(QtCore.QRect(370, 0, 101, 21))
        self.set_directory_path_button.setObjectName("set_directory_path_button")
        self.save_results_action_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_results_action_button.setGeometry(QtCore.QRect(370, 30, 101, 21))
        self.save_results_action_button.setObjectName("save_results_action_button")
        self.enable_wordwrap_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.enable_wordwrap_checkbox.setGeometry(QtCore.QRect(150, 400, 131, 22))
        self.enable_wordwrap_checkbox.setObjectName("enable_wordwrap_checkbox")
        self.resultswidgets = QtWidgets.QTabWidget(self.centralwidget)
        self.resultswidgets.setGeometry(QtCore.QRect(180, 80, 211, 311))
        self.resultswidgets.setStyleSheet("QTabWidget::pane {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 2px solid teal;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: teal;\n"
"    border-color: teal;\n"
"}")
        self.resultswidgets.setObjectName("resultswidgets")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.output_text = QtWidgets.QTextBrowser(self.tab)
        self.output_text.setGeometry(QtCore.QRect(0, 0, 211, 291))
        self.output_text.setObjectName("output_text")
        self.resultswidgets.addTab(self.tab, "")
        self.removed_data_tab = QtWidgets.QWidget()
        self.removed_data_tab.setObjectName("removed_data_tab")
        self.removed_data_text = QtWidgets.QTextBrowser(self.removed_data_tab)
        self.removed_data_text.setGeometry(QtCore.QRect(0, 0, 211, 281))
        self.removed_data_text.setObjectName("removed_data_text")
        self.resultswidgets.addTab(self.removed_data_tab, "")
        self.consolewidget = QtWidgets.QWidget(self.centralwidget)
        self.consolewidget.setGeometry(QtCore.QRect(530, 60, 291, 141))
        self.consolewidget.setObjectName("consolewidget")
        self.console_widget_textedit = QtWidgets.QPlainTextEdit(self.consolewidget)
        self.console_widget_textedit.setGeometry(QtCore.QRect(0, 0, 291, 141))
        self.console_widget_textedit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.console_widget_textedit.setReadOnly(True)
        self.console_widget_textedit.setObjectName("console_widget_textedit")
        self.remove_empty_lines_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.remove_empty_lines_checkbox.setGeometry(QtCore.QRect(290, 400, 131, 22))
        self.remove_empty_lines_checkbox.setChecked(True)
        self.remove_empty_lines_checkbox.setTristate(False)
        self.remove_empty_lines_checkbox.setObjectName("remove_empty_lines_checkbox")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(430, 390, 381, 23))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(13)
        font.setBold(False)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("color: qconicalgradient(cx:1, cy:1, angle:0, stop:0.363128 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.import_requests_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_requests_button.setGeometry(QtCore.QRect(19, 400, 101, 24))
        self.import_requests_button.setObjectName("import_requests_button")
        self.StealerLog_File_Structure_label = QtWidgets.QLabel(self.centralwidget)
        self.StealerLog_File_Structure_label.setGeometry(QtCore.QRect(10, 690, 171, 21))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(11)
        font.setBold(False)
        self.StealerLog_File_Structure_label.setFont(font)
        self.StealerLog_File_Structure_label.setObjectName("StealerLog_File_Structure_label")
        self.file_directory_path_label = QtWidgets.QLabel(self.centralwidget)
        self.file_directory_path_label.setGeometry(QtCore.QRect(370, 690, 171, 21))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(11)
        font.setBold(False)
        self.file_directory_path_label.setFont(font)
        self.file_directory_path_label.setObjectName("file_directory_path_label")
        self.stealer_log_file_structure_path = QtWidgets.QTextEdit(self.centralwidget)
        self.stealer_log_file_structure_path.setEnabled(False)
        self.stealer_log_file_structure_path.setGeometry(QtCore.QRect(180, 690, 181, 21))
        self.stealer_log_file_structure_path.setAutoFillBackground(True)
        self.stealer_log_file_structure_path.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stealer_log_file_structure_path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stealer_log_file_structure_path.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stealer_log_file_structure_path.setReadOnly(True)
        self.stealer_log_file_structure_path.setObjectName("stealer_log_file_structure_path")
        self.file_directory_path_path = QtWidgets.QTextEdit(self.centralwidget)
        self.file_directory_path_path.setEnabled(False)
        self.file_directory_path_path.setGeometry(QtCore.QRect(540, 690, 181, 21))
        self.file_directory_path_path.setAutoFillBackground(True)
        self.file_directory_path_path.setInputMethodHints(QtCore.Qt.ImhNone)
        self.file_directory_path_path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_directory_path_path.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_directory_path_path.setReadOnly(True)
        self.file_directory_path_path.setObjectName("file_directory_path_path")
        self.totalLinesNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.totalLinesNumber.setGeometry(QtCore.QRect(530, 210, 61, 23))
        self.totalLinesNumber.setObjectName("totalLinesNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(530, 250, 61, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(530, 290, 61, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.total_lines_label = QtWidgets.QLabel(self.centralwidget)
        self.total_lines_label.setGeometry(QtCore.QRect(440, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(13)
        font.setBold(False)
        self.total_lines_label.setFont(font)
        self.total_lines_label.setObjectName("total_lines_label")
        self.lines_left_Label = QtWidgets.QLabel(self.centralwidget)
        self.lines_left_Label.setGeometry(QtCore.QRect(430, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(13)
        font.setBold(False)
        self.lines_left_Label.setFont(font)
        self.lines_left_Label.setObjectName("lines_left_Label")
        self.total_lines_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.total_lines_label_2.setGeometry(QtCore.QRect(390, 290, 141, 21))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(13)
        font.setBold(False)
        self.total_lines_label_2.setFont(font)
        self.total_lines_label_2.setObjectName("total_lines_label_2")
        self.Directory_Path_Text_Element = QtWidgets.QTextEdit(self.centralwidget)
        self.Directory_Path_Text_Element.setGeometry(QtCore.QRect(120, 0, 241, 31))
        font = QtGui.QFont()
        font.setBold(False)
        self.Directory_Path_Text_Element.setFont(font)
        self.Directory_Path_Text_Element.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Directory_Path_Text_Element.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Directory_Path_Text_Element.setLineWidth(3)
        self.Directory_Path_Text_Element.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Directory_Path_Text_Element.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Directory_Path_Text_Element.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.Directory_Path_Text_Element.setTabChangesFocus(True)
        self.Directory_Path_Text_Element.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.Directory_Path_Text_Element.setObjectName("Directory_Path_Text_Element")
        self.threads_text_label = QtWidgets.QLabel(self.centralwidget)
        self.threads_text_label.setGeometry(QtCore.QRect(760, 0, 49, 16))
        self.threads_text_label.setObjectName("threads_text_label")
        self.showDomainStatsButton = QtWidgets.QPushButton(self.centralwidget)
        self.showDomainStatsButton.setGeometry(QtCore.QRect(610, 210, 80, 24))
        self.showDomainStatsButton.setObjectName("showDomainStatsButton")
        self.total_lines_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.total_lines_label_3.setGeometry(QtCore.QRect(390, 330, 111, 21))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(13)
        font.setBold(False)
        self.total_lines_label_3.setFont(font)
        self.total_lines_label_3.setObjectName("total_lines_label_3")
        self.version_label_text = QtWidgets.QLabel(self.centralwidget)
        self.version_label_text.setGeometry(QtCore.QRect(740, 690, 71, 31))
        self.version_label_text.setObjectName("version_label_text")
        DiamondSorter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DiamondSorter)
        self.statusbar.setObjectName("statusbar")
        DiamondSorter.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(DiamondSorter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 21))
        self.menubar.setObjectName("menubar")
        self.menuDiamond_Sorter = QtWidgets.QMenu(self.menubar)
        self.menuDiamond_Sorter.setObjectName("menuDiamond_Sorter")
        self.menuConsole_Screen = QtWidgets.QMenu(self.menubar)
        self.menuConsole_Screen.setObjectName("menuConsole_Screen")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setToolTip("")
        self.menuAbout.setObjectName("menuAbout")
        self.menuBrowser = QtWidgets.QMenu(self.menubar)
        self.menuBrowser.setObjectName("menuBrowser")
        DiamondSorter.setMenuBar(self.menubar)
        self.ExtensionsBarQDockWidget = QtWidgets.QDockWidget(DiamondSorter)
        self.ExtensionsBarQDockWidget.setMinimumSize(QtCore.QSize(58, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.ExtensionsBarQDockWidget.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/diamond.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExtensionsBarQDockWidget.setWindowIcon(icon)
        self.ExtensionsBarQDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.ExtensionsBarQDockWidget.setObjectName("ExtensionsBarQDockWidget")
        self.widget_container = QtWidgets.QWidget()
        self.widget_container.setObjectName("widget_container")
        self.widget_button_cookies = QtWidgets.QPushButton(self.widget_container)
        self.widget_button_cookies.setEnabled(True)
        self.widget_button_cookies.setGeometry(QtCore.QRect(20, 0, 111, 21))
        self.widget_button_cookies.setObjectName("widget_button_cookies")
        self.widget_button_url_tools = QtWidgets.QPushButton(self.widget_container)
        self.widget_button_url_tools.setEnabled(True)
        self.widget_button_url_tools.setGeometry(QtCore.QRect(340, 0, 111, 21))
        self.widget_button_url_tools.setCheckable(False)
        self.widget_button_url_tools.setObjectName("widget_button_url_tools")
        self.widget_button_requests = QtWidgets.QPushButton(self.widget_container)
        self.widget_button_requests.setEnabled(True)
        self.widget_button_requests.setGeometry(QtCore.QRect(500, 0, 101, 24))
        self.widget_button_requests.setObjectName("widget_button_requests")
        self.widget_button_chat = QtWidgets.QPushButton(self.widget_container)
        self.widget_button_chat.setEnabled(True)
        self.widget_button_chat.setGeometry(QtCore.QRect(670, 0, 81, 24))
        self.widget_button_chat.setObjectName("widget_button_chat")
        self.widget_button_configs = QtWidgets.QPushButton(self.widget_container)
        self.widget_button_configs.setEnabled(True)
        self.widget_button_configs.setGeometry(QtCore.QRect(180, 0, 111, 21))
        self.widget_button_configs.setObjectName("widget_button_configs")
        self.ExtensionsBarQDockWidget.setWidget(self.widget_container)
        DiamondSorter.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.ExtensionsBarQDockWidget)
        self.actionaboutButton = QtWidgets.QAction(DiamondSorter)
        self.actionaboutButton.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionaboutButton.setObjectName("actionaboutButton")
        self.window_menu_actionRequired_Settings = QtWidgets.QAction(DiamondSorter)
        self.window_menu_actionRequired_Settings.setObjectName("window_menu_actionRequired_Settings")
        self.window_menu_actionPrefrences = QtWidgets.QAction(DiamondSorter)
        self.window_menu_actionPrefrences.setObjectName("window_menu_actionPrefrences")
        self.window_menu_actionRegex = QtWidgets.QAction(DiamondSorter)
        self.window_menu_actionRegex.setObjectName("window_menu_actionRegex")
        self.actionRegex_Cheat_Sheet = QtWidgets.QAction(DiamondSorter)
        self.actionRegex_Cheat_Sheet.setObjectName("actionRegex_Cheat_Sheet")
        self.actionHints_Tricks = QtWidgets.QAction(DiamondSorter)
        self.actionHints_Tricks.setObjectName("actionHints_Tricks")
        self.actionDataParsing = QtWidgets.QAction(DiamondSorter)
        self.actionDataParsing.setObjectName("actionDataParsing")
        self.actionDisplay_Console = QtWidgets.QAction(DiamondSorter)
        self.actionDisplay_Console.setObjectName("actionDisplay_Console")
        self.actionDisplay_HTTP_Client = QtWidgets.QAction(DiamondSorter)
        self.actionDisplay_HTTP_Client.setObjectName("actionDisplay_HTTP_Client")
        self.actionEnable_Everything = QtWidgets.QAction(DiamondSorter)
        self.actionEnable_Everything.setObjectName("actionEnable_Everything")
        self.actionLaunch_Browser = QtWidgets.QAction(DiamondSorter)
        self.actionLaunch_Browser.setIcon(icon)
        self.actionLaunch_Browser.setVisible(True)
        self.actionLaunch_Browser.setObjectName("actionLaunch_Browser")
        self.actionUndetected_Chrome = QtWidgets.QAction(DiamondSorter)
        self.actionUndetected_Chrome.setObjectName("actionUndetected_Chrome")
        self.actionShow_Widget_Functions = QtWidgets.QAction(DiamondSorter)
        self.actionShow_Widget_Functions.setObjectName("actionShow_Widget_Functions")
        self.actionInsomnia_HTTP_Client = QtWidgets.QAction(DiamondSorter)
        self.actionInsomnia_HTTP_Client.setObjectName("actionInsomnia_HTTP_Client")
        self.actionloadDirectory = QtWidgets.QAction(DiamondSorter)
        icon = QtGui.QIcon.fromTheme("accessories-text-editor")
        self.actionloadDirectory.setIcon(icon)
        self.actionloadDirectory.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.actionloadDirectory.setObjectName("actionloadDirectory")
        self.menuDiamond_Sorter.addAction(self.window_menu_actionRequired_Settings)
        self.menuDiamond_Sorter.addAction(self.window_menu_actionPrefrences)
        self.menuDiamond_Sorter.addAction(self.window_menu_actionRegex)
        self.menuDiamond_Sorter.addSeparator()
        self.menuDiamond_Sorter.addAction(self.actionShow_Widget_Functions)
        self.menuConsole_Screen.addAction(self.actionDisplay_Console)
        self.menuConsole_Screen.addSeparator()
        self.menuConsole_Screen.addAction(self.actionEnable_Everything)
        self.menuConsole_Screen.addSeparator()
        self.menuSettings.addAction(self.actionRegex_Cheat_Sheet)
        self.menuSettings.addAction(self.actionHints_Tricks)
        self.menuSettings.addAction(self.actionDataParsing)
        self.menuBrowser.addAction(self.actionLaunch_Browser)
        self.menuBrowser.addAction(self.actionUndetected_Chrome)
        self.menuBrowser.addSeparator()
        self.menuBrowser.addAction(self.actionInsomnia_HTTP_Client)
        self.menubar.addAction(self.menuDiamond_Sorter.menuAction())
        self.menubar.addAction(self.menuConsole_Screen.menuAction())
        self.menubar.addAction(self.menuBrowser.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.directory_path_label_main_2.setBuddy(self.savedResultsTextBox)

        self.retranslateUi(DiamondSorter)
        self.tab_widget.setCurrentIndex(0)
        self.stealer_log_format_combo.setCurrentIndex(0)
        self.resultswidgets.setCurrentIndex(0)
        self.stealer_log_format_combo.currentIndexChanged['int'].connect(self.redline_file_structure_text_browser.show) # type: ignore
        self.import_requests_button.clicked.connect(self.input_text.update) # type: ignore
        self.widget_button_cookies.clicked.connect(self.widget_button_configs.setFocus) # type: ignore
        self.console_widget_textedit.windowIconChanged['QIcon'].connect(self.console_widget_textedit.update) # type: ignore
        self.emailPasswordButton.clicked.connect(self.directory_path_label_main_2.deleteLater) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DiamondSorter)

    def retranslateUi(self, DiamondSorter):
        _translate = QtCore.QCoreApplication.translate
        DiamondSorter.setWindowTitle(_translate("DiamondSorter", "DiamondSorter"))
        self.tab_widget.setToolTip(_translate("DiamondSorter", "This will be your basic format options for all functions in \n"
" this window. Your values that you set in place here will be \n"
" how the script performs and operates."))
        self.tab_widget.setWhatsThis(_translate("DiamondSorter", "Find out more"))
        self.deleate_after_sorting_checkbox.setText(_translate("DiamondSorter", "Deleate Files After Sorting?"))
        self.file_type_or_format_for_the_search_label.setToolTip(_translate("DiamondSorter", "<html><head/><body><p>Specify the file format or file name / pattern you would like to search.<br/><br/>Examples:<br/>New Text Document.txt<br/>*Document.txt<br/>*.txt</p></body></html>"))
        self.file_type_or_format_for_the_search_label.setPlaceholderText(_translate("DiamondSorter", "Leave blank to search all files"))
        self.stealer_log_format_label.setText(_translate("DiamondSorter", "Stealer Log Capture Format"))
        self.file_type_or_format_label.setText(_translate("DiamondSorter", "File Type or Format for the Search"))
        self.stealer_log_format_combo.setItemText(1, _translate("DiamondSorter", "Redline / Meta"))
        self.stealer_log_format_combo.setItemText(2, _translate("DiamondSorter", "Racoon"))
        self.stealer_log_format_combo.setItemText(3, _translate("DiamondSorter", "Titan Stealer"))
        self.stealer_log_format_combo.setItemText(4, _translate("DiamondSorter", "White Snake"))
        self.stealer_log_format_combo.setItemText(5, _translate("DiamondSorter", "Worldwind / Prynt"))
        self.label.setText(_translate("DiamondSorter", "File Structure:"))
        self.redline_file_structure_text_browser.setHtml(_translate("DiamondSorter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Autofills</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Cookies</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Firefox_c09zp0gb.default-release.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Network.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default Network.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 DomainDetects.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 ImportantAutofills.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 InstalledBrowsers.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 InstalledSoftware.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 Passwords.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 ProcessList.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Restore</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Fresh Cookies.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Token.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default Token.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 Screenshot.jpg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 UserAgents</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome].txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge].txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 UserInformation.txt</p></body></html>"))
        self.racoon_file_structure_text_browser.setHtml(_translate("DiamondSorter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Autofill</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google Chrome_Profile.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google Chrome_Profile.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Cookies</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google Chrome_Profile.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google Chrome_Profile.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft Edge_Default.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 domain detect.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Downloads</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google Chrome_Profile.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Files</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Default.zip</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 History</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google Chrome_Profile.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google Chrome_Profile.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 information.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 passwords.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 screenshot.jpg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Soft</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📁 Steam</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    📄 config.vdf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    📄 loginusers.vdf</p></body></html>"))
        self.titan_file_structure_text_browser.setHtml(_translate("DiamondSorter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Autofills</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Cookies</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Firefox_c09zp0gb.default-release.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Network.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default Network.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 DomainDetects.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 ImportantAutofills.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 InstalledBrowsers.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 InstalledSoftware.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 Passwords.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 ProcessList.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Restore</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Fresh Cookies.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Token.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default Token.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 Screenshot.jpg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 UserAgents</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome].txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge].txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 UserInformation.txt</p></body></html>"))
        self.worldwind_file_structure_text_browser.setHtml(_translate("DiamondSorter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Browsers</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    📁 BraveSoftware</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 AutoFill.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Bookmarks.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 History.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Passwords.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   📁 Edge</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 AutoFill.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Bookmarks.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 History.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Passwords.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   📁 Google</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 AutoFill.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Bookmarks.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Downloads.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Passwords.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Directories</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Desktop.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Documents.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Downloads.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 OneDrive.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Pictures.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Startup.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Temp.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Videos.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Gaming</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    📁 Minecraft</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 launcher_profiles.json</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    📁 Steam</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 Apps.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Grabber</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📁 DRIVE-C<br />            📁 Desktop</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            📁 Documents</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            📁 Pictures</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            📁 Camera Roll</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                 📄</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                 📄</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            📁 Saved Pictures</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            📁 Screenshots</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Messenger</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📁 Discord</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    📁 leveldb</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 000075.ldb</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 000077.log</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 000078.ldb</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 CURRENT</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 LOCK</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 LOG</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 LOG.old</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 MANIFEST-000001</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📁 Telegram</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    📁 D877F783D5D3EF8C</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 24AF661708B83EDCs</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 3ABD80B4D779F270s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 43E576770DA194D4s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 D877F783D5D3EF8Cs</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 key_datas</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 settingss</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      📄 usertag</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 System</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Process.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 ProductKey.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 SavedNetworks.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 ScanningNetworks.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Windows.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 WorldWind.jpg</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.whitesnake_file_structure_text_browser.setHtml(_translate("DiamondSorter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Autofills</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Cookies</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Firefox_c09zp0gb.default-release.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Network.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default Network.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 DomainDetects.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 ImportantAutofills.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 InstalledBrowsers.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 InstalledSoftware.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 Passwords.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 ProcessList.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 Restore</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Fresh Cookies.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome]_Default Token.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge]_Default Token.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 Screenshot.jpg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📁 UserAgents</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Google_[Chrome].txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  📄 Microsoft_[Edge].txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">📄 UserInformation.txt</p></body></html>"))
        self.domain_managerButton.setText(_translate("DiamondSorter", "Domain Manager"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.formatOptionsTab), _translate("DiamondSorter", "❗Format Options"))
        self.pasteButton.setText(_translate("DiamondSorter", "Paste Input"))
        self.removeLinksButton.setText(_translate("DiamondSorter", "Remove Links"))
        self.copyButton_2.setText(_translate("DiamondSorter", "Copy Output"))
        self.removeEndingPunctuationButton.setText(_translate("DiamondSorter", "Remove Ending Punctuation"))
        self.remove_domainsButton.setText(_translate("DiamondSorter", "- Domains"))
        self.removeDuplicatesButton.setText(_translate("DiamondSorter", "- Duplicates"))
        self.extract_md5Button.setText(_translate("DiamondSorter", "Extract MD5"))
        self.removeSpecialCharacterButton.setText(_translate("DiamondSorter", "Remove after Special Character"))
        self.organizeLinesButton.setText(_translate("DiamondSorter", "Organize"))
        self.remove_trash_button.setText(_translate("DiamondSorter", "Remove Trash"))
        self.remove_capturesButton.setText(_translate("DiamondSorter", "- Captures"))
        self.split_by_linesButton.setText(_translate("DiamondSorter", "Split By Lines"))
        self.removeAfterSpace.setText(_translate("DiamondSorter", "Remove After Space"))
        self.removeAfter_Tab_Space.setText(_translate("DiamondSorter", "- After Tab Space"))
        self.remove_inbetween_two_variablesButton.setText(_translate("DiamondSorter", "Remove Inbetween Variables"))
        self.sort_remove_similarButton.setText(_translate("DiamondSorter", "Remove Similar"))
        self.replace_linesButton.setText(_translate("DiamondSorter", "Replace Lines"))
        self.extract_ip_addressButton.setText(_translate("DiamondSorter", "Extract IP"))
        self.extract_phone_numberButton.setText(_translate("DiamondSorter", "Extract Phn Num"))
        self.format_request_textedit.setPlaceholderText(_translate("DiamondSorter", "Format Request From Variables Above Progress Bar"))
        self.remove_new_lines.setText(_translate("DiamondSorter", "Remove All New Lines"))
        self.consecutive_digits_button.setText(_translate("DiamondSorter", "Consecutive Digits"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.generalComboOptionsTab), _translate("DiamondSorter", "❗General Combo Options"))
        self.emailPasswordButton.setText(_translate("DiamondSorter", "Email:Password"))
        self.usernamePasswordButton.setText(_translate("DiamondSorter", "Username:Password"))
        self.memberIDPINButton.setText(_translate("DiamondSorter", "Member ID:PIN"))
        self.numberPasswordButton.setText(_translate("DiamondSorter", "Number:Password"))
        self.wordpress_finder_button.setText(_translate("DiamondSorter", "Wordpress Finder"))
        self.business_emailfinder_button.setText(_translate("DiamondSorter", "Business Emails"))
        self.governmentDomainsButton.setText(_translate("DiamondSorter", "Gov Domains"))
        self.server_information_button.setText(_translate("DiamondSorter", "Server Information"))
        self.cpanel_account_button.setText(_translate("DiamondSorter", "Cpanel Accounts"))
        self.mailBoxesOptions_ComboButton.setToolTip(_translate("DiamondSorter", "Emails"))
        self.mailBoxesOptions_ComboButton.setWhatsThis(_translate("DiamondSorter", "<html><head/><body><p>Sort by mails</p></body></html>"))
        self.mailBoxesOptions_ComboButton.setText(_translate("DiamondSorter", "✅"))
        self.advertisingButton.setText(_translate("DiamondSorter", "Advertisements"))
        self.socialForumsButton.setText(_translate("DiamondSorter", "Socials && Forums"))
        self.mailbox_options_combo.setToolTip(_translate("DiamondSorter", "Emails"))
        self.mailbox_options_combo.setWhatsThis(_translate("DiamondSorter", "<html><head/><body><p>Sort by mails</p></body></html>"))
        self.mailbox_options_combo.setItemText(0, _translate("DiamondSorter", "United States"))
        self.mailbox_options_combo.setItemText(1, _translate("DiamondSorter", "Canada"))
        self.mailbox_options_combo.setItemText(2, _translate("DiamondSorter", "Business Emails"))
        self.password_working_function_combo.setItemText(1, _translate("DiamondSorter", "Work from Specified Directory"))
        self.password_working_function_combo.setItemText(2, _translate("DiamondSorter", "Work from Input Requests"))
        self.frame_2.setWhatsThis(_translate("DiamondSorter", "These will be the variable inputs you can use\n"
"beside the <b>Desired Format</b> text input. This will\n"
"be saved in the path you have noted in the \n"
" <b>Saved Results</b> text input"))
        self.variables_label_2.setText(_translate("DiamondSorter", "Variables"))
        self.url_variable_label_2.setText(_translate("DiamondSorter", "URL: {URL}"))
        self.label_9.setText(_translate("DiamondSorter", "Username: {USER}"))
        self.label_20.setText(_translate("DiamondSorter", "Password: {PASS}"))
        self.label_21.setText(_translate("DiamondSorter", "Email: {EMAIL}"))
        self.label_22.setText(_translate("DiamondSorter", "IP Address: {IP}"))
        self.creditcard_variable_label_2.setText(_translate("DiamondSorter", "Credit Card: {CC}"))
        self.label_23.setText(_translate("DiamondSorter", "CVC: {CVC}"))
        self.label_24.setText(_translate("DiamondSorter", "AN/RN: {ANRN}"))
        self.label_25.setText(_translate("DiamondSorter", "Personal: {FULLZ}"))
        self.label_26.setText(_translate("DiamondSorter", "Phone List: {PHN}"))
        self.label_27.setText(_translate("DiamondSorter", "Location: {GEO}"))
        self.create_username_list_button.setText(_translate("DiamondSorter", "Create Username List"))
        self.create_password_list.setText(_translate("DiamondSorter", "Create Password List"))
        self.create_number_list.setText(_translate("DiamondSorter", "Create Number List"))
        self.copyButton.setText(_translate("DiamondSorter", "Copy Output"))
        self.tab2_pasteButton.setText(_translate("DiamondSorter", "Paste Input"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.password_format_tab), _translate("DiamondSorter", "🔑 Password Log Formats"))
        self.sort_by_cap_dateButton.setText(_translate("DiamondSorter", "Sort by Capture Date"))
        self.sort_password_by_weightButton.setText(_translate("DiamondSorter", "Sort by Password Weight"))
        self.remove_duplicatesButton.setText(_translate("DiamondSorter", "Remove Duplicates"))
        self.sort_by_file_capturesButton.setText(_translate("DiamondSorter", "Sort by File Captures"))
        self.sort_stealer_typeButton.setText(_translate("DiamondSorter", "Sort by Stealer Type"))
        self.sort_by_geoButton.setText(_translate("DiamondSorter", "Sort by Geo Data"))
        self.remove_skinnyButton.setText(_translate("DiamondSorter", "Remove Skinny Logs"))
        self.sort_tg_groupButton.setText(_translate("DiamondSorter", "Sort by TG Group"))
        self.sort_by_ads_logsButton.setText(_translate("DiamondSorter", "Sort by Ad Logs"))
        self.sort_by_business_capturesButton.setText(_translate("DiamondSorter", "Sort by Business Captures"))
        self.create_a_file_tree_sortinglogsButton.setText(_translate("DiamondSorter", "Create a File Tree"))
        self.sort_email_domainsButton.setText(_translate("DiamondSorter", "Sort Email Domains"))
        self.variable_text_edit_path.setPlaceholderText(_translate("DiamondSorter", "{URL} | {USER} | {PASS}"))
        self.extractBySearchButton.setText(_translate("DiamondSorter", "Extract Search Requests"))
        self.sort_passwords_textButton.setText(_translate("DiamondSorter", "Sort All Passwords.txt"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.sortingLogsTab), _translate("DiamondSorter", "📃 Sorting Logs"))
        self.telegram_folder_sorting_button.setText(_translate("DiamondSorter", "Telegram Folders"))
        self.authy_desktop_button.setText(_translate("DiamondSorter", "Authy Desktop"))
        self.chrome_extensions_button.setText(_translate("DiamondSorter", "Chrome Extensions"))
        self.desktop_wallet_button.setText(_translate("DiamondSorter", "Desktop Wallets"))
        self.browser_wallet_sort_button.setText(_translate("DiamondSorter", "Browser Wallets"))
        self.browser_2fa_extension_button.setText(_translate("DiamondSorter", "Browser 2FA Exten"))
        self.newtextdocuments_button.setText(_translate("DiamondSorter", "New Text Documents"))
        self.text_named_sorting_button.setText(_translate("DiamondSorter", "Text Named Files"))
        self.pgp_button.setText(_translate("DiamondSorter", "PGP & GPG Keys"))
        self.encryption_keys_button.setText(_translate("DiamondSorter", "Encryption Keys"))
        self.auth_files_button.setText(_translate("DiamondSorter", "Auth Files"))
        self.sort_by_cookies_button.setText(_translate("DiamondSorter", "Sort by Cookies"))
        self.remote_desktop_button.setText(_translate("DiamondSorter", "Remote Desktops"))
        self.discord_sorting_button.setText(_translate("DiamondSorter", "Discord Files"))
        self.control_panels_sort_button.setText(_translate("DiamondSorter", "Control Panels"))
        self.button_scrape_keys.setText(_translate("DiamondSorter", "Scrape Keys"))
        self.button_scrape_banking_data.setText(_translate("DiamondSorter", "Scrape Banking Data"))
        self.button_scrape_backup_codes.setText(_translate("DiamondSorter", "Scrape Backup Codes"))
        self.button_scrape_security_data.setText(_translate("DiamondSorter", "Scrape Security Data"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.sortingFilesTab), _translate("DiamondSorter", "📃 Sorting Files"))
        self.sorting_cookies_sort_by_domain.setText(_translate("DiamondSorter", "Sort By Domain"))
        self.sorting_cookies_sort_by_quantity.setText(_translate("DiamondSorter", "Sort by Quantity"))
        self.sorting_cookies_sort_by_values_button.setText(_translate("DiamondSorter", "Sort by Values"))
        self.sorting_cookies_keywords_button.setText(_translate("DiamondSorter", "Keywords"))
        self.sorting_cookies_netscape_to_json_button.setText(_translate("DiamondSorter", "Netscape > Json"))
        self.sorting_cookies_json_to_netscape_button.setText(_translate("DiamondSorter", "JSON > Netscape"))
        self.sorting_cookies_save_password_checkbox.setText(_translate("DiamondSorter", "Save with Passwords"))
        self.sorting_cookies_save_login_cookie_capture_checkbox.setText(_translate("DiamondSorter", "Saved Login Cookie Capture"))
        self.sorting_cookies_save_autofill_data_button.setText(_translate("DiamondSorter", "Save with Autofill Data"))
        self.sorting_cookies_fix_cookie_misprintButton.setText(_translate("DiamondSorter", "Fix Cookie Misprint"))
        self.sorting_cookies_count_total_values.setText(_translate("DiamondSorter", "Count Total Values"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.sortingCookiesTab), _translate("DiamondSorter", "🍪 Sorting Cookies"))
        self.capture_security_quest_answer_button.setText(_translate("DiamondSorter", "Capture Security Q and A"))
        self.capture_all_banking_logs_button.setText(_translate("DiamondSorter", "Capture All Banking Logs"))
        self.parse_fulls_button.setText(_translate("DiamondSorter", "Parse Fullz Data Out"))
        self.sort_cc_dataButton.setText(_translate("DiamondSorter", "Sort CC Data"))
        self.sort_cc_data_with_cvcButton.setText(_translate("DiamondSorter", "Sort CC Data with CVC"))
        self.sort_by_remitliesButton.setText(_translate("DiamondSorter", "Sort by Remitlies"))
        self.sort_by_remetliescookiesButton.setText(_translate("DiamondSorter", "Sort by Remitly Cookies"))
        self.search_inside_new_text_docs.setText(_translate("DiamondSorter", "Search Inside NewText"))
        self.capture_2fa_files_bypassButton.setText(_translate("DiamondSorter", "Capture 2FA Bypass"))
        self.banking_leads_emailButton.setText(_translate("DiamondSorter", "Banking Leads - Email"))
        self.banking_leads_phoneButton.setText(_translate("DiamondSorter", "Banking Leads - Phone"))
        self.scan_potental_phishersButton.setText(_translate("DiamondSorter", "Scan Potental Phishers"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.bankingFeaturesTab), _translate("DiamondSorter", "🏦 Banking Features"))
        self.pushButton.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_2.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_3.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_4.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_5.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_6.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_7.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_8.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_9.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_10.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_11.setText(_translate("DiamondSorter", "PushButton"))
        self.pushButton_12.setText(_translate("DiamondSorter", "PushButton"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.requestedOptionsTab), _translate("DiamondSorter", "Requested Options #1"))
        self.removeAfterSpace_2.setText(_translate("DiamondSorter", "Remove After Space"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.requestedOptionsTab2), _translate("DiamondSorter", "Requested Options #2"))
        self.savedResultsTextBox.setPlaceholderText(_translate("DiamondSorter", "Pick your path to save the results"))
        self.thread_box.setToolTip(_translate("DiamondSorter", "The number of threads you would like the script to run on"))
        self.input_text.setToolTip(_translate("DiamondSorter", "This is for your input requests, searches, and functions"))
        self.input_text.setPlaceholderText(_translate("DiamondSorter", "Input Requests  "))
        self.variable_frame.setToolTip(_translate("DiamondSorter", "These variables is what you will be using when requesting logs in a specific format."))
        self.variables_label.setText(_translate("DiamondSorter", "Variables"))
        self.url_variable_label.setText(_translate("DiamondSorter", "URL: {URL}"))
        self.variable_text_username.setText(_translate("DiamondSorter", "Username: {USER}"))
        self.variable_text_password.setText(_translate("DiamondSorter", "Password: {PASS}"))
        self.variable_text_email.setText(_translate("DiamondSorter", "Email: {EMAIL}"))
        self.variable_text_ip.setText(_translate("DiamondSorter", "IP Address: {IP}"))
        self.creditcard_variable_label.setText(_translate("DiamondSorter", "Credit Card: {CC}"))
        self.variable_text_cvc.setText(_translate("DiamondSorter", "CVC: {CVC}"))
        self.variable_text_anrn.setText(_translate("DiamondSorter", "AN/RN: {ANRN}"))
        self.variable_text_fullz.setText(_translate("DiamondSorter", "Personal: {FULLZ}"))
        self.variable_text_phone.setText(_translate("DiamondSorter", "Phone List: {PHN}"))
        self.directory_path_label_main.setText(_translate("DiamondSorter", "Directory Path:"))
        self.directory_path_label_main_2.setText(_translate("DiamondSorter", "Save Results:"))
        self.set_directory_path_button.setText(_translate("DiamondSorter", "Select Directory"))
        self.save_results_action_button.setText(_translate("DiamondSorter", "Select Directory"))
        self.enable_wordwrap_checkbox.setText(_translate("DiamondSorter", "Enable Word Wrap?"))
        self.output_text.setToolTip(_translate("DiamondSorter", "Mainly for combo uses - this will display the results of your actions when using combolists and data"))
        self.output_text.setPlaceholderText(_translate("DiamondSorter", "Output Lines"))
        self.resultswidgets.setTabText(self.resultswidgets.indexOf(self.tab), _translate("DiamondSorter", "Results Tab"))
        self.removed_data_text.setToolTip(_translate("DiamondSorter", "Mainly for combo uses - this will display the results of your actions when using combolists and data"))
        self.removed_data_text.setPlaceholderText(_translate("DiamondSorter", "Removed Data"))
        self.resultswidgets.setTabText(self.resultswidgets.indexOf(self.removed_data_tab), _translate("DiamondSorter", "Removed Data Tab"))
        self.console_widget_textedit.setPlaceholderText(_translate("DiamondSorter", "Console Display                                                                             File Structure: {Redline/Meta}                                                                            Directory Path: {Path}                                                              .                                                                                             Sorting Option Chosen: {Button Pressed}                                                   .                                                                                                  Functions Output                                           "))
        self.remove_empty_lines_checkbox.setText(_translate("DiamondSorter", "Remove Empty Lines?"))
        self.import_requests_button.setText(_translate("DiamondSorter", "Import Requests"))
        self.StealerLog_File_Structure_label.setText(_translate("DiamondSorter", "Stealer Log File Structure:"))
        self.file_directory_path_label.setText(_translate("DiamondSorter", "File Directory Path Chosen:"))
        self.total_lines_label.setText(_translate("DiamondSorter", "Input Lines"))
        self.lines_left_Label.setText(_translate("DiamondSorter", "Results Tab"))
        self.total_lines_label_2.setText(_translate("DiamondSorter", "Removed Data Tab"))
        self.Directory_Path_Text_Element.setPlaceholderText(_translate("DiamondSorter", "Set your path to work from"))
        self.threads_text_label.setText(_translate("DiamondSorter", "Threads"))
        self.showDomainStatsButton.setText(_translate("DiamondSorter", "Show Stats"))
        self.total_lines_label_3.setText(_translate("DiamondSorter", "Last Function:"))
        self.version_label_text.setText(_translate("DiamondSorter", "version 1.7"))
        self.menuDiamond_Sorter.setTitle(_translate("DiamondSorter", "Diamond Sorter"))
        self.menuConsole_Screen.setTitle(_translate("DiamondSorter", "Console Screen"))
        self.menuSettings.setTitle(_translate("DiamondSorter", "Settings"))
        self.menuAbout.setTitle(_translate("DiamondSorter", "About"))
        self.menuBrowser.setTitle(_translate("DiamondSorter", "Browser"))
        self.ExtensionsBarQDockWidget.setWindowTitle(_translate("DiamondSorter", "Features"))
        self.widget_button_cookies.setToolTip(_translate("DiamondSorter", "Cookies Widget\n"
"This option will help you manage and inspect your cookie data and values."))
        self.widget_button_cookies.setText(_translate("DiamondSorter", "Cookies"))
        self.widget_button_url_tools.setToolTip(_translate("DiamondSorter", "URL Tool Widget\n"
"This widget will allow the user to inspect\n"
"and get the analytics of URL Domains\n"
"And can also help you chase down new leads or\n"
"New approachs to websites."))
        self.widget_button_url_tools.setText(_translate("DiamondSorter", "URL Tool"))
        self.widget_button_requests.setToolTip(_translate("DiamondSorter", "Request Widget - TBA"))
        self.widget_button_requests.setText(_translate("DiamondSorter", "Request"))
        self.widget_button_chat.setToolTip(_translate("DiamondSorter", "About Widget\n"
"This widget will take you the \"Credits\" portion of the softwareThis is where you can find more indepth explinations\n"
"of all the functions and features that is included in this software"))
        self.widget_button_chat.setText(_translate("DiamondSorter", "Chat"))
        self.widget_button_configs.setToolTip(_translate("DiamondSorter", "Configs Widget\n"
"This widget will give you several various functions\n"
"that will help you generate and create a number\n"
"of various checkers such as Cookie Bullet, BL Tools\n"
"Silverbullet, Openbullet, Python and more."))
        self.widget_button_configs.setText(_translate("DiamondSorter", "CFGs"))
        self.actionaboutButton.setText(_translate("DiamondSorter", "aboutButton"))
        self.window_menu_actionRequired_Settings.setText(_translate("DiamondSorter", "Diamond Pad"))
        self.window_menu_actionPrefrences.setText(_translate("DiamondSorter", "Regex Creator"))
        self.window_menu_actionRegex.setText(_translate("DiamondSorter", "Expression Veiwer"))
        self.actionRegex_Cheat_Sheet.setText(_translate("DiamondSorter", "Regex Cheat Sheet"))
        self.actionHints_Tricks.setText(_translate("DiamondSorter", "Hints & Tricks"))
        self.actionDataParsing.setText(_translate("DiamondSorter", "DataParsing"))
        self.actionDisplay_Console.setText(_translate("DiamondSorter", "Display Console"))
        self.actionDisplay_HTTP_Client.setText(_translate("DiamondSorter", "Display HTTP Client"))
        self.actionEnable_Everything.setText(_translate("DiamondSorter", "Enable \"Everything\""))
        self.actionLaunch_Browser.setText(_translate("DiamondSorter", "Launch Browser"))
        self.actionUndetected_Chrome.setText(_translate("DiamondSorter", "Undetected Chrome"))
        self.actionShow_Widget_Functions.setText(_translate("DiamondSorter", "Show Widget Functions"))
        self.actionInsomnia_HTTP_Client.setText(_translate("DiamondSorter", "Insomnia HTTP Client"))
        self.actionloadDirectory.setText(_translate("DiamondSorter", "loadDirectory"))

        self.setWindowTitle(self.windowTitle() + ('' if INSTALLER_MODE else ' ~ WIP'))
        script_dir = os.path.dirname(sys.argv[0])
        icon_path = os.path.join(script_dir, "icons", "diamond.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.result = None
        self.console_layout = QVBoxLayout(self.consolewidget)
        self.console_layout.addWidget(self.consolewidget)
        self.directory_path_text_element = QtWidgets.QTextEdit()
        self.Directory_Path_Text_Element = self.directory_path_text_element
        # Create an instance of ExtensionsBarQDockWidget
        self.extensions_bar = ExtensionsBarQDockWidget()
        redline_file_structure_text_browser = "Redline / Meta"
        racoon_file_structure_text_browser = "Racoon Stealer"
        whitesnake_file_structure_text_browser = "Whitesnake"
        worldwind_file_structure_text_browser = "Worldwind / Prynt"

        self.set_directory_path_button.clicked.connect(self.open_directory_dialog)
        self.save_results_action_button.clicked.connect(self.open_save_directory_dialog)
        self.set_directory_path_button.clicked.connect(self.open_directory_dialog)
        self.save_results_action_button.clicked.connect(self.open_save_directory_dialog)
        self.app = QApplication.instance()

        self.input_text = self.findChild(QTextEdit, "input_text")
        self.output_text = self.findChild(QTextBrowser, "output_text")
        self.removed_data_text = self.findChild(QTextBrowser, "removed_data_text")
        self.input_text.textChanged.connect(self.update_line_count)
        self.output_text.textChanged.connect(self.update_line_count)
        self.removed_data_text.textChanged.connect(self.update_line_count)
        
        self.enable_wordwrap_checkbox = self.findChild(QCheckBox, "enable_wordwrap_checkbox")
        self.enable_wordwrap_checkbox.stateChanged.connect(self.toggle_word_wrap)
        self.enable_remove_empty_lines_checkbox = self.findChild(QCheckBox, "remove_empty_lines_checkbox")

        self.layout = QVBoxLayout()

        self.actionLaunch_Browser.triggered.connect(self.open_browser)
        self.actionInsomnia_HTTP_Client.triggered.connect(launch_insomnia)

        self.remove_trash_button = self.findChild(QPushButton, "remove_trash_button")
        if self.remove_trash_button is not None:
            self.remove_trash_button.clicked.connect(self.remove_trash_button_clicked)
        self.display_function("MyFunction")

        self.import_requests_button = QPushButton("Import Requests")

        self.button = QtWidgets.QPushButton("Process Directory")
        self.button.clicked.connect(self.handle_newtextdocuments)

        #central_widget = QWidget(self)
        #layout = QVBoxLayout(central_widget)

        #self.count_error_lines = QLCDNumber(self)
        ##self.count_left_to_go = QLCDNumber(self)
        #self.count_already_ran = QLCDNumber(self)
        #self.totalLinesNumber = QLCDNumber(self)
        #self.lcdNumber_1 = QLCDNumber(self)


        


    def display_function(self, function_name):
        """Update the text of the running_task_placeholder label."""
        if function_name == self.redline_file_structure_text_browser:
            self.stealer_log_file_structure_path.setText(self.redline_file_structure_text_browser)
        elif function_name == self.racoon_file_structure_text_browser:
            self.stealer_log_file_structure_path.setText(self.racoon_file_structure_text_browser)
        elif function_name == self.whitesnake_file_structure_text_browser:
            self.stealer_log_file_structure_path.setText(self.whitesnake_file_structure_text_browser)
        elif function_name == self.worldwind_file_structure_text_browser:
            self.stealer_log_file_structure_path.setText(self.worldwind_file_structure_text_browser)

    def open_directory_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            selected_directory = dialog.selectedFiles()[0]
            self.Directory_Path_Text_Element.setPlainText(selected_directory)
            
    def open_save_directory_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            selected_directory = dialog.selectedFiles()[0]
            self.Save_Results_Text_Element.setPlainText(selected_directory)
    
    def import_requests(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text Files (*.txt)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            with open(file_path, 'r') as file:
                text = file.read()
                self.input_text.setText(text)

    def remove_trash_button_clicked(self):
        """Handle the button click event for remove_trash_button."""
        options = ["Remove Unknown", "Remove ****", "Remove Short", "Remove Simalar", "Remove User", "Remove Missing Value(U or P)"]  # Replace with your specific options

        # Create the custom dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Remove Trash Options")  # Set the title of the dialog window

        layout = QGridLayout(dialog)  # Use QGridLayout for the layout

        checkboxes = []
        for i, option in enumerate(options):
            checkbox = QCheckBox(option)
            row = i // 4  # Calculate the row based on the index
            col = i % 4  # Calculate the column based on the index
            layout.addWidget(checkbox, row, col)  # Add the checkbox to the layout
            checkboxes.append(checkbox)

        # Add OK and Cancel buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons, row + 1, 0, 1, 4)  # Add the buttons to the layout
        
        # Execute the dialog and get the selected options
        if dialog.exec_() == QDialog.Accepted:
            selected_options = [checkbox.text() for checkbox in checkboxes if checkbox.isChecked()]
            # Start the removal process based on the selected options
            self.start_removal(selected_options)

    def start_removal(self, selected_options):
        """Perform the removal process based on the selected options."""
        # Implement the removal process based on the selected options
        # You can use control structures like if-else or loops to handle different options
    
        # Example code:
        for option in selected_options:
            if option == "Remove Unknown":
                # Handle Option 1 removal
                pass
            elif option == "Remove ****":
                # Handle Option 2 removal
                pass
            elif option == "Remove Short":
                # Handle Option 3 removal
                pass
            elif option == "Remove Simalar":
                # Handle Option 4 removal
                pass
            elif option == "Passwords that has less that 3 characters":
                # Handle Option 5 removal
                pass
            elif option == "Remove ÐµÐâ":
                # Handle Option 6 removal
                pass
            elif option == "Remove Illegal Usernames":
                # Handle Option 7 removal
                pass

    def update_output_text(self):
        output_text = self.password_format_tab.output_text.toPlainText()
        if self.remove_empty_lines_checkbox.isChecked():
            output_text = "\n".join(line for line in output_text.split("\n") if line.strip())
        self.password_format_tab.output_text.setPlainText(output_text)

    def open_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.Directory_Path_Text_Element.setText(directory)

    def open_save_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.savedResultsTextBox.setText(directory)

    def open_browser(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setText("You are about to launch the built-in browser. Continue?")
        message_box.setWindowTitle("Diamond Sorter - Window")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        message_box.setDefaultButton(QtWidgets.QMessageBox.Yes)
    
        result = message_box.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            script_path = os.path.join(current_dir, "references", "scripts", "browser.py")
            subprocess.Popen(["python", script_path])

    def cleanup(self):
        """Cleanup the input text."""
        try:
            # Ask for confirmation
            reply = QMessageBox.question(
                self,
                "Confirmation",
                "Are you sure you want to perform the cleanup action?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
    
            if reply == QMessageBox.Yes:
                input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
                output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
                if input_text is not None and output_text is not None:
                    text = input_text.toPlainText()
                    lines = text.split("\n")
                    cleaned_lines = [line.strip() for line in lines if line.strip()]
    
                    output_text.clear()
                    output_text.setPlainText("\n".join(cleaned_lines))
                    self.update_line_count()  # Assuming update_line_count is a method in your class
    
                    # Display the pop-up window with checkboxes
                    dialog = QDialog(self)
                    layout = QVBoxLayout(dialog)
    
                    # Add checkboxes
                    checkbox1 = QCheckBox("Checkbox 1")
                    checkbox2 = QCheckBox("Checkbox 2")
                    checkbox3 = QCheckBox("Checkbox 3")
                    checkbox4 = QCheckBox("Checkbox 4")
                    checkbox5 = QCheckBox("Checkbox 5")
                    checkbox6 = QCheckBox("Checkbox 6")
                    checkbox7 = QCheckBox("Checkbox 7")
    
                    layout.addWidget(checkbox1)
                    layout.addWidget(checkbox2)
                    layout.addWidget(checkbox3)
                    layout.addWidget(checkbox4)
                    layout.addWidget(checkbox5)
                    layout.addWidget(checkbox6)
                    layout.addWidget(checkbox7)
    
                    # Add OK and Cancel buttons
                    buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                    buttons.accepted.connect(dialog.accept)
                    buttons.rejected.connect(dialog.reject)
    
                    layout.addWidget(buttons)
    
                    if dialog.exec_() == QDialog.Accepted:
                        # OK button pressed, perform further actions based on the checkbox states
                        if checkbox1.isChecked():
                            # Handle checkbox 1 checked
                            pass
                        if checkbox2.isChecked():
                            # Handle checkbox 2 checked
                            pass
                        # ... handle other checkboxes
    
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_userlist(self):
        """Create a list of values before the specified value."""
        try:
            specified_value, ok = QInputDialog.getText(self, "Create User List", "Enter the specified value:")
            if ok and specified_value:
                input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
                output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
                if input_text is not None and output_text is not None:
                    text = input_text.toPlainText()
                    lines = text.split("\n")
                    user_list = [line.split(specified_value)[0].strip() for line in lines if specified_value in line]
    
                    output_text.clear()
                    output_text.setPlainText("\n".join(user_list))
        except Exception as e:
            print(f"An error occurred: {e}")

    def number_password(self):
        """Create a list of number values that could be phone numbers."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
            
            if input_text is not None and output_text is not None and removed_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
                number_list = []
                removed_list = []
                
                for line in lines:
                    numbers = re.findall(r"\d{3}-\d{3}-\d{4}", line)  # Assuming phone numbers are in the format XXX-XXX-XXXX
                    
                    if numbers:
                        number_list.extend(numbers)
                        removed_list.append(line)
                
                output_text.clear()
                output_text.setPlainText("\n".join(number_list))
                
                removed_text.clear()
                removed_text.setLineWrapMode(QTextEdit.WidgetWidth)
                removed_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                removed_text.setPlainText("\n".join(removed_list))
        
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_passwordlist(self):
        """Create a list of values after the specified value."""
        try:
            specified_value, ok = QInputDialog.getText(self, "Create Password List", "Enter the specified value:")
            if ok and specified_value:
                input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
                output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
                if input_text is not None and output_text is not None:
                    text = input_text.toPlainText()
                    lines = text.split("\n")
                    password_list = [line.split(specified_value)[1].strip() for line in lines if specified_value in line]
    
                    output_text.clear()
                    output_text.setPlainText("\n".join(password_list))
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_links(self):
        """Remove links from the input_text widget."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            if input_text is not None:
                text = input_text.toPlainText()
                text_without_links = re.sub(r'http\S+', '', text)
                input_text.clear()
                input_text.setPlainText(text_without_links)
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_install_dialog(self):
        # Create a message box asking the user if they want to install undetected-chromedriver
        reply = QMessageBox.question(
            self,
            "Install undetected-chromedriver",
            "Do you want to run 'pip install undetected-chromedriver'?",
            QMessageBox.Yes | QMessageBox.No
        )

        # Process the user's response
        if reply == QMessageBox.Yes:
            # Run the pip install command
            # You can use the subprocess module to run the command
            # subprocess.run(["pip", "install", "undetected-chromedriver"])
            print("Running: pip install undetected-chromedriver")
        else:
            print("Installation canceled")

        def menuBrowser(self, signalArguments):
            subprocess.Popen(["python", "browser.py"])
    
    def tab_changed(self, index):
        """Perform actions based on the selected tab index."""
        password_working_function_combo = self.findChild(QComboBox, "password_working_function_combo")  # Replace "password_working_function_combo" with the actual object name
        if password_working_function_combo is not None:
            current_value = password_working_function_combo.currentText()
            if current_value == "Working from Directory":
                # Change the file directory path for Working from Directory
                self.Directory_Path_Text_Element.setText("New Directory Path")
            elif current_value == "Working from Input Requests":
                # Change the file directory path for Working from Input Requests
                self.Directory_Path_Text_Element.setText("New Input Requests Path")

    def open_browser(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setText("You are about to launch the built-in browser. Continue?")
        message_box.setWindowTitle("Diamond Sorter - Window")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        message_box.setDefaultButton(QtWidgets.QMessageBox.Yes)

        result = message_box.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            script_path = "browser.py"  # Path to the browser script
            subprocess.Popen(["python", script_path])

    def create_passwordlist(self):
        """Create a list of values after the specified value."""
        try:
            specified_value, ok = QInputDialog.getText(self, "Create Password List", "Enter the specified value:")
            if ok and specified_value:
                input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
                output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
                if input_text is not None and output_text is not None:
                    text = input_text.toPlainText()
                    lines = text.split("\n")
                    password_list = [line.split(specified_value)[1].strip() for line in lines if specified_value in line]
    
                    output_text.clear()
                    output_text.setPlainText("\n".join(password_list))
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_links(self):
        """Remove links from the input_text widget."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            if input_text is not None:
                text = input_text.toPlainText()
                text_without_links = re.sub(r'http\S+', '', text)
                input_text.clear()
                input_text.setPlainText(text_without_links)
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_install_dialog(self):
        # Create a message box asking the user if they want to install undetected-chromedriver
        reply = QMessageBox.question(
            self,
            "Install undetected-chromedriver",
            "Do you want to run 'pip install undetected-chromedriver'?",
            QMessageBox.Yes | QMessageBox.No
        )

        # Process the user's response
        if reply == QMessageBox.Yes:
            # Run the pip install command
            # You can use the subprocess module to run the command
            # subprocess.run(["pip", "install", "undetected-chromedriver"])
            print("Running: pip install undetected-chromedriver")
        else:
            print("Installation canceled")

        def menuBrowser(self, signalArguments):
            subprocess.Popen(["python", "browser.py"])

    def tab_changed(self, index):
        """Perform actions based on the selected tab index."""
        password_working_function_combo = self.findChild(QComboBox, "password_working_function_combo")  # Replace "password_working_function_combo" with the actual object name
        if password_working_function_combo is not None:
            current_value = password_working_function_combo.currentText()
            if current_value == "Working from Directory":
                # Change the file directory path for Working from Directory
                self.Directory_Path_Text_Element.setText("New Directory Path")
            elif current_value == "Working from Input Requests":
                # Change the file directory path for Working from Input Requests
                self.Directory_Path_Text_Element.setText("New Input Requests Path")

    def toggle_word_wrap(self, state):
        """Enable or disable word wrap and scroll bar based on the state of enable_wordwrap_checkbox."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
            if input_text is not None and output_text is not None and removed_text is not None:
                if state == Qt.Checked:
                    input_text.setLineWrapMode(QTextEdit.WidgetWidth)
                    input_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                    output_text.setLineWrapMode(QTextEdit.WidgetWidth)
                    output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                    removed_text.setLineWrapMode(QTextEdit.WidgetWidth)
                    removed_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                else:
                    input_text.setLineWrapMode(QTextEdit.NoWrap)
                    input_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                    output_text.setLineWrapMode(QTextEdit.NoWrap)
                    output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                    removed_text.setLineWrapMode(QTextEdit.NoWrap)
                    removed_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
                # Update the scroll bar visibility
                input_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                input_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                output_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                removed_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                removed_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    
                input_text.updateGeometry()
                output_text.updateGeometry()
                removed_text.updateGeometry()
    
        except Exception as e:
            print(f"An error occurred: {e}")

    def paste_input(self):
        """Paste content from clipboard to input_text widget."""
        try:
            clipboard_content = QtWidgets.QApplication.clipboard().text()
            input_text = self.findChild(QtWidgets.QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            
            if input_text is not None:
                input_text.setPlainText(clipboard_content)
        except Exception as e:
            print(f"An error occurred: {e}")

    def replace_with_listButton():
        repeating_string = input("Enter the repeating string or value: ")
        lines = input("Copy and paste the list of lines: ").splitlines()
    
        for line in lines:
            replaced_line = line.replace(repeating_string, line)
            print(replaced_line)

    def setup_buttons(self):
        self.pasteButton.clicked.connect(self.paste_input)
        self.tab2_pasteButton.clicked.connect(self.paste_input)
        self.removeLinksButton.clicked.connect(self.remove_links)
        self.copyButton_2.clicked.connect(self.copy_output)
        self.removeEndingPunctuationButton.clicked.connect(self.remove_ending_punctuation)
        self.remove_domainsButton.clicked.connect(self.remove_domains)
        self.removeDuplicatesButton.clicked.connect(self.remove_duplicates)
        self.extract_md5Button.clicked.connect(self.extract_md5)
        self.removeSpecialCharacterButton.clicked.connect(self.remove_special_character)
        self.organizeLinesButton.clicked.connect(self.organize_lines)
        self.showDomainStatsButton.clicked.connect(self.show_stats)
        self.remove_capturesButton.clicked.connect(self.remove_captures)
        self.split_by_linesButton.clicked.connect(self.split_by_lines)
        self.removeAfterSpace.clicked.connect(self.removeAfterSpaceclicked)
        self.removeAfter_Tab_Space.clicked.connect(self.removeAfter_Tab_Spaceclicked)
        self.sort_email_domainsButton = QPushButton("Sort Email Domains")
        self.sort_email_domainsButton.clicked.connect(self.sort_email_domains)

        self.sort_remove_similarButton.clicked.connect(self.sort_remove_similar)
        self.emailPasswordButton.clicked.connect(self.email_password)
        self.usernamePasswordButton.clicked.connect(self.username_password)
        self.newtextdocuments_button.clicked.connect(self.handle_newtextdocuments)

        self.widget_button_about.clicked.connect(self.open_about_ui)
        self.widget_button_configs.clicked.connect(self.open_configs_ui)
        self.widget_button_cookies.clicked.connect(self.open_cookies_ui)
        self.widget_button_url_tools.clicked.connect(self.open_url_tools_ui)
        self.remove_inbetween_two_variablesButton.clicked.connect(self.remove_inbetween_two_variablesButtonClicked)  # Replace "remove_inbetween_two_variablesButton" with the actual object name
        self.stealer_log_format_combo.currentIndexChanged.connect(self.update_text_browser)
        self.password_working_function_combo.currentIndexChanged.connect(self.update_work_location_browser)
        self.input_text = self.findChild(QTextEdit, "input_text")
        self.domain_managerButton.clicked.connect(self.launch_domain_manager)
        self.chrome_extensions_button = QPushButton("Chrome Extensions")
        self.newtextdocuments_button = QPushButton("New Text Documents")
        self.discord_sorting_button = QPushButton("Discord Files")
        self.telegram_folder_sorting_button = QPushButton("Telegram Folders")
        self.chrome_extensions_button.clicked.connect(self.handle_chrome_extensions)
        self.discord_sorting_button.clicked.connect(self.handle_discord_files)
        self.telegram_folder_sorting_button.clicked.connect(self.handle_telegram_folders)
        self.telegram_folder_sorting_button.clicked.connect(self.handle_telegram_folder_sorting)
        self.authy_desktop_button.clicked.connect(self.handle_authy_desktop)
        self.desktop_wallet_button.clicked.connect(self.handle_desktop_wallet)
        self.browser_2fa_extension_button.clicked.connect(self.handle_browser_2fa_extension)
        self.text_named_sorting_button.clicked.connect(self.handle_text_named_sorting)
        self.pgp_button.clicked.connect(self.handle_pgp)
        self.encryption_keys_button.clicked.connect(self.handle_encryption_keys)
        self.auth_files_button.clicked.connect(self.handle_auth_files)
        self.sort_by_cookies_button.clicked.connect(self.handle_sort_by_cookies)
        self.button_scrape_keys.clicked.connect(self.handle_scrape_keys)
        self.button_scrape_banking_data.clicked.connect(self.handle_scrape_banking_data)
        self.button_scrape_backup_codes.clicked.connect(self.handle_scrape_backup_codes)
        self.button_scrape_security_data.clicked.connect(self.handle_scrape_security_data)
        self.emailPasswordButton.clicked.connect(self.email_password)
        self.memberIDPINButton.clicked.connect(self.member_id_pin)
        self.numberPasswordButton.clicked.connect(self.number_password)
        self.business_emailfinder_button.clicked.connect(self.business_emails)
        self.emailPasswordButton.clicked.connect(self.email_password)
        self.usernamePasswordButton.clicked.connect(self.username_password)
        self.memberIDPINButton.clicked.connect(self.member_id_pin)
        self.wordpress_finder_button.clicked.connect(self.wordpress_finder)
        self.business_emailfinder_button.clicked.connect(self.business_emails)
        self.governmentDomainsButton.clicked.connect(self.gov_domains)
        self.server_information_button.clicked.connect(self.server_information)
        self.cpanel_account_button.clicked.connect(self.cpanel_accounts)
        self.mailBoxesOptions_ComboButton.clicked.connect(self.checkmark)
        self.advertisingButton.clicked.connect(self.advertisements)
        self.socialForumsButton.clicked.connect(self.socials_forums)
        self.create_password_list.clicked.connect(self.create_passwordlist)
        remove_newlines_btn = QPushButton("Remove Newlines")
        remove_newlines_btn.clicked.connect(self.remove_newlines)
        self.recent_directories = []


        self.stats_values = []  # Define stats_values as an attribute
        self.stats_values_input = []  # Define stats_values_input as an attribute
        self.stats_values_output = []  # Define stats_values_output as an attribute
        self.stats_values_removed = []  # Define stats_values_removed as an attribute

        self.stats_values_urls = []  # Define stats_values_urls as an attribute
        self.stats_values_subdomains = []  # Define stats_values_subdomains as an attribute
        self.stats_values_userpass = []  # Define stats_values_userpass as an attribute
        self.stats_values_emailpass = []  # Define stats_values_emailpass as an attribute
        self.stats_phone_numbers = [] # Define phone numbers captured in the inputtext

        self.IP_Detections = [] # Define phone numbers captured in the inputtext


    def paste_input(self):
        """Paste content from clipboard to input_text widget."""
        try:
            clipboard_content = QtWidgets.QApplication.clipboard().text()
            input_text = self.findChild(QtWidgets.QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            
            if input_text is not None:
                input_text.setPlainText(clipboard_content)
        except Exception as e:
            print(f"An error occurred: {e}")

    def replace_with_listButton():
        repeating_string = input("Enter the repeating string or value: ")
        lines = input("Copy and paste the list of lines: ").splitlines()
    
        for line in lines:
            replaced_line = line.replace(repeating_string, line)
            print(replaced_line)

    def wordpress_finder(self):
        directory_path = self.set_directory_path_element_2.text()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)

    def handle_scrape_keys(self):
        directory_path = self.set_directory_path_element_2.text()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)

    def server_information(self):
        directory_path = self.set_directory_path_element_2.text()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)
    
    def cpanel_accounts(self):
        directory_path = self.set_directory_path_element_2.text()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)
    
    def emails(self):
        directory_path = self.set_directory_path_element_2.text()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)
    
    def html_head(self):
        # Logic for the "<html><head/" button
        pass
    
    def checkmark(self):
        # Logic for the "✅" button
        pass
    
    def advertisements(self):
        directory_path = self.set_directory_path_element_2.text()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)
    
    def socials_forums(self):
        directory_path = self.set_directory_path_element_2.text()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)

    def update_lcdNumber(self):
        count = self.lcdNumber_4.intValue()
        self.lcdNumber_4.display(count)

    def handle_scrape_banking_data(self):
        # Get the directory path from the specified file directory
        directory_path = self.Directory_Path_Text_Element.toPlainText()
        
        # Get the stealer log format combo value
        stealer_log_format = self.stealer_log_format_combo.currentText()
        
    
        # Display the actions, results, and stats in the console widget
        self.console_widget.appendPlainText("Scrape Banking Data button clicked")
        self.console_widget.appendPlainText("Starting crawling from directory: " + directory_path)
        self.console_widget.appendPlainText("Stealer log format: " + stealer_log_format)
        self.stats_values = []  # Define stats_values as an attribute

        # Perform the crawling and display the results
        # Add your crawling and displaying logic here
        
        # Display the stats
        self.console_widget.appendPlainText("Crawling completed. Displaying stats")
        # Add your stats displaying logic here
        
        # Check if the directory path is valid
        if not os.path.isdir(directory_path):
            self.console_data()  # Call the console_data function
            return
        
        # Display the actions, results, and stats in the console widget
        print("Scrape Banking Data button clicked")
        print("Starting crawling from directory:", directory_path)
        print("Stealer log format:", stealer_log_format)
        
        # Perform the crawling and display the results
        # Add your crawling and displaying logic here
        
        # Display the stats
        print("Crawling completed. Displaying stats")
        
    def handle_scrape_backup_codes(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Scrape Backup Codes button
        self.console_widget_textedit.appendPlainText(f"Scrape Backup Codes button clicked. Directory path: {directory_path}")
    
    def business_emails(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Business Emails button
        self.console_widget_textedit.appendPlainText(f"Business Emails button clicked. Directory path: {directory_path}")
    
    def gov_domains(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Gov Domains button
        self.console_widget_textedit.appendPlainText(f"Gov Domains button clicked. Directory path: {directory_path}")
    
    def member_id_pin(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Member ID/PIN button
        self.console_widget_textedit.appendPlainText(f"Member ID/PIN button clicked. Directory path: {directory_path}")
    
    def handle_scrape_security_data(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Scrape Security Data button
        self.console_widget_textedit.appendPlainText(f"Scrape Security Data button clicked. Directory path: {directory_path}")
    
    def handle_command_link(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Command Link Button
        self.console_widget_textedit.appendPlainText(f"Command Link Button clicked. Directory path: {directory_path}")
    
    def handle_telegram_folder_sorting(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Telegram Folder Sorting Button
        self.console_widget_textedit.appendPlainText(f"Telegram Folder Sorting Button clicked. Directory path: {directory_path}")
    
    def handle_authy_desktop(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Authy Desktop Button
        self.console_widget_textedit.appendPlainText(f"Authy Desktop Button clicked. Directory path: {directory_path}")
    
    def handle_desktop_wallet(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Desktop Wallet Button
        self.console_widget_textedit.appendPlainText(f"Desktop Wallet Button clicked. Directory path: {directory_path}")
    
    def handle_browser_2fa_extension(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Browser 2FA Extension Button
        self.console_widget_textedit.appendPlainText(f"Browser 2FA Extension Button clicked. Directory path: {directory_path}")
    
    def handle_text_named_sorting(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Text Named Sorting Button
        self.console_widget_textedit.appendPlainText(f"Text Named Sorting Button clicked. Directory path: {directory_path}")
    
    def handle_pgp(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling PGP Button
        self.console_widget_textedit.appendPlainText(f"PGP Button clicked. Directory path: {directory_path}")
    
    def handle_encryption_keys(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Encryption Keys Button
        self.console_widget_textedit.appendPlainText(f"Encryption Keys Button clicked. Directory path: {directory_path}")
    
    def handle_auth_files(self):
        directory_path = self.set_directory_path_element_2.text()
        # Functionality for handling Auth Files Button
        self.console_widget_textedit.appendPlainText(f"Auth Files Button clicked. Directory path: {directory_path}")

    def handle_sort_by_cookies(self):
        print("Sort by Cookies Button clicked")
        
    def handle_chrome_extensions(self):
        print("Chrome Extensions button clicked")
        
    def handle_scrape_backup_codes(self):
        # Functionality for handling Scrape Backup Codes button
        print("Scrape Backup Codes button clicked")

    def handle_scrape_security_data(self):
        # Functionality for handling Scrape Security Data button
        print("Scrape Security Data button clicked")
        
    def handle_command_link(self):
        # Functionality for handling Command Link Button
        print("Command Link Button clicked")

    def handle_telegram_folder_sorting(self):
        # Functionality for handling Telegram Folder Sorting Button
        print("Telegram Folder Sorting Button clicked")

    def handle_authy_desktop(self):
        # Functionality for handling Authy Desktop Button
        print("Authy Desktop Button clicked")

    def handle_desktop_wallet(self):
        # Functionality for handling Desktop Wallet Button
        print("Desktop Wallet Button clicked")

    def handle_browser_2fa_extension(self):
        # Functionality for handling Browser 2FA Extension Button
        print("Browser 2FA Extension Button clicked")

    def handle_text_named_sorting(self):
        # Functionality for handling Text Named Sorting Button
        print("Text Named Sorting Button clicked")

    def handle_pgp(self):
        # Functionality for handling PGP Button
        print("PGP Button clicked")

    def handle_encryption_keys(self):
        # Functionality for handling Encryption Keys Button
        print("Encryption Keys Button clicked")

    def handle_auth_files(self):
        # Functionality for handling Auth Files Button
        print("Auth Files Button clicked")

    def handle_sort_by_cookies(self):
        # Functionality for handling Sort by Cookies Button
        print("Sort by Cookies Button clicked")
        
    def handle_chrome_extensions(self):
        # Functionality for handling Chrome Extensions button
        print("Chrome Extensions button clicked")
    
    def handle_newtextdocuments(self):
        try:
            directory_path = self.directory_path_text_element.toPlainText()
            if directory_path:
                count = 0
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        if file == "New Text Document.txt":
                            count += 1
    
                message = f"Found {count} occurrences of 'New Text Document.txt'"
                self.console_widget.appendPlainText(message + '\n')
            else:
                # Show an error message informing the user to enter a directory path
                error_message = "Please enter a directory path."
                self.console_widget.appendPlainText(error_message + '\n')
        except Exception as e:
            error_message = "An error occurred: " + str(e)
            self.console_widget.appendPlainText(error_message + '\n')
        
    def handle_file_count_finished(self, count):
        message = f"Found {count} occurrences of 'New Text Document.txt'"
        self.console_widget.appendPlainText(message + '\n')
        self.lcdNumber_4.display(count)

        # Start the timer to update the value of lcdNumber_4 every 5 seconds
        self.timer.start(5000)
    
    def button_clicked():
        process_directory(directory_path_text_element)

    def handle_discord_files(self):
        # Functionality for handling Discord Files button
        print("Discord Files button clicked")

    def handle_telegram_folders(self):
        # Functionality for handling Telegram Folders button
        print("Telegram Folders button clicked")

    def launch_domain_manager(self):
        subprocess.Popen(["python", "domain_sorter.py"])

    def replace_with_listButton():
        repeating_string = input("Enter the repeating string or value: ")
        lines = input("Copy and paste the list of lines: ").splitlines()
    
        for line in lines:
            replaced_line = line.replace(repeating_string, line)
            print(replaced_line)

    def tab2_pasteButton(self):
        """Paste content from clipboard to input_text widget."""
        try:
            clipboard_content = QtWidgets.QApplication.clipboard().text()
            input_text = self.findChild(QtWidgets.QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            
            if input_text is not None:
                input_text.setPlainText(clipboard_content)
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def sort_email_domains(self):
        # Retrieve the list of email domains
        email_domains = self.get_email_domains()
    
        # Perform the sorting operation on the email domains
        sorted_domains = sorted(email_domains)
    
        # Update the GUI with the sorted email domains
        self.update_email_domains(sorted_domains)

    def get_email_domains(self):
        # Replace this with your code to retrieve the list of email domains
        # Example: Querying a database or reading from a file
        email_domains = ["example1.com", "example2.com", "example3.com"]
    
        return email_domains

    def update_email_domains(self, sorted_domains):
        # Replace this with your code to update the GUI with the sorted email domains
        # Example: Updating a list widget or label text
        self.email_domains_list_widget.clear()
        self.email_domains_list_widget.addItems(sorted_domains)

    def sort_remove_similar(self):
        num_consecutive_chars, ok = QInputDialog.getInt(self, "Consecutive Characters", "Enter the number of consecutive characters to remove lines:")
        if ok:
            # Get the input text from the input_text widget
            input_text = self.input_text.toPlainText()
    
            # Split the input text into lines
            lines = input_text.split("\n")
    
            # Define a generator to process lines in smaller batches
            def line_generator(lines, batch_size):
                for i in range(0, len(lines), batch_size):
                    yield lines[i:i+batch_size]
    
            # Remove lines with the specified number of consecutive similar characters
            filtered_lines = []
            removed_lines = []
            for batch in line_generator(lines, 1000):  # Adjust the batch size as needed
                for line in batch:
                    consecutive_count = 1
                    has_similar_chars = False
                    for i in range(len(line) - 1):
                        if line[i] == line[i + 1]:
                            consecutive_count += 1
                            if consecutive_count == num_consecutive_chars:
                                has_similar_chars = True
                        else:
                            consecutive_count = 1
    
                    if not has_similar_chars:
                        filtered_lines.append(line)
                    else:
                        removed_lines.append(line)
    
            # Join the filtered lines into a string
            output_text = "\n".join(filtered_lines)
    
            # Set the output text in the output_text widget
            self.output_text.setPlainText(output_text)
    
            # Join the removed lines into a string
            removed_text = "\n".join(removed_lines)
    
            # Set the removed text in the removed_data_text widget
            self.removed_data_text.setPlainText(removed_text)
    
            print("Lines with", num_consecutive_chars, "consecutive similar characters removed.")

    def remove_newlines(self):
        # GET INPUT TEXT
        input_text = self.input_text.toPlainText()

        # ADD SEPARATING VARIABLE AT THE END OF EACH LINE
        lines = input_text.splitlines()
        modified_lines = [line.strip() + ';' for line in lines]

        # JOIN MODIFIED LINES AND REMOVE NEWLINES
        modified_text = ' '.join(modified_lines)

        # SET MODIFIED TEXT TO OUTPUT TEXT
        self.output_text.setPlainText(modified_text)

    def update_work_location_browser(self, index):
            # Hide all text browsers
        self.Directory_Path_Text_Element.hide()
        self.input_text.setEnabled(False)
    
        # Show the corresponding widget based on the selected index
        if index == 0:
            self.Directory_Path_Text_Element.show()
        elif index == 1:
            self.input_text.setEnabled(True)

    def update_text_browser(self, index):
        # Hide all text browsers
        self.redline_file_structure_text_browser.hide()
        self.racoon_file_structure_text_browser.hide()
        self.worldwind_file_structure_text_browser.hide()
        self.titan_file_structure_text_browser.hide()
        self.whitesnake_file_structure_text_browser.hide()

        # Show the corresponding text browser based on the selected index
        if index == 0:
            self.redline_file_structure_text_browser.show()
            self.display_function("redline_file_structure_text_browser")
        elif index == 1:
            self.racoon_file_structure_text_browser.show()
            self.display_function("racoon_file_structure_text_browser")
        elif index == 2:
            self.titan_file_structure_text_browser.show()
            self.display_function("titan_file_structure_text_browser")
        elif index == 3:
            self.whitesnake_file_structure_text_browser.show()
            self.display_function("whitesnake_file_structure_text_browser")
        elif index == 4:
            self.worldwind_file_structure_text_browser.show()
            self.display_function("worldwind_file_structure_text_browser")

    def open_about_ui(self):
        script_path = os.path.join(current_dir, "references", "about.py")
        subprocess.Popen(["python", script_path])

    def open_configs_ui(self):
        script_path = os.path.join(os.path.dirname(__file__), 'config_developer.py')
        subprocess.Popen(['python', script_path])

    def open_cookies_ui(self):
        script_path = os.path.join(current_dir, "references", "cookies_window.py")
        subprocess.Popen(["python", script_path])
        obj.open_cookies_ui()

    def open_url_tools_ui(self):
        script_path = 'url_tools.py'
        subprocess.Popen(['python', script_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE, env={"PYTHONPATH": sys.executable, "QT_QPA_PLATFORM_PLUGIN_PATH": QtWidgets.QApplication.libraryPaths()[0], "QT_QPA_FONTDIR": QtWidgets.QApplication.fontDir().absolutePath(), "QT_QPA_PLATFORM": "windows"})

    def create_userlist(self):
        # This method will be called when the "create_username_list" button is clicked
        print("Create user list button clicked")
        
        # Get the text from the input_text widget
        text = self.input_text.toPlainText()
        
        # Split the text into lines
        lines = text.split("\n")
        
        # Iterate over the lines
        usernames = []
        for line in lines:
            # Split each line at the ":" delimiter
            parts = line.split(":")
            
            # Extract the value before the delimiter
            value = parts[0].strip()
            
            # If the value contains an "@" symbol (email address), remove the domain
            if "@" in value:
                value = value.split("@")[0]
            
            # Add the value to the usernames list
            usernames.append(value)
        
        # Print the usernames
        print(usernames)
    
    def copy_output(self):
        """Copy content from output_text widget to clipboard."""
        try:
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if output_text is not None:
                clipboard = self.app.clipboard()
                clipboard.setText(output_text.toPlainText())
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_ending_punctuation(self):
        """Remove ending punctuation from the input_text widget."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
            
            if input_text is not None and output_text is not None and removed_data_text is not None:
                text = input_text.toPlainText()
                text_without_punctuation = re.sub(r'([^\w\s]|(?<=\w)[.,!?])\s*$', '', text)
                
                removed_text = re.sub(rf'(?<!\w){re.escape(text_without_punctuation)}(?!\w)', '', text)
                removed_data_text.append(removed_text)
                
                output_text.clear()
                output_text.setPlainText(text_without_punctuation)
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def remove_domains(self):
        """Remove domains from the input_text widget."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                text = input_text.toPlainText()
                text_without_domains = re.sub(r'@\S+\.', '', text)
                output_text.clear()
                output_text.setPlainText(text_without_domains)
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def remove_duplicates(self):
        """Remove duplicate lines from input and display in output."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
                unique_lines = list(set(lines))
                unique_lines.sort(key=lines.index)
                output_text.clear()
                output_text.setPlainText("\n".join(unique_lines))
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def extract_md5(self):
        """Extract MD5 hashes from the input_text widget."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                lines = input_text.toPlainText().split("\n")
                md5_regex = re.compile(r"\b[A-Fa-f0-9]{32}\b")
                extracted_md5 = [match.group() for line in lines for match in md5_regex.finditer(line)]
                output_text.clear()
                output_text.setPlainText("\n".join(extracted_md5))
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def remove_special_character(self):
        """Remove special character from each line."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
            if input_text is not None and output_text is not None and removed_text is not None:
                # Ask the user for the special character to remove after
                special_character, ok = QInputDialog.getText(self, "Remove After Special Character", "Enter the special character:")
    
                if ok and special_character:
                    # Ask the user if they want to remove after the chosen character on every line
                    option, ok = QInputDialog.getItem(self, "Remove Option", "Select an option:", ["Every Line", "First Line"])
    
                    if ok and option:
                        text = input_text.toPlainText()
                        lines = text.split("\n")
                        processed_lines = []
                        removed_characters = []
    
                        for i, line in enumerate(lines):
                            line_parts = line.split(special_character)
                            processed_line = line_parts[0].strip() if line_parts else line.strip()
                            processed_lines.append(processed_line)
    
                            if option == "First Line" and i == 0:
                                removed_character = special_character.join(line_parts[1:]).strip() if len(line_parts) > 1 else ""
                                removed_characters.append(removed_character)
                            else:
                                removed_characters.append(line[len(processed_line):])
    
                        output_text.clear()
                        output_text.setPlainText("\n".join(processed_lines))
    
                        removed_text.clear()  # Clear the previous removed_text
                        removed_text.setPlainText("\n".join(removed_characters))
    
                        self.update_line_count()  # Assuming update_line_count is a method in your class
    
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def show_stats(self, button_text):
        """Show statistics about the input text."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            if input_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
    
                total_lines = len(lines)
                total_characters = sum(len(line) for line in lines)
                average_characters = total_characters / total_lines if total_lines > 0 else 0
    
                # Additional statistics
                total_output = 0
                total_removed = 0
    
                # Extract email addresses from the text
                email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
                email_addresses = re.findall(email_regex, text)
    
                # Extract unique domains from the email addresses
                unique_domains = [email.split('@')[-1] for email in email_addresses]
    
                total_different_domains = len(set(unique_domains))
    
                # Get the top 5 domains with their counts
                top_domains = Counter(unique_domains).most_common(5)
    
                # Calculate the percentages for the top domains
                total_domains = len(unique_domains)
                top_domains_with_percent = [(domain, count, (count / total_domains) * 100) for domain, count in top_domains]
    
                # Format the display for the top domains
                top_domains_display = "\n".join([f"{i+1}. {domain} - {count} - {percent:.2f}%" for i, (domain, count, percent) in enumerate(top_domains_with_percent)])
    
                url_regex = r'\(https?://[^)]+\)'
                url_captures = re.findall(url_regex, text)
                url_captures_info = []
                for url in url_captures:
                    parsed_url = urlparse(url[1:-1])
                    subdomain = parsed_url.hostname.split('.')[0]
                    domain = parsed_url.hostname.split('.')[-2]
                    url_captures_info.append((subdomain, domain))
    
                # Count the number of captures for each subdomain and domain
                captures_counter = Counter(url_captures_info)
    
                # Format the display for the URL captures
                url_captures_display = "\n".join([f"{subdomain} - {domain} - {count}" for (subdomain, domain), count in captures_counter.items()])
    
                stats_message = f"Button Pressed: {button_text}\nTotal Lines (Input): {total_lines}\nTotal Output (Output): {total_output}\nTotal Removed (Removed): {total_removed}\nTotal Characters: {total_characters}\nAverage Characters per Line: {average_characters:.2f}\nTotal Different Domains: {total_different_domains}\n\nTop 5 Domains with Percents:\n{top_domains_display}\n\nURL Captures:\n{url_captures_display}\n\nDetected IP Addresses:\n{', '.join(self.IP_Detections)}\n\nPhone Numbers:\n{', '.join(self.stats_phone_numbers)}"
    
                QMessageBox.information(self, "Statistics", stats_message)
        except Exception as e:
            print(f"An error occurred: {e}")

    def cleanupButton(self):
        """Cleanup the input text."""
        try:
            reply = QMessageBox.question(
                self,
                "Confirmation",
                "Are you sure you want to perform the cleanup action?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
    
            if reply == QMessageBox.Yes:
                input_text = self.findChild(QTextEdit, "input_text")
                output_text = self.findChild(QTextBrowser, "output_text")
                if input_text is not None and output_text is not None:
                    text = input_text.toPlainText()
                    lines = text.split("\n")
                    cleaned_lines = [line.strip() for line in lines]
    
                    output_text.clear()
                    output_text.setPlainText("\n".join(cleaned_lines))
                    self.update_line_count()
                    removed_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name

                    # Display the pop-up window with checkboxes
                    dialog = QDialog(self)
                    layout = QVBoxLayout(dialog)
    
                    # Add checkboxes
                    checkbox1 = QCheckBox("Checkbox 1")
                    checkbox2 = QCheckBox("Checkbox 2")
                    checkbox3 = QCheckBox("Checkbox 3")
                    checkbox4 = QCheckBox("Checkbox 4")
                    checkbox5 = QCheckBox("Checkbox 5")
    
                    layout.addWidget(checkbox1)
                    layout.addWidget(checkbox2)
                    layout.addWidget(checkbox3)
                    layout.addWidget(checkbox4)
                    layout.addWidget(checkbox5)
    
                    # Add OK and Cancel buttons
                    buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                    buttons.accepted.connect(dialog.accept)
                    buttons.rejected.connect(dialog.reject)
    
                    layout.addWidget(buttons)
    
                    if dialog.exec_() == QDialog.Accepted:
                        # OK button pressed, perform further actions based on the checkbox states
                        if checkbox1.isChecked():
                            # Handle checkbox 1 checked
                            pass
                        if checkbox2.isChecked():
                            # Handle checkbox 2 checked
                            pass
                        # ... handle other checkboxes
    
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_inbetween_two_variablesButtonClicked(self):
        """Remove text between two variables on each line."""
        try:
            first_variable, ok1 = QInputDialog.getText(self, "First Variable", "Enter the first variable:")
            second_variable, ok2 = QInputDialog.getText(self, "Second Variable", "Enter the second variable:")
    
            if ok1 and ok2:
                confirmation = f"Are you sure you want to remove text between '{first_variable}' and '{second_variable}'?"
                reply = QMessageBox.question(self, "Confirmation", confirmation, QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    input_text = self.input_text.toPlainText()
                    lines = input_text.split("\n")
                    processed_lines = []
                    removed_data = []
    
                    for line in lines:
                        removed_part = ""
                        if first_variable in line and second_variable in line:
                            start_index = line.index(first_variable) + len(first_variable)
                            end_index = line.index(second_variable)
                            processed_line = line[:start_index] + line[end_index:]
                            removed_part = line[start_index:end_index]
                        else:
                            processed_line = line
    
                        processed_lines.append(processed_line)
                        removed_data.append(removed_part)
    
                    output_text = "\n".join(processed_lines)
                    removed_text = "\n".join(removed_data)
    
                    self.output_text.setPlainText(output_text)
                    self.removed_data_text.setPlainText(removed_text)
    
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def remove_captures(self):
        """Remove captures from each line."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
                processed_lines = [re.sub(r"\(.*?\)", "", line) for line in lines]
    
                output_text.clear()
                output_text.setPlainText("\n".join(processed_lines))
                self.update_line_count()  # Assuming update_line_count is a method in your class
        except Exception as e:
            print(f"An error occurred: {e}")

    def split_by_lines(self):
        """Split content based on user-defined number of lines and save to a specified directory."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            if input_text is not None:
                num_lines, ok = QInputDialog.getInt(self, "Split", "How many lines for each split?")
                if ok and num_lines > 0:
                    split_name, ok = QInputDialog.getText(self, "Split", "What to name the split?")
                    if ok and split_name:
                        directory = os.path.join("split", split_name)
                        if not os.path.exists(directory):
                            os.makedirs(directory)
        
                        lines = input_text.toPlainText().split("\n")
                        for index, start_line in enumerate(range(0, len(lines), num_lines), 1):
                            file_name = f"{split_name}_{index}.txt"
                            file_name = file_name.replace(":", "_")  # Replace colon with underscore
                            file_path = os.path.join(directory, file_name)
                            with open(file_path, "w", encoding="utf-8") as file:
                                file.write('\n'.join(lines[start_line:start_line + num_lines]))
        except Exception as e:
            print(f"An error occurred: {e}")

    def start_sorting(self):
        # Functionality for the Start Sorting button in the General Combo Options tab
        pass

    def password_sorting(self):
        # Functionality for the Start Sorting button in the Password Log Formats tab
        pass

    def organize_lines(self):
        """Sort the lines from the input_text widget in alphabetical order."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
    
                options = ["A-Z", "Z-A", "0-9", "Shortest to longest", "Longest to shortest", "Randomize lines"]
                choice, ok = QInputDialog.getItem(self, "Organize", "Choose an option number:", options, editable=False)
    
                if ok and choice:
                    if choice == "A-Z":
                        sorted_lines = sorted(lines)
                    elif choice == "Z-A":
                        sorted_lines = sorted(lines, reverse=True)
                    elif choice == "0-9":
                        sorted_lines = sorted(lines, key=lambda x: [int(t) if t.isdigit() else t for t in re.split('(\d+)', x)])
                    elif choice == "Shortest to longest":
                        sorted_lines = sorted(lines, key=len)
                    elif choice == "Longest to shortest":
                        sorted_lines = sorted(lines, key=len, reverse=True)
                    elif choice == "Randomize lines":
                        random.shuffle(lines)
                        sorted_lines = lines
                    else:
                        return
    
                    output_text.clear()
                    output_text.setPlainText("\n".join(sorted_lines))
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def split_by_lines(self):
        """Split content based on user-defined number of lines and save to a specified directory."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            if input_text is not None:
                num_lines, ok = QInputDialog.getInt(self, "Split", "How many lines for each split?")
                if ok and num_lines > 0:
                    split_name, ok = QInputDialog.getText(self, "Split", "What to name the split?")
                    if ok and split_name:
                        directory = os.path.join("split", split_name)
                        if not os.path.exists(directory):
                            os.makedirs(directory)
    
                        lines = input_text.toPlainText().split("\n")
                        for index, start_line in enumerate(range(0, len(lines), num_lines), 1):
                            file_path = os.path.join(directory, f"{split_name}_{index}.txt")
                            with open(file_path, "w", encoding="utf-8") as file:
                                file.write('\n'.join(lines[start_line:start_line + num_lines]))
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def combine_files(self):
        """Combine all text files from 'toCombine' directory, save to '_combined_.txt' and remove duplicates."""
        combined_content = []
        dir_path = "toCombine"
    
        for filename in os.listdir(dir_path):
            if filename.endswith(".txt"):
                with open(os.path.join(dir_path, filename), "r", encoding="utf-8") as file:
                    combined_content.extend(file.readlines())
    
        with open("_combined_.txt", "w", encoding="utf-8") as file:
            file.writelines(combined_content)
    
        with open("_combined_.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            unique_lines = list(dict.fromkeys(lines))
    
        with open("_combined_.txt", "w", encoding="utf-8") as file:
            file.writelines(unique_lines)
    
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, ''.join(unique_lines))
        update_line_count()

    def OBSOLETE__cleanup(self):
        """Clean up the lines in the input_text widget."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_data_text = self.findChild(QTextEdit, "removed_data_text")  # Replace "removed_data_text" with the actual object name

            if input_text is not None and output_text is not None:
                lines = input_text.toPlainText().split("\n")
                cleaned_lines = []
    
                for line in lines:
                    if line.strip() and "UNKNOWN" not in line and "****" not in line and "USER" not in line and not line.startswith(":") and not line.endswith(":"):
                        _, _, after_colon = line.partition(":")
                        after_colon = re.sub(r"[^a-zA-Z0-9]+", "", after_colon)
                        if len(after_colon) >= 5:
                            cleaned_lines.append(line)
    
                output_text.clear()
                output_text.setPlainText("\n".join(cleaned_lines))
                self.update_line_count()  # Assuming update_line_count is a method in your class
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_line_count(self):
        """Update the line count in the UI."""
        try:
            total_lines_number_lcd_input = self.findChild(QLCDNumber, "totalLinesNumber")
            results_tab_lcd_input = self.findChild(QLCDNumber, "lcdNumber_2")
            removed_data_tab_lcd_input = self.findChild(QLCDNumber, "lcdNumber_3")
            
            do_remove_empty_lines = self.remove_empty_lines_checkbox.isChecked()
            
            n_input_lines = calc_lines(self.input_text.toPlainText(), do_remove_empty_lines)
            total_lines_number_lcd_input.display(n_input_lines)
            
            n_output_result_lines = calc_lines(self.output_text.toPlainText(), do_remove_empty_lines)
            results_tab_lcd_input.display(n_output_result_lines)
            
            n_output_removed_data_lines = calc_lines(self.removed_data_text.toPlainText(), do_remove_empty_lines)
            removed_data_tab_lcd_input.display(n_output_removed_data_lines)
            
        except Exception as e:
            print(f"An error occurred: {e}")

    def createpasswordlist(self):
        # This method will be called when the "create_password_list" button is clicked
        print("Create password list button clicked")
    
    def email_password(self):
        # Functionality for the Email:Password button
        directory_path = self.Directory_Path_Text_Element.toPlainText()  # Get the directory path from Directory_Path_Text_Element
    
        output_text = ""
    
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as input_file:
                        for line in input_file:
                            if line.strip():  # Check if the line is not empty
                                match = re.findall(r"Email: (.*), Pass: (.*)", line)
                                if match:
                                    email, password = match[0]
                                    output_line = f"{email}:{password}\n"
                                    output_text += output_line
    
        # Show the results in the output_text
        self.output_text.setPlainText(output_text)
    
        # Optional: Show a message box to indicate the operation is complete
        QMessageBox.information(self, "Email:Password", "Email:Password pairs have been combined and displayed successfully.")      

    def email_password(self):
        # Functionality for the Email:Password button
        directory_path = self.Directory_Path_Text_Element.toPlainText()  # Get the directory path from Directory_Path_Text_Element
    
        total_files = 0
        total_folders = 0
        total_scanned = 0
        total_hits = 0
    
        # Create the animated label
        animated_label = QLabel("TASKING RUNNING: EMAIL:PASS")
        animated_label.setStyleSheet("color: red")
        animated_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(animated_label)
        
        # Create the QTimer to toggle the visibility of the animated label
        timer = QTimer(self)
        timer.timeout.connect(lambda: animated_label.setVisible(not animated_label.isVisible()))
        timer.start(500)  # Toggle every 500 milliseconds (0.5 seconds)
    
        for root, dirs, files in os.walk(directory_path):
            total_folders += len(dirs)
            for file in files:
                if file.endswith(".txt"):
                    total_files += 1
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as input_file:  # Specify errors="ignore" to skip invalid characters
                        try:
                            for line in input_file:
                                if line.strip():  # Check if the line is not empty
                                    match = re.findall(r"Email: (.*), Pass: (.*)", line)
                                    if match:
                                        total_hits += 1
                        except UnicodeDecodeError:
                            # Handle the case where the file contains invalid characters for UTF-8 encoding
                            continue
    
        # Stop the QTimer and hide the animated label
        timer.stop()
        animated_label.hide()
    
        # Calculate the total number of scanned files
        total_scanned = total_files + total_folders

    def username_password(self):
        # Functionality for the Email:Password button
        directory_path = self.Directory_Path_Text_Element.toPlainText()  # Get the directory path from Directory_Path_Text_Element
    
        output_text = ""
    
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as input_file:
                        for line in input_file:
                            if line.strip():  # Check if the line is not empty
                                match = re.findall(r"Email: (.*), Pass: (.*)", line)
                                if match:
                                    email, password = match[0]
                                    output_line = f"{email}:{password}\n"
                                    output_text += output_line
    
        # Show the results in the output_text
        self.output_text.setPlainText(output_text)
    
        # Optional: Show a message box to indicate the operation is complete
        QMessageBox.information(self, "Email:Password", "Email:Password pairs have been combined and displayed successfully.")      

    def new_text_documents(self):
        # Functionality for the Email:Password button
        directory_path = self.Directory_Path_Text_Element.toPlainText()  # Get the directory path from Directory_Path_Text_Element
    
        output_text = ""
    
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as input_file:
                        for line in input_file:
                            if line.strip():  # Check if the line is not empty
                                match = re.findall(r"Email: (.*), Pass: (.*)", line)
                                if match:
                                    email, password = match[0]
                                    output_line = f"{email}:{password}\n"
                                    output_text += output_line
    
        # Show the results in the output_text
        self.output_text.setPlainText(output_text)
    
        # Optional: Show a message box to indicate the operation is complete
        QMessageBox.information(self, "Email:Password", "Email:Password pairs have been combined and displayed successfully.") 

    def copy_from_output():
        """Copy content from output_text widget to clipboard."""
        output_content = output_text.get(1.0, tk.END)
        root.clipboard_clear()
        root.clipboard_append(output_content)
    
    def remove_duplicates(self):
        """Remove duplicate lines from input and display in output."""
        try:
            central_widget = self.findChild(QtWidgets.QWidget, "centralwidget")  # Replace "centralwidget" with the actual object name
            if central_widget is not None:
                input_text = central_widget.findChild(QtWidgets.QTextEdit, "input_text")  # Replace "input_text" with the actual object name
                if input_text is not None:
                    lines = input_text.toPlainText().splitlines()
                    unique_lines = list(dict.fromkeys(lines))
                    output_text = central_widget.findChild(QtWidgets.QTextEdit, "output_text")  # Replace "output_text" with the actual object name
                    if output_text is not None:
                        output_text.clear()
                        output_text.setPlainText("\n".join(unique_lines))
                        update_line_count()
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def extract_by_search():
        """Function to extract lines by a search term and save to file."""
        search_term = simpledialog.askstring("Search", "Enter the term to search for:")
    
        if search_term:
            matched_lines = [line for line in input_text.get(1.0, tk.END).splitlines() if
                            search_term.lower() in line.lower()]
    
            with open(f"{search_term}.txt", "a", encoding="utf-8") as file:  # "a" mode appends to the file
                for line in matched_lines:
                    file.write(line + '\n')
    
            with open(f"{search_term}.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                cleaned_lines = list(dict.fromkeys(lines))
    
            with open(f"{search_term}.txt", "w", encoding="utf-8") as file:
                file.writelines(cleaned_lines)
    
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, ''.join(cleaned_lines))
            update_line_count()
    
    def extract_32_chars_after_colon():
        """Extract lines where the content after the colon is exactly 32 characters and save to file."""
        pattern = re.compile(r":.{32}$")
        matched_lines = [line for line in input_text.get(1.0, tk.END).splitlines() if pattern.search(line)]
    
        with open("_Extracted_MD5_.txt", "a", encoding="utf-8") as file:  # "a" mode appends to the file
            for line in matched_lines:
                file.write(line + '\n')
    
        with open("_Extracted_MD5_.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            cleaned_lines = list(dict.fromkeys(lines))
    
        with open("_Extracted_MD5_.txt", "w", encoding="utf-8") as file:
            file.writelines(cleaned_lines)
    
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, ''.join(cleaned_lines))
        update_line_count()

    def copy_from_output(self):
        """Copy content from output_text widget to clipboard."""
        try:
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if output_text is not None:
                clipboard = self.app.clipboard()
                clipboard.setText(output_text.toPlainText())
        except tk.TclError:
            pass

    def extract_by_search(self):
        """Function to extract lines by a search term and save to file."""
        search_term = simpledialog.askstring("Search", "Enter the term to search for:")
        
        if search_term:
            matched_lines = [line for line in input_text.get(1.0, tk.END).splitlines() if search_term.lower() in line.lower()]
    
            with open(f"{search_term}.txt", "a", encoding="utf-8") as file:  # "a" mode appends to the file
                for line in matched_lines:
                    file.write(line + '\n')
    
            with open(f"{search_term}.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                cleaned_lines = list(dict.fromkeys(lines))
    
            with open(f"{search_term}.txt", "w", encoding="utf-8") as file:
                file.writelines(cleaned_lines)
            
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, ''.join(cleaned_lines))
            update_line_count()
    
    def extract_32_chars_after_colon(self):
        """Extract lines where the content after the colon is exactly 32 characters and save to file."""
        pattern = re.compile(r":.{32}$")
        matched_lines = [line for line in input_text.get(1.0, tk.END).splitlines() if pattern.search(line)]
    
        with open("_Extracted_MD5_.txt", "a", encoding="utf-8") as file:  # "a" mode appends to the file
            for line in matched_lines:
                file.write(line + '\n')
    
        with open("_Extracted_MD5_.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            cleaned_lines = list(dict.fromkeys(lines))
    
        with open("_Extracted_MD5_.txt", "w", encoding="utf-8") as file:
            file.writelines(cleaned_lines)
            
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, ''.join(cleaned_lines))
        update_line_count()

    def filter_colon_lines(self):
        """Keep only lines containing a colon and with 5 to 28 characters after the colon."""
        lines = input_text.get(1.0, tk.END).splitlines()
        filtered_lines = []
        
        for line in lines:
            if ":" in line:
                _, _, after_colon = line.partition(":")
                after_length = len(after_colon.strip())
                if 5 <= after_length <= 28:
                    filtered_lines.append(line)
        
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, '\n'.join(filtered_lines))
        update_line_count()
    
    def removeAfterSpaceclicked(self):
        """Handle the button click event for the removeAfterSpace button."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
            
            if input_text is not None and output_text is not None and removed_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
                processed_lines = []
                removed_data = []
                
                for line in lines:
                    if " " in line:
                        parts = line.split(" ")
                        processed_line = parts[0]
                        removed_part = " ".join(parts[1:])
                    else:
                        processed_line = line
                        removed_part = ""
                    
                    processed_lines.append(processed_line)
                    removed_data.append(removed_part)
                
                output_text.clear()
                output_text.setPlainText("\n".join(processed_lines))
                
                removed_text.clear()
                removed_text.setPlainText("\n".join(removed_data))
        
        except Exception as e:
            print(f"An error occurred: {e}")

    def removeAfter_Tab_Spaceclicked(self):
        """Remove anything on each line after a tab space."""
        try:
            input_text = self.input_text.toPlainText()
            lines = input_text.split("\n")
            processed_lines = []
            removed_data_text = []
    
            for line in lines:
                if "\t" in line:
                    parts = line.split("\t")
                    processed_line = parts[0]
                    removed_part = "\t".join(parts[1:])
                else:
                    processed_line = line
                    removed_part = ""
    
                processed_lines.append(processed_line)
                removed_data_text.append(removed_part)
    
            output_text = "\n".join(processed_lines)
            removed_text = "\n".join(removed_data_text)
    
            self.output_text.setPlainText(output_text)
            self.removed_data_text.setPlainText(removed_text)
    
        except Exception as e:
            print(f"An error occurred: {e}")


class ExtensionsBarQDockWidget(QDockWidget):
    def __init__(self):
        super(ExtensionsBarQDockWidget, self).__init__()

        # Create the container widget
        self.widget_container = QWidget()

        # Create buttons for each extension
        self.widget_button_url_tools = QPushButton("URL Tool")
        self.widget_button_requests = QPushButton("Request")
        self.widget_button_cookies = QPushButton("Cookies")
        self.widget_button_configs = QPushButton("CFGs")
        self.widget_button_about = QPushButton("About")

        # Connect button signals to slots
        self.widget_button_url_tools.clicked.connect(self.launch_url_tools_ui)
        self.widget_button_requests.clicked.connect(self.launch_requests_ui)
        self.widget_button_cookies.clicked.connect(self.launch_cookies_ui)
        self.widget_button_configs.clicked.connect(self.launch_configs_ui)
        self.widget_button_about.clicked.connect(self.launch_about_ui)
        
        # Set the container widget as the content of the dock widget
        self.setWidget(self.widget_container)


    def launch_ui_from_subdirectory(self, ui_filename):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        ui_path = os.path.join(script_dir, "ui_files", ui_filename)
        os.system(f"python {ui_path}")

    def launch_url_tools_ui(self):
        self.launch_ui_from_subdirectory("url_tools.ui")

    def launch_requests_ui(self):
        self.launch_ui_from_subdirectory("requests.ui")

    def launch_cookies_ui(self):
        self.launch_ui_from_subdirectory("cookies.ui")

    def launch_configs_ui(self):
        self.launch_ui_from_subdirectory("configs.ui")

    def launch_about_ui(self):
        self.launch_ui_from_subdirectory("about.ui")

class LoadTextFileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Load Text File or Set Directory Path")
        self.layout = QVBoxLayout()

        self.label = QLabel("Choose an option:")
        self.layout.addWidget(self.label)

        self.button_load_file = QPushButton("Load Text File")
        self.button_load_file.clicked.connect(self.load_text_file)
        self.layout.addWidget(self.button_load_file)

        self.button_set_directory = QPushButton("Set Directory Path")
        self.button_set_directory.clicked.connect(self.set_directory_path)
        self.layout.addWidget(self.button_set_directory)

        self.setLayout(self.layout)

        self.checkboxes = []  # Added checkboxes as an instance variable

    def load_text_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt)")
        if file_path:
            msg_box = QMessageBox.question(self, "Confirm", "Are you sure you want to load the text file?\nThis will process and copy the domains.", QMessageBox.Yes | QMessageBox.No)
            if msg_box == QMessageBox.Yes:
                domains = self.get_selected_domains()
                if domains:
                    self.process_and_copy(file_path, domains)
                else:
                    QMessageBox.warning(self, "No Domains Selected", "Please select at least one domain.")
        else:
            QMessageBox.warning(self, "Invalid File", "Please select a valid text file.")

    def set_directory_path(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory_path:
            msg_box = QMessageBox.question(self, "Confirm", "Are you sure you want to set the directory path?\nThis will process and copy the domains.", QMessageBox.Yes | QMessageBox.No)
            if msg_box == QMessageBox.Yes:
                domains = self.get_selected_domains()
                if domains:
                    self.process_and_copy(directory_path, domains)
                else:
                    QMessageBox.warning(self, "No Domains Selected", "Please select at least one domain.")
        else:
            QMessageBox.warning(self, "Invalid Directory", "Please select a valid directory.")

    def process_and_copy(self, path, domains):
        if os.path.isfile(path):
            with open(path, "r") as file:
                lines = file.readlines()

            output_directory = os.path.join(os.path.dirname(path), "Diamond Sorter Domains - Sorted")
            os.makedirs(output_directory, exist_ok=True)

            for line in lines:
                extension = line.strip()
                if extension in domains:
                    output_filename = os.path.join(output_directory, f"{extension}.txt")
                    with open(output_filename, "w") as output_file:
                        output_file.write(extension)

        elif os.path.isdir(path):
            output_directory = os.path.join(path, "Diamond Sorter Domains - Sorted")
            os.makedirs(output_directory, exist_ok=True)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiamondSorter = QtWidgets.QMainWindow()
    ui = Ui_DiamondSorter()
    ui.setupUi(DiamondSorter)
    DiamondSorter.show()
    sys.exit(app.exec_())
