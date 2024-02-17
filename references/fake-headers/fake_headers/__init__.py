from fake_headers.browsers import chrome, firefox, opera, random_browser
from fake_headers.headers import make_header
from fake_headers.platforms import linux, macos, random_os, windows


class Headers:
    '''
    browser - str, chrome/firefox/opera. User Agent browser. Default: random\n
    os - str, win/mac/lin. OS of User Agent. Default: random\n
    headers - bool, True/False. Generate random headers or no. Default: False
    '''

    __os = {
        'win': windows,
        'mac': macos,
        'lin': linux
    }

    __browser = {
        'chrome': chrome,
        'firefox': firefox,
        'opera': opera
    }

    def __init__(self, browser: str = None, os: str = None,
                 headers: bool = False):
        self.__platform = self.__os.get(os, random_os)
        self.__browser = self.__browser.get(browser, random_browser)
        self.__headers = make_header if headers else self.empty

    def empty(self) -> dict:
        return {}

    def generate(self) -> dict:
        platform = self.__platform()
        browser = self.__browser()

        headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'User-Agent': browser.replace('%PLAT%', platform)
        }

        headers.update(self.__headers())

        return headers
