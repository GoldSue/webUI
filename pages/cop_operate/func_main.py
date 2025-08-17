from elements.cop_operate.employee_manage.titlt_main_ele import TitleMainEle
from pages.base_page import BasePage
from elements.cop_operate.employee_manage.func_main__ele import FuncMainEle
from utils.utils import random_digits, random_letters


class FuncMain(BasePage):

    def add_func(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*FuncMainEle.func_main_button)

        self.click(*FuncMainEle.add_func)
        self.send_keys(random_digits(6), *FuncMainEle.add_func_id)
        self.send_keys(random_letters(6), *FuncMainEle.add_func_name)
        self.click(*FuncMainEle.add_func_save)

    def assert_add_func_success(self):
        return self.get_text(*FuncMainEle.assert_add_func_success)

    def edit_func(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*FuncMainEle.func_main_button)

        self.click(*FuncMainEle.edit_func)
        self.send_keys(random_letters(6), *FuncMainEle.edit_func_name)
        self.click(*FuncMainEle.edit_func_save)

    def assert_edit_func_success(self):
        return self.get_text(*FuncMainEle.assert_edit_func_success)

    def stop_func(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*FuncMainEle.func_main_button)

        self.click(*FuncMainEle.stop_func)
        self.click(*FuncMainEle.stop_func_confirm)

    def assert_stop_func_success(self):
        return self.get_text(*FuncMainEle.assert_stop_func_success)

    def start_func(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*FuncMainEle.func_main_button)

        self.click(*FuncMainEle.start_func)

    def assert_start_func_success(self):
        return self.get_text(*FuncMainEle.assert_start_func_success)

    def delete_func(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*FuncMainEle.func_main_button)

        self.click(*FuncMainEle.delete_func)
        self.click(*FuncMainEle.delete_func_confirm)

    def assert_delete_func_success(self):
        return self.get_text(*FuncMainEle.assert_delete_func_success)



