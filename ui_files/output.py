import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QFormLayout, QLineEdit, QComboBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.cookie_values_btn = QPushButton("Cookie Values")
        self.cookie_values_btn.clicked.connect(self.show_dialog)
        self.layout.addWidget(self.cookie_values_btn)

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Option")
        layout = QFormLayout(dialog)

        option_combo = QComboBox()
        option_combo.addItem("By Values")
        option_combo.addItem("By Website")

        layout.addRow("Select option:", option_combo)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(lambda: self.handle_option(option_combo.currentText(), dialog))
        layout.addRow(submit_btn)

        dialog.exec_()

    def handle_option(self, option, dialog):
        if option == "By Values":
            value_dialog = QDialog(self)
            value_dialog.setWindowTitle("Enter Value")
            value_layout = QFormLayout(value_dialog)

            value_line_edit = QLineEdit()
            value_layout.addRow("Value:", value_line_edit)

            submit_btn = QPushButton("Submit")
            submit_btn.clicked.connect(lambda: self.handle_value(value_line_edit.text(), value_dialog))
            value_layout.addRow(submit_btn)

            value_dialog.exec_()
        elif option == "By Website":
            website_dialog = QDialog(self)
            website_dialog.setWindowTitle("Enter Website URL")
            website_layout = QFormLayout(website_dialog)

            website_line_edit = QLineEdit()
            website_layout.addRow("Website URL:", website_line_edit)

            submit_btn = QPushButton("Submit")
            submit_btn.clicked.connect(lambda: self.handle_website(website_line_edit.text(), website_dialog))
            website_layout.addRow(submit_btn)

            website_dialog.exec_()

    def handle_value(self, value, dialog):
        # Handle value submission
        print(f"Submitted value: {value}")
        dialog.close()

    def handle_website(self, website, dialog):
        # Handle website submission
        print(f"Submitted website: {website}")

        web_view = QWebEngineView()

        def fill_input():
            web_view.page().runJavaScript(f'document.getElementsByClassName("select2-search__field")[0].value = "{website}"')

        def submit_form():
            web_view.page().runJavaScript('document.forms[0].submit()')

        def print_results():
            web_view.page().toHtml(lambda html: self.parse_results(html))

        def close_dialog():
            dialog.close()

        web_view.loadFinished.connect(fill_input)
        QTimer.singleShot(2000, submit_form)
        QTimer.singleShot(5000, print_results)
        QTimer.singleShot(6000, close_dialog)

        dialog.close()

    def parse_results(self, html):
        # Parse the HTML and extract the desired information

        # You can use a library like BeautifulSoup or regex to extract the data from the HTML
        # Here is a basic example using regex to extract the desired information
        import re
        pattern = re.compile(r'<td class="cookie-name">(.*?)</td>.*?<td class="unique-domains">(.*?)</td>.*?<td class="last-seen">(.*?)</td>', re.DOTALL)
        matches = pattern.findall(html)

        print("Results:")
        for match in matches:
            cookie_name, unique_domains, last_seen = match
            print(f"Cookie name: {cookie_name.strip()}")
            print(f"Unique domains: {unique_domains.strip()}")
            print(f"Last seen: {last_seen.strip()}")
            print()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()