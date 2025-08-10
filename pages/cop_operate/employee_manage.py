import time

from base.base import BasePage
from elements.cop_operate.employee_manage.employee_manage_ele import EmployeManage
from elements.cop_operate.employee_manage.employee_manage_ele import EmployeManage
from utils.utils import random_digits


class EmployeeMag(BasePage):

    def add_employee(self):
        self.click(*EmployeManage.employee_manage_button)
        self.click(*EmployeManage.add_employee)
        self.send_keys(random_digits(5), *EmployeManage.add_employee_id)
        self.send_keys(random_digits(5), *EmployeManage.add_employee_name)
        self.click(*EmployeManage.add_employ_save)
        self.click(*EmployeManage.add_employee_confirm)

    def assert_add_employee_success(self):
        return self.get_text(*EmployeManage.assert_add_employee_success)

    def edit_employee(self):
        self.click(*EmployeManage.employee_manage_button)
        self.click(*EmployeManage.edit_employee)
        self.send_keys(random_digits(5), *EmployeManage.edit_employee_name)
        self.click(*EmployeManage.edit_employ_save)
        self.click(*EmployeManage.edit_employee_confirm)
    def assert_edit_employee_success(self):
        return self.get_text(*EmployeManage.assert_edit_employee_success)


    def stop_employee(self):
        self.click(*EmployeManage.employee_manage_button)
        self.click(*EmployeManage.stop_employee)

    def assert_stop_employee_success(self):
        return self.get_text(*EmployeManage.assert_stop_employee_success)

    def start_employee(self):
        self.click(*EmployeManage.employee_manage_button)
        self.click(*EmployeManage.start_employee)

    def assert_start_employee_success(self):
        return self.get_text(*EmployeManage.assert_start_employee_success)


    def delete_employee(self):
        self.stop_employee()
        self.click(*EmployeManage.delete_employee)
        self.click(*EmployeManage.delete_employee_confirm)

    def assert_delete_employee_success(self):
        return self.get_text(*EmployeManage.assert_delete_employee_success)
