import sqlite3
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.page)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "New Column"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "New Column"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).child(2).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.treeWidget.topLevelItem(1).child(2).child(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).child(2).child(2).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))



        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.grab_data_button.clicked.connect(self.grabData)
        self.request_data_button.clicked.connect(self.handle_data_request)



    def populateDomainTreeWidget(self):
        # Connect to the database
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()

        # Retrieve the data from the cookies table
        cursor.execute("SELECT * FROM cookies")
        results = cursor.fetchall()

        # Clear the domain_tree_widget
        self.domain_tree_widget.clear()

        # Set the text in the textBrowser
        text = ""
        for result in results:
            domain = result[1]
            url = result[2]
            cookie_name = result[3]
            cookie_id = result[4]
            description = result[5]
            duration = result[6]
            cookie_type = result[7]
            storage_type = result[8]

            text += f"Domain: {domain}\n"
            text += f"URL: {url}\n"
            text += f"Cookie Name: {cookie_name}\n"
            text += f"Cookie ID: {cookie_id}\n"
            text += f"Description: {description}\n"
            text += f"Duration: {duration}\n"
            text += f"Type: {cookie_type}\n"
            text += f"Storage Type: {storage_type}\n\n"

        self.textBrowser.setPlainText(text)

        # Close the database connection
        conn.close()

    def populateTableWidget(self):
        # Connect to the database
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
    
        # Retrieve the data from the cookies table
        cursor.execute("SELECT domain, URL, Cookie_name, cookie_ID, description FROM cookies")
        results = cursor.fetchall()
    
        # Set the table headers
        headers = ["Domain", "URL", "Cookie Name", "Cookie ID", "Cookie Description"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
    
        # Populate the tableWidget with the data
        self.tableWidget.setRowCount(len(results))
        for row, result in enumerate(results):
            for col, value in enumerate(result):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
    
        # Close the database connection
        conn.close()



    def display_stats(self):
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()

        # Retrieve the statistics data from the database
        cursor.execute("SELECT COUNT(*), MIN(column), MAX(column) FROM cookies")
        result = cursor.fetchone()
        count = result[0]
        min_value = result[1]
        max_value = result[2]

        # Update the labels in the frames with the statistics data
        self.frame_stats_1.setText(f"Count: {count}")
        self.label_stats_2.setText(f"Min Value: {min_value}")
        self.label_stats_3.setText(f"Max Value: {max_value}")

        # Close the database connection
        conn.close()


    def grabData(self):
        # Connect to the database
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()
        
        # Create the cookies table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cookies (
                request_datetime TEXT,
                domain TEXT,
                URL TEXT,
                Cookie_name TEXT,
                cookie_ID TEXT,
                description TEXT,
                duration TEXT,
                type TEXT,
                storage_type TEXT
            )
        """)
        
        # Commit the changes and close the connection
        conn.commit()
        # Retrieve the data from the database
        cursor.execute("SELECT * FROM cookies")
        results = cursor.fetchall()

        # Retrieve the count of unique values for domains
        cursor.execute("SELECT COUNT(DISTINCT domain) FROM cookies")
        domain_count = cursor.fetchone()[0]

        # Retrieve the count of unique values for cookie names
        cursor.execute("SELECT COUNT(DISTINCT Cookie_name) FROM cookies")
        cookie_name_count = cursor.fetchone()[0]

        # Retrieve the count of unique values for cookie IDs
        cursor.execute("SELECT COUNT(DISTINCT cookie_ID) FROM cookies")
        cookie_id_count = cursor.fetchone()[0]

        # Retrieve the count of unique values for cookie types
        cursor.execute("SELECT COUNT(DISTINCT type) FROM cookies")
        cookie_type_count = cursor.fetchone()[0]

        # Display the counts in the textBrowser
        self.textBrowser.setPlainText("Data Numbers:\n\n")
        self.textBrowser.append(f"Domains: {domain_count}")
        self.textBrowser.append(f"Cookie Names: {cookie_name_count}")
        self.textBrowser.append(f"Cookie ID: {cookie_id_count}")
        self.textBrowser.append(f"Cookie Types: {cookie_type_count}")

        # Close the database connection
        conn.close()


        # Auto-resize the columns to fit the content
        self.tableWidget.resizeColumnsToContents()

        # Populate the request_data_combobox with unique URLs
        urls = set(result[1] for result in results)
        self.request_data_combobox.clear()
        self.request_data_combobox.addItems(urls)


    def handle_data_request(self):
        # Get the selected URL from the data_request_text field
        selected_url = self.data_request_text.toPlainText()
        
        # Connect to the database
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()
        
        # Retrieve the results for the selected URL from the database
        cursor.execute("SELECT * FROM cookies WHERE URL = ? LIMIT 10", (selected_url,))
        results = cursor.fetchall()
        
        # Clear the domain_tree_widget
        self.domain_tree_widget.clear()
        
        # Populate the domain_tree_widget with the data
        for i, result in enumerate(results):
            url = result[2]
            domain_item = QtWidgets.QTreeWidgetItem(self.domain_tree_widget, [f"URL {i+1}", url])
            
            # Get the favicon URL
            favicon_url = get_favicon(url)
            if favicon_url:
                favicon_item = QtWidgets.QTreeWidgetItem(domain_item, ["Favicon URL", favicon_url])
        
            for j in range(1, 6):
                cookie_name = result[j+2]
                cookie_item = QtWidgets.QTreeWidgetItem(domain_item, [cookie_name])
        
                description = result[j+3]
                description_item = QtWidgets.QTreeWidgetItem(cookie_item, ["Description", description])
        
                duration = result[j+4]
                duration_item = QtWidgets.QTreeWidgetItem(cookie_item, ["Duration", duration])
        
                cookie_type = result[j+5]
                type_item = QtWidgets.QTreeWidgetItem(cookie_item, ["Type", cookie_type])
        
        # Close the database connection
        conn.close()
    
    def get_favicon(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            favicon_link = soup.find('link', rel='icon')
            if favicon_link:
                favicon_url = favicon_link['href']
                if not favicon_url.startswith('http'):
                    parsed_url = urlparse(url)
                    favicon_url = f"{parsed_url.scheme}://{parsed_url.netloc}{favicon_url}"
                return favicon_url
        except requests.exceptions.RequestException:
            return None
      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

