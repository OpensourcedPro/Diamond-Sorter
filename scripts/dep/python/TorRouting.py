import stem.process
import requests
import os
import re

# get dirs
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
tor_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..')).replace("\\", "/")
tor_file = os.path.join(tor_dir, "tor/tor.exe")

class TorProxy():
    def updateGeoIpFile(url):
        try:
            # Extract the file name from the URL
            file_name = os.path.join(tor_dir, url.split("/")[-1])
            # Make a GET request to the raw GitHub URL
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the content to a local file
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
            
            return (os.path.join(tor_dir, file_name))
        except Exception as e:
            pass
        

    def launchTorProxy(self):
        self.socks_port = 9001
        self.control_port = 9002
        
        # update GeoIpFile
        GeoIpFilePath = TorProxy.updateGeoIpFile("https://raw.githubusercontent.com/torproject/tor/main/src/config/geoip")
        
        # launch tor as proxy 
        tor_process = stem.process.launch_tor_with_config(
            config = {
                'SocksPort': str(self.socks_port),
                'ControlPort': str(self.control_port),
                'CookieAuthentication': '1',
                'GeoIPFile': GeoIpFilePath,
            },
            init_msg_handler = lambda line: print(line) if re.search('Bootstrapped', line) else False,
            tor_cmd = tor_file
        )
        
