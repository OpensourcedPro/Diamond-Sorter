import json
import os
import re
import random
import string
import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QUrl, Qt, QProcess, QTimer, QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QLCDNumber, QMainWindow, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout
import hashlib
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices, QColor, QTextCharFormat
import binascii
import json as jsond
import platform
import subprocess
import time
from datetime import datetime
from time import sleep
import shutil
import modules.general_tab
from multiprocessing import Process, Queue
from PyQt5.QtCore import QRunnable, QObject, pyqtSignal
from modules import general_tab, password_log_formats, sorting_files_tab, sorting_cookies_tab
from general_tab import remove_ending_punctuation
import sorting_files_tab

#Gunction for handling the Scrape Security Data button click
def handle_scrape_security_data_button_click():
    sorting_files_tab.handle_scrape_security_data()



def handle_command_link():
    directory_path = self.set_directory_path_element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Command Link/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the command link process and save the results in the specified directory
        # Add your code here to perform the command link process and save the results

        print("Command Link process completed.")
    else:
        print("Invalid directory path.")


def handle_telegram_folders(loaded_directory):
    if not os.path.isdir(loaded_directory):
        print("Invalid directory path.")
        return

    # Define the subfolder names to search for
    subfolder_names = ["Tdata", "Profile_1"]

    # Create the new folder name
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    new_folder_name = f"Diamond Sorter Results/Telegram Folders/{timestamp}"

    # Create the saved directory path
    saved_directory = os.path.join(loaded_directory, new_folder_name)
    os.makedirs(saved_directory)

    # Crawl the loaded directory and search for subfolders
    for root, dirs, files in os.walk(loaded_directory):
        for dir_name in dirs:
            if dir_name in subfolder_names:
                # Get the full path of the subfolder
                subfolder_path = os.path.join(root, dir_name)
                # Copy the subfolder and its contents to the saved directory path
                shutil.copytree(subfolder_path, os.path.join(saved_directory, dir_name))

    print("Telegram Folders sorting completed.")


def handle_authy_desktop(loaded_directory):
    if not os.path.isdir(loaded_directory):
        print("Invalid directory path.")
        return

    # Define the folder name to search for
    folder_name = "Authy"

    # Create the new folder name
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    new_folder_name = f"Diamond Sorter Results/Authy Desktop/{timestamp}"

    # Create the saved directory path
    saved_directory = os.path.join(loaded_directory, new_folder_name)
    os.makedirs(saved_directory)

    # Crawl the loaded directory and search for the specified folder
    for root, dirs, files in os.walk(loaded_directory):
        for dir_name in dirs:
            if dir_name == folder_name:
                # Get the full path of the folder
                folder_path = os.path.join(root, dir_name)
                # Copy the folder and its contents to the saved directory path
                shutil.copytree(folder_path, os.path.join(saved_directory, dir_name))

    print("Authy Desktop folder sorting completed.")

def handle_desktop_wallet():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Desktop Wallet/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Desktop Wallet process and save the results in the specified directory
        # Add your code here to perform the Desktop Wallet process and save the results

        print("Desktop Wallet process completed.")
    else:
        print("Invalid directory path.")

def handle_browser_2fa_extension():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Browser 2FA Extension/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Browser 2FA Extension process and save the results in the specified directory
        # Add your code here to perform the Browser 2FA Extension process and save the results

        print("Browser 2FA Extension process completed.")
    else:
        print("Invalid directory path.")


def handle_text_named_sorting():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Text Named Sorting/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Text Named Sorting process and save the results in the specified directory
        # Add your code here to perform the Text Named Sorting process and save the results

        print("Text Named Sorting process completed.")
    else:
        print("Invalid directory path.")


def handle_pgp():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/PGP/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the PGP process and save the results in the specified directory
        # Add your code here to perform the PGP process and save the results

        print("PGP process completed.")
    else:
        print("Invalid directory path.")


def handle_encryption_keys():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Encryption Keys/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Encryption Keys process and save the results in the specified directory
        # Add your code here to perform the Encryption Keys process and save the results

        print("Encryption Keys process completed.")
    else:
        print("Invalid directory path.")

def handle_sort_by_cookies(self, event):
    # Ask the user what they would like to do
    choice = input("What would you like to do?\n 1. Search Cookies by Domain\n2. Search Cookies by Values\nEnter your choice: ")

    if choice == "1":
        self.search_cookies_by_domain()
    elif choice == "2":
        self.search_cookies_by_values()
    else:
        print("Invalid choice.")

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

# Implement the remaining functions in the same way
    
def handle_newtextdocuments(console_widget, directory_path):
    try:
        if directory_path:
            # Create a new folder to save the results
            now = datetime.now()
            timestamp = now.strftime("%Y%m%d%H%M%S")
            new_folder_name = f"Diamond Sorter Results/New Text Documents/{timestamp}"
            save_directory = os.path.join(directory_path, new_folder_name)
            os.makedirs(save_directory)

            # Perform the New Text Documents process and save the results in the specified directory
            # Add your code here to perform the New Text Documents process and save the results
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file == "New Text Document.txt":
                        # Display the directory path in the console_widget in green
                        console_widget.appendPlainText("\033[92m" + root)
                    else:
                        # Display the directory path in the console_widget
                        console_widget.appendPlainText(root)
        else:
            print("Invalid directory path.")
    except Exception as e:
        error_message = "An error occurred: " + str(e)
        console_widget.appendPlainText(error_message)




def handle_chrome_extensions():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Chrome Extensions/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Chrome Extensions process and save the results in the specified directory
        # Add your code here to perform the Chrome Extensions process and save the results

        print("Chrome Extensions process completed.")
    else:
        print("Invalid directory path.")


def handle_scrape_backup_codes():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Scrape Backup Codes/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Scrape Backup Codes process and save the results in the specified directory
        # Add your code here to perform the Scrape Backup Codes process and save the results

        print("Scrape Backup Codes process completed.")
    else:
        print("Invalid directory path.")


def handle_text_named_sorting():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Text Named Sorting/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Text Named Sorting process and save the results in the specified directory
        # Add your code here to perform the Text Named Sorting process and save the results

        print("Text Named Sorting process completed.")
    else:
        print("Invalid directory path.")


def handle_pgp():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/PGP/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the PGP process and save the results in the specified directory
        # Add your code here to perform the PGP process and save the results

        print("PGP process completed.")
    else:
        print("Invalid directory path.")


def handle_encryption_keys():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Encryption Keys/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Encryption Keys process and save the results in the specified directory
        # Add your code here to perform the Encryption Keys process and save the results

        print("Encryption Keys process completed.")
    else:
        print("Invalid directory path.")


def handle_discord_files():
    directory_path = self.Directory_Path_Text_Element.toPlainText()
    if directory_path:
        # Create a new folder to save the results
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"Diamond Sorter Results/Discord Files/{timestamp}"
        save_directory = os.path.join(directory_path, new_folder_name)
        os.makedirs(save_directory)

        # Perform the Discord Files process and save the results in the specified directory
        # Add your code here to perform the Discord Files process and save the results

        print("Discord Files process completed.")
    else:
        print("Invalid directory path.")


def handle_file_count_finished(self, count):
    message = f"Found {count} occurrences of 'New Text Document.txt'"
    self.console_widget.appendPlainText(message + '\n')
    self.lcdNumber_4.display(count)

    # Start the timer to update the value of lcdNumber_4 every 5 seconds
    self.timer.start(5000)

def launch_domain_manager(self):
    subprocess.Popen(["python", "domain_sorter.py"])

def replace_with_listButton():
    repeating_string = input("Enter the repeating string or value: ")
    lines = input("Copy and paste the list of lines: ").splitlines()

    for line in lines:
        replaced_line = line.replace(repeating_string, line)
        print(replaced_line)

