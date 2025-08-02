import time

from selenium.webdriver.common.by import By

from base.base import BasePage
from elements.loginEle import LoginEle as login
import pytest


class LoginPage(BasePage):

    def login(self, username, password):
        self.send_keys(username, *login.username)
        self.send_keys(password, *login.password)
        time.sleep(3)
        self.click(*login.login_button, timeout= 4)

    def get_right_message(self):
        time.sleep(3)
        text =  self.get_text(*login.right_message, timeout= 10)
        print("[DEBUG] 正在查找元素:", text)
        return text

    def get_error_message(self):
        return self.get_text(*login.error_message,timeout= 10)




