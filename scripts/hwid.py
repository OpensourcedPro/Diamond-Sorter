import hashlib
import requests
import time
import diamondsorter

def get_hwid():
    import os, platform
    node = os.getenv("computername") + platform.processor() + os.getenv("SystemDrive")
    hwid = hashlib.sha256(node.encode()).hexdigest()
    return hwid

def check_hwid(hwid):
    # Check the hardware ID against a list stored in a text file
    try:
        with open("hwid_list.txt", "r") as file:
            for line in file:
                if hwid in line:
                    return True
        return False
    except:
        return False

def check_hwid_online(hwid):
    # Check the hardware ID against a list stored on a website
    try:
        headers = {
            "Authorization": "97ae8e140f94ef52411b6a88b49feb9ae85b4d3c78ba460b8d32d7088d2223a04ee59094a187d24b36c4f1fa0a9a7c43d323dccb56180cf9b36df400fee2f0b8"
        }
        response = requests.get("https://hastebin.com/share/hufozozayu", headers=headers)
        if response.status_code == 200:
            for line in response.text.splitlines():
                if hwid in line:
                    return True
        return False
    except:
        return False

def launch_diamondsorter():
    diamondsorter.DiamondSorter()

# Main program
if __name__ == "__main__":
    hwid = get_hwid()
    if check_hwid(hwid) or check_hwid_online(hwid):
        print("Your HWID is on the list. The program can run.")
        launch_diamondsorter()
    else:
        print("Your HWID is not allowed. Your HWID is:", hwid)
        time.sleep(10)
        exit()