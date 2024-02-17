import os
import sys
import requests
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QLabel, QDialog, QMessageBox, QInputDialog, QRadioButton, QVBoxLayout, QMainWindow, QDialogButtonBox, QTreeWidget, QWidget, QTabWidget, QTreeWidgetItem
from undetected_chromedriver import Chrome, ChromeOptions
from PyQt5.QtWebEngineWidgets import QWebEngineView

class NetworkRequest:
    def __init__(self, url, method, status_code, content_type):
        self.url = url
        self.method = method
        self.status_code = status_code
        self.content_type = content_type

network_requests = []  # Define an empty list to store NetworkRequest objects


class ElementsTab(QWidget):
    def __init__(self):
        super().__init__()

        self.web_view = QWebEngineView()
        self.elements_list_view = QListView()
        self.elements_model = QStringListModel()

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.elements_list_view)
        self.setLayout(layout)

    def load_webpage(self, url):
        self.web_view.load(url)

        # Connect the loadFinished signal to get_html_source method
        self.web_view.loadFinished.connect(self.get_html_source)

    def get_html_source(self, success):
        if success:
            self.web_view.page().toHtml(self.handle_html_source)

    def handle_html_source(self, html):
        source_code = html[0]
        # Process or display the source code as needed
        source_code_list = source_code.splitlines()
        self.elements_model.setStringList(source_code_list)
        self.elements_list_view.setModel(self.elements_model)




class ErrorDialog(QDialog):
    def __init__(self, error_message):
        super(ErrorDialog, self).__init__()
        self.setWindowTitle("Error")
        layout = QVBoxLayout(self)
        error_label = QLabel(error_message)
        layout.addWidget(error_label)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create the Log Network tab
        log_network_tab = QWidget()
        log_network_layout = QVBoxLayout(log_network_tab)
        network_tree_widget = QTreeWidget()
        network_tree_widget.setHeaderLabels(["Status", "Type", "Initiator", "Time", "Waterfall"])
        log_network_layout.addWidget(network_tree_widget)

        # Add the Log Network tab to the main window
        self.tab_widget.addTab(log_network_tab, "Log Network")

        # Populate the network log
        self.populate_network_log(network_tree_widget)
        self.setFixedSize(1600, 790)  # Replace 800 and 600 with your desired window size

    def populate_network_log(self, network_tree_widget):
        # Simulated network log data
        network_log_data = [
            {"status": "200", "type": "HTML", "initiator": "index.html", "time": "100ms", "waterfall": "▇▇▇▇▇▇▇▇▇▇▇▇▇"},
            {"status": "404", "type": "CSS", "initiator": "styles.css", "time": "50ms", "waterfall": "▇▇▇▇▇▇"},
            {"status": "200", "type": "JS", "initiator": "script.js", "time": "80ms", "waterfall": "▇▇▇▇▇▇▇▇"},
            # Add more log data here...
        ]

        # Populate the network log with the data
        for log_data in network_log_data:
            item = QTreeWidgetItem(network_tree_widget, [
                log_data["status"],
                log_data["type"],
                log_data["initiator"],
                log_data["time"],
                log_data["waterfall"]
            ])

class ConfigDeveloperController:
    def __init__(self, app):
        self.app = app
        self.configs_dialog = QtWidgets.QDialog()
        uic.loadUi('config_developer.ui', self.configs_dialog)
        self.setup_ui()
        self.network_log_widget = QWidget()
        self.network_log_layout = QVBoxLayout(self.network_log_widget)
        self.network_tree_widget = QTreeWidget(self.network_log_widget)
        self.network_tree_widget.setHeaderLabels(["Status", "Type", "Initiator", "Time", "Waterfall"])
        self.network_log_layout.addWidget(self.network_tree_widget)
        
    def setup_ui(self):
        self.url_text_edit = self.configs_dialog.findChild(QtWidgets.QLineEdit, "url_text_edit")

        # Get the checkbox widget
        self.useragent_label = self.configs_dialog.findChild(QtWidgets.QCheckBox, "useragent_label")
        self.useragent_label.setVisible(True)
        # Get the button widget
        self.project_setpath_button = self.configs_dialog.findChild(QtWidgets.QPushButton, "project_setpath_button")
        # Set up other UI components and signals/slots
        self.project_setpath_button.clicked.connect(self.open_file_dialog)
        self.scroll_area = self.configs_dialog.findChild(QtWidgets.QScrollArea, "scrollArea")
        self.text_browser = QtWidgets.QTextBrowser()
        self.scroll_area.setWidget(self.text_browser)
        self.http_get_button = self.configs_dialog.findChild(QtWidgets.QPushButton, "HTTP_GET_Button")
        self.http_get_button.clicked.connect(self.send_http_request)
        self.configs_dialog.test_url_connectionButton = QtWidgets.QPushButton("Test URL Connection")

    def closeEvent(self, event):
        # Show a notification when the window is being closed
        QMessageBox.information(self, "Window Closed", "The application is closing.")
        # End the script
        QCoreApplication.quit()

    def display_error_dialog(self, error_message):
        dialog = ErrorDialog(error_message)
        dialog.exec_()

    def send_http_request(self, headers):
        url, ok = QInputDialog.getText(self.configs_dialog, "DiamondSorter - Config Developer", "Enter your URL Request:")
        dialog = QInputDialog()
        dialog.setWindowTitle("Enter URL")
        dialog.setLabelText("URL:")
        dialog.setInputMode(QInputDialog.TextInput)
        dialog.setTextEchoMode(QLineEdit.Normal)
        dialog.resize(471, 111)
    
        cookies = {
            'xf_csrf': '***',
            'xf_session': '',
        }
    
        data = {
            '_xfToken': '',
            'login': '',
            'password': '************',
            'remember': '1',
            '_xfRedirect': 'https://.com/',
        }
    
        if ok and url:
            try:
                response = requests.get(url, headers=headers, cookies=cookies, data=data)
                response.raise_for_status()  # Raise an exception if the request was not successful
                self.text_browser.setText(response.text)
    
                network_tab = self.configs_dialog.HTTP_CONSOLE_QTABWIDGET.findChild(QWidget, "NetworkTab")
                network_tree_widget = network_tab.findChild(QTreeWidget, "network_tree_widget")
    
                if network_tree_widget is None:
                    network_tree_widget = QTreeWidget(network_tab)
                    network_tree_widget.setObjectName("network_tree_widget")
                    layout = QVBoxLayout(network_tab)
                    layout.addWidget(network_tree_widget)
                    network_tab.setLayout(layout)
    
                network_tree_widget.clear()
    
                network_requests = []
    
                network_request = NetworkRequest(url, "GET", response.status_code, response.headers['Content-Type'])
                network_requests.append(network_request)
    
                # Populate the captured network requests in the tree widget
                for request in network_requests:
                    url_item = QTreeWidgetItem(network_tree_widget, [request.url])
                    method_item = QTreeWidgetItem(url_item, [f"Method: {request.method}"])
                    status_code_item = QTreeWidgetItem(url_item, [f"Status Code: {request.status_code}"])
                    content_type_item = QTreeWidgetItem(url_item, [f"Content Type: {request.content_type}"])
    
                    url_item.setExpanded(True)
    
                network_tree_widget.setHeaderLabels(["Captured Network Requests"])
                network_tree_widget.expandAll()
    
            except requests.exceptions.RequestException as e:
                self.display_error_dialog(str(e))
                
    def open_file_dialog(self):
        file_dialog = QFileDialog.getOpenFileName(self.configs_dialog, "Select a Text File", "", "Text Files (*.txt)")
        selected_file = file_dialog[0]
        if selected_file:
            file_parts = os.path.split(selected_file)
            file_name = file_parts[-1]
            parent_folders = file_parts[:-1]

            if len(parent_folders) >= 2:
                formatted_text = os.path.join(parent_folders[-2], parent_folders[-1], file_name)
            else:
                formatted_text = os.path.join(*parent_folders, file_name)

            project_setpath_text_browser = self.configs_dialog.findChild(QtWidgets.QTextBrowser, "project_setpath_text_browser")
            project_setpath_text_browser.setText(formatted_text)

    def run(self):
        self.configs_dialog.exec_()


    def show_help():
        help_text = """
    HTTP headers
    HTTP headers let the client and the server pass additional information with an HTTP request or response. An HTTP header consists of its case-insensitive name followed by a colon (:), then by its value. Whitespace before the value is ignored.
    
    Custom proprietary headers have historically been used with an X- prefix, but this convention was deprecated in June 2012 because of the inconveniences it caused when nonstandard fields became standard in RFC 6648; others are listed in an IANA registry, whose original content was defined in RFC 4229. IANA also maintains a registry of proposed new HTTP headers.
    
    Headers can be grouped according to their contexts:
    
    - Request headers: Contain more information about the resource to be fetched, or about the client requesting the resource.
    - Response headers: Hold additional information about the response, like its location or about the server providing it.
    - Representation headers: Contain information about the body of the resource, like its MIME type, or encoding/compression applied.
    - Payload headers: Contain representation-independent information about payload data, including content length and the encoding used for transport.
    
    Headers can also be grouped according to how proxies handle them:
    
    - End-to-end headers: These headers must be transmitted to the final recipient of the message: the server for a request, or the client for a response. Intermediate proxies must retransmit these headers unmodified and caches must store them.
    - Hop-by-hop headers: These headers are meaningful only for a single transport-level connection, and must not be retransmitted by proxies or cached. Note that only hop-by-hop headers may be set using the Connection header.
    
    Here are some examples of common HTTP headers:
    
    - Authentication headers: WWW-Authenticate, Authorization, Proxy-Authenticate, Proxy-Authorization.
    - Caching headers: Age, Cache-Control, Expires, Vary.
    - Conditionals headers: Last-Modified, ETag, If-Match, If-None-Match, If-Modified-Since, If-Unmodified-Since.
    - Content negotiation headers: Accept, Accept-Encoding, Accept-Language.
    - Cookies headers: Cookie, Set-Cookie.
    - CORS headers: Access-Control-Allow-*.
    - Security headers: Content-Security-Policy, Strict-Transport-Security, X-XSS-Protection.
    - Request context headers: Host, Referer, User-Agent.
    - Response context headers: Allow, Server.
    - Other headers: Date, Link, Retry-After, Upgrade.
    
    These are just a few examples, and there are many more HTTP headers available for various purposes. You can refer to the HTTP specification or specific RFCs for detailed information on each header.
    
    Remember that headers play an important role in communication between clients and servers, and understanding their usage and semantics is crucial for building robust and secure web applications.
    
    If you need further assistance or have specific questions about a particular header, feel free to ask!
    """
    
        print(help_text)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = ConfigDeveloperController(app)
    controller.run()
    sys.exit(app.exec_())
    
    
    
    
