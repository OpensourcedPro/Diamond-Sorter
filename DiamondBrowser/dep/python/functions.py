from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import re
import os

# import outside python
from dep.python.fake import *

# get current dir
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

back_png = current_dir+'/UIres/back.png'
forward_png = current_dir+'/UIres/arrow-right.png'
reload_png = current_dir+'/UIres/reload.png'


# validate url
regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain
    r'localhost|' #localhost
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


class functions():
    # showContextMenu, UpdateUserAgent, get_profile
    class misc():
        def showContextMenu(self):
            # get mouse position
            mouse_position = self.mapFromGlobal(QCursor.pos())
            
            # Create the context menu and add actions
            menu = QMenu(self)
            back_action = QAction(QIcon(back_png), "back", self)
            forward_action = QAction(QIcon(forward_png), "forward", self)
            reload_action = QAction(QIcon(reload_png), "reload", self)
            menu.addAction(back_action)
            menu.addAction(forward_action)
            menu.addAction(reload_action)
            # set style (hover aka. selected is not working I will have to fix this)
            menu.setStyleSheet('background-color: rgb(35, 34, 39);\n'
                            'color: white;\n'
                            'QMenu::item:selected{\n'
                            '    background-color: rgb(27, 27, 27);\n'
                            '}')

            # EVENTS [context menu]
            # back event
            back_action.triggered.connect(lambda: self.tabs.currentWidget().back())
            # forward event
            forward_action.triggered.connect(lambda: self.tabs.currentWidget().forward())
            # reload event
            reload_action.triggered.connect(lambda: self.tabs.currentWidget().reload())

            # Show the context menu at the mouse position
            menu.exec_(self.mapToGlobal(QPoint(mouse_position.x(), mouse_position.y())))

        
        # create and get a profile
        def get_profile(self, current_dir):
            self.profile = QWebEngineProfile.defaultProfile()
            # set the cookie path
            self.profile.setPersistentStoragePath(os.path.join(current_dir, "data/defaultUser"))
            # set the cache path
            self.profile.setCachePath(os.path.join(current_dir, "data/defaultUser"))


        # get default search engine
        def set_url(self):
            if self.RouteTrafficThroughTor:
                return self.tor_search_engine
            else:
                return self.search_engine
        
        
    # set_tab_title, update_urlbar, add_new_tab, navigate_to_url,
    # tab_open_doubleclick, current_tab_changed, close_current_tab, reload_tabs
    # activate fullscreen mode
    class tab_functions():  
        # activate fullscreen mode
        def Fullscreen(self, request):
            if request.toggleOn():
                self.showFullScreen()
                # hide gui elements
                self.tabs.setTabBarAutoHide(True) # tabbar
                self.wpWidget_3.hide() # search bar
                self.settings_widget.hide() # settings window
            else:
                self.showNormal()
                # show gui elements
                self.tabs.setTabBarAutoHide(False) # tabbar
                self.wpWidget_3.show() # search bar
                self.settings_widget.show() # settings window
            request.accept()
        
        # change tab title
        def set_tab_title(i, browser, tabs, title):
            # check if tab title is provided if not get it
            if title is None:
                title = browser.page().title()

            # set tab title and shorten it after 25 chars
            if len(title) > 25:
                title = title[:25] + "..."
            tabs.setTabText(i, " "+title+" ")  
          

        # update the url bar
        def update_urlbar(self, q, browser = None):
            if browser != self.tabs.currentWidget():
                return
            raw_url = q.toString()

            # set text to the url bar
            self.urlbar.setText(q.toString())
            # set cursor position
            self.urlbar.setCursorPosition(0)  
        
        
        # method for adding new tab
        def add_new_tab(self, tabs, qurl = None, label ="Blank"):
            self.tabs = tabs
            try:
                # if url is blank
                if qurl is None:
                    # creating aurl
                    qurl = self.set_url()

                # creating a QWebEngineView object
                self.browser = QWebEngineView()
                page = QWebEnginePage(self.browser)
                self.browser.setPage(page)
                self.browser.page().setBackgroundColor(QColor(45, 45, 45, 255))
                self.browser.setObjectName("browser")
                self.verticalLayout_3.addWidget(self.browser)

                # create custom context menu
                self.browser.setContextMenuPolicy(Qt.CustomContextMenu)
                self.browser.customContextMenuRequested.connect(lambda: functions.misc.showContextMenu(self))

                # allow full screen
                self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
                # allow plugins
                self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

                # setting url to browser
                self.browser.setUrl(QUrl(qurl))

                # setting tab index
                self.i = self.tabs.addTab(self.browser, label)
                self.tabs.setCurrentIndex(0)

                # adding action to the browser when url is changed
                # update the url
                self.browser.urlChanged.connect(lambda qurl, browser = self.browser:
                                        functions.tab_functions.update_urlbar(self, qurl, browser))

                # adding action to the browser when loading is finished
                # set the tab title
                self.browser.loadFinished.connect(lambda _, i=self.i, browser=self.browser, tabs=tabs:
                                        functions.tab_functions.set_tab_title(i, browser, tabs, None))
            
                # fullscreen mode event
                self.browser.page().fullScreenRequested.connect(lambda request: functions.tab_functions.Fullscreen(self, request))
            except Exception as e:
                raise (e)  



        # navigate to url
        def navigate_to_url(self):
            q = QUrl(self.urlbar.text())

            # if scheme is blank and there is no domain end then use the default search machine to get a result
            if q.scheme() == "":
                # add a scheme to check if the user just forgot to add it if its still not valid use google
                if (re.match(regex, "https://"+q.toString()) is not None) == False:
                    # domain is not a url use search engine (if Tor: tor search engine)
                    search = (q.toString()).replace(" ", "+")
                    if self.RouteTrafficThroughTor:
                        q = QUrl(self.tor_search_engine_addr + search)
                    else:
                        q = QUrl(self.search_engine_addr + search)
                else:
                    # domain is a url add https
                    q.setScheme("https")
                
            # if scheme is http
            if q.scheme() == "http":
                reply = QMessageBox.question(self, 'Warning', 'You are using "http" change to "https" ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    # set scheme
                    q.setScheme("https")
                else:
                    pass
            # set the url
            self.tabs.currentWidget().load(q)


        # when double clicked is pressed on tabs
        def tab_open_doubleclick(self, tabs):
            # creating a new tab
            functions.tab_functions.add_new_tab(self, tabs)


        # when tab is changed
        def current_tab_changed(self, tabs):
            # get the curl
            qurl = tabs.currentWidget().url()
            # update the url
            functions.tab_functions.update_urlbar(self, qurl, self.tabs.currentWidget())
            
            
        # reload all tabs
        def reload_tabs(self):
            # reload all open tabs
            for i in range(self.tabs.count()):
                widget = self.tabs.widget(i)
                # Refresh the content of the widget
                widget.reload()
            return