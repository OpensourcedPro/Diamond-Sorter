import configparser
import os

# get dirs
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
dep_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..')).replace("\\", "/")
youtube_ad_blocking_js = os.path.join(current_dir, "interceptor/YouTubeSpecific/adBlock.txt")

# get config
config_dir = os.path.join(dep_dir, "config.cfg")
config = configparser.ConfigParser()
config.read(config_dir)

def getBlockerSettings():
    blocker = config['Blocker']
    
    # youtube blocking
    youtube_ad_blocker = blocker["youtube_ad_blocker"]
    if youtube_ad_blocker == "true": youtube_ad_blocker = True
    else: youtube_ad_blocker = False

    return youtube_ad_blocker
# get vars
youtube_ad_blocker = getBlockerSettings()

def getJavascript():
    youtube_ad_blocker_js = ""
    
    # youtube ad blocking js
    with open(youtube_ad_blocking_js, "r") as f:
        content = f.read()
        youtube_ad_blocker_js += content
    
    return youtube_ad_blocker_js
# get js
youtube_ad_blocker_js = getJavascript()

class javascript():
    def inject(self):
        # run injection when page is done loading
        self.browser.loadFinished.connect(self.on_load_finished)
        
        
    def on_load_finished(self, status):
        if status:
            if youtube_ad_blocker:
                # check if the page is youtube
                is_youtube = self.browser.url().host() == "www.youtube.com"
                # check
                if is_youtube:
                    # page is youtube inject javascript
                    self.browser.page().runJavaScript(youtube_ad_blocker_js)