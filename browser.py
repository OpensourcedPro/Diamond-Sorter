import sys
import os
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon
import qtawesome as qta
import logging
from colorama import Fore,Style
from datetime import datetime

# Made by J3tus

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.original_icon_names = self.load_icons()
        self.search_history = []

        navbar = QToolBar()
        self.addToolBar(navbar)
        
        navbar_container = QWidget(self)
        navbar_layout = QVBoxLayout(navbar_container)
        navbar_layout.setContentsMargins(0, 0, 0, 0)
        navbar_layout.addWidget(navbar)

        main_layout = QVBoxLayout()
        main_layout.addWidget(navbar_container)

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.currentChanged.connect(self.tab_changed)
        self.setCentralWidget(self.tab_widget)

        tab_widget_container = QWidget(self)
        tab_layout = QVBoxLayout(tab_widget_container)
        tab_layout.setContentsMargins(0, 0, 0, 0)
        tab_layout.addWidget(self.tab_widget)

        main_layout.addWidget(tab_widget_container)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.create_tab()
        self.main_window = QWidget(self)
       
        back_btn = QAction(self.load_icon('Back', 'fa.chevron-left', 'black'), 'Back', self)
        back_btn.setStatusTip('Back to the previous page')
        back_btn.triggered.connect(self.browser_back)
        navbar.addAction(back_btn)

        forward_btn = QAction(self.load_icon('Forward', 'fa.chevron-right', 'black'), 'Forward', self)
        forward_btn.setStatusTip('Forward to the next page')
        forward_btn.triggered.connect(self.browser_forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(self.load_icon('Reload', 'fa.refresh', 'black'), 'Reload', self)
        reload_btn.setStatusTip('Reload the page')
        reload_btn.triggered.connect(self.reload_page)
        navbar.addAction(reload_btn)

        home_btn = QAction(self.load_icon('Home', 'fa.home', 'black'), 'Home', self)
        home_btn.setStatusTip('Go to the home page')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.secure_indicator = QLabel()
        self.secure_indicator.setStatusTip('Secure Connection')
        navbar.addWidget(self.secure_indicator)
        self.secure_indicator.setVisible(False)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        search_btn = QAction(self.load_icon('Search', 'fa.search', 'black'), 'Search', self)
        search_btn.setStatusTip('Search using Google')
        search_btn.triggered.connect(self.search_google)
        navbar.addAction(search_btn)

        new_tab_btn = QAction(self.load_icon('New Tab', 'fa.plus', 'black'), 'New Tab', self)
        new_tab_btn.setStatusTip('Open a new tab')
        new_tab_btn.triggered.connect(self.create_tab)
        navbar.addAction(new_tab_btn)

        self.dark_mode = QAction(self.load_icon('Dark Mode', 'fa5.sun', 'black'), 'Dark Mode', self)
        self.dark_mode.setCheckable(True)
        self.dark_mode.toggled.connect(self.toggle_dark_mode)
        navbar.addAction(self.dark_mode)
  
        self.showMinimized()
        self.centerWindow()
        self.setWindowTitle('PyBrowser')

        self.setup_logging()
        self.log_user_action('Browser Status', 'Browser opened')

        self.navigate_home()
        self.current_tab = self.tab_widget.currentWidget()

        self.dark_stylesheet_path = os.path.join(os.getcwd(), 'ui', 'darkstylesheet.css')
        self.light_stylesheet_path = os.path.join(os.getcwd(), 'ui', 'lightstylesheet.css')

        if not os.path.exists(self.dark_stylesheet_path):
            self.create_stylesheet_file(self.dark_stylesheet_path, 'Dark Mode Styles')
            
        if not os.path.exists(self.light_stylesheet_path):
            self.create_stylesheet_file(self.light_stylesheet_path, 'Light Mode Styles')

        self.toggle_dark_mode()

    def centerWindow(self):
        screenGeometry = QDesktopWidget().screenGeometry()
        x = (screenGeometry.width() - self.width()) // 3
        y = (screenGeometry.height() - self.height()) * 6
        self.setGeometry(x, y, 1200, 800)

    def create_default_icons(self, default_icons_path):
        icons = {
            "Back": "fa.chevron-left",
            "Forward": "fa.chevron-right",
            "Reload": "fa.refresh",
            "Home": "fa.home",
            "New Tab": "fa.plus",
            "Search": "fa.search",
            "Dark Mode": "fa5.moon",
            "Light Mode": "mdi6.lightbulb-on-10",
            "Secure Indicator": "fa.lock",
            "Unsecure Indicator": "fa.unlock"
        }
        os.makedirs(os.path.dirname(default_icons_path), exist_ok=True)

        if not os.path.exists(default_icons_path):
            with open(default_icons_path, "w") as default:
                json.dump(icons, default, indent=4)

            print("Default icons added to icons.json")
            self.original_icon_names = self.load_icons()
        else:
            print(f"File {default_icons_path} already exists. Skipping creation.")

    def load_icons(self, debug=True):
        default_icons_path = os.path.join(os.getcwd(), 'ui', 'icons.json')

        if os.path.exists(default_icons_path):
            try:
                with open(default_icons_path, 'r') as default_icons_file:
                    if debug:
                        print("icons.json found. Using Custom icons")
                    return json.load(default_icons_file)
            except json.JSONDecodeError:
                print("Error decoding icons.json file. Using default icons.")
        else:
            self.create_default_icons(default_icons_path)

    def load_icon(self, action_name, default_icon_name, color, set=True):
        if not self.original_icon_names: self.original_icon_names = self.load_icons()
        icon_name = self.original_icon_names.get(action_name, default_icon_name)
        if set == False:
            return icon_name
        return qta.icon(icon_name, color=color)

    def setup_logging(self):
        log_directory = os.path.join(os.getcwd(), 'logs')
        os.makedirs(log_directory, exist_ok=True)

        log_file_path = os.path.join(log_directory, 'user_actions.log')
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s',
                            handlers=[logging.FileHandler(log_file_path), logging.StreamHandler()])

    def log_user_action(self, action_name, details):
        log_text = f"{action_name}: {details}"
        print(f"{Fore.GREEN}INFO{Style.RESET_ALL} - {log_text}")  # Added colorama log formatting
        logging.info(log_text)

    def read_stylesheet(self, file_path, default_stylesheet, debug=False):
        try:
            with open(file_path, 'r') as stylesheet_file:
                if debug != False:
                    print("Using Custom Styles")
                return stylesheet_file.read()
        except IOError:
            print(f"{file_path} not found or unreadable. Using default styles.")
            return default_stylesheet

    def toggle_dark_mode(self):
        icon_color = 'black' if self.dark_mode.isChecked() else 'white'
        for action in self.findChildren(QAction):
            action_name = action.text()
            if action_name:
                default_icon_name = self.original_icon_names.get(action_name, '')
                icon_name = self.load_icon(action_name, default_icon_name, icon_color, set=False)
                action.setIcon(qta.icon(icon_name, color=icon_color))
        dark_mode_stylesheet = self.read_stylesheet(self.dark_stylesheet_path, 'dark_mode_stylesheet', False)
        light_mode_stylesheet = self.read_stylesheet(self.light_stylesheet_path, 'light_mode_stylesheet', False)

        if not self.dark_mode.isChecked():
            self.setStyleSheet(light_mode_stylesheet)
            self.dark_mode.setIcon(qta.icon('mdi6.lightbulb-on-10', color="white"))
            self.secure_indicator.setPixmap(self.load_icon('Secure Indicator', "fa.lock", 'white').pixmap(20, 20))
            self.log_user_action('Dark Mode', 'ON')
        else:
            self.setStyleSheet(dark_mode_stylesheet)
            self.dark_mode.setIcon(qta.icon('fa5.moon'))
            self.secure_indicator.setPixmap(self.load_icon('Secure Indicator', "fa.lock", 'black').pixmap(20, 20))
            self.log_user_action('Dark Mode', 'OFF')

    def create_stylesheet_file(self, file_path, content):
        darkstylesheet = """
            QMainWindow {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QToolBar {
                background-color: #2d2d2d;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #333333;
                color: #ffffff;
            }
            QTabBar::tab {
                background-color: #2b2b2b; 
                color: white;
                padding: 8px;
                border-color: black;
                margin-left: 1px;
            }
            """
        lightstylesheet = """
            QMainWindow {
                background-color: #ffffff;
                color: #000000;
            }
            QToolBar {
                background-color: #ffffff;
                color: #000000;
            }
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
            }
            QTabBar::tab {
                background-color: whitesmoke; 
                color: black;
                padding: 8px;
                margin-left: 1px;
            }
        """
        try:
            with open(file_path, 'w') as stylesheet_file:
                if content == "Dark Mode Styles":
                    content = lightstylesheet
                elif content == "Light Mode Styles":
                    content = darkstylesheet
                stylesheet_file.write(content)
                print(f"Created {file_path}")
        except IOError:
            print(f"Error creating at {file_path}")

    def navigate_home(self):
        self.current_tab.setUrl(QUrl("http://www.google.com"))
        self.log_user_action('Navigate Home', 'https://www.google.com')

    def navigate_to_url(self):
        entered_text = self.url_bar.text()

        if entered_text.startswith(("www.", "http://", "https://")):
            q = QUrl(entered_text)
            if q.scheme() == "":
                q.setScheme("http")
            self.current_tab.setUrl(q)
            self.log_user_action('Navigate URL', entered_text)
        else:
            google_search_url = f"https://www.google.com/search?q={entered_text}"
            self.current_tab.setUrl(QUrl(google_search_url))
            self.log_user_action('Search Google', entered_text)

    def update_urlbar(self, q):
        full_url = q.url()
        page_title = self.current_tab.page().title()
        prefixes_to_remove = ["https://", "http://", "www."]
        for prefix in prefixes_to_remove:
            if prefix in page_title:
                page_title = page_title.replace(prefix, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.current_tab), page_title[:15])
        if hasattr(self, 'url_bar') and isinstance(self.url_bar, QLineEdit):
            self.url_bar.setText(full_url)
            self.url_bar.setCursorPosition(0)
            icons = self.load_icons(debug=False)
            secure_icon = icons["Secure Indicator"] if q.scheme() == "https" else icons["Unsecure Indicator"]
            self.secure_indicator.setPixmap(self.load_icon('Secure Indicator', secure_icon, 'black').pixmap(20, 20))
            self.secure_indicator.setVisible(True)

    def search_google(self):
        search_query = self.url_bar.text()
        if search_query:
            google_search_url = f"https://www.google.com/search?q={search_query}"
            self.current_tab.setUrl(QUrl(google_search_url))
            self.log_user_action('Search Google', search_query)

    def closeEvent(self, event):
        self.log_user_action('Browser Status', 'Browser closed')
        event.accept()

    def browser_back(self):
        current_url = self.current_tab.url().toString()
        self.current_tab.back()
        new_url = self.current_tab.url().toString()
        self.log_user_action('Go Back', f'Navigated back from {current_url} to {new_url}')

    def browser_forward(self):
        current_url = self.current_tab.url().toString()
        self.current_tab.forward()
        new_url = self.current_tab.url().toString()
        self.log_user_action('Go Forward', f'Navigated forward from {current_url} to {new_url}')

    def reload_page(self):
        current_url = self.current_tab.url().toString()
        self.current_tab.reload()
        self.log_user_action('Reload Page', f'Reloaded page at {current_url}')

    def create_tab(self):
        browser = QWebEngineView()
        browser.urlChanged.connect(self.update_urlbar)
        self.tab_widget.addTab(browser, "Loading...")  
        self.tab_widget.setCurrentWidget(browser)
        self.tab_widget.setMovable(True)
        self.current_tab = browser
        self.navigate_home()
        self.log_user_action('Open Tab', f'Tab opened with URL: {self.current_tab.url().toString()}')

    def close_tab(self, index):
        widget = self.tab_widget.widget(index)
        widget.close()
        self.log_user_action('Close Tab', f'Tab closed with URL: {widget.url().toString()}')
        self.tab_widget.removeTab(index)
        if self.tab_widget.count() == 0:
            self.close()

    def tab_changed(self, index):
        self.current_tab = self.tab_widget.widget(index)

if __name__ == "__main__":
    try:
        print(f"""
              {Fore.CYAN}Thank you for using PyBrowser! 
              Made by J3tus.
              Discord: jetusw
              {Style.RESET_ALL}""")
        print(f"{Fore.YELLOW}Starting PyBrowser...{Style.RESET_ALL}")
        app = QApplication(sys.argv)
        QApplication.setApplicationName("PyBrowser")
        window = Browser()
        app.exec_()
       

    except KeyboardInterrupt:
        logging.info(f"Browser Status: Forced close")
        quit()