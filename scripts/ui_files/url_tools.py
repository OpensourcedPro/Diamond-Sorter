import os
import sys
import requests
from PyQt5 import QtGui

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QTextEdit, QVBoxLayout, QPushButton, QMessageBox, QFileDialog, QDialog, QTreeWidgetItem, QScrollArea
from bs4 import BeautifulSoup
from colored import fg, attr
from PyQt5.QtCore import QThread, pyqtSignal
from requests.exceptions import RequestException
import requests
from requests.exceptions import RequestException, ConnectionError



class CheckLoginThread(QThread):
    progressUpdated = pyqtSignal(int)
    resultUpdated = pyqtSignal(str)
    speedUpdated = pyqtSignal(str)

    def __init__(self, url, subdirs):
        super(CheckLoginThread, self).__init__()
        self.url = url
        self.subdirs = subdirs
        
        
class UrlToolsWindow(QDialog):
    def __init__(self):
        super(UrlToolsWindow, self).__init__()
        # Existing code...

        # Create the console display area
        self.console_display = QPlainTextEdit()
        self.console_display.setReadOnly(True)  # Make it read-only
        self.console_display.setObjectName("console_display")

        # Add the console display to the layout
        self.layout.addWidget(self.console_display)
        self.console_display.appendPlainText("Hello, world!")
        self.console_display.textChanged.connect(self.handle_console_input)
        
        
        
class UrlToolsWindow(QDialog):
    finished = pyqtSignal(int)
    def __init__(self):
        super(UrlToolsWindow, self).__init__()
        uic.loadUi(r'url_tools.ui', self)
        self.http_request_html_button.clicked.connect(self.load_website_source_code)

        self.url_target_textedit = QtWidgets.QTextEdit()
        self.url_target_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.url_target_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.url_target_textedit.setObjectName("url_target_textedit")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.url_target_label.setFont(font)
        self.url_target_label.setObjectName("url_target_label")
        self.analytics_and_config_tab_widget = QtWidgets.QTabWidget(UrlToolsWindow)
        self.analytics_and_config_tab_widget.setObjectName("analytics_and_config_tab_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.captcha_button = QtWidgets.QPushButton(self.tab)
        self.captcha_button.setObjectName("captcha_button")
        self.cloudflare_button = QtWidgets.QPushButton(self.tab)
        self.cloudflare_button.setObjectName("cloudflare_button")
        self.akamai_button = QtWidgets.QPushButton(self.tab)
        self.akamai_button.setObjectName("akamai_button")
        self.push_button = QtWidgets.QPushButton(self.tab)
        self.push_button.setObjectName("push_button")
        self.http_request_button = QtWidgets.QPushButton(self.tab)
        self.http_request_button.setObjectName("http_request_button")
        self.alternatives_button = QtWidgets.QPushButton(self.tab)
        self.alternatives_button.setObjectName("alternatives_button")
        self.seo_data_details_button = QtWidgets.QPushButton(self.tab)
        self.seo_data_details_button.setObjectName("seo_data_details_button")
        self.sub_domains_button = QtWidgets.QPushButton(self.tab)
        self.sub_domains_button.setObjectName("sub_domains_button")
        self.sub_domains_button.setWhatsThis("")
        self.simalar_web_button = QtWidgets.QPushButton(self.tab)
        self.simalar_web_button.setObjectName("simalar_web_button")
        self.traffic_button = QtWidgets.QPushButton(self.tab)
        self.traffic_button.setObjectName("traffic_button")
        self.google_dork_button = QtWidgets.QPushButton(self.tab)
        self.google_dork_button.setObjectName("google_dork_button")
        self.xpath_scraper_button = QtWidgets.QPushButton(self.tab)
        self.xpath_scraper_button.setObjectName("xpath_scraper_button")
        self.analyze_csp = QtWidgets.QPushButton(self.tab)
        self.analyze_csp.setObjectName("analyze_csp")
        self.check_url_login_directories = QtWidgets.QPushButton(self.tab)
        self.check_url_login_directories.setObjectName("check_url_login_directories")
        self.check_api_login_directories = QtWidgets.QPushButton(self.tab)
        self.check_api_login_directories.setObjectName("check_api_login_directories")
        self.check_url_login_directories = QtWidgets.QPushButton(self.tab)
        self.check_url_login_directories.setObjectName("check_url_login_directories")
        self.check_api_login_directories = QtWidgets.QPushButton(self.tab)
        self.check_api_login_directories.setObjectName("check_api_login_directories")
        self.analytics_and_config_tab_widget.addTab(self.tab, "")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.http_request_get_button = QtWidgets.QPushButton(self.tab_2)
        self.http_request_get_button.setObjectName("http_request_get_button")
        self.http_request_post_button = QtWidgets.QPushButton(self.tab_2)
        self.http_request_post_button.setObjectName("http_request_post_button")
        self.http_request_headers_button = QtWidgets.QPushButton(self.tab_2)
        self.analytics_and_config_tab_widget = self.findChild(QtWidgets.QTabWidget, "analytics_and_config_tab_widget")
        self.results_window_textedit = self.findChild(QtWidgets.QTextEdit, "results_window_textedit")
        self.source_code_tab = self.findChild(QtWidgets.QTabWidget, "WebsiteSourceCodeTab")

        self.results_textwindow_label = QtWidgets.QLabel(UrlToolsWindow)
        self.results_textwindow_label.setObjectName("results_textwindow_label")
        self.connection_label = QtWidgets.QLabel(UrlToolsWindow)
        self.connection_label.setObjectName("connection_label")
        self.connection_widget = QtWidgets.QWidget(UrlToolsWindow)
        self.check_api_login_directories.clicked.connect(self.perform_check_api_logins)
        self.connection_widget.setObjectName("connection_widget")
        self.http_request_headers_button.setObjectName("http_request_headers_button")
        self.http_request_parse_button = QtWidgets.QPushButton(self.tab_2)
        self.http_request_parse_button.setObjectName("http_request_parse_button")
        self.http_request_html_button = QtWidgets.QPushButton(self.tab_2)
        self.http_request_html_button.setObjectName("http_request_html_button")
        self.http_request_css_button = QtWidgets.QPushButton(self.tab_2)
        self.http_request_css_button.setObjectName("http_request_css_button")
        self.http_request_referrer_button = QtWidgets.QPushButton(self.tab_2)
        self.http_request_referrer_button.setObjectName("http_request_referrer_button")
        QtCore.QMetaObject.connectSlotsByName(UrlToolsWindow)
        self.seo_data_details_button.clicked.connect(self.perform_seo_data_details)
        self.simalar_web_button.clicked.connect(self.perform_simalar_web)
        self.setWindowIcon(QtGui.QIcon('images\diamond.png'))
        self.setWindowTitle("Icon")

    def load_website_source_code(self):
        url = self.url_target_textedit.toPlainText()
        if not url.startswith('http'):
            url = 'http://' + url
        
        if not url:
            QMessageBox.critical(self, "Error", "No URL set")
            return
    
        try:
            response = requests.get(url)
            response.raise_for_status()
            source_code = response.text
    
            # Create a QStandardItemModel for the tree view
            model = QtGui.QStandardItemModel()
            model.setHorizontalHeaderLabels(["Element"])
    
            # Parse the source code for HTML, CSS, and JS elements
            # Customize this part based on your requirements
            # Here, we assume that HTML elements are enclosed in <html> tags,
            # CSS elements are enclosed in <style> tags, and
            # JS elements are enclosed in <script> tags
            html_item = QtGui.QStandardItem("HTML")
            css_item = QtGui.QStandardItem("CSS")
            js_item = QtGui.QStandardItem("JavaScript")
    
            start_tag = "<html>"
            end_tag = "</html>"
            start_idx = source_code.find(start_tag)
            end_idx = source_code.find(end_tag)
            if start_idx != -1 and end_idx != -1:
                html_text = source_code[start_idx:end_idx + len(end_tag)]
                html_item.appendRow(QtGui.QStandardItem(html_text))
    
            start_tag = "<style>"
            end_tag = "</style>"
            start_idx = source_code.find(start_tag)
            end_idx = source_code.find(end_tag)
            if start_idx != -1 and end_idx != -1:
                css_text = source_code[start_idx:end_idx + len(end_tag)]
                css_item.appendRow(QtGui.QStandardItem(css_text))
    
            start_tag = "<script>"
            end_tag = "</script>"
            start_idx = source_code.find(start_tag)
            end_idx = source_code.find(end_tag)
            if start_idx != -1 and end_idx != -1:
                js_text = source_code[start_idx:end_idx + len(end_tag)]
                js_item.appendRow(QtGui.QStandardItem(js_text))
    
            # Append the items to the model
            model.appendRow(html_item)
            model.appendRow(css_item)
            model.appendRow(js_item)
    
            # Set the model to the QTreeView
            current_widget = self.analytics_and_config_tab_widget.currentWidget()
            if isinstance(current_widget, QtWidgets.QWidget):
                tree_view = current_widget.findChild(QtWidgets.QTreeView)
                if isinstance(tree_view, QtWidgets.QTreeView):
                    tree_view.setModel(model)
    
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")
     
            



    def perform_check_api_logins(self):
        # Code logic to perform API login checks
        pass

    def perform_seo_data_details(self):
        # Code logic to perform SEO data extraction
        pass

    def perform_simalar_web(self):
        # Code logic to find similar websites
        pass
                
    def http_request_get_button_clicked(self):
        print("HTTP Request GET button clicked")
        
    def http_request_post_button_clicked(self):
        print("HTTP Request POST button clicked")
        
    def http_request_headers_button_clicked(self):
        print("HTTP Request Headers button clicked")
        
    def http_request_parse_button_clicked(self):
        print("HTTP Request Parse button clicked")
        
    def http_request_html_button_clicked(self):
        print("HTTP Request HTML button clicked")
        
    def http_request_css_button_clicked(self):
        print("HTTP Request CSS button clicked")
        
    def http_request_referrer_button_clicked(self):
        print("HTTP Request Referrer button clicked")

class Ui_UrlToolsWindow(object):
    def setupUi(self, UrlToolsWindow):
        UrlToolsWindow.setObjectName("UrlToolsWindow")
        UrlToolsWindow.resize(706, 640)
        self.retranslateUi(UrlToolsWindow)
        QtCore.QMetaObject.connectSlotsByName(UrlToolsWindow)
        self.seo_data_details_button.clicked.connect(self.perform_seo_data_details)
        self.simalar_web_button.clicked.connect(self.perform_simalar_web)


    def codeModificationChanged(self):
        url = self.url_target_textedit.toPlainText().strip()

        # Add the url to the history textedit
        self.url_history_textedit.appendPlainText(url)

        # Clear the url_target_textedit for new input
        self.url_target_textedit.clear()


    def update_url_history(self):
        url = self.url_target_textedit.toPlainText().strip()
        if url:
            self.url_history.append(url)

    def perform_seo_data_details(self):
        url = self.url_target_textedit.toPlainText()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
    
        title = soup.find("title").text.strip()
    
        metadata = [
            ("Description", "content"),
            ("SEO Keywords", "content"),
            ("Canonical_url", "href"),
            ("Robots", "content")
        ]
    
        result = f"<h2>Title:</h2>\n<p>{title}</p>\n"
    
        for tag, attr in metadata:
            element = soup.find("meta", attrs={"name": tag})
            if element:
                value = element.get(attr, "")
            else:
                value = "missing"
            result += f"<h2>{tag}:</h2>\n<p>{value}</p>\n"
    
        result += "<h2>General Headers:</h2>\n"
        for header in response.headers:
            result += f"<p>{header}: {response.headers[header]}</p>\n"
    
        result += "<h2>Response Headers:</h2>\n"
        for header in response.headers:
            result += f"<p>{header}: {response.headers[header]}</p>\n"
    
        result += "<h2>Request Headers:</h2>\n"
        for header in response.request.headers:
            result += f"<p>{header}: {response.request.headers[header]}</p>\n"
    
        self.results_window_textedit.setHtml(result)
    
    def perform_simalar_web(self):
        url = self.url_target_textedit.toPlainText()
        
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Extract headers
        headers = response.headers
        
        # Extract response content
        content = response.content
        
        # Extract response status code
        status_code = response.status_code
        
        # Example result
        result = f"Headers: {headers}\n\nContent: {content}\n\nStatus Code: {status_code}"
        
        self.results_window_textedit.setPlainText(result)

    def perform_check_url_logins(self):
        url = self.url_target_textedit.toPlainText()
        login_subdirs = []
        with open("C:/Users/Dooms/OneDrive/Documents/Diamond Srter/login-subdir/post.txt", "r") as file:
            login_subdirs = [line.strip() for line in file.readlines()]
    
        # Create an instance of the custom thread
        check_login_thread = CheckLoginThread(url, login_subdirs)
        # Connect the signals to update the progress bar and connection_console
        check_login_thread.progressUpdated.connect(self.update_progress_bar)
        check_login_thread.resultUpdated.connect(self.update_connection_console)
        check_login_thread.speedUpdated.connect(self.update_connection_speed)
        # Start the thread
        check_login_thread.start()

    def run(self):
        total_subdirs = len(self.subdirs)
        for i, subdir in enumerate(self.subdirs):
            # Perform the login check for each subdir
            full_url = self.url + subdir
            # Update the progress bar
            progress = int((i + 1) / total_subdirs * 100)
            self.progressUpdated.emit(progress)
            # Update the connection_console with the current subdir being checked
            self.resultUpdated.emit(f"Checking subdir: {subdir}")
            # Perform the login check and update the connection_console with the result
            # ...
            # You can update the connection_console using self.resultUpdated.emit(result)
            # ...
            # Update the connection speed information
            speed_info = f"Connection speed for subdir {subdir}: {speed}%"
            self.speedUpdated.emit(speed_info)



    def update_progress_bar(self, value):
        # Update the value of the progress bar
        self.ui.progress_bar.setValue(value)


    def perform_check_api_logins(self):
        url = self.ui.url_target_textedit.toPlainText()
        api_subdirs = []
        with open("C:/Users/Dooms/OneDrive/Documents/Diamond Srter/login-subdir/get.txt", "r") as file:
            api_subdirs = [line.strip() for line in file.readlines()]

        # Create an instance of the custom thread
        check_login_thread = CheckLoginThread(url, api_subdirs)
        # Connect the signals to update the progress bar and connection_console
        check_login_thread.progressUpdated.connect(self.update_progress_bar)
        check_login_thread.resultUpdated.connect(self.update_connection_console)
        check_login_thread.speedUpdated.connect(self.update_connection_speed)
        check_login_thread.finished.connect(check_login_thread.deleteLater) # Cleanup the thread
        # Start the thread
        check_login_thread.start()


    def analyze_csp(self):
        url = self.url_target_textedit.toPlainText()
        
        if not url:
            return
            t_help = {
            "child-src": "Defines the valid sources for web workers and nested browsing contexts loaded using elements such as <frame> and <iframe>.",
            "connect-src": "Restricts the URLs which can be loaded using script interfaces",
            "default-src": "Serves as a fallback for the other fetch directives.",
            "font-src": "Specifies valid sources for fonts loaded using @font-face.",
            "frame-src": "Specifies valid sources for nested browsing contexts loading using elements such as <frame> and <iframe>.",
            "img-src": "Specifies valid sources of images and favicons.",
            "manifest-src": "Specifies valid sources of application manifest files.",
            "media-src": "Specifies valid sources for loading media using the <audio> , <video> and <track> elements.",
            "object-src": "Specifies valid sources for the <object>, <embed>, and <applet> elements.",
            "prefetch-src": "Specifies valid sources to be prefetched or prerendered.",
            "script-src": "Specifies valid sources for JavaScript.",
            "style-src": "Specifies valid sources for stylesheets.",
            "webrtc-src": "Specifies valid sources for WebRTC connections.",
            "worker-src": "Specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts.",

            "base-uri": "Restricts the URLs which can be used in a document's <base> element.",
            "plugin-types": "Restricts the set of plugins that can be embedded into a document by limiting the types of resources which can be loaded.",
            "sandbox": "Enables a sandbox for the requested resource similar to the <iframe> sandbox attribute.",
            "disown-opener": "Ensures a resource will disown its opener when navigated to.",

            "form-action": "Restricts the URLs which can be used as the target of a form submissions from a given context.",
            "frame-ancestors": "Specifies valid parents that may embed a page using <frame>, <iframe>, <object>, <embed>, or <applet>.",
            "navigate-to": "Restricts the URLs to which a document can navigate by any means (a, form, window.location, window.open, etc.)",

            "report-uri": "Instructs the user agent to report attempts to violate the Content Security Policy. These violation reports consist of JSON documents sent via an HTTP POST request to the specified URI.",
            "report-to": "Fires a SecurityPolicyViolationEvent.",

            "block-all-mixed-content": "Prevents loading any assets using HTTP when the page is loaded using HTTPS.",
            "referrer": "Used to specify information in the referer (sic) header for links away from a page. Use the Referrer-Policy header instead.",
            "require-sri-for": "Requires the use of SRI for scripts or styles on the page.",
            "upgrade-insecure-requests": "Instructs user agents to treat all of a site's insecure URLs (those served over HTTP) as though they have been replaced with secure URLs (those served over HTTPS). This directive is intended for web sites with large numbers of insecure legacy URLs that need to be rewritten.",

            "*": {"t":"Wildcard, allows any URL except data: blob:filesystem: schemes.","c":"red"},
            "'none'": {"t":"Prevents loading resources from any source.","c":"green"},
            "'self'": {"t":"Allows loading resources from the same origin (same scheme, host and port).","c":"green"},
            "data:": {"t":"Allows loading resources via the data scheme (eg Base64 encoded images).","c":"yellow"},
            "blob:": {"t":"Allows loading resources via the blob scheme (eg Base64 encoded images).","c":"yellow"},
            "domain.example.com": {"t":"Allows loading resources from the specified domain name.","c":"green"},
            "*.example.com": {"t":"Allows loading resources from any subdomain under example.com.","c":"green"},
            "https://cdn.com": {"t":"Allows loading resources only over HTTPS matching the given domain.","c":"green"},
            "https:": {"t":"Allows loading resources only over HTTPS on any domain.","c":"green"},
            "'unsafe-inline'": {"t":"Allows use of inline source elements such as style attribute, onclick, or script tag bodies (depends on the context of the source it is applied to) and javascript: URIs.","c":"red"},
            "'unsafe-eval'": {"t":"Allows unsafe dynamic code evaluation such as JavaScript eval()","c":"red"},
            "'nonce-'": {"t":"Allows script or style tag to execute if the nonce attribute value matches the header value. Note that 'unsafe-inline' is ignored if either a hash or nonce value is present in the source list.","c":"green"},
            "'sha256-'": {"t":"Allow a specific script or style to execute if it matches the hash. Doesn't work for javascript: URIs. Note that 'unsafe-inline' is ignored if either a hash or nonce value is present in the source list.","c":"green"},
            }
        if not self.url_target_textedit.toPlainText():
                return

                analyze_dialog = QtWidgets.QDialog(self)
                analyze_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
                analyze_dialog.setWindowTitle("Analyzing Content Security Policy")
                analyze_dialog.layout = QtWidgets.QVBoxLayout(analyze_dialog)
            
                loading_label = QtWidgets.QLabel(analyze_dialog)
                loading_movie = QtGui.QMovie("loading.gif")
                loading_label.setMovie(loading_movie)
                loading_label.setAlignment(QtCore.Qt.AlignCenter)
                loading_movie.start()
            
                analyze_dialog.layout.addWidget(loading_label)
            
                analyze_dialog.show()
            
                QtCore.QCoreApplication.processEvents()
            
                # Perform the analysis
                url = self.url_target_textedit.toPlainText()
                # Your analysis code here...
            
                analyze_dialog.close()



    def website_bf_hidden_content_button():
        # Get the URL target from the url_target_textedit
        url = url_target_textedit.toPlainText()
    
        # Display a file dialog to select the wordlist file
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Wordlist File")
    
        # Perform the bruteforce operation using the selected URL and wordlist file
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file]
    
        for word in words:
            r = requests.get(f'{url}/{word}')
            if r.status_code == 200:
                print(f">> {url}{word} | Status: {r.status_code}")
            else:
                print(f"> {url}{word} | Status: {r.status_code}")



if __name__ == '__main__':
    app = QApplication([])
    window = UrlToolsWindow()
    window.show()
    app.exec_()