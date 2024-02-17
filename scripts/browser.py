from PyQt5.QtNetwork import QNetworkProxy, QNetworkProxyFactory

# Import the required libraries
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import socket
import struct

# Import UI components
from dep.UIdep.settingspage import Ui_settings
from dep.UIdep.searchbar import Ui_searchbar
from dep.UIdep.tabbar import Ui_tabbar

# Import other Python modules
from dep.python.interceptor import UrlRequestInterceptor
from dep.python.javascriptInjecting import javascript
from dep.python.TorRouting import TorProxy
from dep.python.functions import functions
from dep.python.settings import settings
from dep.python.fake import *
import psutil
import psutil







connections = psutil.net_connections()
for conn in connections:
    # Process the network connection information as needed
    print(conn)

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")


# Set up the debug port and URL
DEBUG_PORT = '5588'
DEBUG_URL = 'http://127.0.0.1:%s' % DEBUG_PORT
os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = DEBUG_PORT



# Hide JavaScript logs
class WebEnginePage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        if self.debug_javaScriptConsoleMessage:
            print("Lvl: "+level+" - Msg: "+msg)


# Create the main window
class MainWindow(QWidget, javascript, Ui_searchbar, Ui_tabbar, Ui_settings, settings, TorProxy):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent = parent)
        functions.misc.get_profile(self, current_dir)
        self.settings_load()
        self.setWindowTitle("Diamond Browser")
        self.setWindowIcon(QIcon("icon/diamond.ico"))
        self.setMouseTracking(True)
        self.setupUi(self)
        self.tabsetupUi(self)
        self.settingssetupUi(self)
        self.show_hideSettingsPage()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.settings_apply()
        self.inject()
        self.resize(1500, 800)
        self.launchTorProxy()
        self.urlbar.returnPressed.connect(lambda: functions.tab_functions.navigate_to_url(self))
        self.back_PushButton.clicked.connect(lambda: self.tabs.currentWidget().back())
        self.forward_PushButton.clicked.connect(lambda: self.tabs.currentWidget().forward())
        self.reload_PushButton.clicked.connect(lambda: self.tabs.currentWidget().reload())
        self.home_PushButton.clicked.connect(lambda: self.tabs.currentWidget().setUrl(QUrl(functions.misc.set_url(self))))
        self.settings_PushButton.clicked.connect(lambda: self.show_hideSettingsPage())
        self.setSpoofSettings()
        self.setProxy()

    def setProxy(self):
        proxy_address, ok = QInputDialog.getText(self, "Set Proxy Address", "Enter the proxy address (e.g., IP:Port):")
        if ok:
            proxy = QNetworkProxy()
            proxy.setType(QNetworkProxy.HttpProxy)
            proxy.setHostName(proxy_address.split(':')[0])
            proxy.setPort(int(proxy_address.split(':')[1]))

            QNetworkProxy.setApplicationProxy(proxy)

    def setSpoofSettings(self):
        ip, ok = QInputDialog.getText(self, "Set Spoof IP", "Enter the spoof IP address:")
        if ok:
            palette = self.palette()
            text_color = QColor(255, 255, 255)  # Set the desired text color
            button_color = QColor(0, 0, 0)  # Set the desired button text color
            palette.setColor(QPalette.Text, text_color)
            palette.setColor(QPalette.ButtonText, button_color)
            self.setPalette(palette)

            port, ok = QInputDialog.getText(self, "Set Spoof Port", "Enter the spoof port:")
            if ok:
                zipcode, ok = QInputDialog.getText(self, "Set Spoof ZIP Code", "Enter the spoof ZIP code or geographic location:")
                if ok:
                    # Do something with the spoof IP, port, and ZIP code/geo location
                    print("Spoof IP:", ip)
                    print("Spoof Port:", port)
                    print("Spoof ZIP Code / Geo Location:", zipcode)









    def resizeEvent(self, event):
        self.settings_widget.setGeometry(QRect((self.width() - 320), 62, 320, self.height()))
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 320, (self.height() - 20)))
        self.background.setGeometry(QRect(0, 0, 320, (self.height())))
        self.scrollArea.setGeometry(QRect(0, 0, 320, (self.height())))
        self.scrollAreaWidgetContents.setMinimumSize(self.scrollAreaWidgetContents.minimumWidth(), 700)

    def showContextMenu(self, pos):
        menu = QMenu(self)
        connection_info_action = QAction("Connection Information", self)
        connection_info_action.triggered.connect(self.showConnectionInfo)
        menu.addAction(connection_info_action)
        basic_stats_action = QAction("Basic Connection Stats", self)
        basic_stats_action.triggered.connect(self.showBasicStats)
        menu.addAction(basic_stats_action)
        widget = self.focusWidget()
        if isinstance(widget, QLineEdit):
            cursor = widget.cursorForPosition(pos)
            selected_text = cursor.selectedText().strip()
            if selected_text:
                search_action = QAction("Search '%s'" % selected_text, self)
                search_action.triggered.connect(lambda: self.search(selected_text))
                menu.addAction(search_action)
        open_new_tab_action = QAction("Open New Tab", self)
        open_new_tab_action.triggered.connect(self.openNewTab)
        menu.addAction(open_new_tab_action)
        menu.exec_(self.mapToGlobal(pos))

    def openNewTab(self):
        new_page = QWidget()
        self.tab_widget.addTab(new_page, "New Tab")
        self.tab_widget.setCurrentWidget(new_page)

    def showConnectionInfo(self):
        connections = socket.net_connections()
        print("Connection Information:")
        for conn in connections:
            print(f"Protocol: {conn.type}")
            print(f"Local Address: {conn.laddr}")
            print(f"Remote Address: {conn.raddr}")
            print(f"Status: {conn.status}")
            print(f"PID: {conn.pid}")
            print("----------------------")

    def showBasicStats(self):
        net_stats = psutil.net_io_counters()
        print("Basic Connection Stats:")
        print(f"Bytes Sent: {net_stats.bytes_sent}")
        print(f"Bytes Received: {net_stats.bytes_recv}")
        print(f"Packets Sent: {net_stats.packets_sent}")
        print(f"Packets Received: {net_stats.packets_recv}")
        print(f"Error In: {net_stats.errin}")
        print(f"Error Out: {net_stats.errout}")
        print(f"Dropped In: {net_stats.dropin}")
        print(f"Dropped Out: {net_stats.dropout}")

    def search(self, text):
        search_url = QUrl("https://www.google.com/search?q={}".format(text))
        QDesktopServices.openUrl(search_url)

def main(appName, appVersion):
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    app.setApplicationName(appName +" "+ appVersion)
    app.setApplicationVersion(appVersion)
    interceptor = UrlRequestInterceptor()
    QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

def spoof_ip_address(destination_ip, spoofed_ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except socket.error as e:
        print("Failed to create raw socket. Error: ", e)
        return
    ip_version = 4
    ip_header_length = 5
    ip_tos = 0
    ip_total_length = 0
    ip_identifier = 54321
    ip_flags = 0x02
    ip_fragment_offset = 0
    ip_ttl = 255
    ip_protocol = socket.IPPROTO_TCP
    ip_checksum = 0
    ip_source = socket.inet_aton(spoofed_ip)
    ip_destination = socket.inet_aton(destination_ip)
    ip_header = struct.pack('!BBHHHBBH4s4s', (ip_version << 4) + ip_header_length, ip_tos, ip_total_length, ip_identifier,
                            (ip_flags << 13) + ip_fragment_offset, ip_ttl, ip_protocol, ip_checksum, ip_source,
                            ip_destination)
    ip_checksum = calculate_checksum(ip_header)
    ip_header = struct.pack('!BBHHHBBH4s4s', (ip_version << 4) + ip_header_length, ip_tos, ip_total_length, ip_identifier,
                            (ip_flags << 13) + ip_fragment_offset, ip_ttl, ip_protocol, socket.htons(ip_checksum),
                            ip_source, ip_destination)
    try:
        s.sendto(ip_header + payload, (destination_ip, 0))
    except socket.error as e:
        print("Failed to send spoofed IP packet. Error: ", e)
    s.close()

if __name__ == "__main__":
    with open (os.path.join(current_dir, "appInfo.txt")) as F:
        appName = F.readline()
        appVersion = F.readline()
    F.close()
    main(appName, appVersion)