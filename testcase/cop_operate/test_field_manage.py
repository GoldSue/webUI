from conftest import assert_with_log
from pages.cop_operate.field_manage import FieldManage

class TestFieldManage():

    # def test_add_field(self, login,go_cop_operate):
    #     field_manage = FieldManage(login)
    #     field_manage.add_field()
    #     actual = field_manage.assert_add_field_success()
    #     assert_with_log("新增成功", actual)
    #
    # def test_edit_field(self, login,go_cop_operate):
    #     field_manage = FieldManage(login)
    #     field_manage.edit_field()
    #     actual = field_manage.assert_edit_field_success()
    #     assert_with_log("修改成功", actual)
    #
    # def test_delete_field(self, login,go_cop_operate):
    #     field_manage = FieldManage(login)
    #     field_manage.delete_field()
    #     actual = field_manage.assert_delete_field_success()
    #     assert_with_log("删除成功", actual)

    def test_import_field(self, login,go_cop_operate):
        field_manage = FieldManage(login)
        field_manage.import_file()
        actual = field_manage.assert_import_file_success()
        assert_with_log("导入成功", actual)