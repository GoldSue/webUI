from pages.user_mag.user_manage.add_cop_user import AddCopUser
from config.logger import logger



class TestAddCopUser():

    def test_add_cop_user(self, login, go_user_mag):
        add_cop_user = AddCopUser(login)
        add_cop_user.add_cop_user()
        actual = add_cop_user.assert_add_cop_success()
        expected = "新增成功"
        logger.info(f"✅ 实际：{actual}")
        expected = expected
        logger.info(f"✅ 预期：{actual}")
        assert expected in actual, f"断言失败！实际结果：{actual}"

        # add_cop_user.close_add()
