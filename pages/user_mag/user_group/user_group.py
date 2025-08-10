import time

from base.base import BasePage
from elements.user_mag_ele.user_group_ele import UserGroupEle
from utils.utils import random_digits


class UserGroup(BasePage):

    def add_user_group(self):
        self.click(*UserGroupEle.user_group)
        self.click(*UserGroupEle.add_user_group)
        self.send_keys(random_digits(6), *UserGroupEle.add_user_group_id)
        self.send_keys("1111", *UserGroupEle.add_user_group_name)
        self.click(*UserGroupEle.add_user_group_save)

    def assert_add_user_group_success(self):
        time.sleep(0.5)
        return self.get_text(*UserGroupEle.assert_add_user_group_success, timeout=2)

    def add_child_user_group(self):
        self.click(*UserGroupEle.user_group)
        self.click(*UserGroupEle.add_child_user_group)
        self.send_keys(random_digits(6), *UserGroupEle.add_child_user_group_id)
        self.send_keys("2222", *UserGroupEle.add_child_user_group_name)
        self.click(*UserGroupEle.add_user_group_save)

    def assert_add_child_user_group_success(self):
        return self.get_text(*UserGroupEle.assert_add_child_user_group_success)

    def edit_user_group(self):
        self.click(*UserGroupEle.user_group)
        self.click(*UserGroupEle.edit_user_group)
        self.send_keys(random_digits(6), *UserGroupEle.edit_user_group_name)
        self.click(*UserGroupEle.edit_user_group_save)

    def assert_edit_user_group_success(self):
        return self.get_text(*UserGroupEle.assert_edit_user_group_success)

    def delete_user_group(self):
        self.click(*UserGroupEle.user_group)
        self.click(*UserGroupEle.delete_user_group)
        self.click(*UserGroupEle.delete_user_group_confirm)

    def assert_delete_user_group_success(self):
        return self.get_text(*UserGroupEle.assert_delete_user_group_success)

