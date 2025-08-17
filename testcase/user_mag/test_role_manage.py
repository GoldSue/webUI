import allure

from conftest import assert_with_log
from pages.user_mag.role_manage.role_manage import RoleManage
from config.logger import logger

@allure.feature('用户管理')
class TestRoleManage():

    @allure.story('角色管理')
    @allure.title('新增角色')
    def test_add_role(self,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.add_role()
        actual = role_manage.assert_add_role_success()
        assert_with_log("新增成功", actual)

    @allure.story('角色管理')
    @allure.title('批量新增角色')
    def test_add_role_batch(self,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.add_role_batch()
        actual = role_manage.assert_add_role_batch_success()
        assert_with_log('导入成功', actual)

    @allure.story('角色管理')
    @allure.title('修改角色')
    def test_edit_role(self,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.edit_user()
        actual = role_manage.assert_edit_role_success()
        assert_with_log("修改成功", actual)

    @allure.story('角色管理')
    @allure.title('删除角色')
    def test_delete_role(self,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.delete_user()
        actual = role_manage.assert_delete_role_success()
        assert_with_log("删除成功", actual)

