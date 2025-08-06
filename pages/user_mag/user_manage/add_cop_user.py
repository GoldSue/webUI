from base.base import BasePage
from elements.user_mag_ele.add_cop_user_ele import AddCopUser as addcop
from utils.utils import random_digits,random_letters_digits,random_letters


class AddCopUser(BasePage):


    def add_cop_user(self):
        self.click(*addcop.add_cop_button)
        self.click(*addcop.add_cop)
        self.click(*addcop.add_new_cop)
        self.send_keys(random_digits(6), *addcop.user_id)
        self.send_keys(random_letters(4), *addcop.user_name)
        self.send_keys(random_letters_digits(8), *addcop.user_pwd)
        self.click(*addcop.add_save)

    def assert_add_cop_success(self):
        return self.get_text(*addcop.assert_add_cop_success)

    def close_add(self):
        self.click(*addcop.close_add)