import allure

from config.logger import logger
from conftest import assert_with_log

from pages.user_mag.user_group.user_group import UserGroup

@allure.feature('用户管理')
class TestUserGroup():
    @allure.story('用户群组')
    @allure.title('新增用户群组')
    def test_add_user_group(self,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.add_user_group()
        actual = user_group.assert_add_user_group_success()
        assert_with_log("用户群组已新增", actual)

    @allure.story('用户群组')
    @allure.title('新增子用户群组')
    def test_add_child_user_group(self,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.add_child_user_group()
        actual = user_group.assert_add_child_user_group_success()
        assert_with_log("用户群组已新增", actual)

    @allure.story('用户群组')
    @allure.title('修改用户群组')
    def test_edit_user_group(self,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.edit_user_group()
        actual = user_group.assert_edit_user_group_success()
        assert_with_log("用户群组已修改", actual)

    @allure.story('用户群组')
    @allure.title('删除用户群组')
    def test_delete_user_group(self,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.delete_user_group()
        actual = user_group.assert_delete_user_group_success()
        assert_with_log("用户群组已删除", actual)