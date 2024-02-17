import json
import os
import re
import random
import string
import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QUrl, Qt, QProcess, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QMainWindow, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout
import hashlib
import binascii  # hex encoding
import json as jsond  # json
import platform  # check platform
import subprocess  # needed for mac device
import time  # sleep before exit
from datetime import datetime
from time import sleep
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class DomainSorter(QMainWindow):
    def __init__(self):
        super(DiamondSorter, self).__init__()
        uic.loadUi(r'ui_files\domain_sorter.ui', self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DomainSorter()
    window.show()
    sys.exit(app.exec_())