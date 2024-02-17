from PyQt5.QtWidgets import QTextEdit, QApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class GeneralTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.buttons = []

        self.setup_buttons()
        
    def setup_buttons(self):
        # Create and add buttons to the layout
        copy_output_button = QPushButton("Copy Output")
        copy_output_button.clicked.connect(copy_output)
        self.buttons.append(copy_output_button)
        self.layout.addWidget(copy_output_button)

        remove_ending_punctuation_button = QPushButton("Remove Ending Punctuation")
        remove_ending_punctuation_button.clicked.connect(remove_ending_punctuation)
        self.buttons.append(remove_ending_punctuation_button)
        self.layout.addWidget(remove_ending_punctuation_button)


def copy_output(output_text):
    """Copy content from output_text widget to clipboard."""
    try:
        clipboard = QApplication.clipboard()
        clipboard.setText(output_text.toPlainText())
    except Exception as e:
        print(f"An error occurred: {e}")

def replace_with_listButton():
    repeating_string = input("Enter the repeating string or value: ")
    lines = input("Copy and paste the list of lines: ").splitlines()

    for line in lines:
        replaced_line = line.replace(repeating_string, line)
        print(replaced_line)

def paste_input(input_text):
    """Paste content from clipboard to input_text widget."""
    try:
        clipboard_content = QApplication.clipboard().text()
        input_text.setPlainText(clipboard_content)
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_special_character(input_text, output_text):
    """Remove special character from each line."""
    try:
        text = input_text.toPlainText()
        lines = text.split("\n")
        processed_lines = [re.sub(r"[^a-zA-Z0-9 ]+", "", line) for line in lines]

        output_text.clear()
        output_text.setPlainText("\n".join(processed_lines))
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_md5(input_text, output_text):
    """Extract MD5 hashes from the input_text widget."""
    try:
        lines = input_text.toPlainText().split("\n")
        md5_regex = re.compile(r"\b[A-Fa-f0-9]{32}\b")
        extracted_md5 = [match.group() for line in lines for match in md5_regex.finditer(line)]
        output_text.clear()
        output_text.setPlainText("\n".join(extracted_md5))
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

def remove_domains(input_text, output_text):
    """Remove domains from the input_text widget."""
    try:
        text = input_text.toPlainText()
        text_without_domains = re.sub(r'@\S+\.', '', text)
        output_text.clear()
        output_text.setPlainText(text_without_domains)
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_duplicates(input_text, output_text):
    """Remove duplicate lines from input and display in output."""
    try:
        text = input_text.toPlainText()
        lines = text.split("\n")
        unique_lines = list(set(lines))
        unique_lines.sort(key=lines.index)
        output_text.clear()
        output_text.setPlainText("\n".join(unique_lines))
    except Exception as e:
        print(f"An error occurred: {e}")

    
    
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

def split_by_linesButton(self):
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