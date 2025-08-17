from pages.base_page import BasePage
from elements.user_mag_ele.role_manage_ele import RoleManageEle
from utils.utils import random_digits


class RoleManage(BasePage):


    def add_role(self):
        self.click(*RoleManageEle.role_manage_button)
        self.click(*RoleManageEle.add_role_button)
        self.send_keys(random_digits(6), *RoleManageEle.role_id)
        self.send_keys(random_digits(6), *RoleManageEle.role_name)
        self.send_keys("角色管理者", *RoleManageEle.role_description)
        self.click(*RoleManageEle.save_role_button)

    def assert_add_role_success(self):
        return self.get_text(*RoleManageEle.assert_add_role_success)

    def add_role_batch(self):
        self.click(*RoleManageEle.role_manage_button)
        self.click(*RoleManageEle.add_role_batch)
        self.upload_file("data", RoleManageEle.add_role_batch_file, "import_role.xlsx")
        self.click(*RoleManageEle.add_role_batch_button)

    def assert_add_role_batch_success(self):
        return self.get_text(*RoleManageEle.assert_add_role_batch_success)

    def edit_user(self):
        self.click(*RoleManageEle.role_manage_button)
        self.click(*RoleManageEle.edit_user_button)
        self.send_keys(random_digits(6), *RoleManageEle.edit_user_name)
        self.click(*RoleManageEle.edit_user_save)

    def assert_edit_role_success(self):
        return self.get_text(*RoleManageEle.assert_edit_role_success)

    def delete_user(self):
        self.click(*RoleManageEle.role_manage_button)
        self.click(*RoleManageEle.delete_user_button)
        self.click(*RoleManageEle.delete_user_confirm)

    def assert_delete_role_success(self):
        return self.get_text(*RoleManageEle.assert_delete_role_success)

