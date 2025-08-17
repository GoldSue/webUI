import time

from pages.base_page import BasePage
from elements.cop_operate.cop_organ.cop_organ import CopOrganEle
from utils.utils import random_letters, random_digits


class CopOrgan(BasePage):


    def go_to_cop_organ(self):
        self.click(*CopOrganEle.cop_organ_moudle)
    def add_dep(self):
        self.go_to_cop_organ()
        self.click(*CopOrganEle.add_dep)
        self.click(*CopOrganEle.add_dep_select)
        self.click(*CopOrganEle.add_dep_selected)
        self.send_keys(random_letters(4), *CopOrganEle.add_dep_id)
        self.send_keys(random_letters(4), *CopOrganEle.add_dep_name)
        self.click(*CopOrganEle.add_dep_leader_select)
        self.click(*CopOrganEle.add_dep_leader_search)
        self.send_keys("9999", *CopOrganEle.add_dep_leader_search)
        self.click(*CopOrganEle.add_dep_leader_search_button)
        self.click(*CopOrganEle.add_dep_leader_selected)
        self.click(*CopOrganEle.add_dep_confirm)
        self.click(*CopOrganEle.add_dep_save)

    def assert_add_dep_success(self):
        return self.get_text(*CopOrganEle.assert_add_dep_success)



    def add_sub_dep(self):
        self.go_to_cop_organ()
        self.click(*CopOrganEle.add_sub_befor)
        # self.click(*CopOrganEle.add_sub_dep_selected)
        self.click(*CopOrganEle.add_sub_dep)
        self.send_keys(random_digits(4),*CopOrganEle.add_sub_dep_id)
        self.send_keys(random_letters(4), *CopOrganEle.add_sub_dep_name)
        self.click(*CopOrganEle.add_sub_dep_leader_select)
        self.send_keys("9999", *CopOrganEle.add_sub_dep_leader_search)
        self.click(*CopOrganEle.add_sub_dep_leader_search_button)
        self.click(*CopOrganEle.add_sub_dep_leader_selected)
        self.click(*CopOrganEle.add_sub_dep_confirm)
        self.click(*CopOrganEle.add_sub_dep_save)

    def assert_add_sub_dep_success(self):
        return self.get_text(*CopOrganEle.assert_add_sub_dep_success)

    def search_dep(self):
        # self.click(*CopOrganEle.cop_organ_moudle)
        # self.click(*CopOrganEle.delete_cop_type)
        # self.click(*CopOrganEle.delete_cop_type_selected)
        # self.send_keys('2121', *CopOrganEle.delete_sub_dep_search_input)
        # self.click(*CopOrganEle.delete_sub_dep_search_button)
        self.click(*CopOrganEle.edit_cop_befor)

    def edit_sub_dep(self):
        self.go_to_cop_organ()
        self.search_dep()
        self.click(*CopOrganEle.edit_sub_dep_more)
        self.click(*CopOrganEle.edit_sub_dep)
        self.send_keys(random_letters(4), *CopOrganEle.edit_sub_dep_name)
        self.click(*CopOrganEle.edit_sub_save)

    def assert_edit_sub_dep_success(self):
        return self.get_text(*CopOrganEle.assert_edit_sub_dep_success)

    def delete_sub_dep(self):
        self.go_to_cop_organ()
        self.search_dep()
        self.click(*CopOrganEle.edit_sub_dep_more)
        self.click(*CopOrganEle.delete_sub_dep)
        self.click(*CopOrganEle.delete_sub_dep_confirm)

    def assert_delete_sub_dep(self):
        return self.get_text(*CopOrganEle.assert_delete_sub_dep_success)


    def add_dep_member(self):
        self.go_to_cop_organ()
        self.search_dep()
        self.click(*CopOrganEle.dep_member)
        if self.ele_exist(*CopOrganEle.is_member_exit, timeout=2):
            self.click(*CopOrganEle.delete_search_selected)
            self.click(*CopOrganEle.delete_member_delete)
            self.click(*CopOrganEle.delete_member_confirm)
        self.click(*CopOrganEle.add_member)
        self.click(*CopOrganEle.add_member_name)
        self.send_keys("9999",*CopOrganEle.add_member_search)
        self.click(*CopOrganEle.add_member_search_button)
        self.click(*CopOrganEle.add_member_selected)
        self.click(*CopOrganEle.add_member_confirm)
        self.click(*CopOrganEle.add_member_deter)
        self.click(*CopOrganEle.add_member_deter_selected)
        self.click(*CopOrganEle.add_member_save)

    def assert_add_dep_member_success(self):
        return self.get_text(*CopOrganEle.assert_add_member_success)

    def edit_dep_member(self):
        self.wait_mask_disappear(timeout=5)
        time.sleep(0.5)
        self.go_to_cop_organ()
        self.search_dep()
        self.click(*CopOrganEle.dep_member)
        self.click(*CopOrganEle.edit_member_selected)
        self.click(*CopOrganEle.edit_member_edit)
        self.click(*CopOrganEle.edit_member_save)

    def assert_edit_dep_member_success(self):
        self.click(*CopOrganEle.cop_organ_moudle)
        return self.get_text(*CopOrganEle.assert_edit_member_success)

    def delete_dep_member(self):
        # self.wait_for_disappear(*CopOrganEle.wait_mask_dis)
        self.go_to_cop_organ()
        self.search_dep()
        self.click(*CopOrganEle.dep_member)
        self.click(*CopOrganEle.delete_search_selected)
        self.click(*CopOrganEle.delete_member_delete)
        self.click(*CopOrganEle.delete_member_confirm)

    def assert_delete_dep_member_success(self):
        return self.get_text(*CopOrganEle.assert_delete_member_success)

    def add_derter_level(self):
        self.go_to_cop_organ()
        self.click(*CopOrganEle.member_derter_level)
        self.click(*CopOrganEle.add_deter_level)
        self.send_keys(random_digits(4), *CopOrganEle.add_deter_level_id)
        self.send_keys(random_digits(2), *CopOrganEle.add_deter_level_name)
        self.send_keys(random_digits(4), *CopOrganEle.add_deter_level_order)
        self.click(*CopOrganEle.add_deter_level_save)

    def assert_add_deter_level_success(self):
        return self.get_text(*CopOrganEle.assert_add_deter_level_success)


    def edit_derter_level(self):
        self.go_to_cop_organ()
        self.click(*CopOrganEle.member_derter_level)
        self.click(*CopOrganEle.edit_deter_level)
        self.send_keys(random_letters(2), *CopOrganEle.edit_deter_level_name)
        self.send_keys(random_digits(4), *CopOrganEle.edit_deter_level_order)
        self.click(*CopOrganEle.edit_deter_level_save)

    def assert_edit_deter_level(self):
        return self.get_text(*CopOrganEle.assert_edit_deter_level_success)

    def delete_derter_level(self):
        self.go_to_cop_organ()
        self.click(*CopOrganEle.member_derter_level)
        self.click(*CopOrganEle.delete_deter_level)
        self.click(*CopOrganEle.delete_deter_level_confirm)

    def assert_delete_deter_level(self):
        return self.get_text(*CopOrganEle.assert_delete_deter_level_success)
