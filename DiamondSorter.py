import json
import os
import re
import random
import string
import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QUrl, Qt, QTimer, pyqtSignal, pyqtSlot, QThread, QThreadPool, QBasicTimer, QTimerEvent, QMessageLogContext, QtMsgType, QRect
from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QShortcut, QMainWindow, QListWidget, QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout, QMenu, QAction, QTabBar, QSystemTrayIcon
from PyQt5.QtXml import QDomDocument
import hashlib
from multiprocessing import Process, Queue
from PyQt5.QtGui import QDesktopServices, QTextCursor, QTextDocument, QColor, QCursor, QTextCharFormat, QIcon, QPainter, QTextOption
import binascii
import json as jsond
import platform
import subprocess
from datetime import datetime
from time import sleep
import shutil
from collections import Counter, deque
from urllib.parse import urlparse
from multiprocessing import Process
import logging
import zipfile
import ctypes
import pystray
from pystray import MenuItem as item
from tqdm import tqdm
import ui_form 
import requests
import time
import curses
from PIL import Image
import pyperclip
from flask import session
import warnings
from PyQt5.QtGui import QKeySequence
from PyQt5 import QAxContainer
import difflib

warnings.filterwarnings("ignore", category=UserWarning, message="QLayout: Cannot add parent widget")
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning, message="Unknown property transform")
warnings.filterwarnings("ignore", category=UserWarning, message="Unknown property transform-origin")



INSTALLER_MODE = False # CHANGE THIS LINE WHEN COMPILE
if INSTALLER_MODE:
    top_classes = [QtWidgets.QMainWindow, ui_form.Ui_DiamondSorter]
else:
    top_classes = [QtWidgets.QMainWindow]

def get_current_working_dir():
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(__file__)
    return application_path

def calc_lines(txt, remove_empty_lines = True):
    if not txt.strip():
        return 0
    all_lines = txt.strip().split('\n')
    if not remove_empty_lines:
        return len(all_lines)
    else:
        return len([i for i in all_lines if bool(i.strip())])

def copytree(src, dst, skip_existing=True):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for root, dirs, files in os.walk(src):
        for dir_ in dirs:
            dest_dir = os.path.join(dst, os.path.relpath(os.path.join(root, dir_), src))
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
        for file_ in files:
            src_file = os.path.join(root, file_)
            dest_file = os.path.join(dst, os.path.relpath(src_file, src))
            if not skip_existing or not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)

class LogFilter(logging.Filter):
    def filter(self, record):
        # Filter out specific log messages containing "Unknown property transform-origin" and "Unknown property transform"
        if "Unknown property transform-origin" in record.msg or "Unknown property transform" in record.msg:
            return False
        return True

def custom_log_handler(log_context, log_type, message):
    # Implement your custom logging behavior here
    # For example, you can print the log message to the console
    print(message)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_filter = LogFilter()
logger.addFilter(log_filter)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.Handler.logMessage = custom_log_handler
logging.getLogger("PyQt5.QtCore").setLevel(logging.WARNING)
logging.getLogger("PyQt5.QtGui").setLevel(logging.WARNING)
logging.getLogger("PyQt5.QtWidgets").setLevel(logging.WARNING)

class WordpressFinderThread(QThread):
    results_obtained = pyqtSignal(str)

    def __init__(self, directory_path):
        super().__init__()
        self.directory_path = directory_path

    def run(self):
        # Perform crawling logic and find WordPress instances in the directory
        results = crawl_directory_for_wordpress(self.directory_path)

        # Emit the results as a signal
        self.results_obtained.emit(results)

class OverlayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("I Agree to the Terms and Conditions")
        layout.addWidget(label)

        checkbox = QCheckBox()
        layout.addWidget(checkbox)

        button = QPushButton("Continue")
        layout.addWidget(button)













class CrawlerThread(QThread):
    finished = pyqtSignal()
    copied = pyqtSignal(str)
    not_copied = pyqtSignal(str)
    
    def __init__(self, loaded_directory, folder_name, saved_directory, directory_path=None, input_textedit=None):
        super().__init__()
        self.loaded_directory = loaded_directory
        self.folder_name = folder_name
        self.saved_directory = saved_directory
        self.directory_path = directory_path
        self.input_textedit = input_textedit

    def run(self):
        try:
            if self.input_textedit is not None:
                directory_path = self.set_directory_path_element.toPlainText()
                results = self.crawl_directory(output_text)
                self.copied.emit(results)
            else:
                error_message = "Missing input_textedit for directory path."
                self.not_copied.emit(error_message)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            self.not_copied.emit(error_message)

    def crawl_directory(self, directory_path):
        # Implement the logic to crawl the directory here using the provided directory path
        results = f"Crawling directory: {directory_path}"
        return results




class MyProcess(Process):
    def __init__(self, queue):
        super(MyProcess, self).__init__()
        self.queue = queue

    def run(self):
        result = 1 + 100
        self.queue.put(result)

class CookieWindow(QtWidgets.QDialog):
    def __init__(self):
        super(CookieWindow, self).__init__()
        uic.loadUi(r'cookies_window.py', self)

class TaskTracker(QMainWindow):
    def __init__(self):
        super(TaskTracker, self).__init__()

        # Create the main window layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Create the text edit widget for displaying tasks
        self.task_text_edit = QTextEdit()
        main_layout.addWidget(self.task_text_edit)

        # Create the combo box for selecting task filters
        self.filter_combo = QComboBox()
        self.filter_combo.addItem("All")
        self.filter_combo.addItem("Completed")
        self.filter_combo.addItem("Pending")
        main_layout.addWidget(self.filter_combo)

        # Create the button for adding a new task
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        main_layout.addWidget(add_button)

        # Set the main widget as the central widget of the main window
        self.setCentralWidget(main_widget)
        save_results_action_button.clicked.connect(self.open_save_directory_dialog)



    def handle_scrape_banking_data(self):
        # Get the directory path from the specified file directory
        directory_path = self.Directory_Path_Text_Element.toPlainText()

    def update_line_count(self):
        """Update the line count in the UI."""
        # WHAT SHOULD BE HERE?
        try:
            total_lines_number = self.findChild(QLabel, "totalLinesNumber")
            if total_lines_number is None:
                return
            input_text = self.findChild(QTextEdit, "input_text")
            output_text = self.findChild(QTextEdit, "output_text")
            if input_text is not None:
                input_lines = len(input_text.toPlainText().split("\n"))
                # totalLinesNumber.display(input_lines)
            if output_text is not None:
                output_lines = len(output_text.toPlainText().split("\n"))

        except Exception as e:
            print(f"An error occurred: {e}")

    def import_requests(self):
        try:
            file_dialog = QFileDialog(self)
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("Text Files (*.txt)")
            if file_dialog.exec_():
                file_path = file_dialog.selectedFiles()[0]
                with open(file_path, 'r') as file:
                    text = file.read()
                    self.input_text.setText(text)
        except Exception as e:
            print(f"An error occurred: {e}")

def launch_insomnia():
    message_box = QtWidgets.QMessageBox()
    message_box.setText("You are about to launch Insomnia. Continue?")
    message_box.setWindowTitle("Diamond Sorter - Window")
    message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    message_box.setDefaultButton(QtWidgets.QMessageBox.Yes)

    result = message_box.exec_()
    if result == QtWidgets.QMessageBox.Yes:
        insomnia_path = r'references\Insomnia.exe'
        subprocess.Popen(insomnia_path)

class GlowTabBar(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_index = 0
        self.glow_color = QColor(255, 0, 0)
        self.glow_width = 5

    def paintEvent(self, event):
        painter = QPainter(self)
        option = self.tabRect(self.current_index)
        option.setWidth(option.width() + 2 * self.glow_width)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.glow_color)
        painter.drawRoundedRect(option, 5, 5)

        super().paintEvent(event)

    def setCurrentIndex(self, index):
        self.current_index = index
        self.update()

class DiamondSorter(*top_classes):
    finished = pyqtSignal(int)
    def __init__(self, directory_path=None, input_textedit=None):
        super(DiamondSorter, self).__init__()
        if INSTALLER_MODE:
            self.setupUi(self)
        else:
            uic.loadUi(r'form.ui', self)
        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        # Set the icon for the system tray
        icon = QIcon("./icons/diamond.png")
        self.tray_icon.setIcon(icon)
        # Create a context menu for the system tray icon
        menu = QMenu()
        
        
        # Create a "Show App" action for the context menu
        show_app_action = QAction("Show Application", self)
        show_app_action.triggered.connect(self.launch_show_app)
        menu.addAction(show_app_action)

        # Create a "Minimize App" action for the context menu
        minimize_app_action = QAction("Minimize", self)
        minimize_app_action.triggered.connect(self.launch_minimize)
        menu.addAction(minimize_app_action)

        # Create a submenu for Community actions
        community_menu = menu.addMenu("Community")

        # Add actions for Launch Homepage, Chat, and Github to the Community submenu
        self.create_action("Launch Homepage", self.launch_homepage, community_menu)
        self.create_action("Launch Chat", self.launch_chat, community_menu)
        self.create_action("Github Repo", self.launch_github, community_menu)

        
        # Create an "Exit" action for the context menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_application)
        menu.addAction(exit_action)

        # Set the context menu for the system tray icon
        self.tray_icon.setContextMenu(menu)

        # Show the system tray icon
        self.tray_icon.show()
        
        self.setWindowTitle(self.windowTitle() + ('' if INSTALLER_MODE else ' ~ WIP'))
        script_dir = os.path.dirname(sys.argv[0])
        icon_path = os.path.join(script_dir, "icons", "diamond.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.result = None
        self.console_layout = QVBoxLayout(self.consolewidget)
        self.console_layout.addWidget(self.consolewidget)
        self.setup_buttons()
        self.ask_user_dialog_box = QtWidgets.QInputDialog()
        self.directory_path_text_element = QtWidgets.QTextEdit()
        self.Directory_Path_Text_Element = self.directory_path_text_element
        # Create an instance of ExtensionsBarQDockWidget
        self.extensions_bar = ExtensionsBarQDockWidget()
        redline_file_structure_text_browser = "Redline / Meta"
        racoon_file_structure_text_browser = "Racoon Stealer"
        whitesnake_file_structure_text_browser = "Whitesnake"
        worldwind_file_structure_text_browser = "Worldwind / Prynt"
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
        self.windows_menu_actionDiamondPad.triggered.connect(self.launch_DiamondPad)
        self.remove_trash_button = self.findChild(QPushButton, "remove_trash_button")
        if self.remove_trash_button is not None:
            self.remove_trash_button.clicked.connect(self.remove_trash_button_clicked)
        self.display_function("MyFunction")
        self.button = QtWidgets.QPushButton("Process Directory")
        self.file_tree_view_button.clicked.connect(self.file_tree_structure_print)
        
        #central_widget = QWidget(self)
        #layout = QVBoxLayout(central_widget)

        #self.count_error_lines = QLCDNumber(self)
        ##self.count_left_to_go = QLCDNumber(self)
        #self.count_already_ran = QLCDNumber(self)
        #self.totalLinesNumber = QLCDNumber(self)
        #self.lcdNumber_1 = QLCDNumber(self)
        menu_bar = self.menuBar()
        # Create the search action and add it to the menu bar
        search_action = QAction("Search", self)
        search_action.triggered.connect(self.search_buttons)
        menu_bar.addAction(search_action)
        # Create the taskbar manager icon
        menu = (
            pystray.MenuItem("Show", self.on_show),
            pystray.MenuItem("Minimize", self.on_minimize),
            pystray.MenuItem("Quit", self.on_quit),
        )
        # Show the script window
        self.show()
        self.text_history = deque(maxlen=10)  # Store the last 10 entered texts
        # Connect the appropriate signal to update the history and text box
        self.button.clicked.connect(self.update_directory_text)
        directory_path = self.Directory_Path_Text_Element.toPlainText()
        self.top_extensions = self.get_top_file_extensions(directory_path, 3)  # Pass the value directly instead of using 'n=3'
        self.set_directory_path_button.clicked.connect(self.open_directory_dialog)
        self.create_username_button = QPushButton("Create Username List")
        self.create_username_button.clicked.connect(self.create_username_list_button_clicked)
        self.get_file_stats_button.clicked.connect(self.display_file_stats)
        self.search_input_shortcut = QShortcut(QKeySequence("Ctrl+F"), self.input_text, context=Qt.WidgetShortcut)
        self.search_input_shortcut.activated.connect(self.show_search_dialog_input)
        
        self.search_output_shortcut = QShortcut(QKeySequence("Ctrl+F"), self.output_text, context=Qt.WidgetShortcut)
        self.search_output_shortcut.activated.connect(self.show_search_dialog_output)
        
        self.search_removed_shortcut = QShortcut(QKeySequence("Ctrl+F"), self.removed_data_text, context=Qt.WidgetShortcut)
        self.search_removed_shortcut.activated.connect(self.show_search_dialog_removed)
        self.import_requests_button.clicked.connect(self.import_requests_dialog)
        self.import_requests_button = QPushButton("Import Requests")
        self.sorting_cookies_sort_by_domain.clicked.connect(self.sort_cookies_by_domain)



    def launch_minimize(self):
        # Minimize the application window
        self.showMinimized()

    def create_menus(self):
        # Create a submenu for Community actions
        community_menu = QMenu("Community")
        self.menuBar().addMenu(community_menu)

        # Add actions for Launch Homepage, Chat, and Github to the Community submenu
        self.create_action("Launch Homepage", self.launch_homepage, community_menu)
        self.create_action("Launch Chat", self.launch_chat, community_menu)
        self.create_action("Launch GitHub", self.launch_github, community_menu)

    def create_action(self, title, handler, menu):
        action = QAction(title, self)
        action.triggered.connect(handler)
        menu.addAction(action)

    def launch_show_app(self):
        # Check if the application is not at the top level
        if self.windowState() == QtCore.Qt.WindowMinimized or self.isHidden():
            self.setWindowState(QtCore.Qt.WindowActive)
            self.showNormal()

    def exit_application(self):
        # Perform any necessary cleanup before exiting
        self.tray_icon.hide()
        sys.exit()

    def launch_homepage(self):
        # Open the homepage URL in the default browser
        url = QUrl("https://opensourced.pro")
        QDesktopServices.openUrl(url)

    def launch_chat(self):
        # Open the chat URL in the default browser
        url = QUrl("https://t.me/+B6IXL7boGTYxYzNh")
        QDesktopServices.openUrl(url)

    def launch_github(self):
        # Open the GitHub URL in the default browser
        url = QUrl("https://github.com/OpenSourcedPro")
        QDesktopServices.openUrl(url)

    def telegram_bot_token_extractor(input_text):
        # Check if input_text is a string or bytes-like object
        if not isinstance(input_text, (str, bytes)):
            try:
                input_text = str(input_text)
            except Exception as e:
                raise TypeError("Input text must be a string or bytes-like object") from e
    
        # Rest of your code...
        token_pattern = r'\b\d{9}:[\w-]{35}\b'
        tokens = re.findall(token_pattern, input_text)
        output_text = '\n'.join(tokens)
        removed_data = re.sub(token_pattern, '', input_text)
        removed_data_text = removed_data.strip()
    
        return output_text, removed_data_text
        
    def sort_cookies_by_domain(self):
        # Function to be executed when the button is clicked
        # Add your code for crawling the directory and searching for requests here
        # Save the extracted lines in the appropriate folder and file structure
    
        # Example code for demonstration purposes
        directory_path_text_element = self.directory_path_text_element  # Use the directory_path_text_element variable
        user_requests = self.dialog_text_edit.toPlainText().split("\n")  # Get user-submitted requests as a list
        output_directory = self.savedResultsTextBox.text()  # Get the output directory specified by the user
    
        sorted_cookies_folder = "Sorted Cookies on Request"
    
        # Create the sorted cookies folder if it doesn't exist
        if not os.path.exists(sorted_cookies_folder):
            os.mkdir(sorted_cookies_folder)
    
        for request in user_requests:
            if not request:
                continue  # Skip empty requests
    
            request_folder = os.path.join(sorted_cookies_folder, request)
            if not os.path.exists(request_folder):
                os.makedirs(request_folder)
    
            for root, dirs, files in os.walk(directory_path_text_element):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        lines = f.readlines()
    
                    # Find the lines that contain the request
                    matching_lines = [line for line in lines if request in line]
    
                    if matching_lines:
                        # Create the output file path
                        output_subdirectory = os.path.join(output_directory, request_folder)
                        if not os.path.exists(output_subdirectory):
                            os.makedirs(output_subdirectory)
    
                        output_file_path = os.path.join(output_subdirectory, file)
    
                        # Write the matching lines to the output file
                        with open(output_file_path, "w") as f:
                            f.writelines(matching_lines)
    
        # Append to the console widget
        self.console_widget_textedit.append("Sorting cookies by domain completed!")
    

    def show_text_dialog(self):
        # Display the multi-line text dialog
        text, ok = QInputDialog.getMultiLineText(self, "Specify Requests", "Enter your requests (separate each one on a new line):")

        if ok:
            # Split the requests into a list
            requests = text.split('\n')

            # Crawl the file directory and search for requests
            for root, dirs, files in os.walk(set_directory_path_element):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        lines = f.readlines()

                    # Search for requests and save the extracted lines
                    for request in requests:
                        if request in lines:
                            # Create the directory structure for the extracted lines
                            request_folder = os.path.join('Sorted Cookies on Request', request.replace('/', '_'))
                            os.makedirs(request_folder, exist_ok=True)

                            # Save the extracted lines in the appropriate file
                            output_file_path = os.path.join(request_folder, f'{os.path.basename(root)}.txt')
                            with open(output_file_path, 'w') as f:
                                f.writelines(lines)

            print("Extraction completed.")







    def import_requests_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                self.input_text.clear()  # Clear the existing text before importing
                chunk_size = 1024  # Set the desired chunk size
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    self.input_text.insertPlainText(chunk)
                    QApplication.processEvents()  # Allow the application to process other events
            
        
        
    def show_search_dialog_input(self):
        text, ok = QInputDialog.getText(self, 'Search', 'Enter search query:')
        if ok:
            query = text.strip()
            if query:
                cursor = self.input_text.textCursor()
                if cursor.hasSelection():
                    cursor.clearSelection()
                
                found = self.input_text.find(query, QTextDocument.FindWholeWords | QTextDocument.FindCaseSensitively)
                if found:
                    self.input_text.setTextCursor(cursor)
                    self.input_text.ensureCursorVisible()
                else:
                    QMessageBox.information(self, 'Search', 'The word was not found in the input text.')
    
    def show_search_dialog_output(self):
        text, ok = QInputDialog.getText(self, 'Search', 'Enter search query:')
        if ok:
            query = text.strip()
            if query:
                cursor = self.output_text.textCursor()
                if cursor.hasSelection():
                    cursor.clearSelection()
                
                found = self.output_text.find(query, QTextDocument.FindWholeWords | QTextDocument.FindCaseSensitively)
                if found:
                    self.output_text.setTextCursor(cursor)
                    self.output_text.ensureCursorVisible()
                else:
                    QMessageBox.information(self, 'Search', 'The word was not found in the output text.')
    
    def show_search_dialog_removed(self):
        text, ok = QInputDialog.getText(self, 'Search', 'Enter search query:')
        if ok:
            query = text.strip()
            if query:
                cursor = self.removed_data_text.textCursor()
                if cursor.hasSelection():
                    cursor.clearSelection()
                
                found = self.removed_data_text.find(query, QTextDocument.FindWholeWords | QTextDocument.FindCaseSensitively)
                if found:
                    self.removed_data_text.setTextCursor(cursor)
                    self.removed_data_text.ensureCursorVisible()
                else:
                    QMessageBox.information(self, 'Search', 'The word was not found in the removed data text.')
    








    def display_file_stats(self):
        directory_path = self.set_directory_path_element.toPlainText()

        if os.path.exists(directory_path):
            file_stats = []
            for root, dirs, files in os.walk(directory_path):
                file_stats.append(f"Folder: {root}")
                for file in files:
                    file_path = os.path.join(root, file)
                    file_stats.append(f"File: {file_path}")
            self.console_widget_textedit.setPlainText("\n".join(file_stats))
        else:
            self.console_widget_textedit.setPlainText("Invalid directory path.")


    def open_directory_dialog(self):
        directory = self.set_directory_path_element.toPlainText()
        if directory:
            print("Scanning files and folders...")
            scan_files_folders(directory)


    def scan_files_folders(directory):
        counts = {
            "file_count": 0,
            "folder_count": 0,
            "cookie_count": 0,
            "new_text_document_count": 0,
            "passwords_count": 0,
            "profile_1_count": 0,
            "dat_count": 0,
            "compressed_count": 0
        }
    
        for root, dirs, files in tqdm(os.walk(directory), desc="Scanning files and folders", unit=" files"):
            counts["folder_count"] += len(dirs)
            counts["file_count"] += len(files)
    
            for file in files:
                counts["cookie_count"] += file.endswith(".txt")
                counts["new_text_document_count"] += file.endswith(".txt") and not file.startswith("cookies")
                counts["passwords_count"] += file == "Passwords.txt"
                counts["profile_1_count"] += file == "Profile_1"
                counts["dat_count"] += file.endswith(".dat")
                counts["compressed_count"] += zipfile.is_zipfile(os.path.join(root, file))
    
        print(f"Number of Folders: \033[91m{counts['folder_count']}\033[0m    Number of Files: \033[92m{counts['file_count']}\033[0m    Number of Cookies: \033[93m{counts['cookie_count']}\033[0m      Number of New Text Documents: \033[94m{counts['new_text_document_count']}\033[0m")
        print(f"Number of Passwords.txt: \033[95m{counts['passwords_count']}\033[0m    Number of Profile_1: \033[96m{counts['profile_1_count']}\033[0m    Number of .dat files: \033[97m{counts['dat_count']}\033[0m")
        print(f"Number of Compressed Files: \033[33m{counts['compressed_count']}\033[0m")
    
    
    def file_tree_structure_print(self):
        directory_path = self.set_directory_path_element.text()
        # Call the structure.py file with the directory path as a command-line argument
        subprocess.run(["python", "./references/structure.py", directory_path])

    def on_show(self):
        # Show the script window if it is minimized or hidden
        if self.isMinimized():
            self.showNormal()
        elif not self.isVisible():
            self.show()

    def on_minimize(self):
        self.showMinimized()

    def on_quit(self):
        os._exit(0)

    def update_directory_text(self):
        text = self.input_text.toPlainText()
        self.text_history.append(text)
        self.set_directory_path_element.setText(text)

    def submit_function(self):
        text = self.input_text.toPlainText()
        self.input_text.clear()

    def search_buttons(self):
        keyword, ok = QInputDialog.getText(self, "Search", "Enter a keyword:")
        if ok:
            found_buttons = []
            for button in self.findChildren(QPushButton):
                if keyword.lower() in button.text().lower():
                    found_buttons.append(button)
            if found_buttons:
                # Open the tab containing the first found button
                tab_widget = self.findChild(QWidget, "tab_widget")
                tab_index = tab_widget.indexOf(found_buttons[0].parentWidget())
                if tab_index != -1:
                    tab_widget.setCurrentIndex(tab_index)
                    
                # Highlight the found buttons and connect the clicked signal to a slot
                for found_button in found_buttons:
                    found_button.setStyleSheet("background-color: yellow;")
                    found_button.clicked.connect(self.reset_button_style)
            else:
                QMessageBox.information(self, "Search Results", "No buttons found matching the keyword.")
    
    def reset_button_style(self):
        sender = self.sender()
        sender.setStyleSheet("")  # Reset the style sheet

    def launch_DiamondPad(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setText("You are about to launch the built-in notepad. Continue?")
        message_box.setWindowTitle("Diamond Pad")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        message_box.setDefaultButton(QtWidgets.QMessageBox.Yes)
    
        result = message_box.exec_()
        if result == QtWidgets.QMessageBox.Yes:
            script_path = os.path.join(current_dir, "references", "scripts", "browser.py")
            subprocess.Popen(["python", script_path])

    def get_log_stats_function(self):
        directory_path = self.set_directory_path_element.text()
    
        if os.path.exists(directory_path):
            folder_names = set()
            text_documents = 0
    
            for root, dirs, files in os.walk(directory_path):
                for folder in dirs:
                    folder_names.add(folder)
                for file in files:
                    if file.endswith('.txt'):
                        text_documents += 1
    
            folder_names_count = len(folder_names)
            text_documents_count = text_documents
    
            self.console_widget_textedit.setPlainText(f"Multiple folder names detected: {folder_names_count}\nText documents found: {text_documents_count}")
        else:
            self.console_widget_textedit.setPlainText("Invalid directory path.")
    
    def removeAfter_Tab_Space_clicked(self):
        num_tabs, ok = QInputDialog.getInt(self, "Specify Number of Tab Spaces",
                                        "Enter the number of Tab Spaces to move after:")
    
        if ok:
            lines = self.input_text.toPlainText().split('\n')
            output_lines = []
            removed_lines = []
    
            for line in lines:
                tab_count = line.count('\t')
                if tab_count > num_tabs:
                    removed_lines.append(line)
                else:
                    output_lines.append(line)
    
            self.output_text.setPlainText('\n'.join(output_lines))
            self.removed_data_text.setPlainText('\n'.join(removed_lines))
        else:
            print("User canceled the input dialog")
    
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
        options = ["Remove Unknown", "Remove ****", "Remove Short", "Remove Similar", "Remove User", "Remove Missing Value(U or P)", "Remove Lines Without :"]  # Add the new option
    
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
            self.start_removal(selected_options, similarity_threshold=0.8)
    
    
    def start_removal(self, selected_options, similarity_threshold):
        """Perform the removal process based on the selected options."""
        input_text = self.input_text.toPlainText()
        removed_lines = []
        for option in selected_options:
            if option == "Remove Unknown":
                input_text, removed = self.remove_unknown(input_text)
                removed_lines.extend(removed)
            elif option == "Remove ****":
                input_text, removed = self.remove_consecutive_asterisks(input_text)
                removed_lines.extend(removed)
            elif option == "Remove Short":
                input_text, removed = self.remove_short_lines(input_text)
                removed_lines.extend(removed)
            elif option == "Remove Similar":
                input_text, removed = self.remove_similar_lines(input_text, similarity_threshold)
                removed_lines.extend(removed)
            elif option == "Passwords that has less that 3 characters":
                input_text, removed = self.remove_weak_passwords(input_text)
                removed_lines.extend(removed)
            elif option == "Remove ÐµÐâ":
                input_text, removed = self.remove_non_english_lines(input_text)
                removed_lines.extend(removed)
            elif option == "Remove Illegal Usernames":
                input_text, removed = self.remove_illegal_usernames(input_text)
                removed_lines.extend(removed)
            elif option == "Remove Lines Without :":  # Handle the new option
                input_text, removed = self.remove_lines_without_separator(input_text)
                removed_lines.extend(removed)

        self.output_text.setPlainText(input_text)
        self.removed_data_text.setPlainText("\n".join(removed_lines))



    def remove_unknown(self, text):
        self.console_widget_textedit.appendPlainText("Removing lines with 'UNKNOWN'")
        lines = text.split("\n")
        removed_lines = [line for line in lines if "UNKNOWN" not in line]
        cleaned_text = "\n".join(removed_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join([line for line in lines if line not in removed_lines]))
    
        return cleaned_text, [line for line in lines if line not in removed_lines]
    
    
    def remove_consecutive_asterisks(self, text):
        self.console_widget_textedit.appendPlainText("Removing lines with four or more consecutive asterisks")
        lines = text.split("\n")
        removed_lines = [line for line in lines if "****" not in line]
        cleaned_text = "\n".join(removed_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join([line for line in lines if line not in removed_lines]))
    
        return cleaned_text, [line for line in lines if line not in removed_lines]
    
    
    def remove_similar_lines(self, text, similarity_threshold):
        self.console_widget_textedit.appendPlainText("Removing lines that are similar to other lines")
        lines = text.split("\n")
        cleaned_lines = []
        removed_lines = []
        for line in lines:
            is_similar = False
            for cleaned_line in cleaned_lines:
                if self.are_lines_similar(line, cleaned_line):
                    is_similar = True
                    removed_lines.append(line)
                    break
            if not is_similar:
                cleaned_lines.append(line)
        cleaned_text = "\n".join(cleaned_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join(removed_lines))
    
        return cleaned_text, removed_lines
    
    
    def are_lines_similar(self, line1, line2):
        similarity_score = difflib.SequenceMatcher(None, line1, line2).ratio()
        similarity_threshold = 0.8
        if similarity_score > similarity_threshold:
            return True
        else:
            return False
    
    
    def remove_lines_without_separator(self, text):
        self.console_widget_textedit.appendPlainText("Removing lines without ':' separator")
        lines = text.split("\n")
        removed_lines = [line for line in lines if ":" in line]
        cleaned_text = "\n".join(removed_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join([line for line in lines if line not in removed_lines]))
    
        return cleaned_text, [line for line in lines if line not in removed_lines]
    
    
    def remove_weak_passwords(self, text):
        self.console_widget_textedit.appendPlainText("Removing lines with weak passwords")
        lines = text.split("\n")
        cleaned_lines = [line for line in lines if len(line.split(":")[-1].strip()) > 3]
        cleaned_text = "\n".join(cleaned_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join([line for line in lines if line not in cleaned_lines]))
    
        return cleaned_text, [line for line in lines if line not in cleaned_lines]
    
    
    def remove_non_english_lines(self, text):
        self.console_widget_textedit.appendPlainText("Removing lines with non-English characters")
        lines = text.split("\n")
        cleaned_lines = [line for line in lines if self.is_english(line)]
        cleaned_text = "\n".join(cleaned_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join([line for line in lines if line not in cleaned_lines]))
    
        return cleaned_text, [line for line in lines if line not in cleaned_lines]
    
    
    def remove_illegal_usernames(self, text):
        self.console_widget_textedit.appendPlainText("Removing lines with illegal usernames")
        lines = text.split("\n")
        cleaned_lines = [line for line in lines if self.is_valid_username(line)]
        cleaned_text = "\n".join(cleaned_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join([line for line in lines if line not in cleaned_lines]))
    
        return cleaned_text, [line for line in lines if line not in cleaned_lines]
    
    
    
    def remove_short_lines(self, text):
        self.console_widget_textedit.appendPlainText("Removing lines with 3 or fewer characters on either side of ':'")
    
        lines = text.split("\n")
        removed_lines = [line for line in lines if len(line.split(":")[0].strip()) > 3 and len(line.split(":")[1].strip()) > 3]
        cleaned_text = "\n".join(removed_lines)
    
        output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
        removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
        if output_text is not None:
            output_text.clear()
            output_text.setPlainText(cleaned_text)
    
        if removed_data_text is not None:
            removed_data_text.clear()
            removed_data_text.setPlainText("\n".join([line for line in lines if line not in removed_lines]))
    
        return cleaned_text, [line for line in lines if line not in removed_lines]
    
    def is_english(self, line):
        return all(ord(c) < 128 for c in line)

    def is_valid_username(self, line):
        # Implement the logic to check if a username is valid
        # Example code for checking if a username is valid:
        username = line.split(":")[0]
        pattern = r"^[a-zA-Z0-9_-]{3,20}$"
        return re.match(pattern, username) is not None

    def update_output_text(self):
        output_text = self.password_format_tab.output_text.toPlainText()
        if self.remove_empty_lines_checkbox.isChecked():
            output_text = "\n".join(line for line in output_text.split("\n") if line.strip())
        self.password_format_tab.output_text.setPlainText(output_text)

    def open_directory_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            selected_directory = dialog.selectedFiles()[0]
            self.set_directory_path_element.setPlainText(selected_directory)
    
    def process_directory(self, directory):
        file_count = 0
        folder_count = 0
        cookie_count = 0
        new_text_document_count = 0
        passwords_count = 0
        profile_1_count = 0
        dat_count = 0
        compressed_count = 0  # Initialize the count for compressed files
    
        progress_bar = tqdm(total=100, desc="Scanning files and folders", unit="iteration")
    
        for root, dirs, files in os.walk(directory):
            folder_count += len(dirs)
            file_count += len(files)
            cookie_count += sum(file.endswith(".txt") for file in files)
            new_text_document_count += sum(file.endswith(".txt") and not file.startswith("cookies") for file in files)
            passwords_count += sum(file == "Passwords.txt" for file in files)
            profile_1_count += sum(file == "Profile_1" for file in files)
            dat_count += sum(file.endswith(".dat") for file in files)
            compressed_count += sum(zipfile.is_zipfile(os.path.join(root, file)) for file in files)  # Increment the compressed count for each ZIP file
    
            # Update the progress bar
            progress_bar.update(1)
    
        progress_bar.close()
    
        # Format the results for console log and widget
        console_results = f"Folders: \033[91m{folder_count}\033[0m    Files: \033[92m{file_count}\033[0m\n"
        console_results += f"Profile_1: \033[93m{profile_1_count}\033[0m    Cookies: \033[94m{cookie_count}\033[0m\n"
        console_results += f"Passwords: \033[95m{passwords_count}\033[0m    .dat files: \033[96m{dat_count}\033[0m\n"
        console_results += f"Compressed Files: \033[33m{compressed_count}\033[0m\n"
    
        widget_results = f"Folders: {folder_count}    Files: {file_count}\n"
        widget_results += f"Profile_1: {profile_1_count}    Cookies: {cookie_count}\n"
        widget_results += f"Passwords: {passwords_count}    .dat files: {dat_count}\n"
        widget_results += f"Compressed Files: {compressed_count}\n"
    
        self.console_widget_textedit.appendPlainText(widget_results)
        print(console_results)

    def get_top_file_extensions(self, directory, n=3):
        file_extensions = []
        
        directory_path = self.directory_path_text_element.toPlainText()
        
        if not directory_path:
            self.console_widget_textedit.appendPlainText("Error: No directory path provided.")
            return

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                _, extension = os.path.splitext(file)
                if extension:  # Exclude blank extensions
                    file_extensions.append(extension)

        counter = Counter(file_extensions)
        top_extensions = counter.most_common(3)

        result = "Top 3 File Extensions:\n"
        for extension, count in top_extensions:
            result += f"Extension: {extension} | Count: {count}\n"

        self.console_widget_textedit.appendPlainText(result)

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
            required_modules = ["stem", "adblock"]
            missing_modules = []
            for module in required_modules:
                spec = importlib.util.find_spec(module)
                if spec is None:
                    missing_modules.append(module)
    
            if missing_modules:
                error_message = "The following modules are missing: {}".format(", ".join(missing_modules))
                QtWidgets.QMessageBox.critical(self, "Missing Modules", error_message, QtWidgets.QMessageBox.Ok)
            else:
                script_path = os.path.join(current_dir, "scripts", "browser.py")
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
           console_widget_textedit.appendPlainText("An error occurred: {e}")

    def number_password(self):
        """Create a list of number values that could be phone numbers."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
            
            if input_text is not None and output_text is not None and removed_data_text is not None:
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
                
                removed_data_text.clear()
                removed_data_text.setLineWrapMode(QTextEdit.WidgetWidth)
                removed_data_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                removed_data_text.setPlainText("\n".join(removed_list))
        
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
        input_text = self.findChild(QTextEdit, "input_text").toPlainText()  # Replace "input_text" with the actual object name
    
        # Find and remove links
        removed_links = re.findall(r"(https?://\S+)", input_text)
        cleaned_text = re.sub(r"(https?://\S+)", "", input_text)
    
        # Update output_text and removed_data_text
        self.findChild(QTextEdit, "output_text").setPlainText(cleaned_text)  # Replace "output_text" with the actual object name
        self.findChild(QTextBrowser, "removed_data_text").setPlainText("\n".join(removed_links))  # Replace "removed_data_text" with the actual object name

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
            script_path = os.path.join("scripts", "browser.py")
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
            removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
            if input_text is not None and output_text is not None and removed_data_text is not None:
                if state == Qt.Checked:
                    input_text.setLineWrapMode(QTextEdit.WidgetWidth)
                    input_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                    output_text.setLineWrapMode(QTextEdit.WidgetWidth)
                    output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                    removed_data_text.setLineWrapMode(QTextEdit.WidgetWidth)
                    removed_data_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                else:
                    input_text.setLineWrapMode(QTextEdit.NoWrap)
                    input_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                    output_text.setLineWrapMode(QTextEdit.NoWrap)
                    output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                    removed_data_text.setLineWrapMode(QTextEdit.NoWrap)
                    removed_data_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
                # Update the scroll bar visibility
                input_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                input_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                output_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                removed_data_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                removed_data_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    
                input_text.updateGeometry()
                output_text.updateGeometry()
                removed_data_text.updateGeometry()
    
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

    def setup_buttons(self):
        self.pasteButton.clicked.connect(self.paste_input)
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
        self.removeAfter_Tab_Space.clicked.connect(self.removeAfter_Tab_Space_clicked)
        self.sort_email_domainsButton = QPushButton("Sort Email Domains")
        self.sort_email_domainsButton.clicked.connect(self.sort_email_domains)

        self.sort_remove_similarButton.clicked.connect(self.sort_remove_similar)
        self.emailPasswordButton.clicked.connect(self.email_password)
        self.usernamePasswordButton.clicked.connect(self.username_password)
        self.newtextdocuments_button.clicked.connect(self.handle_newtextdocuments)
        self.widget_button_chat.clicked.connect(self.open_chat)
        self.widget_button_configs.clicked.connect(self.open_configs_ui)
        self.widget_button_cookies.clicked.connect(self.open_cookies_ui)

        self.remove_inbetween_two_variablesButton.clicked.connect(self.remove_inbetween_two_variablesButtonClicked)  # Replace "remove_inbetween_two_variablesButton" with the actual object name
        self.stealer_log_format_combo.currentIndexChanged.connect(self.update_text_browser)
        self.password_working_function_combo.currentIndexChanged.connect(self.update_work_location_browser)
        self.input_text = self.findChild(QTextEdit, "input_text")
        self.domain_managerButton.clicked.connect(self.launch_domain_manager)
        self.widget_button_urltools.clicked.connect(self.launch_url_manager)

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
        self.numberPasswordButton.clicked.connect(self.number_password)
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
        self.sort_cc_dataButton = QPushButton("Sort CC Data")
        self.sort_cc_dataButton.clicked.connect(self.sort_cc_data)
        self.get_cookie_stats_button = QPushButton("Get Stats")
        self.get_cookie_stats_button.clicked.connect(self.scan_files_folders)
        self.get_log_stats_button = QPushButton("Get Log Stats")
        self.get_log_stats_button.clicked.connect(self.scan_files_folders)
        self.get_file_stats_button = QPushButton("Get File Stats")
        self.get_file_stats_button.clicked.connect(self.scan_files_folders)
        self.extract_phone_numberButton.clicked.connect(self.extract_phone_numbers_button_clicked)
        self.clear_tabs_button.clicked.connect(self.clear_tabs)
        self.clear_tabs_button = QPushButton("Clear Tabs")
        self.file_tree_view_button = QPushButton("Display Your Selected File Structure")
        self.remove_empty_lines_button = QPushButton("Remove Empty Lines")
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
        self.clear_tabs_button.clicked.connect(self.clear_tabs)
        self.widget_button_loghunter.clicked.connect(self.log_hunter_function)
        self.extract_ip_addressButton.clicked.connect(self.extract_ip_address_clicked)

        self.remove_skinnyButton.clicked.connect(self.remove_skinnyButton_clicked)
        self.sort_password_by_weightButton.clicked.connect(self.sort_password_by_weightButton_clicked)
        self.sort_by_cap_dateButton.clicked.connect(self.sort_by_cap_dateButton_clicked)
        self.sort_passwords_textButton.clicked.connect(self.sort_passwords_textButton_clicked)
        self.remove_after_button.clicked.connect(self.show_remove_after_dialog)
        self.file_tree_view_button.clicked.connect(self.file_tree_view_button_clicked)
        self.remove_empty_lines_button.clicked.connect(self.remove_empty_lines_function)
        self.encryption_keys_button.clicked.connect(self.encryption_keys_button_clicked)
        self.sorting_cookies_count_total_values.clicked.connect(self.sorting_cookies_count_total_function)
        self.password_working_function_combo.currentIndexChanged.connect(self.handle_password_working_function_change)
        self.rcovery_key_button.clicked.connect(self.handle_recovery_key_button_click)
        self.eth_private_button
        self.wallet_import_format_button
        self.recovery_phrase_button
        self.parse_button.clicked.connect(self.parse_and_arrange)
        self.file_tree_structure_button.clicked.connect(self.file_tree_structure_button_function)
        self.remove_before_button_2.clicked.connect(self.remove_before_button_2_function)
        self.sort_by_cookies_button.clicked.connect(self.sort_by_cookies_function)
        self.authy_desktop_button.clicked.connect(self.authy_desktop_functions)
        self.remote_desktop_button.clicked.connect(self.remote_desktop_functions)
        self.pgp_button.clicked.connect(self.pgp_gpg_key_functions)
        self.values_list_widget = QListWidget()
        self.reformat_button.clicked.connect(self.reformat_button_function)
        self.donation_text_edit = QTextEdit("donation_text_edit")
        # Set the initial donation text
        self.donation_text_edit.setPlainText("49yNe4Unj6CiUBiXEQD4UL7avZ3wvD8qKgWXTnFwTobTVjvVQ3EGK1y3sdq8WYAJh5RrhG4E5UNQv3XiedSP8s27MgqPJMh")
        # Set up the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.scroll_text)
        self.timer.start(100)  # Adjust the interval for the desired scrolling speed
        self.extract_emails_button = QPushButton("Extract Emails")
        self.extract_emails_button.clicked.connect(self.extract_emails)


    
    def handle_button_click(self, button_name):
        # List of specific buttons that trigger the error dialog
        specific_buttons = [
            "Sort by Cookies", "Authy Desktop", "New Text Documents", "Chrome Extensions",
            "Desktop Wallets", "Auth Files", "PGP GPG Keys", "Text Named Files",
            "Browser 2FA Exten", "Browser Wallets", "Remote Desktop", "Encryption keys",
            "Control Panels", "Telegram Folders", "Scrape Keys", "Scrape Banking Data",
            "Scrape Backup Codes", "Scrape Security Data", "Discord Folders"
        ]
        
        if button_name in specific_buttons and not self.set_directory_path_element:
            # Display an error dialog as the path is not set
            self.display_error_dialog("Error", "Path not set for the selected option.")

    def display_error_dialog(self, title, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec_()

    def extract_emails(input_text):
        extracted_emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', input_text)
        removed_data = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', input_text)
        return extracted_emails, removed_data
    
    # Example usage
    input_text = "Hello, my email is test@example.com. Please contact me at test2@example.com."
    extracted_emails, removed_data = extract_emails(input_text)
    print("Extracted Emails:")
    for email in extracted_emails:
        print(email)
    print("Removed Data:")
    print(removed_data)
        
    def handle_sort_by_cookies(self):
        pass


    def scroll_text(self):
        # Get the current text
        text = self.donation_text_edit.toPlainText()
        
        # Scroll the text by moving the first character to the end
        scrolled_text = text[1:] + text[0]
        
        # Set the scrolled text
        self.donation_text_edit.setPlainText(scrolled_text)


    def reformat_button_function(self):
        # Create the custom dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Reformat Settings")
    
        # Create labels and line edits for current and desired formats
        current_label = QLabel("Current Format:")
        current_line_edit = QLineEdit()
    
        desired_label = QLabel("Desired Format:")
        desired_line_edit = QLineEdit()
    
        separator_label = QLabel("Separator Value:")
        separator_line_edit = QLineEdit()
    
        # Create a layout for the dialog
        layout = QVBoxLayout()
        layout.addWidget(current_label)
        layout.addWidget(current_line_edit)
        layout.addWidget(desired_label)
        layout.addWidget(desired_line_edit)
        layout.addWidget(separator_label)
        layout.addWidget(separator_line_edit)
    
        # Create OK button
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(lambda: dialog.accept())  # Close the dialog when OK is clicked
        layout.addWidget(ok_button)
    
        # Set the layout for the dialog
        dialog.setLayout(layout)
    
        # Show the dialog and wait for user input
        if dialog.exec_() == QDialog.Accepted:
            # Retrieve the values from the line edits
            current_format = current_line_edit.text()
            desired_format = desired_line_edit.text()
            separator_value = separator_line_edit.text()
    
            # Get the input text
            input_text = self.input_text.toPlainText()
    
            # Create the regular expression pattern with the current_format and separator_value
            pattern = rf'{re.escape(current_format)}:\S+'
    
            # Create the replacement string with the desired_format and separator_value
            replacement = rf'{desired_format}{separator_value}'
    
            # Use regular expressions to match the pattern in the input text and replace it with the replacement string
            transformed_text = re.sub(pattern, replacement, input_text)
    
            # Update the output text with the transformed text
            self.output_text.setPlainText(transformed_text)
    
            # Show a message box to indicate the transformation is complete
            QMessageBox.information(self, "Transformation Complete", "Text has been transformed.")


    def sort_by_cookies_function():
        # Display text input window to enter the domains
        domains = input("Enter the domains to sort cookies by (one per line): ").splitlines()
        
        # Get the directory path
        directory_path = self.directory_path_text_element.toPlainText()
        
        # Iterate over each domain and search for matching cookie text files
        for domain in domains:
            # Search for cookie text files containing the specific domain
            cookie_files = search_cookie_files(directory_path, domain)
            
            # Save the results under Diamond Sorter/Sorter Cookies/REQUEST/Cookies.txt
            save_results(cookie_files, "Diamond Sorter/Sorter Cookies/REQUEST", "Cookies.txt")
            
            # Display each hit in the console
            if cookie_files:
                print(f"Found matching cookies for domain: {domain}")
                for file in cookie_files:
                    print(f" - {file}")
            else:
                print(f"No matching cookies found for domain: {domain}")


    def authy_desktop_functions(self):
        # Get the directory path
        directory_path = self.directory_path_text_element.toPlainText()

        # Define the search_folders function within the same class
        def search_folders(root_dir, folder_names):
            found_folders = []
            for root, dirs, _ in os.walk(root_dir):
                for folder in folder_names:
                    if folder.upper() in map(str.upper, dirs):
                        found_folders.append(os.path.join(root, folder))
            return found_folders

        # Define the process_folder function to simulate processing and return results
        def process_folder(folder):
            # Simulate processing and return some results
            return [f"Processed file in folder: {folder}/file1.txt", "Processed folder: subfolder"]

        # Define the save_results function to save results under a specified directory
        def save_results(folders, save_directory):
            for folder in folders:
                result_folder = os.path.join(save_directory, os.path.basename(folder))
                os.makedirs(result_folder, exist_ok=True)
                for root, _, files in os.walk(folder):
                    for file in files:
                        shutil.copy2(os.path.join(root, file), result_folder)

        # Search for folders with the names AUTHY or AUTHDESKTOP
        authy_folders = search_folders(directory_path, ["AUTHY", "AUTHDESKTOP"])

        # Iterate over each folder, process it, and display results
        for folder in authy_folders:
            print(f"Crawled path: {folder}")
            results = process_folder(folder)
            if results:
                print("Results:")
                for result in results:
                    print(result)
            else:
                print("No results found.")

        # Save the results under Diamond Sorter/Sorter Authy/AuthyDesktop_Result
        save_results(authy_folders, "Diamond Sorter/Sorter Authy/AuthyDesktop_Result")
    
    def remote_desktop_functions(self):
        # Get the directory path
        directory_path = self.directory_path_text_element.toPlainText()

        # Define the search_files function within the same class
        def search_files(root_dir, extensions):
            found_files = []
            for root, _, files in os.walk(root_dir):
                for file in files:
                    if any(file.endswith(ext) for ext in extensions):
                        found_files.append(os.path.join(root, file))
            return found_files

        # Search for text files in the specified directory
        text_files = search_files(directory_path, [".txt"])

        # Move the text files to a remote desktop folder
        remote_folder = "RemoteDesktop"
        for file_path in text_files:
            destination_path = os.path.join(remote_folder, os.path.basename(file_path))
            shutil.move(file_path, destination_path)

        # Display updates and notices in the console
        console_text = []
        console_text.append("Updates and Notices:")
        console_text.append(f" - Moved {len(text_files)} text files to the '{remote_folder}' folder.")

        # Set the console text with the updates
        self.console_widget_textedit.setPlainText('\n'.join(console_text))

    def pgp_gpg_key_functions(self):
        # Get the directory path
        directory_path = self.directory_path_text_element.toPlainText()

        # Define the search_folders function within the same class
        def search_folders(root_dir, folders):
            found_folders = []
            for root, dirs, files in os.walk(root_dir):
                for folder in folders:
                    if folder in dirs:
                        found_folders.append(os.path.join(root, folder))
            return found_folders

        # Define the search_files function to filter files with specified extensions
        def search_files(folders, extensions):
            found_files = []
            for folder in folders:
                for root, _, files in os.walk(folder):
                    for file in files:
                        if any(file.endswith(ext) for ext in extensions):
                            found_files.append(os.path.join(root, file))
            return found_files

        # Define the move_files function to move files to a specified results folder
        def move_files(files, results_folder):
            for file in files:
                destination_path = os.path.join(results_folder, os.path.basename(file))
                shutil.move(file, destination_path)

        # Search inside all folders named FileGrabber for files with pgp or gpg extensions
        filegrabber_folders = search_folders(directory_path, ["FileGrabber"])
        pgp_gpg_files = search_files(filegrabber_folders, [".pgp", ".gpg"])

        # Move the files to a results folder named PGP Sorted
        results_folder = "PGP Sorted"
        move_files(pgp_gpg_files, results_folder)

        # Display updates and notices in the console
        console_text = []
        console_text.append("Updates and Notices:")
        console_text.append(f" - Found {len(pgp_gpg_files)} PGP/GPG key files.")
        console_text.append(f" - Moved files to the '{results_folder}' folder.")

        # Set the console text with the updates
        self.console_widget_textedit.setPlainText('\n'.join(console_text))


    def new_text_document_functions(self):
        # Get the directory path
        directory_path = self.directory_path_text_element.toPlainText()
        
        # Search for New Text Document.txt files
        new_text_document_files = search_files(directory_path, ["New Text Document.txt"])
        
        # Ask the user if they want to move or copy the files
        user_choice = input("Do you want to move or copy the New Text Document.txt files? (M for move, C for copy): ")
        
        # Process the files based on user choice
        if user_choice.lower() == "m":
            # Move the files to the results folder
            results_folder = "Results"
            move_files(new_text_document_files, results_folder)
            print(f"Moved {len(new_text_document_files)} files to {results_folder} folder.")
        elif user_choice.lower() == "c":
            # Copy the files to the results folder
            results_folder = "Results"
            copy_files(new_text_document_files, results_folder)
            print(f"Copied {len(new_text_document_files)} files to {results_folder} folder.")
        else:
            print("Invalid choice. Please choose either M for move or C for copy.")
    
    def text_named_files_functions(self):
        directory_path = self.directory_path_text_element.toPlainText()
        print("Pass")

    def remove_before_button_2_function(self):
        value, ok = QInputDialog.getText(self, "Remove Before", "Enter the value to remove before:")
        if ok:
            input_text = self.input_text.toPlainText()
            output_text = ""
            removed_data = ""
    
            # Find the index of the specified value
            index = input_text.find(value)
    
            if index != -1:
                # Extract the text after the specified value
                output_text = input_text[index + len(value):].strip()
                # Extract the text before the specified value
                removed_data = input_text[:index].strip()
            else:
                # Value not found in the input text
                output_text = input_text
    
            # Update the output_text and removed_data accordingly
            self.output_text.setPlainText(output_text)
            self.removed_data_text.setPlainText(removed_data)  
    
            
    def file_tree_structure_button_function(text):
        # Set the root directory path using the appropriate method or code
        root_directory = text
    
        def display_file_tree_structure(directory, level=0):
            files = []
            folders = []
    
            for file in os.listdir(directory):
                path = os.path.join(directory, file)
                if os.path.isfile(path):
                    files.append(file)
                elif os.path.isdir(path):
                    folders.append(file)
    
            for file in files:
                print(f"{'  ' * level}|-- {file}")
    
            for folder in folders:
                print(f"{'  ' * level}|-- {folder}")
                new_path = os.path.join(directory, folder)
                display_file_tree_structure(new_path, level + 1)
    
        try:
            folder_names = []
            for i in range(3):
                folder_name = input(f"Enter folder {i+1} name: ")
                folder_names.append(folder_name)
    
            directory_path = os.path.join(root_directory, *folder_names)
            display_file_tree_structure(directory_path)
    
        except FileNotFoundError:
            print("One or more folders do not exist.")
        except NotADirectoryError:
            print("One or more folder names are invalid.")


    def remove_empty_lines_function(text):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Input must be a non-empty string")
    
        lines = text.split('\n')
        non_empty_lines = [line.strip() for line in lines if line.strip()]
        modified_text = '\n'.join(non_empty_lines)
    
        return modified_text

    def parse_and_arrange(self):
        # Get the format request from the format_request_textedit
        format_request = self.format_request_textedit.toPlainText()
    
        # Find the line format and separator from the format request
        line_format, separator = self.parse_format_request(format_request)
    
        if line_format is not None and separator is not None:
            # Get the lines from the input_text
            input_text = self.input_text.toPlainText()
            input_lines = input_text.splitlines()
    
            # Replace options with corresponding values and join the parsed lines
            parsed_lines = [
                line_format.replace("{URL}", "Replace with URL value")
                .replace("{EMAIL}", "Replace with EMAIL value")
                .replace("{USER}", "Replace with USER value")
                .replace("{PASS}", "Replace with PASS value")
                .replace("{IP}", "Replace with IP value")
                .replace("{CC}", "Replace with CC value")
                .replace("{MM}", "Replace with MM value")
                .replace("{YYYY}", "Replace with YYYY value")
                for line in input_lines
            ]
    
            # Arrange the parsed lines based on the separator
            arranged_text = separator.join(parsed_lines)
    
            # Set the arranged text in the output_text
            self.output_text.setPlainText(arranged_text)
        else:
            QtWidgets.QMessageBox.warning(
                self.format_request_textedit, "Invalid Format", "Invalid format request."
            )

    def run(self):
        # Create the main window and layout
        main_window = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(main_window)

        # Add the input_text, format_request_textedit, parse_button, and output_text widgets to the layout
        layout.addWidget(self.input_text)
        layout.addWidget(self.format_request_textedit)
        layout.addWidget(self.parse_button)
        layout.addWidget(self.output_text)

        main_window.show()
        self.app.exec_()





    def handle_recovery_key_button_click(self):
        selected_directory = set_directory_path_element.get_selected_directory()
        regex_pattern = input("Enter the regular expression pattern: ")
        regex = re.compile(regex_pattern)
        result_texts = []
    
        for root, dirs, files in os.walk(selected_directory):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        contents = f.read()
                        matches = regex.findall(contents)
                        if matches:
                            result_texts.extend(matches)
    
        for result in result_texts:
            console_widget_textedit.append(result)
        
        
        
        
    def handle_password_working_function_change(self, index):
        selected_option = self.password_working_function_combo.itemText(index)
        console_widget = self.findChild(QPlainTextEdit, "console_widget_textedit")
        if console_widget is not None:
            console_widget.insertPlainText(f"Selected option: {selected_option}\n")


    def crawl_directory(directory_path, console_widget_textedit):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        content = f.read()
                        matches = re.findall(r"^[a-zA-Z0-9]{24}$", content)
                        if matches:
                            console_widget_textedit.append(f"Found matching pattern in {file_path}:")
                            for match in matches:
                                console_widget_textedit.append(match)
    
    
    def sorting_cookies_count_total_function(directory_path):
        domain_dict = {}
        try:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file.endswith(".txt"):
                        file_path = os.path.join(directory_path, file)
                        with open(file_path, "r") as f:
                            for line in f:
                                # Rest of your code...
                                pass
        except (FileNotFoundError, TypeError) as e:
            print(f"An error occurred while processing the files: {e}")

    def display_file_stats(self):
        directory_path = self.set_directory_path_element.toPlainText()

        if os.path.exists(directory_path):
            try:
                file_stats = []
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        if file.endswith(".txt"):
                            file_path = os.path.join(directory_path, file)
                            with open(file_path, "r") as f:
                                for line in f:
                                    # Rest of your code...
                                    pass
                self.console_widget_textedit.setPlainText("\n".join(file_stats))
            except (FileNotFoundError, TypeError) as e:
                error_message = f"An error occurred while processing the files: {e}"
                self.console_widget_textedit.setPlainText(error_message)
        else:
            self.console_widget_textedit.setPlainText("Invalid directory path.")


    def remove_empty_lines_function(self):
        input_text = self.input_text.toPlainText()
        lines = input_text.split("\n")  # Split the text into lines
        non_empty_lines = [line for line in lines if line.strip()]  # Filter out empty lines
        output_text = "\n".join(non_empty_lines)  # Join the non-empty lines back together
    
        self.output_text.clear()  # Clear the output widget
        self.output_text.insertPlainText(output_text)  # Display the non-empty lines in the output widget


    
    def encryption_keys_button_clicked(self):
        directory_path = self.set_directory_path_element.toPlainText()  # Get the directory path from the GUI element
        saved_results_path = self.savedResultsTextBox.toPlainText()

        try:
            # Check if a save path is set
            if not saved_results_path:
                error_message = "Please set a save path before processing encrypted key files."
                self.console_widget_textedit.setPlainText(error_message)
                return

            # List to store the found encrypted key files
            encrypted_key_files = []

            # Regular expression pattern to match PGP or GPG encrypted keys
            regex_pattern = r"-----BEGIN PGP (PUBLIC|PRIVATE) KEY BLOCK-----.*?-----END PGP (PUBLIC|PRIVATE) KEY BLOCK-----"

            # Crawl the directory and search for text files containing encrypted keys
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r", encoding='utf-8') as f:
                            file_content = f.read()

                            if re.search(regex_pattern, file_content, re.DOTALL):
                                encrypted_key_files.append(file_path)

            # Save the found encrypted key files to the specified path
            for file_path in encrypted_key_files:
                destination_path = os.path.join(saved_results_path, os.path.basename(file_path))
                shutil.copy(file_path, destination_path)

            # Display the paths of encrypted key files in the console_text widget
            console_text = []
            for file_path in encrypted_key_files:
                console_text.append(file_path)

            self.console_widget_textedit.setPlainText('\n'.join(console_text))

        except Exception as e:
            error_message = f"An error occurred while processing the files: {e}"
            self.console_widget_textedit.setPlainText(error_message)



    def file_tree_view_button_clicked(self):
        print("test")
        root_dir = os.path.basename(self.set_directory_path_element)  # Access folder_path as an attribute of the class
        file_tree = []  # List to store the file tree structure

        # Append current directory icon and name
        folder_icon = '├──'
        folder_color = Fore.LIGHTBLACK_EX
        if os.path.isdir(self.set_directory_path_element):
            if is_archived_folder(self.set_directory_path_element):
                folder_color = Fore.LIGHTBLACK_EX + Style.BRIGHT
            else:
                folder_color = Fore.RESET
        file_tree.append(f"{indent}{folder_color}{folder_icon} {root_dir}/")

        # Append all files in the current directory with icons and color coding
        for file in os.listdir(self.set_directory_path_element):
            file_path = os.path.join(self.set_directory_path_element, file)
            file_icon = '├──'
            file_name, file_extension = os.path.splitext(file)
            color = get_file_color(file_extension)
            file_icon = get_file_icon(file_extension)
            file_tree.append(f"{indent}│   {color}{file_icon} {file_name}{file_extension}")

        # Recursively call the function for each subdirectory
        for subdir in os.listdir(self.set_directory_path_element):
            subdir_path = os.path.join(self.set_directory_path_element, subdir)
            if os.path.isdir(subdir_path):
                self.file_tree_view_button(subdir_path, indent + '│   ')  # Access the method as an attribute of the class using self

        return file_tree

    
    def get_file_color(file_extension):
        # Assign colors based on file extensions
        if file_extension == '.txt':
            return Fore.MAGENTA
        elif file_extension == '.py':
            return Fore.YELLOW
        elif file_extension == '.csv':
            return Fore.RED
        elif file_extension == '.exe':
            return Fore.CYAN
        else:
            return Style.RESET_ALL
    
    def get_file_icon(file_extension):
        # Assign icons based on file extensions
        if file_extension == '.txt':
            return '📄'
        elif file_extension == '.py':
            return '🐍'
        elif file_extension == '.csv':
            return '📊'
        elif file_extension == '.exe':
            return '💻'
        else:
            return '📄'
    
    def is_archived_folder(folder_path):
        # Check if the folder is an archived folder
        folder_name = os.path.basename(folder_path)
        return folder_name.endswith('.zip') or folder_name.endswith('.tar') or folder_name.endswith('.gz')

    def remove_skinnyButton_clicked(self):
        directory_path = self.set_directory_path_element.toPlainText()  # Get the directory path from set_directory_path_element
        
        # Ensure that the directory path is valid
        if not os.path.isdir(directory_path):
            QMessageBox.warning(self, "Error", "Invalid directory path. Please select a valid directory.")
            return
        
        # Variables for crawl progress and count
        crawl_count = 0
        total_count = 0
        
        # Crawling and removal logic
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file == "password.txt":
                    total_count += 1  # Increment total count
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    if file_size < 2048:  # 2KB in bytes
                        os.remove(file_path)
                        crawl_count += 1  # Increment crawl count
        
        # Display crawl progress and total count in console_widget_textedit
        output = f"Crawl Progress: {crawl_count}/{total_count} password.txt files"
        self.console_widget_textedit.setPlainText(output)
        
        QMessageBox.information(self, "Remove Skinny", "Password files less than 2KB have been removed successfully.")
    
    def sort_password_by_weightButton_clicked(self):
        options = ["Largest to Smallest", "Smallest to Largest", "Group by Weight Range"]
        selected_option, ok = QInputDialog.getItem(self, "Sort Passwords by Weight", "Choose a sorting option:", options, editable=False)
        
        if ok:
            if selected_option == "Largest to Smallest":
                self.sort_passwords("desc")
            elif selected_option == "Smallest to Largest":
                self.sort_passwords("asc")
            elif selected_option == "Group by Weight Range":
                self.group_passwords_by_weight()
    
    def sort_passwords(self, order):
        # Sorting logic based on the order (asc or desc)
        pass

    def group_passwords_by_weight(self):
        lightest_weight, ok = QInputDialog.getInt(self, "Group Passwords by Weight", "Enter the lightest weight:")
        if ok:
            heaviest_weight, ok = QInputDialog.getInt(self, "Group Passwords by Weight", "Enter the heaviest weight:")
            if ok:
                # Grouping logic based on the weight range
                pass
    
    def sort_by_cap_dateButton_clicked(self):
        directory_path = self.set_directory_path_element.toPlainText()  # Get the directory path from set_directory_path_element
        
        # Ensure that the directory path is valid
        if not os.path.isdir(directory_path):
            QMessageBox.warning(self, "Error", "Invalid directory path. Please select a valid directory.")
            return
        
        capture_dates = []
        
        # Crawling logic
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file == "UserInformation.txt":
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as input_file:
                        for line in input_file:
                            if line.startswith("Capture Date:"):
                                capture_date = line.split(":")[1].strip()
                                capture_dates.append(capture_date)
        
        # Sort capture dates
        sorted_dates = sorted(capture_dates, key=lambda x: datetime.strptime(x, "%Y-%m-%d"), reverse=True)
        
        # Display sorted dates in console_widget_textedit
        output = "Sorted Capture Dates:\n" + "\n".join(sorted_dates)
        self.console_widget_textedit.setPlainText(output)
        
        QMessageBox.information(self, "Sort by Capture Date", "Capture dates have been sorted successfully.")

    def sort_passwords_textButton_clicked(self):
        # Prompt the user to choose move or copy action
        action_options = ["Move", "Copy"]
        selected_action, ok = QInputDialog.getItem(self, "Choose Action", "Choose an action:", action_options, editable=False)
    
        if ok:
            # Get the directory path from set_directory_path_element
            directory_path = self.set_directory_path_element.toPlainText()
    
            # Ensure that the directory path is valid
            if not os.path.isdir(directory_path):
                QMessageBox.warning(self, "Error", "Invalid directory path. Please select a valid directory.")
                return
    
            # Get the saving results path from savedResultsTextBox
            results_path = self.savedResultsTextBox.toPlainText()
    
            # Ensure that the results path is valid
            if not os.path.isdir(results_path):
                QMessageBox.warning(self, "Error", "Invalid results path. Please set a valid path.")
                return
    
            # Crawling and action logic
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file == "Password.txt":
                        file_path = os.path.join(root, file)
                        if selected_action == "Move":
                            shutil.move(file_path, results_path)
                        elif selected_action == "Copy":
                            shutil.copy(file_path, results_path)
    
            QMessageBox.information(self, "Sort Passwords", f"Password files have been {selected_action.lower()}ed successfully.")

    def extract_ip_address_clicked(self):
        input_text = self.input_text.toPlainText()
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_port_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+'
        
        ip_addresses = re.findall(ip_pattern, input_text)
        ip_port_addresses = re.findall(ip_port_pattern, input_text)
        
        extracted_ips = ip_addresses + ip_port_addresses
        removed_data = re.sub(ip_pattern, "", input_text)
        removed_data = re.sub(ip_port_pattern, "", removed_data)
        
        self.output_text.setPlainText('\n'.join(extracted_ips))
        self.removed_data_text.setPlainText(removed_data)

    def show_remove_after_dialog(self):
        value, ok = QInputDialog.getText(self, "Remove After", "Enter the value to remove after:")
        if ok:
            num_values, ok = QInputDialog.getInt(self, "Remove After", "Enter the number of values to remove after:")
            if ok:
                self.remove_after_value(value, num_values)
    
    def remove_after_value(self, value, num_values):
        input_text = self.input_text.toPlainText()
        lines = input_text.split('\n')
        removed_lines = []
        output_lines = []
    
        for line in lines:
            if value in line:
                index = lines.index(line)
                removed_lines.extend(lines[index+1: index+1+num_values])
                output_lines.append(line)
            else:
                output_lines.append(line)
    
        self.output_text.setPlainText('\n'.join(output_lines))
        self.removed_data_text.setPlainText('\n'.join(removed_lines))
    
    def clear_tabs(self):
        self.output_text.clear()
        self.removed_data_text.clear()

    def extract_phone_numbers_button_clicked(self):
        try:
            input_text = self.findChild(QtWidgets.QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QtWidgets.QTextEdit, "output_text")  # Replace "output_text" with the actual object name
    
            if input_text is not None and output_text is not None:
                text = input_text.toPlainText()
                phone_numbers = re.findall(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", text)
                extracted_phone_numbers = "\n".join(phone_numbers)
    
                output_text.clear()
                output_text.setPlainText(extracted_phone_numbers)
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_file_stats():
        pass

    def get_cookie_stats():
        pass

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
        directory_path = self.set_directory_path_element.toPlainText()
        self.console_widget_textedit.appendPlainText(f"Wordpress Finder button clicked. Directory path: {directory_path}")

        # Create the thread and connect the signal to a slot
        self.wordpress_finder_thread = WordpressFinderThread(directory_path)
        self.wordpress_finder_thread.results_obtained.connect(self.handle_wordpress_finder_results)

        # Start the thread
        self.wordpress_finder_thread.start()

    def handle_wordpress_finder_results(self, results):
        self.savedResultsTextBox.setText(results)
        selected_directory = self.set_directory_path_element.toPlainText()
        save_directory = os.path.join(selected_directory, "Sorted", "Date", "Wordpress", datetime.now().strftime("%Y%m%d"))
        self.crawlThread = CrawlerThread(selected_directory, "", save_directory)
        self.crawlThread.copied.connect(self.console_widget_textedit.appendPlainText)
        self.crawlThread.not_copied.connect(self.dummy_message)
        self.crawlThread.finished.connect(self.finish_crawl)
        self.crawlThread.start()
        self.server_information(path_to_directory, path_to_output)

    def handle_scrape_keys(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Perform crawling logic and find WordPress instances in the directory
        # Save the results in the savedResultsTextBox
        results = crawl_directory_for_wordpress(directory_path)
        self.savedResultsTextBox.setText(results)

    def server_information(self, path, output_dir):
        counter = 1
        ftp_pattern = re.compile(r"ftp:\/\/(?:\w+\:\w+@)?[\w.-]+(?:\:\d+)?(?:\/.*)?", re.IGNORECASE)
    
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
        def process_file(file_path):
            nonlocal counter
            with open(file_path, "r") as input_file:
                lines = input_file.readlines()
                for line in lines:
                    if re.search(ftp_pattern, line):
                        output_subdir = os.path.join(output_dir, "ftp")
                        os.makedirs(output_subdir, exist_ok=True)
                        output_file = os.path.join(output_subdir, f"{counter}.txt")
                        with open(output_file, "a") as output:
                            output.write(line)
                        # Increment the counter in a thread-safe manner
                        with threading.Lock():
                            counter += 1
    
        def process_directory(root, files):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    thread = threading.Thread(target=process_file, args=(file_path,))
                    thread.start()

        for root, dirs, files in os.walk(path):
            # Start a thread for processing each directory
            process_thread = threading.Thread(target=process_directory, args=(root, files))
            process_thread.start()

    def cpanel_accounts(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Perform crawling logic and find cPanel accounts in the directory
        results = self.find_cpanel_accounts(directory_path)
        self.savedResultsTextBox.setText(results)
        self.console_widget_textedit.appendPlainText(results)

    def find_cpanel_accounts(self, directory_path):
        results = ""
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.lower() == "passwords.txt":
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:  # Specify the appropriate encoding
                        lines = f.readlines()
                        for i in range(len(lines)):
                            line = lines[i].strip()
                            if any(keyword in line.lower() for keyword in ["2083", "2096", "2087", "cpanel", "whm"]):
                                url = line
                                username = lines[i + 1].strip()
                                password = lines[i + 2].strip()
                                result = f"URL: {url} USER: {username} PASS: {password}"
                                results += result + "\n"
        return results



    def emails(self):
        directory_path = self.set_directory_path_element.toPlainText()

    def handle_chrome_extensions(self):
        print("Chrome Extensions button clicked")
        
        directory_path = self.Directory_Path_Text_Element.toPlainText()
        output_dir = self.savedResultsTextBox.toPlainText()
        
        extensions_folders = ["Extensions", "Extension", "Plugins"]
        
        for root, dirs, files in os.walk(directory_path):
            for folder in dirs:
                if folder in extensions_folders:
                    if os.path.exists(output_dir):
                        # Prompt the user to choose between move or copy
                        user_choice = input("Do you want to move or copy the results? (move/copy): ")
                        
                        if user_choice.lower() == "move":
                            # Move the folder to the output directory
                            os.rename(os.path.join(root, folder), os.path.join(output_dir, folder))
                        elif user_choice.lower() == "copy":
                            # Copy the folder to the output directory
                            shutil.copytree(os.path.join(root, folder), os.path.join(output_dir, folder))
                        else:
                            print("Invalid choice. Please try again.")
                    
                    # Display the folder found in the console
                    self.console_widget_textedit.appendPlainText(f"Found folder: {folder}")

    def checkmark(self):
        # Logic for the "✅" button
        pass

    def advertisements(self):
        directory_path = self.set_directory_path_element.toPlainText()
        facebook_strings = []
    
        # Perform crawling logic and find Facebook-related string data
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    for line in f:
                        if 'facebook' in line.lower():
                            facebook_strings.append(line.strip())
    
        # Save the results in the savedResultsTextBox
        self.savedResultsTextBox.setText('\n'.join(facebook_strings))

    def socials_forums(self):
        directory_path = self.set_directory_path_element.toPlainText()
        self.savedResultsTextBox.setText(results)

    def update_lcdNumber(self):
        count = self.lcdNumber_4.intValue()
        self.lcdNumber_4.display(count)

    def sort_cc_data(self):
        counter = 1
        cc_pattern = re.compile(r"(\b(?:\d{4}[\s\-]{0,1}){3}\d{4}\b)")
        exp_pattern = re.compile(r"(?:0[1-9]|1[0-2])\/?([0-9]{2})")
        cvv_pattern = re.compile(r"(\b\d{3,4}\b)")
        directory_path = self.set_directory_path_element.toPlainText()
        output_dir = self.savedResultsTextBox.toPlainText()
    
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".txt"):
                    with open(os.path.join(root, file), "r") as input_file:
                        lines = input_file.readlines()
                        for line in lines:
                            cc_match = re.search(cc_pattern, line)
                            exp_match = re.search(exp_pattern, line)
                            cvv_match = re.search(cvv_pattern, line)
                            if cc_match and exp_match and cvv_match:
                                output_subdir = os.path.join(output_dir, "cc")
                                os.makedirs(output_subdir, exist_ok=True)
                                output_file = os.path.join(output_subdir, f"{counter}.txt")
                                with open(output_file, "a") as output:
                                    output.write(f"CC: {cc_match[0]}, Expiry: {exp_match[0]}, CVV: {cvv_match[0]}\n")
                                counter += 1
    
        self.console_widget_textedit.appendPlainText(f"Sort Credit Card Data button clicked. Directory path: {directory_path}")
        self.console_widget_textedit.appendPlainText("Sorting completed successfully.")

    def handle_scrape_banking_data(self):
        # Get the directory path from the specified file directory
        directory_path = self.set_directory_path_element.toPlainText()
        
        # Get the stealer log format combo value
        stealer_log_format = self.stealer_log_format_combo.currentText()
        
    
        # Display the actions, results, and stats in the console widget
        self.console_widget_textedit.appendPlainText("Scrape Banking Data button clicked")
        self.console_widget_textedit.appendPlainText("Starting crawling from directory: " + directory_path)
        self.console_widget_textedit.appendPlainText("Stealer log format: " + stealer_log_format)
        self.stats_values = []  # Define stats_values as an attribute

        # Perform the crawling and display the results
        # Add your crawling and displaying logic here
        
        # Display the stats
        self.console_widget_textedit.appendPlainText("Crawling completed. Displaying stats")
        # Add your stats displaying logic here
        
        # Check if the directory path is valid
        if not os.path.isdir(directory_path):
            self.console_widget_textedit()  # Call the console_data function
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
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling Scrape Backup Codes button
        self.console_widget_textedit.appendPlainText(f"Scrape Backup Codes button clicked. Directory path: {directory_path}")

    def business_emails(self):
        directory_path = self.set_directory_path_element.toPlainText()
        output_file = os.path.join(directory_path, "results.txt")
        with open(output_file, 'w', encoding='utf-8') as output:
            save_option = int(input("Choose the format for saving the results:\n1. EMAIL:PASS\n2. USER:PASS\n"))
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file == "Passwords.txt":
                        with open(os.path.join(root, file), 'r', encoding='utf-8') as input_file:
                            lines = input_file.readlines()
                            for i in range(len(lines)):
                                if keyword in lines[i]:
                                    for j in range(i+1, len(lines)):
                                        if "Username:" in lines[j]:
                                            username = remove_spaces(lines[j].split("Username:")[1])
                                        elif "Password:" in lines[j]:
                                            password = remove_spaces(lines[j].split("Password:")[1])
                                            if len(username) >= 3 and len(password) >= 3:
                                                is_email = "@" in username
                                                if (save_option == 1 and is_email) or (save_option == 2 and not is_email):
                                                    entry = f"{username}:{password}"
                                                    set_console_color(10)
                                                    print(entry)
                                                    reset_console_color()
                                                    output.write(entry + "\n")
                                                else:
                                                    set_console_color(12)
                                                    print(entry)
                                                    reset_console_color()
                                            break
    
        self.console_widget_textedit.appendPlainText(f"Business Emails button clicked. Directory path: {directory_path}")
        self.savedResultsTextBox.setText(output_file)

    def gov_domains(self):
        directory_path = self.set_directory_path_element.toPlainText()
        gov_domains = []
    
        # Perform crawling logic and find passwords.txt files
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.lower() == 'passwords.txt':
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            # Use regular expressions to extract URLs with .gov domain
                            urls = re.findall(r'\bhttps?://\S+\.gov\b', line)
                            gov_domains.extend(urls)
                    # Display the file path in the console_widget
                    self.console_widget_textedit.appendPlainText(file_path)
    
        # Display the found .gov domains in the console_widget
        for domain in gov_domains:
            self.console_widget_textedit.appendPlainText(domain)

    def member_id_pin(self):
        directory_path = self.set_directory_path_element.toPlainText()
        loaded_directory = directory_path.strip()
    
        # Functionality for handling Member ID/PIN button
        self.console_widget_textedit.appendPlainText(f"Member ID/PIN button clicked. Directory path: {directory_path}")
    
        username_password_pattern = re.compile(r"Username:\s*(\S+)\s+Password:\s*(\S+)")
    
        output_text = ""
        file_count = 0
        hit_count = 0
    
        for root, _, files in os.walk(loaded_directory):
            for file in files:
                if file == "Passwords.txt":
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as password_file:
                        self.console_widget_textedit.appendPlainText(f"Crawling file: {file_path}")
                        file_count += 1
                        file_hits = 0
                        for line in password_file:
                            matches = re.findall(username_password_pattern, line)
                            for match in matches:
                                output_text += f"Username: {match[0]}   Password: {match[1]}\n"
                                hit_count += 1
                                file_hits += 1
    
                        if file_hits > 0:
                            output_text += f"\nFile: {file_path}\nTotal Hits: {file_hits}\n\n"
    
        # Display the member ID:PIN results in the output_text window if hits were found
        if hit_count > 0:
            self.output_text.setText(output_text)
        else:
            self.output_text.setText("No hits found.")
    
        # Display the total number of files and hits found
        self.console_widget_textedit.appendPlainText(f"Total Files: {file_count}")
        self.console_widget_textedit.appendPlainText(f"Total Hits: {hit_count}")
    
    def handle_scrape_security_data(self):
        directory_path = self.set_directory_path_element.toPlainText()
        loaded_directory = directory_path.strip()
    
        # Functionality for handling Scrape Security Data button
        self.console_widget_textedit.appendPlainText(f"Scrape Security Data button clicked. Directory path: {directory_path}")
    
        search_words = ["Security Code", "Backup Code", "Phrase"]
        output_text = ""
    
        for root, _, files in os.walk(loaded_directory):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as text_file:
                        self.console_widget_textedit.appendPlainText(f"Scraping file: {file_path}")
                        for line in text_file:
                            for word in search_words:
                                if word in line:
                                    output_text += f"Found word '{word}' in file '{file_path}': {line}\n"
    
        # Display the search results in the console_widget_textedit
        if output_text:
            self.console_widget_textedit.appendPlainText(output_text)
        else:
            self.console_widget_textedit.appendPlainText("No results found.")
    
    def handle_command_link(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling Command Link Button
        self.console_widget_textedit.appendPlainText(f"Command Link Button clicked. Directory path: {directory_path}")
    
    def handle_telegram_folder_sorting(self):
        # Confirm the loaded file directory path
        if not os.path.isdir(loaded_directory):
            choice = self.ask_user_dialog_box("Copy or Move?")  # Replace this with your actual dialog box implementation
        if choice == "Copy" or choice == "Move":
            folders_to_sort = ["Profile_1", "Telegram", "Tdata"]
            num_folders_found = 0
            for folder_name in folders_to_sort:
                folder_path = os.path.join(directory_path, folder_name)
                if os.path.exists(folder_path):
                    destination_folder = os.path.join(directory_path, "saved_results", folder_name)
                    if choice == "Copy":
                        shutil.copytree(folder_path, destination_folder)
                    elif choice == "Move":
                        shutil.move(folder_path, destination_folder)
                    num_folders_found += 1
    
            self.console_widget_textedit.appendPlainText(f"Found {num_folders_found} folders while crawling.")
        else:
            self.console_widget_textedit.appendPlainText("Invalid choice!")
    
        self.savedResultsTextBox.setText(directory_path)
        self.console_widget_textedit.appendPlainText(f"Telegram Folder Sorting Button clicked. Directory path: {directory_path}")
    
        # Crawl the loaded directory and search for the specified folder
        self.crawlThread = CrawlerThread(selected_directory, folder_name, saved_directory)
        self.crawlThread.copied.connect(self.console_widget_textedit.appendPlainText)
        self.crawlThread.not_copied.connect(self.dummy_message)
        self.crawlThread.finished.connect(self.finish_crawl)
        self.crawlThread.start()

    def handle_authy_desktop(self):
        loaded_directory = self.set_directory_path_element.toPlainText()
        # Confirm the loaded file directory path
        if not os.path.isdir(loaded_directory):
            print("Invalid directory path.")
            return
    
        # Define the folder name to search for
        folder_name = "Authy"
    
        # Create the new folder name
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"AuthySorted.{timestamp}"
    
        # Create the saved directory path
        saved_directory = os.path.join(loaded_directory, new_folder_name)
        os.makedirs(saved_directory)
    
        # Crawl the loaded directory and search for the specified folder
        self.crawlThread = CrawlerThread(loaded_directory, folder_name, saved_directory)
        self.crawlThread.copied.connect( self.console_widget_textedit.appendPlainText )
        self.crawlThread.not_copied.connect( self.dummy_message )
        self.crawlThread.finished.connect(self.finish_crawl)
        self.crawlThread.start()
        '''
        for root, dirs, files in os.walk(loaded_directory):
            for dir_name in dirs:
                if dir_name == folder_name:
                    # Get the full path of the folder
                    folder_path = os.path.join(root, dir_name)
                    # Copy the folder and its contents to the saved directory path
                    shutil.copytree(folder_path, os.path.join(saved_directory, dir_name))
        '''
        print("Authy Desktop folder sorting completed.")

    def finish_crawl(self):
        print('Crawled EVERYTHING')

    def dummy_message(self, path):
        self.console_widget_textedit.appendPlainText(f'Not copied: {path}')

    def handle_desktop_wallet(self):
        print("About to start crawling for .dat Files.")
    
        selected_directory = self.set_directory_path_element.toPlainText()  # Get the selected directory path
    
        # Display a confirmation dialog
        reply = QMessageBox.question(self, "Confirmation", f"Start crawling in the specified path?\n\n{selected_directory}",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
        if reply == QMessageBox.Yes:
            # Confirm the loaded file directory path
            if not os.path.isdir(selected_directory):
                print("Invalid directory path.")
                return
    
            # Define the folder name to search for
            folder_name = "Desktop Wallets"
    
            # Create the new folder name
            now = datetime.now()
            timestamp = now.strftime("%Y%m%d%H%M%S")
            new_folder_name = f"DesktopWalletsSorted.{timestamp}"
    
            # Create the saved directory path
            saved_directory = os.path.join(selected_directory, new_folder_name)
            os.makedirs(saved_directory)
    
            # Crawl the loaded directory and search for the specified folder
            self.crawlThread = CrawlerThread(selected_directory, folder_name, saved_directory)
            self.crawlThread.copied.connect(self.console_widget_textedit.appendPlainText)
            self.crawlThread.not_copied.connect(self.dummy_message)
            self.crawlThread.finished.connect(self.finish_crawl)
            self.crawlThread.start()
    
        self.set_directory_path_element.setPlainText(selected_directory)
        self.console_widget_textedit.appendPlainText(f"Desktop Wallet Button clicked. Directory path: {selected_directory}")

    def handle_browser_2fa_extension(self):
        directory_path = self.set_directory_path_element.toPlainText()

        if not directory_path or not os.path.isdir(directory_path):
            self.console_widget_textedit.appendPlainText("Invalid directory path.")
            return

        dialog = QtWidgets.QInputDialog()
        dialog.setInputMode(QtWidgets.QInputDialog.TextInput)
        dialog.setLabelText("Copy or Move?")
        dialog.setWindowTitle("Choice")

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            choice = dialog.textValue()

            if choice == "Copy":
                extensions_folders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder)) and folder.lower() == "extensions"]
                for folder in extensions_folders:
                    source_folder = os.path.join(directory_path, folder)
                    destination_folder = os.path.join(directory_path, "saved_results", folder)
                    shutil.copytree(source_folder, destination_folder)

            elif choice == "Move":
                extensions_folders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder)) and folder.lower() == "extensions"]
                for folder in extensions_folders:
                    source_folder = os.path.join(directory_path, folder)
                    destination_folder = os.path.join(directory_path, "saved_results", folder)
                    shutil.move(source_folder, destination_folder)

            else:
                self.console_widget_textedit.appendPlainText("Invalid choice!")

    def handle_text_named_sorting(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling Text Named Sorting Button
        self.console_widget_textedit.appendPlainText(f"Text Named Sorting Button clicked. Directory path: {directory_path}")

    def handle_pgp(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling PGP Button
        self.console_widget_textedit.appendPlainText(f"PGP Button clicked. Directory path: {directory_path}")

    def handle_encryption_keys(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling Encryption Keys Button
        self.console_widget_textedit.appendPlainText(f"Encryption Keys Button clicked. Directory path: {directory_path}")

    def handle_auth_files(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling Auth Files Button
        self.console_widget_textedit.appendPlainText(f"Auth Files Button clicked. Directory path: {directory_path}")

    def scan_files_folders(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling Encryption Keys Button
        self.console_widget_textedit.appendPlainText(f"Encryption Keys Button clicked. Directory path: {directory_path}")
        button = self.ui.get_log_stats_button

        file_count = 0
        folder_count = 0
        cookie_count = 0
        new_text_document_count = 0
        passwords_count = 0
        profile_1_count = 0
        dat_count = 0
        compressed_count = 0  # Initialize the count for compressed files
        
        directory_path = self.directory_path_text_element.toPlainText()
        
        if not directory_path:
            self.console_widget_textedit.appendPlainText("Error: No directory path provided.\n\n")
            return

        for root, dirs, files in os.walk(directory_path):
            folder_count += len(dirs)
            file_count += len(files)
            cookie_count += sum(file.endswith(".txt") for file in files)
            new_text_document_count += sum(file.endswith(".txt") and not file.startswith("cookies") for file in files)
            passwords_count += sum(file == "Passwords.txt" for file in files)
            profile_1_count += sum(file == "Profile_1" for file in files)
            dat_count += sum(file.endswith(".dat") for file in files)
            compressed_count += sum(zipfile.is_zipfile(os.path.join(root, file)) for file in files)  # Increment the compressed count for each ZIP file

        result = f"Number of Folders: {folder_count}\nNumber of Files: {file_count}\nNumber of Cookies: {cookie_count}\nNumber of New Text Documents: {new_text_document_count}\nNumber of Passwords.txt: {passwords_count}\nNumber of Profile_1: {profile_1_count}\nNumber of .dat files: {dat_count}\nNumber of Compressed Files: {compressed_count}\n"
        
        self.console_widget_textedit.appendPlainText(result)

    def handle_newtextdocuments(self):
        try:
            directory_path = self.set_directory_path_element.toPlainText()
            if directory_path:
                count = 0
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        if file == "New Text Document.txt":
                            count += 1
    
                message = f"Found {count} occurrences of 'New Text Document.txt'"
            else:
                # Show an error message informing the user to enter a directory path
                error_message = "Please enter a directory path."
                self.console_widget_textedit.appendPlainText(error_message + '\n')
        except Exception as e:
            error_message = "An error occurred: " + str(e)
            self.console_widget_textedit.appendPlainText(error_message + '\n')
        
    def handle_file_count_finished(self, count):
        message = f"Found {count} occurrences of 'New Text Document.txt'"
        self.lcdNumber_4.display(count)

        # Start the timer to update the value of lcdNumber_4 every 5 seconds
        self.timer.start(5000)

    def handle_discord_files(self):
        # Functionality for handling Discord Files button
        print("Discord Files button clicked")

    def handle_telegram_folders(self):
        directory_path = self.set_directory_path_element.toPlainText()
        # Functionality for handling Telegram Folder Sorting Button
        choice = self.ask_user_dialog_box("Copy or Move?")  # Replace this with your actual dialog box implementation
        if choice == "Copy" or choice == "Move":
            folders_to_sort = ["Profile_1", "Telegram", "Tdata"]
            num_folders_found = 0
            for folder_name in folders_to_sort:
                folder_path = os.path.join(directory_path, folder_name)
                if os.path.exists(folder_path):
                    destination_folder = os.path.join(directory_path, "saved_results", folder_name)
                    if choice == "Copy":
                        shutil.copytree(folder_path, destination_folder)
                    elif choice == "Move":
                        shutil.move(folder_path, destination_folder)
                    num_folders_found += 1

            self.console_widget_textedit.appendPlainText(f"Found {num_folders_found} folders while crawling.")
        else:
            self.console_widget_textedit.appendPlainText("Invalid choice!")

        self.savedResultsTextBox.setText(directory_path)
        self.console_widget_textedit.appendPlainText(f"Telegram Folder Sorting Button clicked. Directory path: {directory_path}")

    def launch_domain_manager(self):
        subprocess.Popen(["python", "domain_sorter.py"])
        
    def launch_url_manager(self):
        subprocess.Popen(["python", "url_tools.py"])
        
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
    
            output_text = "\n".join(filtered_lines)
            self.output_text.setPlainText(output_text)
            removed_data_text = "\n".join(removed_lines)
            self.removed_data_text.setPlainText(removed_data_text)
    
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

    def open_chat(self):
        script_path = os.path.join(get_current_working_dir(), "DiamondSorter_Chat", "main.py")
        subprocess.Popen(["python", script_path])
        
    def log_hunter_function(self):
        script_path = os.path.join(get_current_working_dir(), "ui_files", "Ui_logs_window.py")
        subprocess.Popen(["python", script_path])

    def open_configs_ui(self):
        script_path = os.path.join(get_current_working_dir(), 'config_developer.py')
        subprocess.Popen(['python', script_path])

    def open_email_sorter(self):
        try:
            import urh
        except ModuleNotFoundError:
            error_dialog = QMessageBox(self)
            error_dialog.setWindowTitle("Module Not Found")
            error_dialog.setText("The 'urh' module is not installed.")
            error_dialog.setInformativeText("Please run the following command in the console:\n\npython -m pip install urh")
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.exec_()
            return
    
        script_path = os.path.join(get_current_working_dir(), 'email_sorter.py')
        subprocess.Popen(['python', script_path])

    def open_cookies_ui(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Choose an Option")
        
        layout = QHBoxLayout()
        
        evaluation_button = QPushButton("Evaluation", dialog)
        sorting_button = QPushButton("Sorting", dialog)
        checking_button = QPushButton("Checking", dialog)
        
        layout.addWidget(evaluation_button)
        layout.addWidget(sorting_button)
        layout.addWidget(checking_button)
        
        dialog.setLayout(layout)
        
        checking_button.clicked.connect(self.perform_checking)

        dialog.exec_()

    def perform_checking(self):
        # Perform the desired actions when the "Checking" button is clicked
        script_path = os.path.join(get_current_working_dir(), "DiamondChecker", "main.py")
        subprocess.Popen(["python", script_path])
        obj.open_cookies_ui()

    def create_username_list_button_clicked(self):
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
                
                removed_data_text = re.sub(rf'(?<!\w){re.escape(text_without_punctuation)}(?!\w)', '', text)
                removed_data_text.append(removed_data_text)
                
                output_text.clear()
                output_text.setPlainText(text_without_punctuation)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        
    def remove_domains(self):
        """Remove domains from the input_text widget."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
            if input_text is not None and output_text is not None:
                text = input_text.toPlainText()
    
                # Remove domains and store removed domains
                lines = text.split('\n')
                new_lines = []
                removed_domains = []
    
                for line in lines:
                    # Find the @ symbol before the : separator
                    separator_index = line.find(':')
                    if separator_index != -1:
                        at_index = line.find('@', 0, separator_index)
                        if at_index != -1:
                            domain = line[at_index:separator_index]
                            line = line.replace(domain, '')
                            removed_domains.append(domain)
                    
                    new_lines.append(line)
    
                text_without_domains = '\n'.join(new_lines)
    
                output_text.clear()
                output_text.setPlainText(text_without_domains)
    
                removed_data_text.clear()
                removed_data_text.setPlainText('\n'.join(removed_domains))
    
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
            removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
    
            if input_text is not None and output_text is not None and removed_data_text is not None:
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
    
                        removed_data_text.clear()  # Clear the previous removed_data_text
                        removed_data_text.setPlainText("\n".join(removed_characters))
    
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

                # Override the text options to prevent editing but allow highlighting
                text_edit_options = input_text.document().defaultTextOption()
                text_edit_options.setFlags(text_edit_options.flags() | Qt.TextEditable)
                input_text.document().setDefaultTextOption(text_edit_options)

    
                # Show the statistics message with selectable text
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Statistics")
                msg_box.setText(stats_message)
                msg_box.setTextInteractionFlags(Qt.TextSelectableByMouse)

                msg_box.exec_()
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
                    removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name

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
                    removed_data_text = "\n".join(removed_data)
    
                    self.output_text.setPlainText(output_text)
                    self.removed_data_text.setPlainText(removed_data_text)
    
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

    def start_sorting(self):
        # Functionality for the Start Sorting button in the General Combo Options tab
        pass

    def password_sorting(self):
        # Functionality for the Start Sorting button in the Password Log Formats tab
        
        # Prompt the user to select the preferred sorting criteria
        sorting_criteria = input("Please enter your preferred sorting criteria (Size, Lines, or Geo): ")
        
        # Get the directory path from the text element
        directory_path = self.Directory_Path_Text_Element.toPlainText()
        
        # Proceed with crawling and sorting Passwords.txt files based on the selected criteria
        if sorting_criteria == "Size":
            # Sort by file size
            # Implement the sorting logic here
            pass
        elif sorting_criteria == "Lines":
            # Sort by the number of lines
            # Implement the sorting logic here
            pass
        elif sorting_criteria == "Geo":
            # Sort by geographic location
            # Implement the sorting logic here
            pass
        else:
            print("Invalid sorting criteria entered. Please try again.")

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
                        sorted_lines = sorted(lines, key=lambda x: [int(t) if t.isdigit() else t for t in re.split('(\\d+)', x)])
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
        directory_path = self.set_directory_path_element.toPlainText()  # Get the directory path from Directory_Path_Text_Element
        
        if not os.path.isdir(directory_path):
            QMessageBox.warning(self, "Error", "\nInvalid directory path. Please select a valid directory.\n")
            self.open_directory_dialog()  # Call the method to open the directory dialog
            return
        
        output_text = ""
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with codecs.open(file_path, "r", encoding="utf-8", errors="ignore") as input_file:
                        for line in input_file:
                            if line.strip():  # Check if the line is not empty
                                match = re.findall(r"Email: (.*), Pass: (.*)", line)
                                if match:
                                    email, password = match[0]
                                    output_line = f"{email}:{password}"
                                    output_text += output_line
        
        # Show the results in the output_text
        self.output_text.setPlainText(output_text)
        
        # Save the results to savedResultsTextBox
        self.savedResultsTextBox.setText(output_text)
        
        # Create folder "Diamond Sorter" if it doesn't exist
        diamond_sorter_folder = os.path.join(os.path.expanduser("~"), "Diamond Sorter")
        if not os.path.exists(diamond_sorter_folder):
            os.makedirs(diamond_sorter_folder)
        
        # Create subfolder "Sorted" if it doesn't exist
        sorted_folder = os.path.join(diamond_sorter_folder, "Sorted")
        if not os.path.exists(sorted_folder):
            os.makedirs(sorted_folder)
        
        # Optional: Show a message box to indicate the operation is complete
        QMessageBox.information(self, "Email:Password", "Email:Password pairs have been combined and displayed successfully.")
    
    def username_password(self):
        try:
            directory_path = self.set_directory_path_element.toPlainText()
            saved_results_path = self.savedResultsTextBox.toPlainText()
    
            output_text = ""
            removed_data = ""
    
            sorted_logs_path = os.path.join(saved_results_path, "Sorted Logs")
            created_resources_path = os.path.join(saved_results_path, "Created Resources")
    
            os.makedirs(sorted_logs_path, exist_ok=True)
            os.makedirs(created_resources_path, exist_ok=True)
    
            current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            current_date_folder = os.path.join(created_resources_path, current_date)
            os.makedirs(current_date_folder, exist_ok=True)
    
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r") as input_file:
                            for line in input_file:
                                if "Email:" in line:
                                    email = line.split("Email:")[1].strip()
                                    output_text += line
                                else:
                                    removed_data += line
    
            self.output_text.insertPlainText(output_text)
            self.removed_data_text.insertPlainText(removed_data)
    
            filename = f"{current_date}.User.Pass.{output_text.count('')}.txt"
            save_path = os.path.join(current_date_folder, filename)
            with open(save_path, "w") as output_file:
                output_file.write(output_text)
    
            console_widget = self.findChild(QPlainTextEdit, "console_widget_textedit")
            if console_widget is not None:
                console_widget.insertPlainText("Email:Password pairs have been combined and displayed successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        
        
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
                                    output_line = f"{email}:{password}"
                                    output_text += output_line
    
        # Show the results in the output_text
        self.output_text.setPlainText(output_text)
    
        # Optional: Show a message box to indicate the operation is complete
        QMessageBox.information(self, "Email:Password\n", "Email:Password pairs have been combined and displayed successfully.") 

    def copy_from_output():
        """Copy content from output_text widget to clipboard."""
        output_content = output_text.get(1.0, tk.END)
        root.clipboard_clear()
        root.clipboard_append(output_content)

    def extract_phone_numbers_button_clicked(self):
        input_text = self.input_text.toPlainText()
        phone_number_pattern = r'\b(?:\+\d{1,3}\s?)?(?:\(\d{1,3}\)\s?)?(?:\d{1,4}[\s-]?\d{1,4}[\s-]?\d{1,9})\b'
        
        phone_numbers = re.findall(phone_number_pattern, input_text)
        self.output_text.setPlainText('\n'.join(phone_numbers))
        
        lines = input_text.split('\n')
        removed_lines = [line for line in lines if not any(re.findall(phone_number_pattern, line))]
        self.removed_data_text.setPlainText('\n'.join(removed_lines))

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
    
                        # Store removed text in removed_data_text object
                        removed_data_text = central_widget.findChild(QtWidgets.QTextEdit, "removed_data_text")  # Replace "removed_data_text" with the actual object name
                        if removed_data_text is not None:
                            removed_lines = list(set(lines) - set(unique_lines))
                            removed_data_text.clear()
                            removed_data_text.setPlainText("\n".join(removed_lines))
    
                        # Print result function in console_widget_textedit
                        console_widget_textedit = central_widget.findChild(QtWidgets.QTextEdit, "console_widget_textedit")  # Replace "console_widget_textedit" with the actual object name
                        if console_widget_textedit is not None:
                            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            console_widget_textedit.appendPlainText(f"[{timestamp}] extract_phone_numbers_button_clicked function called.")
                            console_widget_textedit.appendPlainText(f"[{timestamp}] Removed {len(lines) - len(phone_numbers)} duplicate lines.")
                            console_widget_textedit.appendPlainText(f"[{timestamp}] Stored removed lines in removed_data_text object.")
        except Exception as e:
            print(f"An error occurred: {e}")

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
            input_text = self.findChild(QTextBrowser, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextBrowser, "output_text")  # Replace "output_text" with the actual object name
            removed_data_text = self.findChild(QTextBrowser, "removed_data_text")  # Replace "removed_data_text" with the actual object name
            
            if input_text is not None and output_text is not None and removed_data_text is not None:
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
                
                removed_data_text.clear()
                removed_data_text.setPlainText("\n".join(removed_data))
        
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_results(output, console_widget_textedit):
        console_widget_textedit.append(output)

    def extract_ip_variable(directory_path):
        user_info_file = os.path.join(directory_path, "UserInformation.txt")
        ip_variable = "{IP}"  # Variable to extract
    
        if os.path.exists(user_info_file):
            with open(user_info_file, "r") as file:
                for line in file:
                    if line.startswith("IP:"):
                        ip = line.strip().split(":")[1].strip()
                        return ip
    
        return None

    def parse_button_function(self):
        format_text = self.format_request_textedit.toPlainText()  # Get input text from format_request_textedit
        directory_path = self.file_directory_path_path.toPlainText()  # Get the directory path from file_directory_path_path
        variables_chosen = f"=====================\n\nEntered Data\n\n=====================\n{format_text}"
        results_path = self.savedResultsTextBox.toPlainText()  # Get the saving results path from savedResultsTextBox
        format_capture = f"Capture Format:\n{format_text}"
        results_path_text = f"\n\nSaving Results to Path: {results_path}"
        self.console_widget_textedit.setPlainText(f"Crawling From:{directory_path}{results_path_text}\n{format_capture}\n{variables_chosen}\n")
    
        if not os.path.isdir(directory_path):
            QMessageBox.warning(self, "Error", "Invalid directory path. Please select a valid directory.")
            self.open_directory_dialog()  # Call the method to open the directory dialog
            return
    
        try:
            print("Directory path:", directory_path)  # Add this line to print the directory path
            status = "Parsing completed."
            extracted_variables = {}
    
            # Extract variables
            ip_variable = "{IP}"
            extracted_variables = {}
    
            # Extract variables
            extracted_variables["IP"] = ip_variable
    
            for variable in ["CC", "CVC"]:
                value = self.extract_autofill_variable(directory_path, variable)
                if value:
                    extracted_variables[variable] = value
    
            # Define additional variables
            extracted_variables["FULLZ"] = "{FULLZ}"
            extracted_variables["MM"] = "{MM}"
            extracted_variables["YY"] = "{YY}"
            extracted_variables["?"] = "{?}"
            extracted_variables["A"] = "{A}"
            extracted_variables["$"] = "{$}"
    
            # Process variables
            processed_output = self.process_variables(format_text, extracted_variables)
    
            # Display results
            output = f"Results:\n{processed_output}\n\nStatus: {status}"
            self.display_results(output)
        except AttributeError:
            error_message = "Error: Invalid directory path!"
            QMessageBox.critical(self, "Error", error_message, QMessageBox.Ok)

    def extract_autofill_variable(self, directory_path, variable):
        autofills_folder = os.path.join(directory_path, "Autofills")
        variable_names = {
            "CC": ["ccName", "cardNumber", "Card", "card-number", "ccnumber", "cc"],
            "CVC": ["cvc", "cvv", "securityCode"],
        }
        value = None
    
        if os.path.exists(autofills_folder):
            for file_name in os.listdir(autofills_folder):
                file_path = os.path.join(autofills_folder, file_name)
                with open(file_path, "r") as file:
                    content = file.read()
    
                    for name in variable_names.get(variable, []):
                        pattern = r"Name:\s*{}\s*.*?Value:\s*(.+)".format(name)
                        match = re.search(pattern, content, re.IGNORECASE)
                        if match:
                            value = match.group(1)
                            break
    
                if value:
                    break
    
        return value

    def process_variables(self, format_text, variables):
        result = format_text
    
        for variable, value in variables.items():
            result = result.replace("{" + variable + "}", str(value))
    
        return result

class ExtensionsBarQDockWidget(QDockWidget):
    def __init__(self):
        super(ExtensionsBarQDockWidget, self).__init__()

        # Create the container widget
        self.widget_container = QWidget()

        # Create buttons for each extension
        self.widget_button_urltools = QPushButton("URL Tools")
        self.widget_button_requests = QPushButton("Request")
        self.widget_button_cookies = QPushButton("Cookies")
        self.widget_button_email_sorter = QPushButton("Email Domain Sorter")
        self.widget_button_configs = QPushButton("CFGs")
        self.widget_button_loghunter = QPushButton("Log Hunter")
        self.widget_button_chat = QPushButton("Chat")

        # Connect button signals to slots
        self.widget_button_requests.clicked.connect(self.launch_requests_ui)
        self.widget_button_cookies.clicked.connect(self.launch_cookies_ui)
        self.widget_button_configs.clicked.connect(self.launch_configs_ui)
        self.widget_button_email_sorter.clicked.connect(self.open_domain_sorter)
        self.widget_button_chat.clicked.connect(self.open_chat)
        
        # Set the container widget as the content of the dock widget
        self.setWidget(self.widget_container)

    def launch_ui_from_subdirectory(self, ui_filename):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        ui_path = os.path.join(script_dir, "ui_files", ui_filename)
        os.system(f"python {ui_path}")

    def launch_requests_ui(self):
        self.launch_ui_from_subdirectory("requests.ui")

    def launch_cookies_ui(self):
        subdirectory = os.path.join("DiamondChecker", "main.py")
        subprocess.Popen(["python", subdirectory])

    def launch_configs_ui(self):
        self.launch_ui_from_subdirectory("configs.ui")

    def launch_domain_manager(self):
        script_path = os.path.join("ui_files", "url_tools.py")
        
    def open_domain_sorter(self):
        script_path = os.path.join("ui_files", "domain_sorter.py")
        if os.path.isfile(script_path):
            subprocess.Popen(["python", script_path])

    def open_chat(self):
        pass

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

    def process_and_copy(self, directory_path):
        domains = self.get_selected_domains()
        if domains:
            directory = self.set_directory_path_element.toPlainText()
            console_result = scan_files_folders(directory)
            top_extensions = get_top_file_extensions(directory, n=3)
            console_result += "\n\nTop 3 File Extensions:\n"
            for extension, count in top_extensions:
                console_result += f"\033[94mExtension:\033[0m {extension} \033[94m|\033[0m \033[94mCount:\033[0m {count}\n"
            self.console_widget_textedit.setPlainText(console_result)
            self.copy_files(domains, directory_path)
        else:
            QMessageBox.warning(self, "No Domains Selected", "Please select at least one domain.")








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiamondSorter()
    window.show()
    sys.exit(app.exec_())
    