from conftest import assert_with_log
from pages.cop_operate.employee_manage import EmployeeMag
from config.logger import logger
from utils.detedect import log_and_time


class TestEmployeeManage():

    def test_add_employee(self,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.add_employee()
        actual = employee_mag.assert_add_employee_success()
        assert_with_log("新增成功", actual)

    def test_add_employ_batch(self,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.add_employ_batch()
        actual = employee_mag.assert_add_employee_batch_success()
        assert_with_log("导入成功", actual)
    #
    def test_edit_employee(self,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.edit_employee()
        actual = employee_mag.assert_edit_employee_success()
        assert_with_log("修改成功", actual)


    def test_stop_employee(self,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.stop_employee()
        actual = employee_mag.assert_stop_employee_success()
        assert_with_log("停用成功", actual)


    def test_start_employee(self,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.start_employee()
        actual = employee_mag.assert_start_employee_success()
        assert_with_log("启用成功", actual)


    def test_delete_employee(self,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.delete_employee()
        actual = employee_mag.assert_delete_employee_success()
        assert_with_log("删除成功", actual)