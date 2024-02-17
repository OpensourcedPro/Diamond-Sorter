from PyQt5.QtWidgets import QTextEdit, QApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

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



def createpasswordlist(self):
    # This method will be called when the "create_password_list" button is clicked
    print("Create password list button clicked")
    # Add your code to create the password list here

def create_numberlist(self):
    # This method will be called when the "create_number_list" button is clicked
    print("Create number list button clicked")
    # Add your code to create the number list here


def server_information(self):
    # Logic for the "Server Information" button
    pass
    
def wordpress_finder(self):
    # Logic for the "Wordpress Finder" button
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
