# from encodings.punycode import adapt
import allure

from conftest import assert_with_log
from pages.user_mag.user_manage.add_cop_user import CopUser
from config.logger import logger


@allure.feature('用户管理')
class TestAddCopUser():

    @allure.story('用户管理')
    @allure.title('新增企业用户')
    def test_add_cop_user(self,login, go_user_mag):
        op_user = CopUser(login)
        op_user.add_cop_user()
        actual = op_user.assert_add_cop_success()
        assert_with_log("新增成功", actual)

    @allure.story('用户管理')
    @allure.title('批量新增企业用户')
    def test_add_cop_user_batch(self,login, go_user_mag):
        op_user = CopUser(login)
        op_user.add_cop_batch()
        actual = op_user.assert_add_cop_batch_success()
        assert_with_log("导入成功", actual)

    @allure.story('用户管理')
    @allure.title('搜索企业用户')
    def test_search_cop_user(self,login, go_user_mag):
        search_cop_user = CopUser(login)
        search_cop_user.search_cop_user()
        actual = search_cop_user.assert_search_cop_success()
        assert_with_log("共1笔记录", actual)

    @allure.story('用户管理')
    @allure.title('编辑企业用户')
    def test_edit_cop_user(self,login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.edit_cop_user()
        actual = cop_user.assert_edit_success()
        assert_with_log("修改成功", actual)

    @allure.story('用户管理')
    @allure.title('停用企业用户')
    def test_stop_cop_user(self,login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.stop_cop_user()
        actual = cop_user.assert_stop_success()
        assert_with_log("停用成功", actual)

    @allure.story('用户管理')
    @allure.title('启用企业用户')
    def test_start_cop_user(self,login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.start_cop_user()
        actual = cop_user.assert_start_success()
        assert_with_log("启用成功", actual)

    @allure.story('用户管理')
    @allure.title('删除企业用户')
    def test_delete_cop_user(self,login, go_user_mag):
        cop_user = CopUser(login)
        cop_user.delete_cop_user()
        actual = cop_user.assert_delete_success()
        assert_with_log("用户已删除", actual)


