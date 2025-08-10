# from encodings.punycode import adapt

from pages.user_mag.user_manage.add_cop_user import CopUser
from config.logger import logger



class TestAddCopUser():

    def test_add_cop_user(self, login, go_user_mag):
        op_user = CopUser(login)
        op_user.add_cop_user()
        actual = op_user.assert_add_cop_success()
        expected = "新增成功"
        logger.info(f"✅ 实际：{actual}")
        expected = expected
        logger.info(f"✅ 预期：{actual}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

    def test_search_cop_user(self, login, go_user_mag):
        search_cop_user = CopUser(login)
        search_cop_user.search_cop_user()
        actual = search_cop_user.assert_search_cop_success()
        expected = "共1笔记录"
        logger.info(f"✅ 实际结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"
    def test_edit_cop_user(self, login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.edit_cop_user()
        actual = cop_user.assert_edit_success()
        expected = "修改成功"
        logger.info(f"✅ 实际结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

    def test_stop_cop_user(self, login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.stop_cop_user()
        actual = cop_user.assert_stop_success()
        expected = "停用成功"
        logger.info(f"✅ 实际结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"
    #
    def test_start_cop_user(self, login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.start_cop_user()
        actual = cop_user.assert_start_success()
        expected = "启用成功"
        logger.info(f"✅ 实际结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"
    #
    def test_delete_cop_user(self, login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.delete_cop_user()
        actual = cop_user.assert_delete_success()
        expected = "用户已删除"
        logger.info(f"✅ 实际结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"


