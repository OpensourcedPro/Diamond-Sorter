from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import *
from PyQt5 import QtCore
import os

# import outside python
from dep.python.functions import functions

# import UI components
from dep.UIdep.settingspage import Ui_settings
from dep.UIdep.searchbar import Ui_searchbar

# get dir
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

# images
close_png = current_dir+'/UIres/close.png'
close_gray_png = current_dir+'/UIres/close_gray.png'


class Ui_tabbar(object):
    def tabsetupUi(self, tabWidget):
        # creating a tab widget
        self.tabs = QTabWidget()
        # make tabs closable
        self.tabs.setTabsClosable(True)
        # making document mode true
        self.tabs.setDocumentMode(True)
        # making tabs visible
        self.tabs.setObjectName("tabs")
        # create stylesheet for the tabs
        self.tabs.setStyleSheet("""
            QTabBar::close-button {
                image: url("""+close_gray_png+"""); 
            }

            QTabBar::close-button:selected {
                image: url("""+close_png+"""); 
            }

            QTabBar::close-button:hover {
                background-color:rgba(210, 210, 210, 30);
            }

            QTabBar::close-button:hover:selected {
                background-color:rgba(144, 144, 144, 30);
                border-radius:5px;
            }
            
            QTabBar {
                background-color: rgb(35, 34, 39);
                color: rgb(255, 255, 255);
                border-bottom: 1.5px solid white;
            }

            QTabBar::tab {
                background-color: rgb(27, 27, 27);
                margin-left: 1px;
                margin-right: 2px;
                margin-top: 2px;
                margin-bottom: 4px;
            }

            QTabBar::tab:selected {
                background-color: rgb(27, 27, 27);
                border-top: 0.5px solid white;
                border-right: 0.5px solid white;
                border-left: 0.5px solid white;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }


            QTabBar::tab:hover {
                background-color:rgb(10, 10, 10);
            }
            """)

        # add tabs to widget
        self.verticalLayout_3.addWidget(self.tabs)
        
        QtCore.QMetaObject.connectSlotsByName(tabWidget)
        
        # creating first tab
        functions.tab_functions.add_new_tab(self, self.tabs, functions.misc.set_url(self), 'Homepage')
      
        # adding action when double clicked
        self.tabs.tabBarDoubleClicked.connect(lambda: functions.tab_functions.tab_open_doubleclick(self, self.tabs))
        
        # adding action when tab is changed
        self.tabs.currentChanged.connect(lambda: functions.tab_functions.current_tab_changed(self, self.tabs))
        
        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)  
        
    # close tab
    def close_current_tab(self, index):
        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return
        # mute the tab
        #for tabIndex in range(self.tabs.count()):
        #    if tabIndex == (index+1):
        #        self.browser.setAudioMuted(True)
        #    else:pass
        # else remove the tab
        self.tabs.removeTab(index)
        
        
        