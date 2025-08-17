from conftest import assert_with_log
from pages.cop_operate.func_main import FuncMain


class TestFuncMain():

    def test_add_func(self,login, go_cop_operate):
        func_main = FuncMain(login)
        func_main.add_func()
        actual = func_main.assert_add_func_success()
        assert_with_log("新增成功",actual)

    def test_edit_func(self,login, go_cop_operate):
        func_main = FuncMain(login)
        func_main.edit_func()
        actual = func_main.assert_edit_func_success()
        assert_with_log("修改成功",actual)

    def test_stop_func(self,login, go_cop_operate):
        func_main = FuncMain(login)
        func_main.stop_func()
        actual = func_main.assert_stop_func_success()
        assert_with_log("停用成功",actual)

    def test_start_func(self,login, go_cop_operate):
        func_main = FuncMain(login)
        func_main.start_func()
        actual = func_main.assert_start_func_success()
        assert_with_log("启用成功",actual)

    def test_delete_func(self,login, go_cop_operate):
        func_main = FuncMain(login)
        func_main.delete_func()
        actual = func_main.assert_delete_func_success()
        assert_with_log("删除成功",actual)


