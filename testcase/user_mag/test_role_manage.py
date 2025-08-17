from conftest import assert_with_log
from pages.user_mag.role_manage.role_manage import RoleManage
from config.logger import logger

class TestRoleManage():

    # def test_add_role(self,assert_log,login,go_user_mag):
    #     role_manage = RoleManage(login)
    #     role_manage.add_role()
    #     actual = role_manage.assert_add_role_success()
    #     expected = "新增成功"
    #     assert_log(expected, actual)

    def test_add_role_batch(self,assert_log,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.add_role_batch()
        actual = role_manage.assert_add_role_batch_success()
        assert_with_log('导入成功', actual)

    # def test_edit_role(self,assert_log,login,go_user_mag):
    #     role_manage = RoleManage(login)
    #     role_manage.edit_user()
    #     actual = role_manage.assert_edit_role_success()
    #     expected = "修改成功"
    #     assert_log(expected, actual)
    #
    # def test_delete_role(self,assert_log,login,go_user_mag):
    #     role_manage = RoleManage(login)
    #     role_manage.delete_user()
    #     actual = role_manage.assert_delete_role_success()
    #     expected = "删除成功"
    #     assert_log(expected, actual)

