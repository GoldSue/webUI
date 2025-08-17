import time

from pages.base_page import BasePage
from elements.cop_operate.opetate_unit.operate_unit_ele import OperateUnit as op
from pages.home_page import HomePage
from utils.utils import random_digits, random_letters


class OperateUnit(BasePage):


    def module_cop_operate(self):
        home_page = HomePage(self.driver)

        home_page.get_home_page()
        home_page.go_to_module(*op.cop_operate,module_name="企业运营")

    def add_cop_(self):
        self.click(*op.add_cop_operate_unit)
        self.send_keys(random_digits(6), *op.cop_operate_unit_id)
        self.send_keys(random_digits(6), *op.cop_operate_unit_name)
        self.click(*op.cop_operate_unit_type)
        self.click(*op.cop_operate_select_type)
        self.click(*op.add_cop_save)

    def assert_add_operate_unit_success(self):
        return self.get_text(*op.assert_add_operate_unit_success)

    def edit_cop_operate_unit(self):
        self.click(*op.edit_cop_operate_unit)
        self.send_keys(random_digits(6), *op.cop_operate_unit_name)
        self.click(*op.cop_operate_unit_type)
        self.click(*op.cop_operate_select_type2)
        self.click(*op.add_cop_save)

    def assert_edit_cop_success(self):
        return self.get_text(*op.assert_edit_cop_success)

    def delete_cop_operate_unit(self):
        self.click(*op.delete_cop_operate_unit)
        self.click(*op.delete_cop_operate_confirm)

    # def assert_delete_success(self):
    #     return self.get_text(*op.assert_delete_success)

    def cop_setting(self):
        self.click(*op.cop_operate_unit_setting)
        self.click(*op.cop_operate_unit_setting_add)
        # time.sleep(1)
        self.click(*op.cop_type)
        self.click(*op.cop_type_select)
        self.send_keys(random_digits(6), *op.cop_code)
        self.send_keys(random_letters(4), *op.cop_name)
        self.click(*op.cop_operate_unit_setting_save)

    def assert_cop_setting_success(self):
        return self.get_text(*op.assert_cop_setting_success)


