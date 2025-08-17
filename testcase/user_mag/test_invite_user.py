import time

import allure

from config.logger import logger
from conftest import assert_with_log
from pages.user_mag.user_manage.invite_user import UserManage

@allure.feature('用户管理')
class TestUserManage():

    @allure.story('用户管理')
    @allure.title('邀请用户')
    def test_invite_user(self,assert_log,login,go_user_mag):
        user_manage = UserManage(login)
        user_manage.invite_user()
        actual = user_manage.assert_invite_success()
        expected = '邀请发起成功'
        assert_log(expected, actual)

    @allure.story('用户管理')
    @allure.title('批量邀请用户')
    def test_invite_user_batch(self,login,go_user_mag):
        user_manage = UserManage(login)
        user_manage.invite_user_batch()
        actual = user_manage.assert_batch_success()
        assert_with_log("邀请发起成功", actual)

    @allure.story('用户管理')
    @allure.title('发送邀请链接')
    def test_send_invite_url(self,login,go_user_mag):
        user_manage = UserManage(login)
        logger.info("开始测试用户管理-生成邀请用户链接")
        user_manage.gen_invite_url()
        actual = user_manage.assert_email_success()
        assert_with_log("通知信件发送成功", actual)


