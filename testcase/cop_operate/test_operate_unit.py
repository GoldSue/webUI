from conftest import assert_with_log
from pages.cop_operate.operate_unit import OperateUnit
from config.logger import logger



class TestOperateUnit():

    def test_add_operate_unit(self,login,go_cop_operate):
        operate_unit = OperateUnit(login)
        operate_unit.add_cop_()
        actual = operate_unit.assert_add_operate_unit_success()
        assert_with_log("新增成功", actual)

    def test_edit_cop_operate_unit(self,login, go_cop_operate):
        operate_unit = OperateUnit(login)
        operate_unit.edit_cop_operate_unit()
        actual = operate_unit.assert_edit_cop_success()
        assert_with_log("修改成功", actual)

    # def test_delete_cop_operate_unit(self, login):
    #     operate_unit = OperateUnit(login)
    #     operate_unit.delete_cop_operate_unit()
    #     actual = operate_unit.assert_delete_success()
    #     expected = "无法删除"
    #     logger.info("✅ 预期结果：{}".format(expected))
    #     logger.info("✅ 实际结果：{}".format(actual))
    #     assert expected in actual, f"❌ 断言失败！实际结果：{actual}"

    def test_cop_setting(self,login, go_cop_operate):
        operate_unit = OperateUnit(login)
        operate_unit.cop_setting()
        actual = operate_unit.assert_cop_setting_success()
        assert_with_log("操作成功", actual)
