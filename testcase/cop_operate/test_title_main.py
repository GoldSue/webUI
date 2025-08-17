import allure

from config.logger import logger
from conftest import assert_with_log
from pages.cop_operate.title_main import TitletMain


@allure.feature('企业运营')
class TestTitleMain():
    @allure.story('员工管理')
    @allure.title('新增职称')
    def test_add_title(self,login, go_cop_operate):
        title_main = TitletMain(login)
        title_main.add_title()
        actual = title_main.assert_add_title_success()
        assert_with_log("新增成功", actual)

    @allure.story('员工管理')
    @allure.title('新增职称')
    def test_edit_title(self,login, go_cop_operate):
        title_main = TitletMain(login)
        title_main.edit_title()
        actual = title_main.assert_edit_title_success()
        assert_with_log("修改成功", actual)

    @allure.story('员工管理')
    @allure.title('新增职称')
    def test_delete_title(self,login, go_cop_operate):
        title_main = TitletMain(login)
        title_main.delete_title()
        actual = title_main.assert_delete_title_success()
        assert_with_log("删除成功", actual)

