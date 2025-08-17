import time

from config.logger import logger
from conftest import assert_with_log
from pages.user_mag.user_manage.invite_user import UserManage


class TestUserManage():

    def test_invite_user(self,assert_log,login,go_user_mag):
        user_manage = UserManage(login)
        user_manage.invite_user()
        actual = user_manage.assert_invite_success()
        expected = '邀请发起成功'
        assert_log(expected, actual)

    def test_invite_user_batch(self,assert_log,login,go_user_mag):
        user_manage = UserManage(login)
        user_manage.invite_user_batch()
        actual = user_manage.assert_batch_success()
        assert_with_log("邀请发起成功", actual)


    def test_send_invite_url(self,assert_log,login,go_user_mag):
        user_manage = UserManage(login)
        logger.info("开始测试用户管理-生成邀请用户链接")
        user_manage.gen_invite_url()
        actual = user_manage.assert_email_success()
        expected = '通知信件发送成功'
        assert_log(expected, actual)


