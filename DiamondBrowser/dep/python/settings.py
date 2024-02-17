from PyQt5.QtNetwork import QNetworkProxy, QNetworkProxyQuery, QNetworkProxyFactory
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtCore import QUrl
import configparser
import time
import os

# import outside python
from dep.python.fake import *

# dirs
dep_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..')).replace("\\", "/")

# get config
config_file = os.path.join(dep_dir, "config.cfg")
config = configparser.ConfigParser()
config.read(config_file)

# default values
default_search_engine = "https://google.com"
default_search_engine_addr = "https://google.com/search?q="
tor_default_search_engine = "https://duckduckgo.com"
tor_default_search_engine_addr = "https://duckduckgo.com/?&q="

developer = config['Developer']
general = config['General']
custom = config['Custom'] 
blocker = config['Blocker']
useragent = config['User.Agent']
privacy = config['Privacy']
proxy = config['Proxy']

class settings():
    def settings_load(self): 
        config.read(config_file)
        developer = config['Developer']
        general = config['General']
        custom = config['Custom']
        blocker = config['Blocker']
        useragent = config['User.Agent']
        privacy = config['Privacy']
        proxy = config['Proxy']
        
        # [Developer]
        debug_javaScriptConsoleMessage = developer["debug_javaScriptConsoleMessage"]
        if debug_javaScriptConsoleMessage == "True": self.debug_javaScriptConsoleMessage = True
        else: self.debug_javaScriptConsoleMessage = False

        # [General]
        javascript = general["javascript"]
        if javascript == "True": self.javascript = True
        else: self.javascript = False
        
        # [Custom]
        search_engine = custom["search_engine"]
        if search_engine == "": self.search_engine = default_search_engine
        else: self.search_engine = search_engine
        search_engine_addr = custom["search_engine_addr"]
        if search_engine_addr == "": self.search_engine_addr = default_search_engine_addr
        else: self.search_engine_addr = search_engine_addr
        #
        tor_search_engine = custom["tor_search_engine"]
        if tor_search_engine == "": self.tor_search_engine = tor_default_search_engine
        else: self.tor_search_engine = tor_search_engine
        tor_search_engine_addr = custom["tor_search_engine_addr"]
        if tor_search_engine_addr == "": self.tor_search_engine_addr = tor_default_search_engine_addr
        else: self.tor_search_engine_addr = tor_search_engine_addr    
        
        # [Blocker]
        # ad blocking
        ad_blocker = blocker["ad_blocker"]
        if ad_blocker == "True": self.ad_blocker = True
        else: self.ad_blocker = False
        #
        ad_auto_update = blocker["ad_auto_update"]
        if ad_auto_update == "True": self.ad_auto_update = True
        else: self.ad_auto_update = False
        #
        ad_lists = blocker["ad_lists"]
        if ad_lists == "": self.ad_lists = ""
        else: self.ad_lists = ad_lists
        
        # privacy blocking
        privacy_blocker = blocker["privacy_blocker"]
        if privacy_blocker == "True": self.privacy_blocker = True
        else: self.privacy_blocker = False
        #
        privacy_auto_update = blocker["privacy_auto_update"]
        if privacy_auto_update == "True": self.privacy_auto_update = True
        else: self.privacy_auto_update = False
        #
        privacy_lists = blocker["privacy_lists"]
        if privacy_lists == "": self.privacy_lists = ""
        else: self.privacy_lists = privacy_lists
        
        # cookie blocking
        cookie_blocker = blocker["cookie_blocker"]
        if cookie_blocker == "True": self.cookie_blocker = True
        else: self.cookie_blocker = False
        #
        cookie_auto_update = blocker["cookie_auto_update"]
        if cookie_auto_update == "True": self.cookie_auto_update = True
        else: self.cookie_auto_update = False
        #
        cookie_lists = blocker["cookie_lists"]
        if cookie_lists == "": self.cookie_lists = ""
        else: self.cookie_lists = cookie_lists
        
        # [User.Agent]
        default_user_agent = useragent["default_user_agent"]
        if default_user_agent == "True": self.default_user_agent = True
        else: self.default_user_agent = False
        #
        random_user_agent = useragent["random_user_agent"]
        if random_user_agent == "True": self.random_user_agent = True
        else: self.random_user_agent = False
        #
        custom_user_agent = useragent["custom_user_agent"]
        if custom_user_agent == "True": self.custom_user_agent = True
        else: self.custom_user_agent = False
        #
        custom_user_agent_input = useragent["custom_user_agent_input"]
        if custom_user_agent_input == "": self.custom_user_agent_input = ""
        else: self.custom_user_agent_input = custom_user_agent_input
        
        # [Privacy]
        RouteTrafficThroughTor = privacy["RouteTrafficThroughTor"]
        if RouteTrafficThroughTor == "True": self.RouteTrafficThroughTor = True
        else: self.RouteTrafficThroughTor = False
        #
        TrackingLinkProtection = privacy["TrackingLinkProtection"]
        if TrackingLinkProtection == "True": self.TrackingLinkProtection = True
        else: self.TrackingLinkProtection = False
        
        # [Proxy]
        OffProxy = proxy["OffProxy"]
        if OffProxy == "True": self.OffProxy = True
        else: self.OffProxy = False    
        #
        CustomProxy = proxy["CustomProxy"]
        if CustomProxy == "True": self.CustomProxy = True
        else: self.CustomProxy = False   
        #
        custom_proxy_address_input = proxy["custom_proxy_address_input"]
        if custom_proxy_address_input == "": self.custom_proxy_address_input = "0.0.0.0"
        else: self.custom_proxy_address_input = custom_proxy_address_input
        #
        custom_proxy_port_input = proxy["custom_proxy_port_input"]
        if custom_proxy_port_input == "": self.custom_proxy_port_input = "0000"
        else: self.custom_proxy_port_input = custom_proxy_port_input
        #
        applyProxy = proxy["applyProxy"]
        if applyProxy == "True": self.applyProxy = True
        else: self.applyProxy = False   
        
        
    def settings_save(self):
        # [Developer]
        developer["debug_javaScriptConsoleMessage"] = str(self.debug_javaScriptConsoleMessage)

        # [General]
        general["javascript"] = str(self.javascript)
        
        # [Custom]
        custom["search_engine"] = str(self.search_engine)
        custom["search_engine_addr"] = str(self.search_engine_addr)
        #
        custom["tor_search_engine"] = str(self.tor_search_engine)
        custom["tor_search_engine_addr"] = str(self.tor_search_engine_addr)
        
        # [Blocker]
        # ad blocking
        blocker["ad_blocker"] = str(self.ad_blocker)
        #
        blocker["ad_auto_update"] = str(self.ad_auto_update)
        #
        blocker["ad_lists"] = str(self.ad_lists)
        
        # privacy blocking
        blocker["privacy_blocker"] = str(self.privacy_blocker)
        #
        blocker["privacy_auto_update"] = str(self.privacy_auto_update)
        #
        blocker["privacy_lists"] = str(self.privacy_lists)
        
        # cookie blocking
        blocker["cookie_blocker"] = str(self.cookie_blocker)
        #
        blocker["cookie_auto_update"] = str(self.cookie_auto_update)
        #
        blocker["cookie_lists"] = str(self.cookie_lists)
        
        # [User.Agent]
        useragent["default_user_agent"] = str(self.default_user_agent)
        #
        useragent["random_user_agent"] = str(self.random_user_agent)
        #
        useragent["custom_user_agent"] = str(self.custom_user_agent)
        #
        useragent["custom_user_agent_input"] = str(self.custom_user_agent_input)
        
        # [Privacy]
        privacy["RouteTrafficThroughTor"] = str(self.RouteTrafficThroughTor)
        #
        privacy["TrackingLinkProtection"] = str(self.TrackingLinkProtection)
        
        # [Proxy]
        proxy["OffProxy"] = str(self.OffProxy)  
        #
        proxy["CustomProxy"] = str(self.CustomProxy)
        #
        proxy["custom_proxy_address_input"] = str(self.custom_proxy_address_input)
        #
        proxy["custom_proxy_port_input"] = str(self.custom_proxy_port_input)
        # 
        proxy["applyProxy"] = str(self.applyProxy)
        
  
        with open(config_file, 'w') as configfile:
            config.write(configfile)


    def settings_apply(self):
        # save the settings before applying them
        self.settings_save()
        
        proxy = QNetworkProxy()
        
        # apply all settings than can be applied
        
        # [General]
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, self.javascript)
            
        # [User.Agent]
        # check if the default user agent should be used
        if self.default_user_agent:
            self.UserAgentInput_widget.setDisabled(True)
            self.UserAgentInput_widget.setStyleSheet("background-color: #4a4949; color: #4a4949;")
            self.profile.setHttpUserAgent("")
            # disable user agent input and change color to display
            self.UserAgentInput_plainTextEdit.setReadOnly(True)
            self.UserAgentInput_plainTextEdit.setStyleSheet("color: gray;")
            
        # check if random user agent should be used
        elif self.random_user_agent:
            self.UserAgentInput_widget.setDisabled(True)
            self.UserAgentInput_widget.setStyleSheet("background-color: #4a4949; color: #4a4949;")
            # generate and set a random useragent
            self.profile.setHttpUserAgent(fake.useragent())
            # disable user agent input and change color to display
            self.UserAgentInput_plainTextEdit.setReadOnly(True)
            self.UserAgentInput_plainTextEdit.setStyleSheet("color: gray;")
        
        # check if custom user agent should be used
        elif self.custom_user_agent:
            self.UserAgentInput_widget.setDisabled(False)
            self.UserAgentInput_widget.setStyleSheet("background-color: transparent; color: white;")
            # get and set useragent
            self.profile.setHttpUserAgent(str(self.custom_user_agent_input))
            # enable user agent input and change color to display
            self.UserAgentInput_plainTextEdit.setReadOnly(False)
            self.UserAgentInput_plainTextEdit.setStyleSheet("color: white;")
            
        # [Privacy]
        if self.RouteTrafficThroughTor:
            # set proxy
            proxy.setType(QNetworkProxy.Socks5Proxy)
            proxy.setHostName("127.0.0.1")
            proxy.setPort(self.socks_port)
        if not self.RouteTrafficThroughTor:
            QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.NoProxy))
            
        # [Proxy]
        if not self.RouteTrafficThroughTor:
            if self.OffProxy:
                self.ProxyInput_widget.setDisabled(True)
                self.ProxyInput_widget.setStyleSheet("background-color: #4a4949; color: #4a4949;")
                self.applyProxy = False
                # Deactivate proxy
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.NoProxy))
            
            elif self.CustomProxy:
                self.ProxyInput_widget.setDisabled(False)
                self.ProxyInput_widget.setStyleSheet("background-color: transparent; color: white;")
                # set custom proxy
                if self.applyProxy:
                    proxy.setType(QNetworkProxy.Socks5Proxy)
                    proxy.setHostName(str(self.custom_proxy_address_input))
                    proxy.setPort(int(self.custom_proxy_port_input))
                    proxy.setCapabilities(QNetworkProxy.SctpTunnelingCapability)
        if self.RouteTrafficThroughTor:
            self.ProxyInput_widget.setDisabled(True)
            self.ProxyInput_widget.setStyleSheet("background-color: #4a4949; color: #4a4949;")
            
        # set proxy
        QNetworkProxy.setApplicationProxy(proxy) 
        # reload the browser so settings can apply
        self.browser.reload()
        
