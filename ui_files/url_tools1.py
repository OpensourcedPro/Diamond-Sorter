import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, QGridLayout, QMenu, QAction, QTabBar
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QLineEdit
import datetime
from datetime import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from qmaterialwidgets import IndeterminateProgressRing
from PyQt5.QtWidgets import QSpinBox



from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UrlToolsWindow(object):
    def setupUi(self, UrlToolsWindow):
        UrlToolsWindow.setObjectName("UrlToolsWindow")
        UrlToolsWindow.resize(1200, 684)
        UrlToolsWindow.setMinimumSize(QtCore.QSize(1200, 671))
        UrlToolsWindow.setMaximumSize(QtCore.QSize(1200, 702))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        UrlToolsWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("diamond.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UrlToolsWindow.setWindowIcon(icon)
        UrlToolsWindow.setStyleSheet("QWidget {\n"
"  background-color: #232629;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox,\n"
"QFrame {\n"
"  background-color: #232629;\n"
"  border: 2px solid #4f5b62;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTreeView,\n"
"QListView,\n"
"QLineEdit,\n"
"QComboBox {\n"
"  color: #1de9b6;\n"
"  background-color: #31363b;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;\n"
"}\n"
"\n"
"QRadioButton::indicator,\n"
"QCheckBox::indicator {\n"
"  width: 16px;\n"
"  height: 16px;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 0;\n"
"  transform: rotate(45deg);\n"
"  transform-origin: center;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover,\n"
"QCheckBox::indicator:hover {\n"
"  border-color: rgba(29, 233, 182, 0.8);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #1de9b6;\n"
"}")
        self.url_target_textedit = QtWidgets.QTextEdit(UrlToolsWindow)
        self.url_target_textedit.setGeometry(QtCore.QRect(520, 10, 351, 31))
        self.url_target_textedit.setToolTip("")
        self.url_target_textedit.setStatusTip("")
        self.url_target_textedit.setAccessibleName("")
        self.url_target_textedit.setAccessibleDescription("")
        self.url_target_textedit.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.url_target_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.url_target_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.url_target_textedit.setTabChangesFocus(True)
        self.url_target_textedit.setDocumentTitle("")
        self.url_target_textedit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.url_target_textedit.setMarkdown("")
        self.url_target_textedit.setObjectName("url_target_textedit")
        self.analytics_and_config_tab_widget = QtWidgets.QTabWidget(UrlToolsWindow)
        self.analytics_and_config_tab_widget.setEnabled(True)
        self.analytics_and_config_tab_widget.setGeometry(QtCore.QRect(490, 380, 691, 271))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.analytics_and_config_tab_widget.setFont(font)
        self.analytics_and_config_tab_widget.setStyleSheet("QTabWidget::pane {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 2px solid teal;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: teal;\n"
"    border-color: teal;\n"
"}")
        self.analytics_and_config_tab_widget.setObjectName("analytics_and_config_tab_widget")
        self.Analytics_Tab = QtWidgets.QWidget()
        self.Analytics_Tab.setObjectName("Analytics_Tab")
        self.captcha_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.captcha_button.setEnabled(True)
        self.captcha_button.setGeometry(QtCore.QRect(470, 40, 61, 24))
        self.captcha_button.setObjectName("captcha_button")
        self.cloudflare_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.cloudflare_button.setEnabled(True)
        self.cloudflare_button.setGeometry(QtCore.QRect(550, 40, 80, 24))
        self.cloudflare_button.setObjectName("cloudflare_button")
        self.akamai_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.akamai_button.setEnabled(True)
        self.akamai_button.setGeometry(QtCore.QRect(390, 40, 61, 24))
        self.akamai_button.setObjectName("akamai_button")
        self.http_request_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.http_request_button.setEnabled(True)
        self.http_request_button.setGeometry(QtCore.QRect(420, 10, 161, 24))
        self.http_request_button.setObjectName("http_request_button")
        self.alternatives_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.alternatives_button.setEnabled(True)
        self.alternatives_button.setGeometry(QtCore.QRect(30, 70, 81, 24))
        self.alternatives_button.setObjectName("alternatives_button")
        self.seo_data_details_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.seo_data_details_button.setEnabled(True)
        self.seo_data_details_button.setGeometry(QtCore.QRect(30, 10, 161, 24))
        self.seo_data_details_button.setObjectName("seo_data_details_button")
        self.sub_domains_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.sub_domains_button.setEnabled(True)
        self.sub_domains_button.setGeometry(QtCore.QRect(190, 40, 80, 24))
        self.sub_domains_button.setWhatsThis("")
        self.sub_domains_button.setObjectName("sub_domains_button")
        self.simalar_web_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.simalar_web_button.setEnabled(True)
        self.simalar_web_button.setGeometry(QtCore.QRect(30, 40, 80, 24))
        self.simalar_web_button.setObjectName("simalar_web_button")
        self.traffic_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.traffic_button.setEnabled(True)
        self.traffic_button.setGeometry(QtCore.QRect(120, 40, 61, 24))
        self.traffic_button.setObjectName("traffic_button")
        self.xpath_scraper_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.xpath_scraper_button.setEnabled(False)
        self.xpath_scraper_button.setGeometry(QtCore.QRect(530, 360, 81, 24))
        self.xpath_scraper_button.setObjectName("xpath_scraper_button")
        self.analyze_csp = QtWidgets.QPushButton(self.Analytics_Tab)
        self.analyze_csp.setEnabled(False)
        self.analyze_csp.setGeometry(QtCore.QRect(330, 360, 191, 24))
        self.analyze_csp.setObjectName("analyze_csp")
        self.check_url_login_directories = QtWidgets.QPushButton(self.Analytics_Tab)
        self.check_url_login_directories.setEnabled(True)
        self.check_url_login_directories.setGeometry(QtCore.QRect(120, 70, 101, 24))
        self.check_url_login_directories.setObjectName("check_url_login_directories")
        self.check_api_login_directories = QtWidgets.QPushButton(self.Analytics_Tab)
        self.check_api_login_directories.setEnabled(True)
        self.check_api_login_directories.setGeometry(QtCore.QRect(230, 70, 91, 24))
        self.check_api_login_directories.setObjectName("check_api_login_directories")
        self.website_bf_hidden_content_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.website_bf_hidden_content_button.setEnabled(True)
        self.website_bf_hidden_content_button.setGeometry(QtCore.QRect(20, 100, 161, 24))
        self.website_bf_hidden_content_button.setObjectName("website_bf_hidden_content_button")
        self.javascript_links_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.javascript_links_button.setEnabled(True)
        self.javascript_links_button.setGeometry(QtCore.QRect(190, 100, 111, 24))
        self.javascript_links_button.setObjectName("javascript_links_button")
        self.add_to_log_hunter_button = QtWidgets.QPushButton(self.Analytics_Tab)
        self.add_to_log_hunter_button.setGeometry(QtCore.QRect(549, 170, 121, 41))
        self.add_to_log_hunter_button.setObjectName("add_to_log_hunter_button")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-analytics-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics_and_config_tab_widget.addTab(self.Analytics_Tab, icon1, "")
        self.Config_Functions_Tab = QtWidgets.QWidget()
        self.Config_Functions_Tab.setObjectName("Config_Functions_Tab")
        self.config_function_get_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_get_button.setEnabled(True)
        self.config_function_get_button.setGeometry(QtCore.QRect(440, 20, 80, 24))
        self.config_function_get_button.setObjectName("config_function_get_button")
        self.config_function_post_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_post_button.setEnabled(True)
        self.config_function_post_button.setGeometry(QtCore.QRect(550, 20, 80, 24))
        self.config_function_post_button.setObjectName("config_function_post_button")
        self.config_function_headers_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_headers_button.setEnabled(True)
        self.config_function_headers_button.setGeometry(QtCore.QRect(440, 70, 80, 24))
        self.config_function_headers_button.setObjectName("config_function_headers_button")
        self.config_function_parse_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_parse_button.setEnabled(True)
        self.config_function_parse_button.setGeometry(QtCore.QRect(550, 70, 80, 24))
        self.config_function_parse_button.setObjectName("config_function_parse_button")
        self.config_function_html_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_html_button.setEnabled(True)
        self.config_function_html_button.setGeometry(QtCore.QRect(440, 110, 80, 24))
        self.config_function_html_button.setObjectName("config_function_html_button")
        self.config_function_css_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_css_button.setEnabled(True)
        self.config_function_css_button.setGeometry(QtCore.QRect(550, 110, 80, 24))
        self.config_function_css_button.setObjectName("config_function_css_button")
        self.config_function_referrer_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_referrer_button.setEnabled(True)
        self.config_function_referrer_button.setGeometry(QtCore.QRect(440, 150, 80, 24))
        self.config_function_referrer_button.setObjectName("config_function_referrer_button")
        self.config_function_put_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_put_button.setEnabled(True)
        self.config_function_put_button.setGeometry(QtCore.QRect(330, 20, 80, 24))
        self.config_function_put_button.setObjectName("config_function_put_button")
        self.config_function_delete_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_delete_button.setEnabled(True)
        self.config_function_delete_button.setGeometry(QtCore.QRect(330, 70, 80, 24))
        self.config_function_delete_button.setObjectName("config_function_delete_button")
        self.config_function_connect_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_connect_button.setEnabled(True)
        self.config_function_connect_button.setGeometry(QtCore.QRect(10, 20, 80, 24))
        self.config_function_connect_button.setObjectName("config_function_connect_button")
        self.config_function_options_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_options_button.setEnabled(True)
        self.config_function_options_button.setGeometry(QtCore.QRect(110, 20, 80, 24))
        self.config_function_options_button.setObjectName("config_function_options_button")
        self.config_function_trace_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_trace_button.setEnabled(True)
        self.config_function_trace_button.setGeometry(QtCore.QRect(210, 20, 80, 24))
        self.config_function_trace_button.setObjectName("config_function_trace_button")
        self.config_function_patch_button = QtWidgets.QPushButton(self.Config_Functions_Tab)
        self.config_function_patch_button.setEnabled(True)
        self.config_function_patch_button.setGeometry(QtCore.QRect(10, 60, 80, 24))
        self.config_function_patch_button.setObjectName("config_function_patch_button")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-administrative-tools-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics_and_config_tab_widget.addTab(self.Config_Functions_Tab, icon2, "")
        self.Website_Source_code_Tab = QtWidgets.QWidget()
        self.Website_Source_code_Tab.setObjectName("Website_Source_code_Tab")
        self.website_source_css_links_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_css_links_button.setEnabled(True)
        self.website_source_css_links_button.setGeometry(QtCore.QRect(150, 30, 81, 24))
        self.website_source_css_links_button.setObjectName("website_source_css_links_button")
        self.scrape_website_fonts_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.scrape_website_fonts_button.setEnabled(True)
        self.scrape_website_fonts_button.setGeometry(QtCore.QRect(250, 30, 111, 24))
        self.scrape_website_fonts_button.setObjectName("scrape_website_fonts_button")
        self.website_source_external_links = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_external_links.setEnabled(True)
        self.website_source_external_links.setGeometry(QtCore.QRect(380, 30, 111, 24))
        self.website_source_external_links.setObjectName("website_source_external_links")
        self.scrape_imagesbutton = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.scrape_imagesbutton.setEnabled(True)
        self.scrape_imagesbutton.setGeometry(QtCore.QRect(520, 30, 81, 24))
        self.scrape_imagesbutton.setObjectName("scrape_imagesbutton")
        self.website_source_get_core_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_get_core_button.setEnabled(True)
        self.website_source_get_core_button.setGeometry(QtCore.QRect(20, 70, 81, 24))
        self.website_source_get_core_button.setObjectName("website_source_get_core_button")
        self.website_source_page_details = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_page_details.setEnabled(True)
        self.website_source_page_details.setGeometry(QtCore.QRect(130, 110, 111, 24))
        self.website_source_page_details.setObjectName("website_source_page_details")
        self.website_source_js_links_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_js_links_button.setEnabled(True)
        self.website_source_js_links_button.setGeometry(QtCore.QRect(10, 110, 111, 24))
        self.website_source_js_links_button.setObjectName("website_source_js_links_button")
        self.website_source_whois = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_whois.setEnabled(True)
        self.website_source_whois.setGeometry(QtCore.QRect(260, 110, 111, 24))
        self.website_source_whois.setObjectName("website_source_whois")
        self.website_source_get_emails = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_get_emails.setEnabled(True)
        self.website_source_get_emails.setGeometry(QtCore.QRect(390, 110, 111, 24))
        self.website_source_get_emails.setObjectName("website_source_get_emails")
        self.website_source_getlinks = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_getlinks.setEnabled(True)
        self.website_source_getlinks.setGeometry(QtCore.QRect(520, 110, 111, 24))
        self.website_source_getlinks.setObjectName("website_source_getlinks")
        self.website_source_get_images_files_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_get_images_files_button.setEnabled(True)
        self.website_source_get_images_files_button.setGeometry(QtCore.QRect(450, 70, 91, 24))
        self.website_source_get_images_files_button.setObjectName("website_source_get_images_files_button")
        self.website_source_get_css_files_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_get_css_files_button.setEnabled(True)
        self.website_source_get_css_files_button.setGeometry(QtCore.QRect(330, 70, 111, 24))
        self.website_source_get_css_files_button.setObjectName("website_source_get_css_files_button")
        self.javascript_links_button_10 = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.javascript_links_button_10.setEnabled(False)
        self.javascript_links_button_10.setGeometry(QtCore.QRect(10, 360, 111, 24))
        self.javascript_links_button_10.setObjectName("javascript_links_button_10")
        self.website_source_getjs_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_getjs_button.setEnabled(True)
        self.website_source_getjs_button.setGeometry(QtCore.QRect(230, 70, 91, 24))
        self.website_source_getjs_button.setObjectName("website_source_getjs_button")
        self.website_source_headers_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_headers_button.setEnabled(True)
        self.website_source_headers_button.setGeometry(QtCore.QRect(110, 70, 111, 24))
        self.website_source_headers_button.setObjectName("website_source_headers_button")
        self.website_source_robots_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_robots_button.setEnabled(True)
        self.website_source_robots_button.setGeometry(QtCore.QRect(10, 150, 111, 24))
        self.website_source_robots_button.setObjectName("website_source_robots_button")
        self.website_source_detect_fonts_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_detect_fonts_button.setEnabled(True)
        self.website_source_detect_fonts_button.setGeometry(QtCore.QRect(410, 150, 111, 24))
        self.website_source_detect_fonts_button.setObjectName("website_source_detect_fonts_button")
        self.website_source_virus_total_stats_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_virus_total_stats_button.setEnabled(True)
        self.website_source_virus_total_stats_button.setGeometry(QtCore.QRect(140, 150, 111, 24))
        self.website_source_virus_total_stats_button.setObjectName("website_source_virus_total_stats_button")
        self.website_source_extract_colors_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_extract_colors_button.setEnabled(True)
        self.website_source_extract_colors_button.setGeometry(QtCore.QRect(530, 150, 101, 24))
        self.website_source_extract_colors_button.setObjectName("website_source_extract_colors_button")
        self.website_source_ip_location_button = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_ip_location_button.setEnabled(True)
        self.website_source_ip_location_button.setGeometry(QtCore.QRect(270, 150, 111, 24))
        self.website_source_ip_location_button.setObjectName("website_source_ip_location_button")
        self.website_source_css_links_button_2 = QtWidgets.QPushButton(self.Website_Source_code_Tab)
        self.website_source_css_links_button_2.setEnabled(True)
        self.website_source_css_links_button_2.setGeometry(QtCore.QRect(30, 30, 81, 24))
        self.website_source_css_links_button_2.setObjectName("website_source_css_links_button_2")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-source-code-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics_and_config_tab_widget.addTab(self.Website_Source_code_Tab, icon3, "")
        self.Quick_Brute_Tab = QtWidgets.QWidget()
        self.Quick_Brute_Tab.setObjectName("Quick_Brute_Tab")
        self.xpath_login_field_textedit = QtWidgets.QTextEdit(self.Quick_Brute_Tab)
        self.xpath_login_field_textedit.setGeometry(QtCore.QRect(30, 20, 191, 31))
        self.xpath_login_field_textedit.setObjectName("xpath_login_field_textedit")
        self.xpath_password_field_textedit = QtWidgets.QTextEdit(self.Quick_Brute_Tab)
        self.xpath_password_field_textedit.setGeometry(QtCore.QRect(30, 60, 191, 31))
        self.xpath_password_field_textedit.setObjectName("xpath_password_field_textedit")
        self.textEdit = QtWidgets.QTextEdit(self.Quick_Brute_Tab)
        self.textEdit.setGeometry(QtCore.QRect(230, 20, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.Quick_Brute_Tab)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 60, 221, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.Quick_Brute_Tab)
        self.comboBox.setGeometry(QtCore.QRect(480, 40, 131, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.Quick_Brute_Tab)
        self.label.setGeometry(QtCore.QRect(480, 10, 131, 16))
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.Quick_Brute_Tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(450, 170, 168, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-brute-force-attack-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics_and_config_tab_widget.addTab(self.Quick_Brute_Tab, icon4, "")
        self.Bot_Tools_Tab = QtWidgets.QWidget()
        self.Bot_Tools_Tab.setObjectName("Bot_Tools_Tab")
        self.telegram_bottools_token = QtWidgets.QTextEdit(self.Bot_Tools_Tab)
        self.telegram_bottools_token.setGeometry(QtCore.QRect(10, 20, 271, 31))
        self.telegram_bottools_token.setObjectName("telegram_bottools_token")
        self.telegram_chatID_bottools = QtWidgets.QTextEdit(self.Bot_Tools_Tab)
        self.telegram_chatID_bottools.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.telegram_chatID_bottools.setObjectName("telegram_chatID_bottools")
        self.telegram_groupID_bottools = QtWidgets.QTextEdit(self.Bot_Tools_Tab)
        self.telegram_groupID_bottools.setGeometry(QtCore.QRect(160, 70, 121, 31))
        self.telegram_groupID_bottools.setObjectName("telegram_groupID_bottools")
        self.telegram_groupID_bottools_2 = QtWidgets.QTextEdit(self.Bot_Tools_Tab)
        self.telegram_groupID_bottools_2.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.telegram_groupID_bottools_2.setObjectName("telegram_groupID_bottools_2")
        self.telegram_groupID_bottools_3 = QtWidgets.QTextEdit(self.Bot_Tools_Tab)
        self.telegram_groupID_bottools_3.setGeometry(QtCore.QRect(160, 120, 121, 31))
        self.telegram_groupID_bottools_3.setObjectName("telegram_groupID_bottools_3")
        self.results_window_textedit_4 = QtWidgets.QTextEdit(self.Bot_Tools_Tab)
        self.results_window_textedit_4.setGeometry(QtCore.QRect(440, 40, 181, 181))
        self.results_window_textedit_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_textedit_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_textedit_4.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.results_window_textedit_4.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.results_window_textedit_4.setObjectName("results_window_textedit_4")
        self.label_2 = QtWidgets.QLabel(self.Bot_Tools_Tab)
        self.label_2.setGeometry(QtCore.QRect(510, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.check_bot_stats_button = QtWidgets.QPushButton(self.Bot_Tools_Tab)
        self.check_bot_stats_button.setGeometry(QtCore.QRect(470, 10, 31, 21))
        self.check_bot_stats_button.setObjectName("check_bot_stats_button")
        self.forward_messages_button = QtWidgets.QPushButton(self.Bot_Tools_Tab)
        self.forward_messages_button.setGeometry(QtCore.QRect(320, 180, 111, 31))
        self.forward_messages_button.setObjectName("forward_messages_button")
        self.getUpdates_Button = QtWidgets.QPushButton(self.Bot_Tools_Tab)
        self.getUpdates_Button.setGeometry(QtCore.QRect(320, 130, 111, 31))
        self.getUpdates_Button.setObjectName("getUpdates_Button")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-bot-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics_and_config_tab_widget.addTab(self.Bot_Tools_Tab, icon5, "")
        self.results_textwindow_label = QtWidgets.QLabel(UrlToolsWindow)
        self.results_textwindow_label.setGeometry(QtCore.QRect(260, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(20)
        self.results_textwindow_label.setFont(font)
        self.results_textwindow_label.setObjectName("results_textwindow_label")
        self.connection_label = QtWidgets.QLabel(UrlToolsWindow)
        self.connection_label.setGeometry(QtCore.QRect(1030, 290, 131, 20))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(11)
        self.connection_label.setFont(font)
        self.connection_label.setObjectName("connection_label")
        self.console_keyboard_textedit = QtWidgets.QTextEdit(UrlToolsWindow)
        self.console_keyboard_textedit.setGeometry(QtCore.QRect(50, 360, 331, 31))
        self.console_keyboard_textedit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.console_keyboard_textedit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.console_keyboard_textedit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.console_keyboard_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.console_keyboard_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.console_keyboard_textedit.setTabChangesFocus(True)
        self.console_keyboard_textedit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.console_keyboard_textedit.setObjectName("console_keyboard_textedit")
        self.Website_Source_Code = QtWidgets.QTabWidget(UrlToolsWindow)
        self.Website_Source_Code.setGeometry(QtCore.QRect(530, 50, 431, 311))
        self.Website_Source_Code.setStyleSheet("QTabWidget::pane {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 2px solid teal;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: teal;\n"
"    border-color: teal;\n"
"}")
        self.Website_Source_Code.setObjectName("Website_Source_Code")
        self.Webpage_Veiw_TabWidget = QtWidgets.QWidget()
        self.Webpage_Veiw_TabWidget.setObjectName("Webpage_Veiw_TabWidget")
        self.wepage_veiw_scroll_area = QtWidgets.QScrollArea(self.Webpage_Veiw_TabWidget)
        self.wepage_veiw_scroll_area.setGeometry(QtCore.QRect(0, 0, 431, 271))
        self.wepage_veiw_scroll_area.setWidgetResizable(True)
        self.wepage_veiw_scroll_area.setObjectName("wepage_veiw_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 427, 267))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.wepage_veiw_scroll_area.setWidget(self.scrollAreaWidgetContents)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-web-view-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Website_Source_Code.addTab(self.Webpage_Veiw_TabWidget, icon6, "")
        self.WebsiteSourceCodeTab = QtWidgets.QWidget()
        self.WebsiteSourceCodeTab.setObjectName("WebsiteSourceCodeTab")
        self.console_data = QtWidgets.QPlainTextEdit(self.WebsiteSourceCodeTab)
        self.console_data.setGeometry(QtCore.QRect(0, 0, 431, 281))
        self.console_data.setObjectName("console_data")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-source-code-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Website_Source_Code.addTab(self.WebsiteSourceCodeTab, icon7, "")
        self.console_data_treeTab = QtWidgets.QWidget()
        self.console_data_treeTab.setObjectName("console_data_treeTab")
        self.console_data_treeView = QtWidgets.QTreeView(self.console_data_treeTab)
        self.console_data_treeView.setGeometry(QtCore.QRect(0, 0, 431, 271))
        self.console_data_treeView.setAutoExpandDelay(-1)
        self.console_data_treeView.setSortingEnabled(True)
        self.console_data_treeView.setAnimated(True)
        self.console_data_treeView.setAllColumnsShowFocus(True)
        self.console_data_treeView.setObjectName("console_data_treeView")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-rest-api-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Website_Source_Code.addTab(self.console_data_treeTab, icon8, "")
        self.save_results_path_checkbox = QtWidgets.QCheckBox(UrlToolsWindow)
        self.save_results_path_checkbox.setGeometry(QtCore.QRect(20, 620, 111, 22))
        self.save_results_path_checkbox.setObjectName("save_results_path_checkbox")
        self.save_results_path_textedit = QtWidgets.QTextEdit(UrlToolsWindow)
        self.save_results_path_textedit.setGeometry(QtCore.QRect(130, 619, 351, 31))
        self.save_results_path_textedit.setTabChangesFocus(True)
        self.save_results_path_textedit.setObjectName("save_results_path_textedit")
        self.send_response_console_button = QtWidgets.QPushButton(UrlToolsWindow)
        self.send_response_console_button.setGeometry(QtCore.QRect(380, 360, 80, 31))
        self.send_response_console_button.setObjectName("send_response_console_button")
        self.submit_web_button = QtWidgets.QPushButton(UrlToolsWindow)
        self.submit_web_button.setEnabled(True)
        self.submit_web_button.setGeometry(QtCore.QRect(880, 10, 80, 31))
        self.submit_web_button.setObjectName("submit_web_button")
        self.MainResults_Widget = QtWidgets.QTabWidget(UrlToolsWindow)
        self.MainResults_Widget.setGeometry(QtCore.QRect(30, 20, 401, 341))
        self.MainResults_Widget.setStyleSheet("QTabWidget::pane {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 2px solid teal;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: teal;\n"
"    border-color: teal;\n"
"}")
        self.MainResults_Widget.setObjectName("MainResults_Widget")
        self.main_results_tab = QtWidgets.QWidget()
        self.main_results_tab.setObjectName("main_results_tab")
        self.results_window_textedit_3 = QtWidgets.QTextEdit(self.main_results_tab)
        self.results_window_textedit_3.setGeometry(QtCore.QRect(0, 0, 401, 311))
        self.results_window_textedit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_textedit_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_textedit_3.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.results_window_textedit_3.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.results_window_textedit_3.setObjectName("results_window_textedit_3")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-grades-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainResults_Widget.addTab(self.main_results_tab, icon9, "")
        self.links_tab = QtWidgets.QWidget()
        self.links_tab.setObjectName("links_tab")
        self.results_window_links_text = QtWidgets.QTextEdit(self.links_tab)
        self.results_window_links_text.setGeometry(QtCore.QRect(0, 0, 401, 321))
        self.results_window_links_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_links_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_links_text.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.results_window_links_text.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.results_window_links_text.setObjectName("results_window_links_text")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../../Downloads/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainResults_Widget.addTab(self.links_tab, icon10, "")
        self.results_window_textedit_2 = QtWidgets.QTextEdit(UrlToolsWindow)
        self.results_window_textedit_2.setGeometry(QtCore.QRect(1000, 20, 191, 261))
        self.results_window_textedit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_textedit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_window_textedit_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.results_window_textedit_2.setLineWrapMode(QtWidgets.QTextEdit.FixedPixelWidth)
        self.results_window_textedit_2.setObjectName("results_window_textedit_2")
        self.tabWidget = QtWidgets.QTabWidget(UrlToolsWindow)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 390, 471, 221))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 2px solid teal;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: teal;\n"
"    border-color: teal;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.cookie_sql_inject_button = QtWidgets.QPushButton(self.tab)
        self.cookie_sql_inject_button.setEnabled(False)
        self.cookie_sql_inject_button.setGeometry(QtCore.QRect(350, 50, 111, 31))
        self.cookie_sql_inject_button.setObjectName("cookie_sql_inject_button")
        self.PLCs_button = QtWidgets.QPushButton(self.tab)
        self.PLCs_button.setEnabled(False)
        self.PLCs_button.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.PLCs_button.setObjectName("PLCs_button")
        self.google_dork_button = QtWidgets.QPushButton(self.tab)
        self.google_dork_button.setEnabled(False)
        self.google_dork_button.setGeometry(QtCore.QRect(10, 50, 91, 31))
        self.google_dork_button.setObjectName("google_dork_button")
        self.scadamode2_button = QtWidgets.QPushButton(self.tab)
        self.scadamode2_button.setEnabled(False)
        self.scadamode2_button.setGeometry(QtCore.QRect(110, 10, 91, 31))
        self.scadamode2_button.setObjectName("scadamode2_button")
        self.scadamode3_button = QtWidgets.QPushButton(self.tab)
        self.scadamode3_button.setEnabled(False)
        self.scadamode3_button.setGeometry(QtCore.QRect(250, 10, 91, 31))
        self.scadamode3_button.setObjectName("scadamode3_button")
        self.url_scan_api_button = QtWidgets.QPushButton(self.tab)
        self.url_scan_api_button.setEnabled(False)
        self.url_scan_api_button.setGeometry(QtCore.QRect(110, 90, 91, 31))
        self.url_scan_api_button.setObjectName("url_scan_api_button")
        self.link_diver_client_button = QtWidgets.QPushButton(self.tab)
        self.link_diver_client_button.setEnabled(False)
        self.link_diver_client_button.setGeometry(QtCore.QRect(250, 50, 91, 31))
        self.link_diver_client_button.setObjectName("link_diver_client_button")
        self.tor_mode_button = QtWidgets.QPushButton(self.tab)
        self.tor_mode_button.setEnabled(False)
        self.tor_mode_button.setGeometry(QtCore.QRect(350, 10, 91, 31))
        self.tor_mode_button.setObjectName("tor_mode_button")
        self.fake_headers_button = QtWidgets.QPushButton(self.tab)
        self.fake_headers_button.setEnabled(False)
        self.fake_headers_button.setGeometry(QtCore.QRect(10, 90, 91, 31))
        self.fake_headers_button.setObjectName("fake_headers_button")
        self.url_blaster_client_button_2 = QtWidgets.QPushButton(self.tab)
        self.url_blaster_client_button_2.setEnabled(False)
        self.url_blaster_client_button_2.setGeometry(QtCore.QRect(110, 50, 91, 31))
        self.url_blaster_client_button_2.setObjectName("url_blaster_client_button_2")
        self.tabWidget.addTab(self.tab, "")
        self.gather_tab_widget = QtWidgets.QWidget()
        self.gather_tab_widget.setObjectName("gather_tab_widget")
        self.gather_site_dossier_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_site_dossier_button.setEnabled(False)
        self.gather_site_dossier_button.setGeometry(QtCore.QRect(10, 10, 80, 31))
        self.gather_site_dossier_button.setObjectName("gather_site_dossier_button")
        self.gather_ssl_cert_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_ssl_cert_button.setEnabled(False)
        self.gather_ssl_cert_button.setGeometry(QtCore.QRect(100, 10, 80, 31))
        self.gather_ssl_cert_button.setObjectName("gather_ssl_cert_button")
        self.gather_sublister_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_sublister_button.setEnabled(False)
        self.gather_sublister_button.setGeometry(QtCore.QRect(190, 10, 80, 31))
        self.gather_sublister_button.setObjectName("gather_sublister_button")
        self.gather_wayback_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_wayback_button.setEnabled(False)
        self.gather_wayback_button.setGeometry(QtCore.QRect(280, 10, 80, 31))
        self.gather_wayback_button.setObjectName("gather_wayback_button")
        self.gather_mass_scan_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_mass_scan_button.setEnabled(False)
        self.gather_mass_scan_button.setGeometry(QtCore.QRect(380, 10, 80, 31))
        self.gather_mass_scan_button.setObjectName("gather_mass_scan_button")
        self.gather_oauth_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_oauth_button.setEnabled(False)
        self.gather_oauth_button.setGeometry(QtCore.QRect(10, 50, 80, 31))
        self.gather_oauth_button.setObjectName("gather_oauth_button")
        self.gather_affilates_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_affilates_button.setEnabled(False)
        self.gather_affilates_button.setGeometry(QtCore.QRect(100, 50, 80, 31))
        self.gather_affilates_button.setObjectName("gather_affilates_button")
        self.gather_viewDNS_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_viewDNS_button.setEnabled(False)
        self.gather_viewDNS_button.setGeometry(QtCore.QRect(190, 50, 80, 31))
        self.gather_viewDNS_button.setObjectName("gather_viewDNS_button")
        self.gather_fingerprint_x_button = QtWidgets.QPushButton(self.gather_tab_widget)
        self.gather_fingerprint_x_button.setEnabled(False)
        self.gather_fingerprint_x_button.setGeometry(QtCore.QRect(280, 50, 80, 31))
        self.gather_fingerprint_x_button.setObjectName("gather_fingerprint_x_button")
        self.tabWidget.addTab(self.gather_tab_widget, "")
        self.tools_tab_widget = QtWidgets.QWidget()
        self.tools_tab_widget.setObjectName("tools_tab_widget")
        self.gather_virus_total_button = QtWidgets.QPushButton(self.tools_tab_widget)
        self.gather_virus_total_button.setGeometry(QtCore.QRect(10, 10, 80, 31))
        self.gather_virus_total_button.setObjectName("gather_virus_total_button")
        self.gather_robots_button = QtWidgets.QPushButton(self.tools_tab_widget)
        self.gather_robots_button.setGeometry(QtCore.QRect(380, 130, 80, 31))
        self.gather_robots_button.setObjectName("gather_robots_button")
        self.gather_otx_alien_button = QtWidgets.QPushButton(self.tools_tab_widget)
        self.gather_otx_alien_button.setGeometry(QtCore.QRect(100, 10, 80, 31))
        self.gather_otx_alien_button.setObjectName("gather_otx_alien_button")
        self.gather_hunt_button = QtWidgets.QPushButton(self.tools_tab_widget)
        self.gather_hunt_button.setGeometry(QtCore.QRect(280, 10, 80, 31))
        self.gather_hunt_button.setObjectName("gather_hunt_button")
        self.gather_hacker_target_button = QtWidgets.QPushButton(self.tools_tab_widget)
        self.gather_hacker_target_button.setGeometry(QtCore.QRect(10, 50, 80, 31))
        self.gather_hacker_target_button.setObjectName("gather_hacker_target_button")
        self.gather_hunterio_button = QtWidgets.QPushButton(self.tools_tab_widget)
        self.gather_hunterio_button.setGeometry(QtCore.QRect(190, 10, 80, 31))
        self.gather_hunterio_button.setObjectName("gather_hunterio_button")
        self.tabWidget.addTab(self.tools_tab_widget, "")
        self.domains_tab_widget = QtWidgets.QWidget()
        self.domains_tab_widget.setObjectName("domains_tab_widget")
        self.gather_button_31 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_31.setGeometry(QtCore.QRect(100, 50, 80, 31))
        self.gather_button_31.setObjectName("gather_button_31")
        self.gather_button_32 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_32.setGeometry(QtCore.QRect(280, 50, 80, 31))
        self.gather_button_32.setObjectName("gather_button_32")
        self.gather_button_33 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_33.setGeometry(QtCore.QRect(190, 50, 80, 31))
        self.gather_button_33.setObjectName("gather_button_33")
        self.gather_button_34 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_34.setGeometry(QtCore.QRect(10, 10, 80, 31))
        self.gather_button_34.setObjectName("gather_button_34")
        self.gather_button_35 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_35.setGeometry(QtCore.QRect(100, 10, 80, 31))
        self.gather_button_35.setObjectName("gather_button_35")
        self.gather_button_36 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_36.setGeometry(QtCore.QRect(190, 10, 80, 31))
        self.gather_button_36.setObjectName("gather_button_36")
        self.gather_button_37 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_37.setGeometry(QtCore.QRect(380, 90, 80, 31))
        self.gather_button_37.setObjectName("gather_button_37")
        self.gather_button_38 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_38.setGeometry(QtCore.QRect(380, 10, 80, 31))
        self.gather_button_38.setObjectName("gather_button_38")
        self.gather_button_39 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_39.setGeometry(QtCore.QRect(280, 90, 80, 31))
        self.gather_button_39.setObjectName("gather_button_39")
        self.gather_button_40 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_40.setGeometry(QtCore.QRect(100, 90, 80, 31))
        self.gather_button_40.setObjectName("gather_button_40")
        self.gather_button_41 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_41.setGeometry(QtCore.QRect(10, 90, 80, 31))
        self.gather_button_41.setObjectName("gather_button_41")
        self.gather_button_42 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_42.setGeometry(QtCore.QRect(380, 50, 80, 31))
        self.gather_button_42.setObjectName("gather_button_42")
        self.gather_button_43 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_43.setGeometry(QtCore.QRect(10, 50, 80, 31))
        self.gather_button_43.setObjectName("gather_button_43")
        self.gather_button_44 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_44.setGeometry(QtCore.QRect(190, 90, 80, 31))
        self.gather_button_44.setObjectName("gather_button_44")
        self.gather_button_45 = QtWidgets.QPushButton(self.domains_tab_widget)
        self.gather_button_45.setGeometry(QtCore.QRect(280, 10, 80, 31))
        self.gather_button_45.setObjectName("gather_button_45")
        self.tabWidget.addTab(self.domains_tab_widget, "")
        self.vulnerabilities_tab_widget = QtWidgets.QWidget()
        self.vulnerabilities_tab_widget.setObjectName("vulnerabilities_tab_widget")
        self.gather_bypass_403_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_bypass_403_button.setGeometry(QtCore.QRect(100, 50, 80, 31))
        self.gather_bypass_403_button.setObjectName("gather_bypass_403_button")
        self.gather_internet_db_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_internet_db_button.setGeometry(QtCore.QRect(280, 50, 80, 31))
        self.gather_internet_db_button.setObjectName("gather_internet_db_button")
        self.gather_choas_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_choas_button.setGeometry(QtCore.QRect(190, 50, 80, 31))
        self.gather_choas_button.setObjectName("gather_choas_button")
        self.gather_subdomain_hijack_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_subdomain_hijack_button.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.gather_subdomain_hijack_button.setObjectName("gather_subdomain_hijack_button")
        self.gather_secrets_db_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_secrets_db_button.setGeometry(QtCore.QRect(140, 10, 80, 31))
        self.gather_secrets_db_button.setObjectName("gather_secrets_db_button")
        self.gather_url_manipulation_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_url_manipulation_button.setGeometry(QtCore.QRect(340, 10, 121, 31))
        self.gather_url_manipulation_button.setObjectName("gather_url_manipulation_button")
        self.gather_bad_secrets_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_bad_secrets_button.setGeometry(QtCore.QRect(10, 50, 80, 31))
        self.gather_bad_secrets_button.setObjectName("gather_bad_secrets_button")
        self.gather_threat_miner_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_threat_miner_button.setGeometry(QtCore.QRect(240, 10, 80, 31))
        self.gather_threat_miner_button.setObjectName("gather_threat_miner_button")
        self.gather_paramma_miner_get_params_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_paramma_miner_get_params_button.setGeometry(QtCore.QRect(150, 90, 161, 31))
        self.gather_paramma_miner_get_params_button.setObjectName("gather_paramma_miner_get_params_button")
        self.gather_parama_minner_cookies_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_parama_minner_cookies_button.setGeometry(QtCore.QRect(10, 90, 131, 31))
        self.gather_parama_minner_cookies_button.setObjectName("gather_parama_minner_cookies_button")
        self.gather_paramma_miners_headers_button = QtWidgets.QPushButton(self.vulnerabilities_tab_widget)
        self.gather_paramma_miners_headers_button.setGeometry(QtCore.QRect(320, 90, 141, 31))
        self.gather_paramma_miners_headers_button.setObjectName("gather_paramma_miners_headers_button")
        self.tabWidget.addTab(self.vulnerabilities_tab_widget, "")
        self.leaking_tab_widget = QtWidgets.QWidget()
        self.leaking_tab_widget.setObjectName("leaking_tab_widget")
        self.gather_button_62 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_62.setGeometry(QtCore.QRect(280, 50, 80, 31))
        self.gather_button_62.setObjectName("gather_button_62")
        self.gather_button_63 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_63.setGeometry(QtCore.QRect(190, 50, 80, 31))
        self.gather_button_63.setObjectName("gather_button_63")
        self.gather_button_64 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_64.setGeometry(QtCore.QRect(10, 10, 80, 31))
        self.gather_button_64.setObjectName("gather_button_64")
        self.gather_button_65 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_65.setGeometry(QtCore.QRect(100, 10, 80, 31))
        self.gather_button_65.setObjectName("gather_button_65")
        self.gather_button_66 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_66.setGeometry(QtCore.QRect(190, 10, 80, 31))
        self.gather_button_66.setObjectName("gather_button_66")
        self.gather_button_68 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_68.setGeometry(QtCore.QRect(380, 10, 80, 31))
        self.gather_button_68.setObjectName("gather_button_68")
        self.gather_button_71 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_71.setGeometry(QtCore.QRect(10, 90, 80, 31))
        self.gather_button_71.setObjectName("gather_button_71")
        self.gather_button_72 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_72.setGeometry(QtCore.QRect(380, 50, 80, 31))
        self.gather_button_72.setObjectName("gather_button_72")
        self.gather_button_73 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_73.setGeometry(QtCore.QRect(10, 50, 80, 31))
        self.gather_button_73.setObjectName("gather_button_73")
        self.gather_button_75 = QtWidgets.QPushButton(self.leaking_tab_widget)
        self.gather_button_75.setGeometry(QtCore.QRect(280, 10, 80, 31))
        self.gather_button_75.setObjectName("gather_button_75")
        self.tabWidget.addTab(self.leaking_tab_widget, "")

        self.retranslateUi(UrlToolsWindow)
        self.analytics_and_config_tab_widget.setCurrentIndex(0)
        self.Website_Source_Code.setCurrentIndex(0)
        self.MainResults_Widget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(3)
        self.simalar_web_button.clicked['bool'].connect(self.results_textwindow_label.update) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(UrlToolsWindow)

    def retranslateUi(self, UrlToolsWindow):
        _translate = QtCore.QCoreApplication.translate
        UrlToolsWindow.setWindowTitle(_translate("UrlToolsWindow", "Diamond Sorter - URL Analysis"))
        self.url_target_textedit.setWhatsThis(_translate("UrlToolsWindow", "URL Target"))
        self.url_target_textedit.setPlaceholderText(_translate("UrlToolsWindow", "https://website-request.com/ or http://request.website.com"))
        self.captcha_button.setText(_translate("UrlToolsWindow", "Captcha"))
        self.cloudflare_button.setText(_translate("UrlToolsWindow", "Cloudflare"))
        self.akamai_button.setText(_translate("UrlToolsWindow", "Akamai"))
        self.http_request_button.setToolTip(_translate("UrlToolsWindow", "Display a HTTP Request Client to see live time stats and info."))
        self.http_request_button.setText(_translate("UrlToolsWindow", "HTTP Request Client"))
        self.alternatives_button.setToolTip(_translate("UrlToolsWindow", "Discover simalar websites and alternatives"))
        self.alternatives_button.setText(_translate("UrlToolsWindow", "Alternatives"))
        self.seo_data_details_button.setToolTip(_translate("UrlToolsWindow", "Get the basic information and stats of your request by SEO"))
        self.seo_data_details_button.setText(_translate("UrlToolsWindow", "SEO Data and Details"))
        self.sub_domains_button.setToolTip(_translate("UrlToolsWindow", "Scan for any related subdomains of the requested website"))
        self.sub_domains_button.setText(_translate("UrlToolsWindow", "Sub Domains"))
        self.simalar_web_button.setToolTip(_translate("UrlToolsWindow", "Find websites simalar to the one based on your request"))
        self.simalar_web_button.setText(_translate("UrlToolsWindow", "Simalar Web"))
        self.traffic_button.setToolTip(_translate("UrlToolsWindow", "Display any traffic stats based on your target"))
        self.traffic_button.setText(_translate("UrlToolsWindow", "Traffic"))
        self.xpath_scraper_button.setText(_translate("UrlToolsWindow", "XPath Scraper"))
        self.analyze_csp.setText(_translate("UrlToolsWindow", "Analyze Content-Security-Policy"))
        self.check_url_login_directories.setToolTip(_translate("UrlToolsWindow", "This will scan the requested website for any possible URL Login pages"))
        self.check_url_login_directories.setText(_translate("UrlToolsWindow", "Check URL Logins"))
        self.check_api_login_directories.setToolTip(_translate("UrlToolsWindow", "This will scan your requested URL for any API endpoints"))
        self.check_api_login_directories.setText(_translate("UrlToolsWindow", "Check API Login"))
        self.website_bf_hidden_content_button.setToolTip(_translate("UrlToolsWindow", "Website bruteforcer to find hidden file and folder\n"
"Requires a wordlist to be used"))
        self.website_bf_hidden_content_button.setWhatsThis(_translate("UrlToolsWindow", "Website bruteforcer to find hidden file and folder\n"
"Requires a wordlist to be used"))
        self.website_bf_hidden_content_button.setText(_translate("UrlToolsWindow", "Website BF Hidden Content"))
        self.javascript_links_button.setText(_translate("UrlToolsWindow", "Javascript Links"))
        self.add_to_log_hunter_button.setText(_translate("UrlToolsWindow", "Add To Log Hunter"))
        self.analytics_and_config_tab_widget.setTabText(self.analytics_and_config_tab_widget.indexOf(self.Analytics_Tab), _translate("UrlToolsWindow", "Analytics"))
        self.config_function_get_button.setText(_translate("UrlToolsWindow", "GET"))
        self.config_function_post_button.setText(_translate("UrlToolsWindow", "POST"))
        self.config_function_headers_button.setText(_translate("UrlToolsWindow", "HEADERS"))
        self.config_function_parse_button.setText(_translate("UrlToolsWindow", "PARSE"))
        self.config_function_html_button.setText(_translate("UrlToolsWindow", "HTML"))
        self.config_function_css_button.setText(_translate("UrlToolsWindow", "CSS"))
        self.config_function_referrer_button.setText(_translate("UrlToolsWindow", "Referrer"))
        self.config_function_put_button.setText(_translate("UrlToolsWindow", "PUT"))
        self.config_function_delete_button.setText(_translate("UrlToolsWindow", "DELETE"))
        self.config_function_connect_button.setText(_translate("UrlToolsWindow", "CONNECT"))
        self.config_function_options_button.setText(_translate("UrlToolsWindow", "OPTIONS"))
        self.config_function_trace_button.setText(_translate("UrlToolsWindow", "TRACE"))
        self.config_function_patch_button.setText(_translate("UrlToolsWindow", "PATCH"))
        self.analytics_and_config_tab_widget.setTabText(self.analytics_and_config_tab_widget.indexOf(self.Config_Functions_Tab), _translate("UrlToolsWindow", "Config Functions"))
        self.website_source_css_links_button.setText(_translate("UrlToolsWindow", "CSS Links"))
        self.scrape_website_fonts_button.setText(_translate("UrlToolsWindow", "Grab Website Font"))
        self.website_source_external_links.setText(_translate("UrlToolsWindow", "External Links"))
        self.scrape_imagesbutton.setText(_translate("UrlToolsWindow", "Images"))
        self.website_source_get_core_button.setText(_translate("UrlToolsWindow", "Get Core"))
        self.website_source_page_details.setText(_translate("UrlToolsWindow", "Page Details"))
        self.website_source_js_links_button.setText(_translate("UrlToolsWindow", "Javascript Links"))
        self.website_source_whois.setText(_translate("UrlToolsWindow", "WhoIs"))
        self.website_source_get_emails.setText(_translate("UrlToolsWindow", "Get Emails"))
        self.website_source_getlinks.setText(_translate("UrlToolsWindow", "Get links"))
        self.website_source_get_images_files_button.setText(_translate("UrlToolsWindow", "Get Images Files"))
        self.website_source_get_css_files_button.setText(_translate("UrlToolsWindow", "Get CSS Files"))
        self.javascript_links_button_10.setText(_translate("UrlToolsWindow", "Get Cookies"))
        self.website_source_getjs_button.setText(_translate("UrlToolsWindow", "Get js files"))
        self.website_source_headers_button.setText(_translate("UrlToolsWindow", "Get Headers"))
        self.website_source_robots_button.setText(_translate("UrlToolsWindow", "Robots"))
        self.website_source_detect_fonts_button.setText(_translate("UrlToolsWindow", "Detect-Fonts"))
        self.website_source_virus_total_stats_button.setText(_translate("UrlToolsWindow", "Virus Total"))
        self.website_source_extract_colors_button.setText(_translate("UrlToolsWindow", "Extract-Colors"))
        self.website_source_ip_location_button.setText(_translate("UrlToolsWindow", "IP Location"))
        self.website_source_css_links_button_2.setText(_translate("UrlToolsWindow", "Get Request"))
        self.analytics_and_config_tab_widget.setTabText(self.analytics_and_config_tab_widget.indexOf(self.Website_Source_code_Tab), _translate("UrlToolsWindow", "Website Source Code Content"))
        self.xpath_login_field_textedit.setPlaceholderText(_translate("UrlToolsWindow", "xPath for the login field"))
        self.xpath_password_field_textedit.setPlaceholderText(_translate("UrlToolsWindow", " xPath for the field password"))
        self.textEdit.setPlaceholderText(_translate("UrlToolsWindow", "xPath to enter the confirmation button."))
        self.textEdit_2.setPlaceholderText(_translate("UrlToolsWindow", "xPath fo successful authorization conditions"))
        self.comboBox.setItemText(1, _translate("UrlToolsWindow", "Firefox"))
        self.comboBox.setItemText(2, _translate("UrlToolsWindow", "Chrome"))
        self.comboBox.setItemText(3, _translate("UrlToolsWindow", "Internet Explorer"))
        self.label.setText(_translate("UrlToolsWindow", "Browser Driver Choice"))
        self.commandLinkButton.setText(_translate("UrlToolsWindow", "Run Brute Force"))
        self.analytics_and_config_tab_widget.setTabText(self.analytics_and_config_tab_widget.indexOf(self.Quick_Brute_Tab), _translate("UrlToolsWindow", "Quick Brute"))
        self.telegram_bottools_token.setPlaceholderText(_translate("UrlToolsWindow", "Telegram Bot ID ( From Botfather )"))
        self.telegram_chatID_bottools.setPlaceholderText(_translate("UrlToolsWindow", "Telegram Chat ID"))
        self.telegram_groupID_bottools.setPlaceholderText(_translate("UrlToolsWindow", "Telegram Group ID"))
        self.telegram_groupID_bottools_2.setPlaceholderText(_translate("UrlToolsWindow", "Target Group ID"))
        self.telegram_groupID_bottools_3.setPlaceholderText(_translate("UrlToolsWindow", "Target Channel ID"))
        self.label_2.setText(_translate("UrlToolsWindow", "Bot Stats"))
        self.check_bot_stats_button.setText(_translate("UrlToolsWindow", "✅"))
        self.forward_messages_button.setText(_translate("UrlToolsWindow", "Forward Messages"))
        self.getUpdates_Button.setText(_translate("UrlToolsWindow", "/getUpdate"))
        self.analytics_and_config_tab_widget.setTabText(self.analytics_and_config_tab_widget.indexOf(self.Bot_Tools_Tab), _translate("UrlToolsWindow", "Bot Tools"))
        self.results_textwindow_label.setText(_translate("UrlToolsWindow", "Results"))
        self.connection_label.setText(_translate("UrlToolsWindow", "Connection Details"))
        self.console_keyboard_textedit.setPlaceholderText(_translate("UrlToolsWindow", "Your console Response Entry Field"))
        self.Website_Source_Code.setTabText(self.Website_Source_Code.indexOf(self.Webpage_Veiw_TabWidget), _translate("UrlToolsWindow", "Webpage Veiw"))
        self.Website_Source_Code.setTabText(self.Website_Source_Code.indexOf(self.WebsiteSourceCodeTab), _translate("UrlToolsWindow", "Website Source Code"))
        self.Website_Source_Code.setTabText(self.Website_Source_Code.indexOf(self.console_data_treeTab), _translate("UrlToolsWindow", "Website API"))
        self.save_results_path_checkbox.setText(_translate("UrlToolsWindow", "Save Results?"))
        self.save_results_path_textedit.setPlaceholderText(_translate("UrlToolsWindow", "Saved File Directory Path"))
        self.send_response_console_button.setText(_translate("UrlToolsWindow", "Response"))
        self.submit_web_button.setText(_translate("UrlToolsWindow", "Submit Web"))
        self.MainResults_Widget.setTabText(self.MainResults_Widget.indexOf(self.main_results_tab), _translate("UrlToolsWindow", "Main Results"))
        self.MainResults_Widget.setTabText(self.MainResults_Widget.indexOf(self.links_tab), _translate("UrlToolsWindow", "Links"))
        self.MainResults_Widget.setTabToolTip(self.MainResults_Widget.indexOf(self.links_tab), _translate("UrlToolsWindow", "Any of your functions with \"Link\" results will show in this tab"))
        self.cookie_sql_inject_button.setText(_translate("UrlToolsWindow", "Cookie SQL Inject"))
        self.PLCs_button.setText(_translate("UrlToolsWindow", "PLCs"))
        self.google_dork_button.setText(_translate("UrlToolsWindow", "Google Mode"))
        self.scadamode2_button.setText(_translate("UrlToolsWindow", "Sacada 2 Mode"))
        self.scadamode3_button.setText(_translate("UrlToolsWindow", "Sacada 3 Mode"))
        self.url_scan_api_button.setText(_translate("UrlToolsWindow", "URL Scan API"))
        self.link_diver_client_button.setText(_translate("UrlToolsWindow", "Link Diver"))
        self.tor_mode_button.setText(_translate("UrlToolsWindow", "TOR Mode"))
        self.fake_headers_button.setText(_translate("UrlToolsWindow", "Fake Headers"))
        self.url_blaster_client_button_2.setText(_translate("UrlToolsWindow", "URL Blaster"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("UrlToolsWindow", "Research"))
        self.gather_site_dossier_button.setText(_translate("UrlToolsWindow", "Site Dossier"))
        self.gather_ssl_cert_button.setText(_translate("UrlToolsWindow", "SSL Cert"))
        self.gather_sublister_button.setText(_translate("UrlToolsWindow", "Sublist3r"))
        self.gather_wayback_button.setText(_translate("UrlToolsWindow", "Wayback"))
        self.gather_mass_scan_button.setText(_translate("UrlToolsWindow", "MASScan"))
        self.gather_oauth_button.setText(_translate("UrlToolsWindow", "OAuth"))
        self.gather_affilates_button.setText(_translate("UrlToolsWindow", "Affiliates"))
        self.gather_viewDNS_button.setText(_translate("UrlToolsWindow", "View DNS"))
        self.gather_fingerprint_x_button.setText(_translate("UrlToolsWindow", "Fingerprint X"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gather_tab_widget), _translate("UrlToolsWindow", "Gather"))
        self.gather_virus_total_button.setText(_translate("UrlToolsWindow", "Virus Total"))
        self.gather_robots_button.setText(_translate("UrlToolsWindow", "Robots"))
        self.gather_otx_alien_button.setText(_translate("UrlToolsWindow", "OTX Alien"))
        self.gather_hunt_button.setText(_translate("UrlToolsWindow", "Hunt"))
        self.gather_hacker_target_button.setText(_translate("UrlToolsWindow", "Hacker Target"))
        self.gather_hunterio_button.setText(_translate("UrlToolsWindow", "Hunterio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tools_tab_widget), _translate("UrlToolsWindow", "Tools"))
        self.gather_button_31.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_32.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_33.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_34.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_35.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_36.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_37.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_38.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_39.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_40.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_41.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_42.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_43.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_44.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_45.setText(_translate("UrlToolsWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.domains_tab_widget), _translate("UrlToolsWindow", "Domains"))
        self.gather_bypass_403_button.setText(_translate("UrlToolsWindow", "Bypass403"))
        self.gather_internet_db_button.setText(_translate("UrlToolsWindow", "Internet DB"))
        self.gather_choas_button.setText(_translate("UrlToolsWindow", "Choas"))
        self.gather_subdomain_hijack_button.setText(_translate("UrlToolsWindow", "Subdomain Hijack"))
        self.gather_secrets_db_button.setText(_translate("UrlToolsWindow", "Secrets DB"))
        self.gather_url_manipulation_button.setText(_translate("UrlToolsWindow", " URL Manipulation"))
        self.gather_bad_secrets_button.setText(_translate("UrlToolsWindow", "Bad Secrets"))
        self.gather_threat_miner_button.setText(_translate("UrlToolsWindow", "Threat Miner"))
        self.gather_paramma_miner_get_params_button.setText(_translate("UrlToolsWindow", "Param Miner Get Params"))
        self.gather_parama_minner_cookies_button.setText(_translate("UrlToolsWindow", "Param Miner Cookies"))
        self.gather_paramma_miners_headers_button.setText(_translate("UrlToolsWindow", "Param Miner Headers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vulnerabilities_tab_widget), _translate("UrlToolsWindow", "Vulnerabilities"))
        self.gather_button_62.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_63.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_64.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_65.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_66.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_68.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_71.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_72.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_73.setText(_translate("UrlToolsWindow", "PushButton"))
        self.gather_button_75.setText(_translate("UrlToolsWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.leaking_tab_widget), _translate("UrlToolsWindow", "Leaking"))


        self.config_function_post_button.clicked.connect(self.perform_config_function_post)


        self.config_function_post_button.clicked.connect(self.perform_config_function_post)
        self.config_function_get_button.clicked.connect(self.handle_get_request)
        self.config_function_post_button.clicked.connect(self.handle_post_request)
        self.config_function_patch_button.clicked.connect(self.handle_patch_request)
        self.website_source_headers_button.clicked.connect(self.handle_head_request)
        self.http_request_button.clicked.connect(self.handle_options_request)
        self.config_function_put_button.clicked.connect(self.handle_put_request)
        self.config_function_trace_button.clicked.connect(self.handle_trace_request)
        self.config_function_headers_button.clicked.connect(self.handle_config_function_headers)
        self.website_source_css_links_button.clicked.connect(self.css_links)
        self.scrape_website_fonts_button.clicked.connect(self.get_font_links)
        self.scrape_imagesbutton.clicked.connect(self.handle_image_urls_button_click)
        self.cloudflare_button.clicked.connect(self.cloudflare_button_clicked)
        self.xpath_scraper_button.clicked.connect(self.xpath_scraper_button_function)
        self.simalar_web_button.clicked.connect(self.simalar_web_button_function)
        self.http_request_button.clicked.connect(self.http_request_button_function)
        self.captcha_button.clicked.connect(self.captcha_button_function)
        self.akamai_button.clicked.connect(self.akamai_button_function)
        self.seo_data_details_button.clicked.connect(self.seo_data_details_button_function)
        self.sub_domains_button.clicked.connect(self.sub_domains_button_function)
        self.traffic_button.clicked.connect(self.traffic_button_function)
        self.captcha_button.clicked.connect(self.captcha_button_function)
        self.check_url_login_directories.clicked.connect(self.check_url_login_directories_functions)
        self.check_api_login_directories.clicked.connect(self.check_api_login_directories_function)
        self.website_source_external_links.clicked.connect(self.handle_external_links_button_click)
        self.gather_subdomain_hijack_button.clicked.connect(self.on_gather_subdomain_hijack_clicked)
        self.submit_web_button.clicked.connect(lambda: self.on_submit_web_button_clicked(self.url_target_textedit, self.webpage_view_tabwidget))
        self.alternatives_button.clicked.connect(self.alternatives_button_function)

        self.webpage_view_tabwidget = QtWidgets.QTabWidget(UrlToolsWindow)
        self.webpage_view_tabwidget.setObjectName("webpage_view_tabwidget")
        self.add_to_log_hunter_button.clicked.connect(self.add_to_log_hunter_button_clicked)
    
    def add_to_log_hunter_button_clicked(self):
        url = self.url_target_textedit.toPlainText().strip()
        full_url = f"https://web-check.xyz/results/{url}"
        
        # Perform the parsing logic using the full_url
        # Fetch the webpage and extract the desired information
        
        # Example code for fetching the webpage using requests library
        import requests
        response = requests.get(full_url)
        if response.status_code == 200:
            # Extract the desired information from the response content
            # Process and store the information in the database
        
            # Example code for storing the information in the cookie_data.db database
            script_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(script_dir, "cookie_data.db")
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
        
            # Define the table schema if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS cookies (
                request_datetime TEXT,
                type TEXT,
                domain TEXT,
                cookie_name TEXT,
                cookie_id TEXT,
                description TEXT,
                duration TEXT,
                storage_type TEXT,
                url TEXT
            )
            """
            cursor.execute(create_table_query)
        
            # Store the parsed data in the database
            # Replace the placeholders with the actual parsed data
            insert_data_query = "INSERT INTO cookies (request_datetime, type, domain, cookie_name, cookie_id, description, duration, storage_type, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            data = [
                # Replace with actual parsed data
                ("2022-01-01", "Type1", "example.com", "Cookie1", "123", "Description1", "1 day", "Storage1", "https://example.com"),
                ("2022-01-02", "Type2", "example.com", "Cookie2", "456", "Description2", "2 days", "Storage2", "https://example.com")
            ]
            cursor.executemany(insert_data_query, data)
        
            # Commit the changes
            conn.commit()
        
            # Get all the data from the database
            select_query = "SELECT * FROM cookies"
            cursor.execute(select_query)
            all_data = cursor.fetchall()
        
            # Get the total count of everything in the database
            count_query = "SELECT COUNT(*) FROM cookies"
            cursor.execute(count_query)
            total_count = cursor.fetchone()[0]
        
            # Close the database connection
            conn.close()
        
            # Display the information in results_window_textedit_2
            self.results_window_textedit_2.clear()
            self.results_window_textedit_2.append(f"Total count: {total_count}")
            for row in all_data:
                self.results_window_textedit_2.append(str(row))
        
        else:
            # Handle error when fetching the webpage
            pass



    def alternatives_button_function(self):
        website = self.url_target_textedit.toPlainText().strip()
    
        # Construct the API URL
        api_url = f"https://data.similarweb.com/api/v1/data?domain={website}"
    
        try:
            # Send a request to the API
            response = requests.get(api_url)
    
            # Check if the response contains valid JSON
            if response.status_code == 200:
                try:
                    data = response.json()
    
                    # Display the results
                    self.results_window_textedit_3.clear()
                    self.results_window_textedit_3.append(f"Results for {website}:")
                    self.results_window_textedit_3.append(json.dumps(data, indent=4))  # Display the API response data
    
                    # Add the flashing effect to the tab
                    tab_index = self.results_window_tabwidget.indexOf(self.results_tab_3)
                    self.results_window_tabwidget.setTabData(tab_index, "flashing-tab")
    
                except json.JSONDecodeError:
                    self.results_window_textedit_3.clear()
                    self.results_window_textedit_3.append("Invalid JSON response from the API.")
    
            else:
                self.results_window_textedit_3.clear()
                self.results_window_textedit_3.append("Error fetching data from the API.")
    
        except requests.exceptions.RequestException as e:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("An error occurred while fetching data from the API.")
            error_dialog.setDetailedText(str(e))
            error_dialog.exec_()
        
    











        self.webpage_view_tabwidget = QtWidgets.QTabWidget(UrlToolsWindow)
        self.webpage_view_tabwidget.setObjectName("webpage_view_tabwidget")
        # Set up the tab widget with tabs and other properties
        
        # Connect the signal with the correct attribute
        self.submit_web_button.clicked.connect(lambda: self.on_submit_web_button_clicked(self.url_target_textedit, self.webpage_view_tabwidget))
    
    def on_submit_web_button_clicked(self, url_target_textedit, webpage_view_tabwidget):
        url = url_target_textedit.toPlainText()

        # Create a QWebEngineView
        web_view = QtWebEngineWidgets.QWebEngineView()
        web_view.load(QtCore.QUrl(url))

        # Add the web view to the webpage_view_tabwidget
        webpage_view_tabwidget.addTab(web_view, "Webpage")



    def on_gather_subdomain_hijack_clicked(url_target_textedit, results_window_textedit_3):
        target_url = self.url_target_textedit.toPlainText()
        fingerprints_url = "https://raw.githubusercontent.com/EdOverflow/can-i-take-over-xyz/master/fingerprints.json"
        fingerprints = json.loads(httpx.get(fingerprints_url).text)
    
        if hijackable:
            # Display the results in results_window_textedit_3
            results_window_textedit_3.setPlainText(f"Hijackable Subdomain: {target_url}\nReason: {reason}")
        else:
            print(f"Subdomain {target_url} not hijackable")





    def check_url_login_directories_functions(self):
        url = self.url_target_textedit.toPlainText().strip()
    
        try:
            # Perform subdomain and path scanning for login-related keywords
            keywords = ["login", "signin", "account", "sign in"]
            results = []
    
            # Check subdomains
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            subdomains = ["www"]  # Add any common subdomains to check
            for subdomain in subdomains:
                subdomain_url = f"http://{subdomain}.{domain}"
                response = requests.get(subdomain_url)
                if any(keyword in response.text.lower() for keyword in keywords):
                    results.append(subdomain_url)
    
            # Check paths
            paths = ["/login", "/signin", "/account", "/sign-in"]  # Add any other common login paths
            for path in paths:
                path_url = f"{url.rstrip('/')}{path}"
                response = requests.get(path_url)
                if any(keyword in response.text.lower() for keyword in keywords):
                    results.append(path_url)
    
            # Example code to append results to the widget
            if results:
                result = "Login-related subdomains or paths found:\n" + "\n".join(results)
            else:
                result = "No login-related subdomains or paths found"
            self.results_window_textedit_3.append(result)
    
        except requests.exceptions.RequestException as e:
            self.results_window_textedit_3.append(f"Error: {e}")


    def get_metadata(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tags = soup.find_all('meta')
            metadata = []
            for tag in meta_tags:
                meta_info = tag.get('name') or tag.get('property') or tag.get('http-equiv')
                if meta_info and len(meta_info) <= 50:
                    content = tag.get('content')
                    if content:
                        metadata.append((meta_info, content))
            return metadata
        except requests.exceptions.RequestException:
            return []


    def xpath_scraper_button_function(self):
        url = self.url_target_textedit.toPlainText().strip()
    
        try:
            response = requests.get(url)
            html = response.text
            
            # Create an lxml ElementTree from the HTML
            tree = etree.HTML(html)
            
            # Perform XPath queries and extract information
            # ...
            
            # Example code to print the XPath-related information
            print("XPath Information:")
            # ...
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")




    def simalar_web_button_function(self):
        # Get the target URL from the text input field
        target_url = self.url_target_textedit.toPlainText()
    
        # Determine the domain from the target URL
        target_domain = urlparse(target_url).netloc
    
        # List to store the extracted URLs
        similar_domains = []
    
        try:
            # Send a request to the target URL
            response = requests.get(target_url)
    
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
    
            # Find all anchor tags within the parsed HTML
            anchor_tags = soup.find_all('a')
    
            for tag in anchor_tags:
                # Extract the href attribute of each anchor tag
                href = tag.get('href')
    
                if href:
                    # Join the URL with the extracted href
                    absolute_url = urljoin(target_url, href)
    
                    # Parse the absolute URL to get the domain
                    parsed_url = urlparse(absolute_url)
                    domain = parsed_url.netloc
    
                    if domain == target_domain:
                        # Add the similar domain URL to the list
                        similar_domains.append(absolute_url)
    
        except Exception as e:
            # Handle any errors that occur during the crawling process
            print(f"Error occurred during crawling: {e}")
            return
    
        # Clear the text in the results window text widget
        self.results_window_links_text.clear()
    
        # Display the results in the results window text widget
        for url in similar_domains:
            self.results_window_links_text.append(url)



    def http_request_button_function(self):
        url = self.url_target_textedit.toPlainText().strip()
        
        try:
            response = requests.get(url)
            
            # Process the response as needed
            print("HTTP Request Response:")
            print(f"Status Code: {response.status_code}")
            print(f"Headers: {response.headers}")
            print(f"Content: {response.text}")
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")



    def captcha_button_function(self):
        url = self.url_target_textedit.toPlainText().strip()
        
        try:
            response = requests.get(url)
            # Perform captcha response and bypass checks here
            # ...
            
            # Example code to print the domain and captcha/bypass status
            domain = response.url
            captcha_status = "Captcha required"  # Replace with actual captcha check result
            bypass_status = "No bypass available"  # Replace with actual bypass check result
            
            result = f"Domain: {domain}\nCaptcha Status: {captcha_status}\nBypass Status: {bypass_status}"
            self.results_window_textedit_3.setPlainText(result)
            
        except requests.exceptions.RequestException as e:
            self.results_window_textedit_3.setPlainText(f"Error: {e}")


    def akamai_button_function(self):
        url = self.url_target_textedit.toPlainText().strip()
        
        try:
            response = requests.get(url)
            headers = response.headers
            
            if 'Server' in headers and 'Akamai' in headers['Server']:
                print("The website is using Akamai.")
            else:
                print("The website is not using Akamai.")
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    

    def seo_data_details_button_function(self):
        url = self.url_target_textedit.toPlainText().strip()
    
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
    
            # Extract SEO data from the soup object
            title = soup.find("title").text if soup.find("title") else ""
            meta_description = soup.find("meta", attrs={"name": "description"})
            meta_description = meta_description["content"] if meta_description else ""
            meta_keywords = soup.find("meta", attrs={"name": "keywords"})
            meta_keywords = meta_keywords["content"] if meta_keywords else ""
    
            # Display the URL and SEO data in results_window_textedit_3
            self.results_window_textedit_3.append(f"URL: {url}")
            self.results_window_textedit_3.append(f"Title: {title}")
            self.results_window_textedit_3.append(f"Meta Description: {meta_description}")
            self.results_window_textedit_3.append(f"Meta Keywords: {meta_keywords}")
    
        except requests.exceptions.RequestException as e:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("An error occurred while fetching SEO data.")
            error_dialog.setDetailedText(str(e))
            error_dialog.exec_()
    
    
    
    
        
    def sub_domains_button_function(self):
        # Get the target URL from url_target_textedit
        target_url = self.url_target_textedit.toPlainText().strip()
    
        # API endpoint to fetch subdomains
        api_endpoint = f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={target_url}"
    
        try:
            # Create a session with SSL verification disabled
            session = requests.Session()
            session.verify = False
    
            # Make a request to the API using the session
            response = session.get(api_endpoint)
    
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the response JSON
                subdomains = response.json()
    
                # Process the subdomains
                for subdomain in subdomains:
                    # Do something with each subdomain
                    print(subdomain)
            else:
                # Handle the API error response
                print("API request failed:", response.status_code)
        except requests.RequestException as e:
            # Handle the request exception
            print("API request failed:", str(e))
        
    
    def traffic_button_function(self):
        try:
            output = subprocess.check_output(["netstat", "-s"]).decode("utf-8")
            self.results_window_textedit_2.setPlainText(output)
        except subprocess.CalledProcessError as e:
            self.results_window_textedit_2.setPlainText(str(e))
    
    
    def captcha_button_function(self):
        url = self.url_target_textedit.toPlainText().strip()
        
        try:
            response = requests.get(url)
            # Perform captcha response and bypass checks here
            # ...
            
            # Example code to print the domain and captcha/bypass status
            domain = response.url
            captcha_status = "Captcha required"  # Replace with actual captcha check result
            bypass_status = "No bypass available"  # Replace with actual bypass check result
            
            result = f"Domain: {domain}\nCaptcha Status: {captcha_status}\nBypass Status: {bypass_status}"
            self.results_window_textedit_3.setPlainText(result)
            
        except requests.exceptions.RequestException as e:
            self.results_window_textedit_3.setPlainText(f"Error: {e}")



    def check_api_login_directories_function(self):
        url = self.url_target_textedit.toPlainText().strip()
    
        try:
            # Perform API record scanning
            response = requests.get(url)
            api_records = []
    
            # Example code to scan for API-related keywords in the response text
            keywords = ["api", "endpoint", "oauth"]
            if any(keyword in response.text.lower() for keyword in keywords):
                api_records.append(url)
    
            # Example code to append results to the widget
            if api_records:
                result = "API records found:\n" + "\n".join(api_records)
            else:
                result = "No API records found"
            self.results_window_textedit_3.append(result)
    
        except requests.exceptions.RequestException as e:
            self.results_window_textedit_3.append(f"Error: {e}")
                
    def handle_font_button_click(self):
        url = self.url_target_textedit.toPlainText().strip()
        
        try:
            if not url:
                raise ValueError("Empty URL provided")
    
            response = requests.get(url)
            # Rest of the code to scrape and display font links
    
        except requests.exceptions.MissingSchema:
            error_message = "Invalid URL: No scheme supplied. Perhaps you meant https://?"
            QMessageBox.critical(self, "Invalid URL", error_message)
    



    def get_font_links(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            font_links = []
    
            # Find all link tags with the 'rel' attribute set to 'stylesheet' or 'preload'
            link_tags = soup.find_all('link', rel=['stylesheet', 'preload'])
            
            for tag in link_tags:
                href = tag.get('href')
                
                # Check if the href attribute is for a font file
                if href and ('.woff' in href or '.woff2' in href or '.ttf' in href or '.otf' in href):
                    font_links.append(href)
    
            return font_links
        
        except ValueError as e:
            QMessageBox.critical(self, "Empty URL", str(e))
    
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Request Error", f"Error: {e}")
    
    
    
    
    def display_font_links(self, font_links):
        if font_links:
            result = "Font Links:\n" + "\n".join(font_links)
        else:
            result = "No font links found."
    
        self.results_window_links_text.setPlainText(result)

    
    def cloudflare_button_clicked(domain):
        try:
            # Query the DNS records for the domain
            answers = dns.resolver.resolve(domain, 'NS')
            
            # Check if any of the DNS records indicate Cloudflare services
            for rdata in answers:
                if 'cloudflare' in str(rdata.target).lower():
                    return True
            
            return False
        
        except dns.resolver.NXDOMAIN:
            print(f"Domain '{domain}' does not exist.")
            return False
        
        except dns.resolver.NoAnswer:
            print(f"No DNS records found for domain '{domain}'.")
            return False
        
        except dns.exception.DNSException as e:
            print(f"Error performing DNS lookup: {e}")
            return False


    def handle_external_links_button_click(self):
        url = self.url_target_textedit.toPlainText().strip()
    
        try:
            # Retrieve the HTML content of the web page
            response = requests.get(url)
            html = response.text
    
            # Create a BeautifulSoup object from the HTML content
            soup = BeautifulSoup(html, 'html.parser')
    
            # Find all anchor tags in the web page
            anchor_tags = soup.find_all('a')
    
            # Extract external links from the anchor tags
            external_links = []
            for tag in anchor_tags:
                href = tag.get('href')
                if href and not href.startswith('#') and not urlparse(href).netloc == urlparse(url).netloc:
                    external_links.append(href)
    
            # Example code to display the external links
            result = "External Links:\n" + "\n".join(external_links)
            self.results_window_textedit_3.setPlainText(result)
    
        except requests.exceptions.RequestException as e:
            self.results_window_textedit_3.setPlainText(f"Error: {e}")







    def handle_image_urls_button_click(self):
        url = self.url_target_textedit.toPlainText()
        image_urls = self.get_image_urls(url)
        self.display_image_urls(image_urls)








    def handle_config_function_headers(self):
        # Add your code here to handle the button click event
        # Perform the necessary actions or operations

        # For example, you can display a message box
        QtWidgets.QMessageBox.information(None, "Config Function Headers", "Button clicked!")

        # Or you can call another function or method to perform specific actions
        self.perform_config_function_headers()










    def perform_config_function_headers(self):
        # Add your code here to perform the desired actions for the config function headers

        # For example, you can set custom headers for requests
        headers = {"User-Agent": "Custom User Agent"}

        # You can then use the custom headers in your requests
        response = requests.get("https://api.example.com", headers=headers)

        # Handle the response or perform any other necessary operations

        # You can also update the UI elements based on the result
        if response.status_code == 200:
            self.results_window_textedit_3.setPlainText("Config function headers successful!")
        else:
            self.results_window_textedit_3.setPlainText("Config function headers failed!")









    def perform_config_function_post(self):
        url = self.url_target_textedit.toPlainText()  # Get the URL from the text edit
        data = {"key": "value"}  # Define the data to be sent in the request

        response = requests.post(url, data=data)  # Send the POST request

        if response.status_code == 200:  # Check if the request was successful
            result_data = response.text  # Get the response data
            self.results_window_textedit_3.setPlainText(result_data)  # Display the data in the text edit








    def handle_head_request(self):
        url = self.url_target_textedit.toPlainText()  # Get the URL from the text edit

        response = requests.head(url)  # Send the HEAD request

        if response.status_code == 200:  # Check if the request was successful
            result_data = response.headers  # Get the response headers
            self.results_window_textedit_3.setPlainText(str(result_data))  # Display the headers in the text edit








    def handle_options_request(self):
        url = self.url_target_textedit.toPlainText()  # Get the URL from the text edit

        response = requests.options(url)  # Send the OPTIONS request

        if response.status_code == 200:  # Check if the request was successful
            result_data = response.headers  # Get the response headers
            self.results_window_textedit_3.setPlainText(str(result_data))  # Display the headers in the text edit









    def handle_put_request(self):
        url = self.url_target_textedit.toPlainText()  # Get the URL from the text edit
        data = {"key": "value"}  # Define the data to be sent in the request

        response = requests.put(url, data=data)  # Send the PUT request

        if response.status_code == 200:  # Check if the request was successful
            result_data = response.text  # Get the response data
            self.results_window_textedit_3.setPlainText(result_data)  # Display the data in the text edit






    def handle_trace_request(self):
        url = self.url_target_textedit.toPlainText()  # Get the URL from the text edit

        response = requests.request("TRACE", url)  # Send the TRACE request

        if response.status_code == 200:  # Check if the request was successful
            result_data = response.text  # Get the response data
            self.results_window_textedit_3.setPlainText(result_data)  # Display the data in








    def handle_get_request(self):
        url = self.url_target_textedit.toPlainText()  # Get the URL from the text edit
        api_url = f"https://api.urlparse.com/v1/query?url={url}"  # Construct the API URL
        response = requests.get(api_url)  # Send the GET request

        if response.status_code == 200:  # Check if the request was successful
            data = response.text  # Get the response data
            self.results_window_textedit_3.setPlainText(data)  # Display the data in the text edit



    
    def handle_post_request(self):
        url = self.url_target_textedit.toPlainText()  # Get the URL from the text edit
        data = {"key": "value"}  # Define the data to be sent in the request

        response = requests.post(url, data=data)  # Send the POST request

        if response.status_code == 200:  # Check if the request was successful
            result_data = response.text  # Get the response data
            self.results_window_textedit_3.setPlainText(result_data) 







    
    def handle_patch_request(self):
        url = self.url_textedit.toPlainText()  # Get the URL from the QTextEdit widget
        data = {"key": "value"}  # Define the data to be sent in the request
    
        try:
            response = requests.patch(url, data=data)  # Send the PATCH request
            response.raise_for_status()  # Check if the request was successful
    
            result_data = response.text  # Get the response data
            self.show_result_dialog(result_data)  # Display the data in a dialog
        except TypeError as e:
            error_message = f"TypeError: {e}"
            self.show_error_dialog(error_message)
        except requests.exceptions.MissingSchema:
            error_message = "Invalid URL: Please enter a valid URL."
            self.show_error_dialog(error_message)
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred while sending the PATCH request: {e}"
            self.show_error_dialog(error_message)
        
        
        
        
        
        
    def handle_head_request(self):
        url = self.url_textedit.toPlainText()  # Get the URL from the QTextEdit widget
    
        try:
            response = requests.head(url)  # Send the HEAD request
            response.raise_for_status()  # Check if the request was successful

            result_data = str(response.headers)  # Get the response headers
            self.show_result_dialog(result_data)  # Display the headers in a dialog
        except requests.exceptions.MissingSchema:
            error_message = "Invalid URL: Please enter a valid URL."
            self.show_error_dialog(error_message)
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred while sending the HEAD request: {e}"
            self.show_error_dialog(error_message)






    def handle_put_request(self):
        url = self.url_textedit.toPlainText()  # Get the URL from the QTextEdit widget
        data = {"key": "value"}  # Define the data to be sent in the request

        try:
            response = requests.put(url, data=data)  # Send the PUT request
            response.raise_for_status()  # Check if the request was successful

            result_data = response.text  # Get the response data
            self.show_result_dialog(result_data)  # Display the data in a dialog
        except requests.exceptions.MissingSchema:
            error_message = "Invalid URL: Please enter a valid URL."
            self.show_error_dialog(error_message)
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred while sending the PUT request: {e}"
            self.show_error_dialog(error_message)





    def handle_trace_request(self):
        url = self.url_textedit.toPlainText()  # Get the URL from the QTextEdit widget

        try:
            response = requests.request("TRACE", url)  # Send the TRACE request
            response.raise_for_status()  # Check if the request was successful

            result_data = response.text  # Get the response data
            self.show_result_dialog(result_data)  # Display the data in a dialog
        except requests.exceptions.MissingSchema:
            error_message = "Invalid URL: Please enter a valid URL."
            self.show_error_dialog(error_message)
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred while sending the TRACE request: {e}"
            self.show_error_dialog(error_message)










    def css_links(self):
        url = self.url_textedit.text()  # Get the URL from the QLineEdit widget
        
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            
            # Check if the response was successful (status code 200)
            response.raise_for_status()
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all CSS links in the HTML
            css_links = []
            for link in soup.find_all('link', rel='stylesheet'):
                href = link.get('href')
                if href.endswith('.css'):
                    css_links.append(href)
            
            if css_links:
                # Display the CSS links
                css_links_str = '\n'.join(css_links)
                QMessageBox.information(self, "CSS Links", css_links_str)
            else:
                QMessageBox.information(self, "CSS Links", "No CSS links found")
        
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred while accessing the URL: {e}"
            QMessageBox.critical(self, "Error", error_message)









    def show_result_dialog(self, result_data):
        result_dialog = QMessageBox(self)
        result_dialog.setWindowTitle("Result")
        result_dialog.setText(result_data)
        result_dialog.exec_()

    def show_error_dialog(self, error_message):
        error_dialog = QMessageBox(self)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(error_message)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.exec_()

    def handle_button_click():
        url = self.url_target_textedit.toPlainText()
        css_links = css_links(url)
        self.results_window_textedit_3.setPlainText('\n'.join(css_links))









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UrlToolsWindow = QtWidgets.QDialog()
    ui = Ui_UrlToolsWindow()
    ui.setupUi(UrlToolsWindow)
    UrlToolsWindow.show()
    sys.exit(app.exec_())
