import time

from base.base import BasePage
from elements.user_mag_ele.add_cop_user_ele import AddCopUser as addcop
from utils.utils import random_digits, random_letters_digits, random_letters, get_case_data


add_user_data = get_case_data('user_mag_data','add_cop_user.yaml', 'add_cop_user')
edit_user_data = get_case_data('user_mag_data','add_cop_user.yaml', 'edit_cop_user')
print(add_user_data)
print(edit_user_data)
class CopUser(BasePage):


    def add_cop_user(self):
        self.click(*addcop.add_cop_button)
        self.click(*addcop.add_cop)
        self.click(*addcop.add_new_cop)

        self.send_keys(add_user_data.get('userID'), *addcop.user_id)
        self.send_keys(add_user_data.get('username'), *addcop.user_name)
        self.send_keys(add_user_data.get('pwd'), *addcop.user_pwd)
        self.click(*addcop.add_save)

    def assert_add_cop_success(self):
        return self.get_text(*addcop.assert_add_cop_success)

    def search_cop_user(self):
        time.sleep(2)
        self.send_keys(add_user_data.get('userID'), *addcop.input_user_id, timeout=3)
        self.click(*addcop.search_user)
    def assert_search_cop_success(self):
        return self.get_text(*addcop.assert_search_cop_success)

    def edit_cop_user(self):
        self.search_cop_user()
        time.sleep(1)
        self.click(*addcop.edit_user)
        time.sleep(1)
        self.send_keys(edit_user_data.get('username'), *addcop.edit_user_name)
        time.sleep(2)
        self.click(*addcop.edit_save)

    def assert_edit_success(self):
        return self.get_text(*addcop.assert_edit_success)

    def stop_cop_user(self):
        time.sleep(1)
        self.search_cop_user()
        time.sleep(1)
        self.click(*addcop.stop_user)
        self.click(*addcop.stop_user_confirm)

    def assert_stop_success(self):
        return self.get_text(*addcop.assert_stop_success)

    def start_cop_user(self):
        self.search_cop_user()
        time.sleep(1)
        self.click(*addcop.start_user)

    def assert_start_success(self):
        return self.get_text(*addcop.assert_start_success)

    def delete_cop_user(self):
        time.sleep(1)
        self.stop_cop_user()
        time.sleep(1)
        self.click(*addcop.delete_user)
        self.click(*addcop.delete_user_confirm)

    def assert_delete_success(self):
        return self.get_text(*addcop.assert_delete_success)


    def close_add(self):
        self.click(*addcop.close_add)