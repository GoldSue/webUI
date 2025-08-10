from config.logger import logger
from pages.cop_operate.title_main import TitletMain

class TestTitleMain():

    def test_add_title(self, login, go_cop_operate):
        title_main = TitletMain(login)
        title_main.add_title()
        actual = title_main.assert_add_title_success()
        expected = "新增成功"
        logger.info(f"✅ 实际结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

    def test_edit_title(self, login, go_cop_operate):
        title_main = TitletMain(login)
        title_main.edit_title()
        actual = title_main.assert_edit_title_success()
        expected = "修改成功"
        logger.info(f"✅ 实际结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

    def test_delete_title(self, login, go_cop_operate):
        title_main = TitletMain(login)
        title_main.delete_title()
        actual = title_main.assert_delete_title_success()
        expected = "删除成功"
        logger.info(f"✅ 断言结果：{actual}")
        logger.info(f"✅ 预期结果：{expected}")
        assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

