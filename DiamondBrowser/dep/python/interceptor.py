from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QUrl
import configparser
import requests
import datetime
import adblock
import os

# get dirs
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
check_file_path = os.path.join(current_dir, "interceptor/lists/last_update_date.txt")
dep_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..')).replace("\\", "/")

ad_list_dir = os.path.join(current_dir, "interceptor/lists/ad")
privacy_list_dir = os.path.join(current_dir, "interceptor/lists/privacy")
cookie_list_dir = os.path.join(current_dir, "interceptor/lists/cookie")
youtube_ad_file = os.path.join(current_dir, "interceptor/YouTubeSpecific/YouTubeAntiBlockFixRules.txt")
tracking_link_list_dir = os.path.join(current_dir, "interceptor/lists/tracking")


# get config
config_file = os.path.join(dep_dir, "config.cfg")
config = configparser.ConfigParser()


def deactivateForceUpdate():
    global force_update
    # write force_update as false
    blocker = config['Blocker']
    blocker["force_update"] = "false"
    # save to file
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    force_update = False
    
def getBlockerSettings():
    config.read(config_file)
    blocker = config['Blocker']
    privacy = config['Privacy']

    # force update
    force_update = blocker["force_update"]
    if force_update == "True": force_update = True
    else: force_update = False

    # ad blocking
    ad_blocker = blocker["ad_blocker"]
    if ad_blocker == "True": ad_blocker = True
    else: ad_blocker = False
    
    ad_auto_update = blocker["ad_auto_update"]
    if ad_auto_update == "True": ad_auto_update = True
    else: ad_auto_update = False
    
    ad_lists = blocker["ad_lists"]
    if ad_lists == "": ad_lists = ""
    else: ad_lists = ad_lists
    
    # privacy blocking
    privacy_blocker = blocker["privacy_blocker"]
    if privacy_blocker == "True": privacy_blocker = True
    else: privacy_blocker = False
    
    privacy_auto_update = blocker["privacy_auto_update"]
    if privacy_auto_update == "True": privacy_auto_update = True
    else: privacy_auto_update = False
    
    privacy_lists = blocker["privacy_lists"]
    if privacy_lists == "": privacy_lists = ""
    else: privacy_lists = privacy_lists
    
    # cookie blocking
    cookie_blocker = blocker["cookie_blocker"]
    if cookie_blocker == "True": cookie_blocker = True
    else: cookie_blocker = False
    
    cookie_auto_update = blocker["cookie_auto_update"]
    if cookie_auto_update == "True": cookie_auto_update = True
    else: cookie_auto_update = False
    
    cookie_lists = blocker["cookie_lists"]
    if cookie_lists == "": cookie_lists = ""
    else: cookie_lists = cookie_lists
    
    # youtube blocking
    youtube_ad_blocker = blocker["youtube_ad_blocker"]
    if youtube_ad_blocker == "True": youtube_ad_blocker = True
    else: youtube_ad_blocker = False
    
    # tracker
    tracking_link_blocker = privacy["TrackingLinkProtection"]
    if tracking_link_blocker == "True": tracking_link_blocker = True
    else: tracking_link_blocker = False

    return force_update, ad_blocker, privacy_blocker, cookie_blocker, ad_auto_update, privacy_auto_update, cookie_auto_update, ad_lists, privacy_lists, cookie_lists, youtube_ad_blocker, tracking_link_blocker

class LastRun():
    def last_updated_function():
        last_execution_date = LastRun.read_last_execution_date()
        if last_execution_date != datetime.datetime.now().date():
            LastRun.update_last_execution_date()
            return True
        else:
            return False
    def update_last_execution_date():
        with open(check_file_path, "w") as file:
            file.write(str(datetime.datetime.now().date()))
    def read_last_execution_date():
        try:
            with open(check_file_path, "r") as file:
                return datetime.datetime.strptime(file.read().strip(), "%Y-%m-%d").date()
        except FileNotFoundError:
            return None
        
def DownloadUpdateLists(force_update):
    def download_file(url, output_dir):
        try:
            # Extract the file name from the URL
            file_name = os.path.join(output_dir, url.split("/")[-1])
            # Make a GET request to the raw GitHub URL
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the content to a local file
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
        except Exception as e:
            pass
    
    # only update once every day except force_update is True
    if force_update:
        # set force_update to normal value and save it
        deactivateForceUpdate()
    else:
        if not LastRun.last_updated_function():
            return
    
    # get vars
    force_update, ad_blocker, privacy_blocker, cookie_blocker, ad_auto_update, privacy_auto_update, cookie_auto_update,ad_lists, privacy_lists, cookie_lists, youtube_ad_blocker, tracking_link_blocker  = getBlockerSettings()

    # ad block auto update and list download
    if ad_auto_update:
        split_urls = ad_lists.split(",")
        # Remove spaces from each substring
        cleaned_urls = [substring.strip() for substring in split_urls]
        for url in cleaned_urls:
            download_file(url, ad_list_dir)
        
    # privacy block auto update and list download
    if privacy_auto_update:
        split_urls = privacy_lists.split(",")
        # Remove spaces from each substring
        cleaned_urls = [substring.strip() for substring in split_urls]
        for url in cleaned_urls:
            download_file(url, privacy_list_dir)
        
    # cookie block auto update and list download
    if cookie_auto_update:
        split_urls = cookie_lists.split(",")
        # Remove spaces from each substring
        cleaned_urls = [substring.strip() for substring in split_urls]
        for url in cleaned_urls:
            download_file(url, cookie_list_dir)

resource_types = {
    0: "main_frame",
    1: "sub_frame",
    2: "stylesheet",
    3: "script",
    4: "image",
    5: "font",
    6: "object_subrequest",
    7: "object",
    8: "media",
    9: "worker",
    10: "shared_worker",
    11: "prefetch",
    12: "favicon",
    13: "xmlhttprequest",
    14: "ping",
    15: "service_worker",
    16: "csp_report",
    17: "plugin_resource",
    18: "object_subrequest",
    19: "main_frame",
    20: "sub_frame",
    255: "other"
}

# Iterate through all files with .txt extension in the specified directory
def init_lists():
    ad_filters = ""
    privacy_filters = ""
    cookie_filters = ""
    youtube_ad_filters = ""
    tracking_link_filters = ""
    
    # ad lists
    for filename in os.listdir(ad_list_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(ad_list_dir, filename)
            with open(file_path, "r") as f:
                content = f.read()
                ad_filters += content
                
    # privacy lists
    for filename in os.listdir(privacy_list_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(privacy_list_dir, filename)
            with open(file_path, "r") as f:
                content = f.read()
                privacy_filters += content

    # cookie lists
    for filename in os.listdir(cookie_list_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(cookie_list_dir, filename)
            with open(file_path, "r") as f:
                content = f.read()
                cookie_filters += content    
    
    # youtube ad lists
    file_path = os.path.join(youtube_ad_file)
    with open(file_path, "r") as f:
        content = f.read()
        youtube_ad_filters += content 
    
    # tracking link lists
    for filename in os.listdir(tracking_link_list_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(tracking_link_list_dir, filename)
            with open(file_path, "r") as f:
                content = f.read()
                tracking_link_filters += content    
    return ad_filters, privacy_filters, cookie_filters, youtube_ad_filters, tracking_link_filters

# get lists
ad_filters, privacy_filters, cookie_filters, youtube_ad_filters, tracking_link_filters = init_lists()


class blocking():
    def ad_blocking(url, source_url, resource_type):
        # init filter sets
        ad_filter_set = adblock.FilterSet(debug=True)
        ad_filter_set.add_filter_list(ad_filters)
        # create engine
        ad_engine = adblock.Engine(filter_set=ad_filter_set)
        
        # check url
        ad_blocker_result = ad_engine.check_network_urls(
            url=url,
            source_url=source_url,
            request_type=resource_type,
        )
        # return True if True else check other filters
        assert isinstance(ad_blocker_result, adblock.BlockerResult)
        if ad_blocker_result.matched: return True
        
        
    def privacy_blocking( url, source_url, resource_type):
        # init filter sets
        privacy_filter_set = adblock.FilterSet(debug=True)
        privacy_filter_set.add_filter_list(privacy_filters)
        # create engine
        privacy_engine = adblock.Engine(filter_set=privacy_filter_set)
        
        # check url
        privacy_blocker_result = privacy_engine.check_network_urls(
            url=url,
            source_url=source_url,
            request_type=resource_type,
        )
        # return True if True else check other filters
        assert isinstance(privacy_blocker_result, adblock.BlockerResult)
        if privacy_blocker_result.matched: return True
        
        
    def cookie_blocking(url, source_url, resource_type):
        # init filter sets
        cookie_filter_set = adblock.FilterSet(debug=True)
        cookie_filter_set.add_filter_list(cookie_filters)
        # create engine
        cookie_engine = adblock.Engine(filter_set=cookie_filter_set)
        
        # check url
        cookie_blocker_result = cookie_engine.check_network_urls(
            url=url,
            source_url=source_url,
            request_type=resource_type,
        )
        # return True if True else check other filters
        assert isinstance(cookie_blocker_result, adblock.BlockerResult)
        if cookie_blocker_result.matched: return True
        
    def youtube_ad_blocking(url, source_url, resource_type):
        # init filter sets
        youtube_ad_filter_set = adblock.FilterSet(debug=True)
        youtube_ad_filter_set.add_filter_list(youtube_ad_filters)
        # create engine
        youtube_ad_engine = adblock.Engine(filter_set=youtube_ad_filter_set)
        
        # check url
        youtube_ad_blocker_result = youtube_ad_engine.check_network_urls(
            url=url,
            source_url=source_url,
            request_type=resource_type,
        )
        # return True if True else check other filters
        assert isinstance(youtube_ad_blocker_result, adblock.BlockerResult)
        if youtube_ad_blocker_result.matched: return True
        
    def tracking_link_blocking(url, source_url, resource_type):
        # init filter sets
        tracking_link_filter_set = adblock.FilterSet(debug=True)
        tracking_link_filter_set.add_filter_list(tracking_link_filters)
        # create engine
        youtube_ad_engine = adblock.Engine(filter_set=tracking_link_filter_set)
        
        # check url
        tracking_link_protection_result = youtube_ad_engine.check_network_urls(
            url=url,
            source_url=source_url,
            request_type=resource_type,
        )
        # return True if True else check other filters
        assert isinstance(tracking_link_protection_result, adblock.BlockerResult)
        if tracking_link_protection_result.matched: return True


class UrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, request):
        # get vars
        force_update, ad_blocker, privacy_blocker, cookie_blocker, ad_auto_update, privacy_auto_update, cookie_auto_update,ad_lists, privacy_lists, cookie_lists, youtube_ad_blocker, tracking_link_blocker  = getBlockerSettings()

        # run auto update
        DownloadUpdateLists(force_update)
        
        # get url as string
        url               = request.requestUrl().toString()
        source_url        = request.firstPartyUrl().toString()
        # get url resource type
        raw_resource_type = int(request.resourceType())
        if raw_resource_type in resource_types:
            resource_type = resource_types[raw_resource_type]
        
        # check if ad blocking is active
        if ad_blocker:
            # check if url should be blocked (ads)
            ad_result = blocking.ad_blocking(url, source_url, resource_type)
            # block if True else pass
            if ad_result == True:
                request.block(True)
                return
            
        # check if privacy blocking is active
        if privacy_blocker:
            # check if url should be blocked (ads)
            privacy_result = blocking.privacy_blocking(url, source_url, resource_type)
            # block if True else pass
            if privacy_result == True:
                request.block(True)
                return
            
        # check if cookie blocking is active
        if cookie_blocker:
            # check if url should be blocked (ads)
            cookie_result = blocking.cookie_blocking(url, source_url, resource_type)
            # block if True else pass
            if cookie_result == True:
                request.block(True)
                return
            
        # check if youtube ad blocking is active
        if youtube_ad_blocker:
            # check if url should be blocked (ads)
            youtube_ad_result = blocking.youtube_ad_blocking(url, source_url, resource_type)
            # block if True else pass
            if youtube_ad_result == True:
                request.block(True)
                return
            
        # check if tracking link blocking is active
        if tracking_link_blocker:
            # check if url should be blocked (ads)
            tracking_link_result = blocking.tracking_link_blocking(url, source_url, resource_type)
            # block if True else pass
            if tracking_link_result == True:
                msg_box = QMessageBox(None)
                msg_box.setWindowTitle('Block or Proceed')
                msg_box.setText('Tracking link detected. Do you want to proceed and risk logging your IP, or block it to keep your privacy?\nWarning even Blocking the link might get your IP logged!')
                msg_box.addButton('Proceed', QMessageBox.NoRole)
                msg_box.setDefaultButton(block_button := msg_box.addButton('Block', QMessageBox.YesRole))
                msg_box.exec_()
                # button actions
                if msg_box.clickedButton() == block_button:
                    request.block(True)
                    return