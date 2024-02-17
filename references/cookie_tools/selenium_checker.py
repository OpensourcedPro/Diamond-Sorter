from selenium import webdriver
from selenium.webdriver.common.by import By


class VerifyCookies:

    def __init__(self, url):
        # get the url
        self.url = url
        self.driver = webdriver.Chrome()
        # use implicit wait
        self.driver.implicitly_wait(10)

    def fetch_cookies(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # cookies before login
        print(f"cookies before login = {self.driver.get_cookies()}")
        self.driver.find_element(By.ID, "user-name").send_keys("visual_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        # cookies after login
        print(f"cookies after login = {self.driver.get_cookies()}")
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        # cookies after logout
        print(f"cookies after logout = {self.driver.get_cookies()}")

    def shutdown(self):
        self.driver.close()


saucedemo_url = "https://www.saucedemo.com/"
cookieObject = VerifyCookies(saucedemo_url)

# calling methods from VerifyCookies
cookieObject.fetch_cookies()
cookieObject.shutdown()