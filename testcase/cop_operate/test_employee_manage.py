from pages.cop_operate.employee_manage import EmployeeMag
from config.logger import logger



class TestEmployeeManage():

    def test_add_employee(self,assert_log,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.add_employee()
        actual = employee_mag.assert_add_employee_success()
        expected = "新增成功"
        assert_log(expected, actual)

    def test_edit_employee(self, assert_log,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.edit_employee()
        actual = employee_mag.assert_edit_employee_success()
        expected = "修改成功"
        assert_log(expected, actual)

    def test_stop_employee(self, assert_log,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.stop_employee()
        actual = employee_mag.assert_stop_employee_success()
        expected = "停用成功"
        assert_log(expected, actual)

    def test_start_employee(self, assert_log,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.start_employee()
        actual = employee_mag.assert_start_employee_success()
        expected = "启用成功"
        assert_log(expected, actual)

    def test_delete_employee(self, assert_log,login,go_cop_operate):
        employee_mag = EmployeeMag(login)
        employee_mag.delete_employee()
        actual = employee_mag.assert_delete_employee_success()
        expected = "删除成功"
        assert_log(expected, actual)