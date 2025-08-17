import allure

from conftest import assert_with_log
from pages.cop_operate.field_manage import FieldManage

@allure.feature('企业运营')
class TestFieldManage():

    @allure.story('场域管理')
    @allure.title('新增场域')
    def test_add_field(self, login,go_cop_operate):
        field_manage = FieldManage(login)
        field_manage.add_field()
        actual = field_manage.assert_add_field_success()
        assert_with_log("新增成功", actual)

    @allure.story('场域管理')
    @allure.title('修改场域')
    def test_edit_field(self, login,go_cop_operate):
        field_manage = FieldManage(login)
        field_manage.edit_field()
        actual = field_manage.assert_edit_field_success()
        assert_with_log("修改成功", actual)

    @allure.story('场域管理')
    @allure.title('删除场域')
    def test_delete_field(self, login,go_cop_operate):
        field_manage = FieldManage(login)
        field_manage.delete_field()
        actual = field_manage.assert_delete_field_success()
        assert_with_log("删除成功", actual)

    @allure.story('场域管理')
    @allure.title('导入场域')
    def test_import_field(self, login,go_cop_operate):
        field_manage = FieldManage(login)
        field_manage.import_file()
        actual = field_manage.assert_import_file_success()
        assert_with_log("导入成功", actual)