from pages.base_page import BasePage
from elements.cop_operate.field_manage.field_manage_ele import FieldManageEle
from utils.utils import random_letters


class FieldManage(BasePage):


    def go_to_field_manage(self):
        self.click(*FieldManageEle.field_manage_button)
    def add_field(self):
        self.go_to_field_manage()

        self.click(*FieldManageEle.add_field)
        self.click(*FieldManageEle.add_field_type)
        self.click(*FieldManageEle.add_field_type_selected)
        self.send_keys("3213", *FieldManageEle.add_field_id)
        self.send_keys(random_letters(4), *FieldManageEle.add_field_name)
        self.click(*FieldManageEle.add_field_save)

    def assert_add_field_success(self):
        return self.get_text(*FieldManageEle.assert_add_field_success)

    def edit_field(self):
        self.go_to_field_manage()
        self.send_keys("3213", *FieldManageEle.edit_search_input)
        self.click(*FieldManageEle.edit_search_button)
        self.click(*FieldManageEle.edit_field)
        self.send_keys(random_letters(4), *FieldManageEle.edit_field_name)
        self.click(*FieldManageEle.edit_field_save)
    def assert_edit_field_success(self):
        return self.get_text(*FieldManageEle.assert_edit_field_success)

    def delete_field(self):
        self.go_to_field_manage()
        self.send_keys("3213", *FieldManageEle.delete_search_input)
        self.click(*FieldManageEle.delete_search_button)
        self.click(*FieldManageEle.delete_field)
        self.click(*FieldManageEle.delete_field_confirm)

    def assert_delete_field_success(self):
        return self.get_text(*FieldManageEle.assert_delete_field_success)

    def import_file(self):
        self.go_to_field_manage()
        self.click(*FieldManageEle.import_file_button)
        self.click(*FieldManageEle.import_file_select)
        self.upload_file('data', FieldManageEle.import_file_up,r"area_corp_export_template_CN.xlsx")
        self.click(*FieldManageEle.import_file)

    def assert_import_file_success(self):
        return self.get_text(*FieldManageEle.assert_import_file_success)







