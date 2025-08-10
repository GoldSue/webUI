from pages.user_mag.role_manage.role_manage import RoleManage
from config.logger import logger

class TestRoleManage():

    def test_add_role(self,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.add_role()
        actual = role_manage.assert_add_role_success()
        expected = "新增成功"
        logger.info("✅ 实际结果：{}".format(actual))
        logger.info("✅ 预期结果：{}".format(expected))
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

    def test_edit_role(self,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.edit_user()
        actual = role_manage.assert_edit_role_success()
        expected = "修改成功"
        logger.info("✅ 实际结果：{}".format(actual))
        logger.info("✅ 预期结果：{}".format(expected))
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

    def test_delete_role(self,login,go_user_mag):
        role_manage = RoleManage(login)
        role_manage.delete_user()
        actual = role_manage.assert_delete_role_success()
        expected = "删除成功"
        logger.info("✅ 实际结果：{}".format(actual))
        logger.info("✅ 预期结果：{}".format(expected))
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

