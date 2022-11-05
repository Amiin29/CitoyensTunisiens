import configparser
from selenium.webdriver.common.by import By

config = configparser.RawConfigParser()
config.read(".\\Configuration\\conf.ini")


class SetProperty_LogIn:
    def __init__(self, driver):
        self.driver = driver

    def GotToLoginPage(self):
        self.driver.find_element(By.XPATH, "loginBtn_XPATH").click()
