import time

from selenium.webdriver.common.by import By

from base.base import BasePage
from elements.loginEle import LoginEle as login
import pytest


class LoginPage(BasePage):


    def open(self):
        self.driver.get("https://console-paas.digiwincloud.com.cn/login")

    def login(self, username, password):
        self.open()
        self.send_keys(username, *login.username)
        self.send_keys(password, *login.password)
        self.driver.find_element(By.TAG_NAME, "body").click()
        self.click(*login.login_button, timeout= 3)



    def get_right_message(self):
        text =  self.get_text(*login.right_message, timeout= 3)
        print("[DEBUG] 正在查找元素:", text)
        return text

    def get_error_message(self):
        return self.get_text(*login.error_message,timeout= 3)




