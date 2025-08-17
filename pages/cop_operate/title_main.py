from pages.base_page import BasePage
from elements.cop_operate.employee_manage.titlt_main_ele import TitleMainEle
from utils.utils import random_digits


class TitletMain(BasePage):

    def add_title(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*TitleMainEle.title_main)
        self.click(*TitleMainEle.add_title)
        self.send_keys(random_digits(6), *TitleMainEle.add_title_id)
        self.send_keys(random_digits(6), *TitleMainEle.add_title_name)
        self.click(*TitleMainEle.add_title_save)

    def assert_add_title_success(self):
        return self.get_text(*TitleMainEle.assert_add_title_success)

    def edit_title(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*TitleMainEle.title_main)
        self.click(*TitleMainEle.edit_title)
        self.send_keys(random_digits(6), *TitleMainEle.edit_title_name)
        self.click(*TitleMainEle.edit_title_save)

    def assert_edit_title_success(self):
        return self.get_text(*TitleMainEle.assert_edit_title_success)

    def delete_title(self):
        self.click(*TitleMainEle.employee_manage_button)
        self.click(*TitleMainEle.title_main)
        self.click(*TitleMainEle.delete_title)
        self.click(*TitleMainEle.delete_title_confirm)

    def assert_delete_title_success(self):
        return self.get_text(*TitleMainEle.assert_delete_title_success)



