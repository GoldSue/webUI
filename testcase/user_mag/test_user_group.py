from config.logger import logger

from pages.user_mag.user_group.user_group import UserGroup


class TestUserGroup():

    def test_add_user_group(self, assert_log,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.add_user_group()
        actual = user_group.assert_add_user_group_success()
        expected = "用户群组已新增"
        assert_log(expected, actual)


    def test_add_child_user_group(self, assert_log,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.add_child_user_group()
        actual = user_group.assert_add_child_user_group_success()
        expected = "用户群组已新增"
        assert_log(expected, actual)

    def test_edit_user_group(self, assert_log,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.edit_user_group()
        actual = user_group.assert_edit_user_group_success()
        expected = "用户群组已修改"
        assert_log(expected, actual)

    def test_delete_user_group(self, assert_log,login,go_user_mag):
        user_group = UserGroup(login)
        user_group.delete_user_group()
        actual = user_group.assert_delete_user_group_success()
        expected = "用户群组已删除"
        assert_log(expected, actual)