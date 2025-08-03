import time

from config.logger import logger
from pages.user_mag.user_manage.invite_user import UserManage


class TestUserManage():

    def test_invite_user(self,login):
        user_manage = UserManage(login)
        logger.info("开始测试用户管理-邀请用户")
        user_manage.invite_user()
        acturl = user_manage.assert_invite_success()
        logger.info(f"实际结果：{acturl}")
        expected = '邀请发起成功'
        logger.info(f"预期结果：{acturl}")
        assert expected in acturl,f"断言失败！实际结果：{acturl}"

    def test_send_invite_url(self,login):
        user_manage = UserManage(login)
        logger.info("开始测试用户管理-生成邀请用户链接")
        user_manage.gen_invite_url()
        acturl = user_manage.assert_email_success()
        logger.info(f"实际结果：{acturl}")
        expected = '通知信件发送成功'
        assert expected in acturl,f"断言失败！实际结果：{acturl}"


