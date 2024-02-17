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
from PyQt5.QtGui import QDesktopServices


import binascii  # hex encoding
import json as jsond  # json
import platform  # check platform
import subprocess  # needed for mac device
import time  # sleep before exit
from datetime import datetime
from time import sleep
import shutil
from multiprocessing import Process, Queue
from PyQt5.QtCore import QRunnable, QObject, pyqtSignal




class Sender(QObject):
    mySignal = pyqtSignal(int)

    def sendData(self, data):
        self.mySignal.emit(data)

class Receiver(QObject):
    @pyqtSlot(int)
    def receiveData(self, data):
        print(f"Received data: {data}")

sender = Sender()
receiver = Receiver()

# Connect the signal from the sender to the slot in the receiver
sender.mySignal.connect(receiver.receiveData)

# Emit the signal from the sender
sender.sendData(10)





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
        uic.loadUi(r'ui_files\cookies_window.py', self)
        # Add any additional setup for the new window here


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

        set_directory_path_button.clicked.connect(self.open_directory_dialog)
        save_results_action_button.clicked.connect(self.open_save_directory_dialog)
        import_requests_button.clicked.connect(self.import_requests_dialog)

    def open_directory_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            selected_directory = dialog.selectedFiles()[0]
            self.set_directory_path_element.setPlainText(selected_directory)

    def handle_scrape_banking_data(self):
        # Get the directory path from the specified file directory
        directory_path = self.set_directory_path_element.toPlainText()

    def update_line_count(self):
        """Update the line count in the UI."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            total_lines_number = self.findChild(QLCDNumber, "totalLinesNumber")  # Replace "totalLinesNumber" with the actual object name

            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None:
                input_lines = len(input_text.toPlainText().split("\n"))
                output_lines = len(output_text.toPlainText().split("\n"))
        except Exception as e:
            print(f"An error occurred: {e}")

    def import_requests(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # Set the file mode to ExistingFile
        file_dialog.setNameFilter("Text Files (*.txt)")  # Set the file filter for text files
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]  # Get the selected file path
            with open(file_path, 'r') as file:
                text = file.read()
                self.input_text.setText(text)

def launch_insomnia():
    message_box = QtWidgets.QMessageBox()
    message_box.setText("You are about to launch Insomnia. Continue?")
    message_box.setWindowTitle("Diamond Sorter - Window")
    message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    message_box.setDefaultButton(QtWidgets.QMessageBox.Yes)

    result = message_box.exec_()
    if result == QtWidgets.QMessageBox.Yes:
        insomnia_path = r'refrences\Insomnia.exe'  # Replace with the actual path to Insomnia.exe
        subprocess.Popen(insomnia_path)

class DiamondSorter(QtWidgets.QMainWindow):
    finished = pyqtSignal(int)
    def __init__(self):
        super(DiamondSorter, self).__init__()
        uic.loadUi(r'ui_files\form.ui', self)
        self.queue = queue
        self.result = None
        self.queue = queue
        self.process = MyProcess(self.queue)
        self.process.start()
        self.console_layout = QVBoxLayout(self.consolewidget)
        self.console_layout.addWidget(self.consolewidget)
        self.set_directory_path_element = QtWidgets.QTextEdit()
        self.setup_buttons()
        self.recent_directories = []
        redline_file_structure_text_browser = "Redline / Meta"
        racoon_file_structure_text_browser = "Racoon Stealer"
        whitesnake_file_structure_text_browser = "Whitesnake"
        worldwind_file_structure_text_browser = "Worldwind / Prynt"
        self.set_directory_path_button.clicked.connect(self.open_directory_dialog)
        self.save_results_action_button.clicked.connect(self.open_save_directory_dialog)
        self.app = QApplication.instance()  # Get the instance of the QApplication
        self.input_text = self.findChild(QTextEdit, "input_text")
        self.output_text = self.findChild(QTextEdit, "output_text")
        self.removed_data_text = self.findChild(QTextBrowser, "removed_data_text")
        self.tabWidget.currentChanged.connect(self.tab_changed) # Connect the currentIndexChanged signal of tabWidget to a slot
        self.enable_wordwrap_checkbox = self.findChild(QCheckBox, "enable_wordwrap_checkbox")  # Replace "enable_wordwrap_checkbox" with the actual object name
        self.enable_wordwrap_checkbox.stateChanged.connect(self.toggle_word_wrap)
        self.enable_remove_empty_lines_checkbox = self.findChild(QCheckBox, "remove_empty_lines_checkbox")
        self.layout = QVBoxLayout()  # Define layout as an instance variable
        self.actionLaunch_Browser.triggered.connect(self.open_browser)
        self.actionInsomnia_HTTP_Client.triggered.connect(launch_insomnia)
        self.remove_trash_button = self.findChild(QPushButton, "remove_trash_button")
        if self.remove_trash_button is not None:
            self.remove_trash_button.clicked.connect(self.remove_trash_button_clicked)
        self.display_function("MyFunction")
        self.import_requests_button = QPushButton("Import Requests")
        self.button = QtWidgets.QPushButton("Process Directory")
        self.extract_phone_number_button = QtWidgets.QPushButton("Extract Phone Numbers")
        self.extract_phone_number_button.clicked.connect(self.perform_extract_phone_number)
        self.button.clicked.connect(self.handle_newtextdocuments)
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.tabWidget.currentChanged.connect(self.tab_changed) 
        self.extract_ip_addressButton = QPushButton("Extract IP")
        self.extract_ip_addressButton.clicked.connect(self.extract_ip_addresses)  # Connect to the class method
        self.lcd_number_2 = self.findChild(QLCDNumber, "lcdNumber_2")
        self.input_text.textChanged.connect(self.process_input_text)
        self.timer = QTimer(self)
        self.timer.setInterval(500)  # Flashing interval in milliseconds
        self.timer.setSingleShot(True)  # Only trigger the timeout once
        self.timer.timeout.connect(self.flash_callback)  # Connect to the class method
        self.timer.start()

    def flash_callback(self):
        """Callback function for the QTimer timeout event."""
        self.totalLinesNumber.setSegmentStyle(QLCDNumber.Flat)
        self.totalLinesNumber.setDigitCount(4)
        self.totalLinesNumber.setMode(QLCDNumber.Dec)
        self.totalLinesNumber.setSegmentStyle(QLCDNumber.Flat)
        self.totalLinesNumber.setSegmentStyle(QLCDNumber.Flat)
        self.totalLinesNumber.setSegmentStyle(QLCDNumber.Flat)
        self.totalLinesNumber.display(9999)
        
        input_lines = len(self.input_text.toPlainText().split("\n"))
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_2.setDigitCount(4)
        self.lcdNumber_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_2.display(input_lines)
        
        output_lines = len(self.output_text.toPlainText().split("\n"))
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_3.setDigitCount(4)
        self.lcdNumber_3.setMode(QLCDNumber.Dec)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_3.display(output_lines)
        
        removed_lines = len(self.removed_data_text.toPlainText().split("\n"))
        self.lcdNumber_4.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_4.setDigitCount(4)
        self.lcdNumber_4.setMode(QLCDNumber.Dec)
        self.lcdNumber_4.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_4.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_4.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_4.display(removed_lines)
        
    def extract_ip_addresses(self):
        pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"  # Regular expression pattern for IP addresses
        ip_addresses = re.findall(pattern, self.input_text.toPlainText())  # Use self.input_text to get the text from the input_text QTextEdit
        ip_addresses.sort()  # Sort the extracted IP addresses
        self.output_text.setPlainText("\n".join(ip_addresses))

    def on_tab_switched(self, index):
        current_tab = self.tabWidget.tabText(index)
        notice = f"Switched to tab: {current_tab}"
        self.console_widget.appendPlainText(notice)






    def process_input_text(self):
        # Initialize the lcdNumber_2 widget
        lcd_number_2 = self.findChild(QLCDNumber, "lcdNumber_2")
        
        # Set the initial value to 9999
        lcd_number_2.display(9999)
        
        # Create a QTimer to control the flashing behavior
        timer = QTimer(self)
        timer.setInterval(500)  # Flashing interval in milliseconds
        timer.setSingleShot(True)  # Only trigger the timeout once
        
        # Define a callback function for the QTimer timeout
        def flash_callback():
            # Display 9999 for two flashes
            lcd_number_2.display(9999)
            QTimer.singleShot(500, lambda: lcd_number_2.display(0))
            QTimer.singleShot(1000, lambda: lcd_number_2.display(9999))
            QTimer.singleShot(1500, lambda: lcd_number_2.display(0))
        
        # Connect the QTimer timeout to the callback function
        timer.timeout.connect(flash_callback)
        
        # Start the QTimer
        timer.start()

    def totalLinesNumber(self, count):
        self.totalLinesNumber.display(count)
    def count_left_to_go(self, count):
        self.count_left_to_go.display(count)
    def count_already_ran(self, count):
        self.count_already_ran.display(count)
    def count_error_lines(self, count):
        self.count_error_lines.display(count)
        
    def handle_process_finished(self, result):
        print(result)
        # Update lcdNumber_1 with the result
        
    def run(self):
        my_function(self.queue, 1)



    def handle_newtextdocuments(self):
        try:
            directory_path = self.set_directory_path_element.toPlainText()
            if directory_path:
                queue = Queue()
                process = MyProcess(queue)
                process.start()
                process.join()
                result = queue.get()
                print(result)
            else:
                error_message = "Please enter a directory path."
                self.console_widget.appendPlainText(error_message + '\n')
        except Exception as e:
            error_message = "An error occurred: " + str(e)
            self.console_widget.appendPlainText(error_message + '\n')
            
            
            
            
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
            self.stealer_log_file_structure_path(self.queue, 1)
        
        
    def remove_trash_button_clicked(self):
        """Handle the button click event for remove_trash_button."""
        options = ["Remove Unknown", "Remove ****", "Remove Short", "Remove Simalar", "Option 5", "Option 6"]  # Replace with your specific options

        # Create the custom dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Remove Trash Options")  # Set the title of the dialog window

        layout = QGridLayout(dialog)  # Use QGridLayout for the layout

        checkboxes = []
        for i, option in enumerate(options):
            checkbox = QCheckBox(option)
            row = i // 3  # Calculate the row based on the index
            col = i % 3  # Calculate the column based on the index
            layout.addWidget(checkbox, row, col)  # Add the checkbox to the layout
            checkboxes.append(checkbox)

        # Add OK and Cancel buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons, row + 1, 0, 1, 3)  # Add the buttons to the layout
        
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
                # Handle Option 1 removal
                pass
            elif option == "Option 5":
                # Handle Option 2 removal
                pass
            elif option == "Option 6":
                # Handle Option 3 removal
                pass


    def update_output_text(self):
        output_text = self.password_format_tab.output_text.toPlainText()
        if self.remove_empty_lines_checkbox.isChecked():
            output_text = "\n".join(line for line in output_text.split("\n") if line.strip())
        self.password_format_tab.output_text.setPlainText(output_text)

    def open_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.set_directory_path_element_2.setText(directory)

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
            script_path = "browser.py"  # Path to the browser script
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



    def update_line_count(self):
        """Update the line count in the UI."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                input_lines = len(input_text.toPlainText().split("\n"))
                output_lines = len(output_text.toPlainText().split("\n"))
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
    
    
    def create_numberlist(self):
        """Create a list of number values that could be phone numbers."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
                number_list = []
                for line in lines:
                    numbers = re.findall(r"\d{3}-\d{3}-\d{4}", line)  # Assuming phone numbers are in the format XXX-XXX-XXXX
                    if numbers:
                        number_list.extend(numbers)
    
                output_text.clear()
                output_text.setPlainText("\n".join(number_list))
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
                self.set_directory_path_element.setText("New Directory Path")
            elif current_value == "Working from Input Requests":
                # Change the file directory path for Working from Input Requests
                self.set_directory_path_element.setText("New Input Requests Path")

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
        self.removeAfter_Tab_Space.clicked.connect(self.removeAfter_Tab_Space_clicked)
        self.sort_email_domainsButton = QPushButton("Sort Email Domains")
        self.sort_email_domainsButton.clicked.connect(self.sort_email_domains)

        self.sort_remove_similarButton.clicked.connect(self.sort_remove_similar)
        self.emailPasswordButton.clicked.connect(self.email_password)
        self.usernamePasswordButton.clicked.connect(self.username_password)
        self.newtextdocuments_button.clicked.connect(self.handle_newtextdocuments)

        self.widget_button_about.clicked.connect(self.open_about_ui)
        self.widget_button_configs.clicked.connect(self.open_configs_ui)
        self.widget_button_cookies.clicked.connect(self.open_cookies_ui)
        self.widget_button_url_tools.clicked.connect(self.open_url_tools)
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
        self.newtextdocuments_button.clicked.connect(self.handle_newtextdocuments)
        self.discord_sorting_button.clicked.connect(self.handle_discord_files)
        self.telegram_folder_sorting_button.clicked.connect(self.handle_telegram_folders)
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
        self.extract_phone_number_button = QtWidgets.QPushButton("Extract Phone Numbers")
        self.extract_phone_number_button.clicked.connect(self.perform_extract_phone_number)
    
        
    def removeAfter_Tab_Space_clicked(self):
        num_tabs, ok = QInputDialog.getInt(self, "Specify Number of Tab Spaces",
                                        "Enter the number of Tab Spaces to move after:")
    
        if ok:
            # Perform the desired action with the value entered by the user
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
            # User canceled the input dialog, handle it accordingly
            print("User canceled the input dialog")


    def perform_extract_phone_number(self):
        input_text = "..."  # Replace with your input text
        output_text = ""
        removed_data_text = ""
        
        # Code logic for extracting phone numbers
        extracted_numbers = extract_phone_number(input_text)
        cleaned_text, phone_numbers = extracted_numbers

        output_text = "\n".join(phone_numbers)
        removed_data_text = cleaned_text

        
    def extract_ip_address_clicked(self):
        # Define the regex pattern for IP address or IP:PORT address
        pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}(?::\d{1,5})?\b"
    
        # Extract lines that match the pattern
        lines = self.input_text.toPlainText().split('\n')
        extracted_lines = []
        removed_lines = []
    
        for line in lines:
            match = re.search(pattern, line)
            if match:
                extracted_lines.append(line)
            else:
                removed_lines.append(line)
    
        # Set the extracted and removed lines in the respective text widgets
        self.output_text.setPlainText('\n'.join(extracted_lines))
        self.removed_data_text.setPlainText('\n'.join(removed_lines))
    
    
    
    
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


    def handle_auth_files(self):
        # Functionality for handling Auth Files Button
        print("Auth Files Button clicked")

    def wordpress_finder(self):
        # Logic for the "Wordpress Finder" button
        pass
    
    def handle_scrape_keys(self):
        # Functionality for handling Scrape Keys button
        print("Scrape Keys button clicked")

    
    def server_information(self):
        # Logic for the "Server Information" button
        pass
    
    def cpanel_accounts(self, set_directory_path_element):
        try:
            directory_path = self.set_directory_path_element.toPlainText()
            if directory_path:
                # Define the regex pattern for Cpanel, WHM, and related port numbers
                pattern = r"\b(Cpanel|WHM|2083|2082|2086|3306|2096)\b"
    
                # Create a new folder for saving the results
                now = datetime.now()
                timestamp = now.strftime("%Y%m%d%H%M%S")
                new_folder_name = f"CpanelAccounts_{timestamp}"
                save_directory = os.path.join(directory_path, new_folder_name)
                os.makedirs(save_directory)
    
                # Crawl the specified directory path and search for matching files
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r') as f:
                            content = f.read()
                            if re.search(pattern, content):
                                shutil.copy2(file_path, save_directory)
    
                print("Cpanel accounts extraction completed.")
            else:
                print("Invalid directory path.")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def emails(self):
        # Logic for the "Emails" button
        pass
    
    def html_head(self):
        # Logic for the "<html><head/" button
        pass
    
    def checkmark(self):
        # Logic for the "✅" button
        pass
    
    def advertisements(self):
        # Logic for the "Advertisements" button
        pass
    
    def socials_forums(self):
        # Logic for the "Socials && Forums" button
        pass

    def update_lcdNumber(self):
        count = self.lcdNumber_4.intValue()
        self.lcdNumber_4.display(count)

    def handle_scrape_banking_data(self):
        # Get the directory path from the specified file directory
        directory_path = self.set_directory_path_element.toPlainText()
        
        # Get the stealer log format combo value
        stealer_log_format = self.stealer_log_format_combo.currentText()
        
    
        # Display the actions, results, and stats in the console widget
        self.console_widget.appendPlainText("Scrape Banking Data button clicked")
        self.console_widget.appendPlainText("Starting crawling from directory: " + directory_path)
        self.console_widget.appendPlainText("Stealer log format: " + stealer_log_format)
        
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
        # Add your stats displaying logic here
    def sort_passwords_textButton(self):
        # Get the specified directory path from the set_directory_path_element
        directory_path = self.set_directory_path_element.toPlainText()
        
        # Loop through all subdirectories in the specified directory
        for subdir, dirs, files in os.walk(directory_path):
            # Loop through all files in the current subdirectory
            for file in files:
                # Check if the current file is a passwords.txt file
                if file.lower() == "passwords.txt" or "Password List.txt" or "_AllPasswords_list.txt":
                    # Define the path to the current file
                    file_path = os.path.join(subdir, file)
                    # Open the current file for reading
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            # Read the contents of the file
                            contents = f.read()
                    except UnicodeDecodeError:
                        print(f"Error: Unable to read file {file_path}. Skipping...")
                        continue
                    # Split the contents of the file into individual password entries
                    entries = contents.split("===============\n")
                    # Loop through each password entry
                    for entry in entries:
                        # Split the entry into individual lines
                        lines = entry.strip().split("\n")
                        # Extract the URL, username, and password from the entry
                        url = ""
                        user = ""
                        password = ""
                        for line in lines:
                            if line.startswith("URL:") or line.startswith("url:") or line.startswith("Url:") or line.startswith("Host:") or line.startswith("HOSTNAME:"):
                                url = line.split(":", 1)[1].strip() if len(line.split(":")) > 1 else ""
                            elif line.startswith("USER:") or line.startswith("login:") or line.startswith("Login") or line.startswith("Username") or line.startswith("USER LOGIN:"):
                                user = line.split(":")[1].strip() if len(line.split(":")) > 1 else ""
                            elif line.startswith("PASS:") or line.startswith("password:") or line.startswith("Password") or line.startswith("USER PASSWORD"):
                                password = line.split(":")[1].strip() if len(line.split(":")) > 1 else ""
                        # Format the entry as "URL:USER:PASS"
                        if url:
                            if url.startswith("android"):
                                package_name = url.split("@")[-1]
                                package_name = package_name.replace("-", "").replace("_", "").replace(".", "")
                                package_name = ".".join(package_name.split("/")[::-1])
                                package_name = ".".join(package_name.split(".")[::-1])
                                url = f"{package_name}android.app"
                            else:
                                url_components = urlsplit(url)
                                url = f"{url_components.scheme}://{url_components.netloc}"
                            formatted_entry = f'"{url}":{user}:{password}\n'
                            # Open the output file for appending
                            with open(os.path.join(output_folder, output_file2, encoding='utf-8'), "a") as f:
                                # Write the formatted entry to the output file
                                f.write(formatted_entry)
        
    def handle_scrape_backup_codes(self):
        pattern = r"\b[A-Za-z0-9]{4,8}\b"  # Example regex pattern for 2FA codes, authentication codes, or PGP
    
        backup_codes = []
        lines = self.input_text.toPlainText().split('\n')
        
        for line in lines:
            matches = re.findall(pattern, line)
            backup_codes.extend(matches)
        
        self.output_text.setPlainText('\n'.join(backup_codes))
    
    def number_password(self):
        pattern = r"\b\d+:[^\s]+\b"
    
        lines = self.input_text.toPlainText().split('\n')
        extracted_combos = []
        removed_lines = []
    
        for line in lines:
            match = re.search(pattern, line)
            if match:
                extracted_combos.append(match.group())
            else:
                removed_lines.append(line)
    
        self.output_text.setPlainText('\n'.join(extracted_combos))
        self.removed_data_text.setPlainText('\n'.join(removed_lines))
    
    def business_emails(self):
        pattern = r"\b[A-Za-z0-9._%+-]+@(?!yahoo\.|gmail\.|hotmail\.|outlook\.|aol\.)(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b"
    
        lines = self.input_text.toPlainText().split('\n')
        extracted_emails = []
        removed_lines = []
    
        for line in lines:
            match = re.search(pattern, line)
            if match:
                extracted_emails.append(match.group())
            else:
                removed_lines.append(line)
    
        self.output_text.setPlainText('\n'.join(extracted_emails))
        self.removed_data_text.setPlainText('\n'.join(removed_lines))
        
    
    def gov_domains(self):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[gov]{2,}\b"
    
        lines = self.input_text.toPlainText().split('\n')
        extracted_domains = []
        removed_lines = []
    
        for line in lines:
            match = re.search(pattern, line)
            if match:
                extracted_domains.append(match.group())
            else:
                removed_lines.append(line)
    
        self.output_text.setPlainText('\n'.join(extracted_domains))
        self.removed_data_text.setPlainText('\n'.join(removed_lines))

    def member_id_pin(self):
        pattern = r"\b\d+:\d+\b"
    
        lines = self.input_text.toPlainText().split('\n')
        extracted_combos = []
        removed_lines = []
    
        for line in lines:
            match = re.search(pattern, line)
            if match:
                extracted_combos.append(match.group())
            else:
                removed_lines.append(line)
    
        self.output_text.setPlainText('\n'.join(extracted_combos))
        self.removed_data_text.setPlainText('\n'.join(removed_lines))
    
    def handle_scrape_security_data(self):
        print("Scrape Security Data button clicked")
        
    def handle_command_link(self):
        print("Command Link Button clicked")
    
    def handle_telegram_folders(self, loaded_directory):
        # Confirm the loaded file directory path
        if not os.path.isdir(loaded_directory):
            print("Invalid directory path.")
            return
    
        # Define the subfolder names to search for
        subfolder_names = ["Tdata", "Profile_1"]
    
        # Create the new folder name
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        new_folder_name = f"DS.{timestamp}.Telegram.Sorted"
    
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
    
        print("Folder sorting completed.")

        
    def handle_authy_desktop(self, loaded_directory):
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
        for root, dirs, files in os.walk(loaded_directory):
            for dir_name in dirs:
                if dir_name == folder_name:
                    # Get the full path of the folder
                    folder_path = os.path.join(root, dir_name)
                    # Copy the folder and its contents to the saved directory path
                    shutil.copytree(folder_path, os.path.join(saved_directory, dir_name))
    
        print("Authy Desktop folder sorting completed.")
    
    def handle_desktop_wallet(self):
        # Functionality for handling Telegram Folder Sorting Button
        print("Telegram Folder Sorting Button clicked")
    
        selected_directory = self.set_directory_path_element.toPlainText()  # Get the selected directory path
    
        # Display a confirmation dialog
        reply = QMessageBox.question(self, "Confirmation", f"Start crawling in the specified path?\n\n{selected_directory}",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # Implement the crawling logic using the selected_directory
            for root, dirs, files in os.walk(selected_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    print(file_path)  # Replace with your desired actions on each file
    
            # Example code to set the selected directory path to a QTextEdit widget
            self.set_directory_path_element.setPlainText(selected_directory)

    def handle_browser_2fa_extension(self):
        print("Browser 2FA Extension Button clicked")






    def handle_text_named_sorting(self):
        print("Text Named Sorting Button clicked")
    
    def handle_pgp(self):
        print("PGP Button clicked")
    
    def handle_encryption_keys(self):
        print("Encryption Keys Button clicked")

    def handle_sort_by_cookies(self):
        print("Sort by Cookies Button clicked")
        
    def handle_chrome_extensions(self):
        print("Chrome Extensions button clicked")
        
    def handle_scrape_backup_codes(self):
        # Functionality for handling Scrape Backup Codes button
        print("Scrape Backup Codes button clicked")

    def handle_text_named_sorting(self):
        # Functionality for handling Text Named Sorting Button
        print("Text Named Sorting Button clicked")

    def handle_pgp(self):
        # Functionality for handling PGP Button
        print("PGP Button clicked")

    def handle_encryption_keys(self):
        # Functionality for handling Encryption Keys Button
        print("Encryption Keys Button clicked")
        
    def handle_discord_files(self):
        # Functionality for handling Discord Files button
        print("Discord Files button clicked")
        
        
        
        
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
            removed_data_text = "\n".join(removed_lines)
    
            # Set the removed text in the removed_data_text widget
            self.removed_data_text.setPlainText(removed_data_text)
    
            print("Lines with", num_consecutive_chars, "consecutive similar characters removed.")
    

    def update_work_location_browser(self, index):
            # Hide all text browsers
        self.set_directory_path_element.hide()
        self.input_text.setEnabled(False)
    
        # Show the corresponding widget based on the selected index
        if index == 0:
            self.set_directory_path_element.show()
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
        elif index == 1:
            self.racoon_file_structure_text_browser.show()
        elif index == 2:
            self.titan_file_structure_text_browser.show()
        elif index == 3:
            self.whitesnake_file_structure_text_browser.show()
        elif index == 4:
            self.worldwind_file_structure_text_browser.show()

        # Call the display_function based on the selected index
        if index == 0:
            self.display_function("redline_file_structure_text_browser")
        elif index == 1:
            self.display_function("racoon_file_structure_text_browser")
        elif index == 2:
            self.display_function("titan_file_structure_text_browser")
        elif index == 3:
            self.display_function("whitesnake_file_structure_text_browser")
        elif index == 4:
            self.display_function("worldwind_file_structure_text_browser")


    def open_about_ui(self):
        about_dialog = QtWidgets.QDialog()
        uic.loadUi(r'ui_files\about.ui', about_dialog)
        about_dialog.exec_()

    def open_configs_ui(self):
        configs_dialog = QtWidgets.QDialog()
        uic.loadUi(r'ui_files\config_developer.ui', configs_dialog)
        configs_dialog.exec_()

    def open_cookies_ui(self):
        cookies_dialog = QtWidgets.QDialog()
        uic.loadUi(r'ui_files\cookies_window.ui', cookies_dialog)
        cookies_dialog.exec_()

    def open_url_tools(self):
        subprocess.Popen(['python', "url_tools.py"])

        
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
    
    # Implement the remaining functions in the same way
        
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
        
    def show_stats(self):
        """Show statistics about the input text."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            if input_text is not None:
                text = input_text.toPlainText()
                lines = text.split("\n")
    
                total_lines = len(lines)
                total_characters = sum(len(line) for line in lines)
                average_characters = total_characters / total_lines if total_lines > 0 else 0
    
                stats_message = f"Total Lines: {total_lines}\nTotal Characters: {total_characters}\nAverage Characters per Line: {average_characters:.2f}"
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

    def cleanup(self):
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
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                input_lines = len(input_text.toPlainText().split("\n"))
                output_lines = len(output_text.toPlainText().split("\n"))
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_line_count(self):
        """Update the line count in the UI."""
        try:
            input_text = self.findChild(QTextEdit, "input_text")  # Replace "input_text" with the actual object name
            output_text = self.findChild(QTextEdit, "output_text")  # Replace "output_text" with the actual object name
            if input_text is not None and output_text is not None:
                input_lines = len(input_text.toPlainText().split("\n"))
                output_lines = len(output_text.toPlainText().split("\n"))
        except Exception as e:
            print(f"An error occurred: {e}")


    def createpasswordlist(self):
        # This method will be called when the "create_password_list" button is clicked
        print("Create password list button clicked")
        # Add your code to create the password list here
    
    def create_numberlist(self):
        # This method will be called when the "create_number_list" button is clicked
        print("Create number list button clicked")
        # Add your code to create the number list here

    def email_password(self):
        # Functionality for the Email:Password button
        directory_path = self.set_directory_path_element.toPlainText()  # Get the directory path from set_directory_path_element
    
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
        directory_path = self.set_directory_path_element.toPlainText()  # Get the directory path from set_directory_path_element
    
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
        directory_path = self.savedResultsTextBox.toPlainText()  # Get the directory path from savedResultsTextBox
                    
        reply = QMessageBox()
        reply.setWindowTitle("Confirmation")
        reply.setText("This will start to export your Username:Password from\nThe specified Directory Path That you have listed above.")
        
        # Set button text
        file_button = reply.addButton("File", QMessageBox.YesRole)
        directory_button = reply.addButton("Directory", QMessageBox.NoRole)
        
        reply.exec()
        
        if reply.clickedButton() == file_button:
            # The input is a file
            if os.path.isfile(directory_path):
                # Run the crawl logic for a single file
                process_file(directory_path)
            else:
                QMessageBox.warning(self, "Invalid Input", "The specified path is not a file. Please provide a valid file path.")
        elif reply.clickedButton() == directory_button:
            # The input is a directory
            if os.path.isdir(directory_path):
                # Run the crawl logic for all files in the directory
                process_directory(directory_path)
            else:
                QMessageBox.warning(self, "Invalid Input", "The specified path is not a directory. Please provide a valid directory path.")



        def new_text_documents(self):
            # Functionality for the Email:Password button
            directory_path = self.set_directory_path_element.toPlainText()  # Get the directory path from set_directory_path_element
        
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
    
    
    def show_domain_statistics():
        """Display domain statistics in the output_text widget in descending order."""
        lines = input_text.get(1.0, tk.END).splitlines()
    
        # Count the number of lines with "Saved Path:"
        saved_path_lines = sum(1 for line in lines if line.strip().lower() == "saved path:")
    
        domains = [re.search(r"@(.+?)\.", line, re.IGNORECASE) for line in lines]
        domain_list = [match.group(1).lower() for match in domains if match]  # Convert to lowercase
    
        domain_stats = {}
        total = len(domain_list)
        for domain in domain_list:
            if domain not in domain_stats:
                domain_stats[domain] = 0
            domain_stats[domain] += 1
    
        sorted_stats = sorted(domain_stats.items(), key=lambda x: x[1], reverse=True)
    
        stats_output = []
    
        if saved_path_lines > 0:
            stats_output.append(f"Saved Path: {saved_path_lines}")
            if results_path_checkbox_var.get():
                stats_output.append(f"Saved Path Directory: {results_path_checkbox_var.get()}")
    
        for domain, count in sorted_stats:
            percentage = (count / total) * 100
            stats_output.append(f"{count} {domain} Lines ({percentage:.2f}%)")
    
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, '\n'.join(stats_output))
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
    
    def show_domain_statistics(self):
        """Display domain statistics in the output_text widget in descending order."""
        lines = input_text.get(1.0, tk.END).splitlines()
    
        # Count the number of lines with "Saved Path:"
        saved_path_lines = sum(1 for line in lines if line.strip().lower() == "saved path:")
    
        domains = [re.search(r"@(.+?)\.", line, re.IGNORECASE) for line in lines]
        domain_list = [match.group(1).lower() for match in domains if match]  # Convert to lowercase
    
        domain_stats = {}
        total = len(domain_list)
        for domain in domain_list:
            if domain not in domain_stats:
                domain_stats[domain] = 0
            domain_stats[domain] += 1
    
        sorted_stats = sorted(domain_stats.items(), key=lambda x: x[1], reverse=True)
        
        stats_output = []
        
        if saved_path_lines > 0:
            stats_output.append(f"Saved Path: {saved_path_lines}")
            if results_path_checkbox_var.get():
                stats_output.append(f"Saved Path Directory: {results_path_checkbox_var.get()}")
    
        for domain, count in sorted_stats:
            percentage = (count / total) * 100
            stats_output.append(f"{count} {domain} Lines ({percentage:.2f}%)")
    
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, '\n'.join(stats_output))
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
            removed_data_text = "\n".join(removed_data_text)
    
            self.output_text.setPlainText(output_text)
            self.removed_data_text.setPlainText(removed_data_text)
    
        except Exception as e:
            print(f"An error occurred: {e}")


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
    app = QApplication(sys.argv)
    queue = Queue()
    window = DiamondSorter()
    window.show()

    process = MyProcess(queue)
    process.start()
    process.join()  # this blocks until the process terminates
    result = queue.get()

    print(result)
    sys.exit(app.exec_())