from pages.user_mag.user_manage.server_auth import ServerAuth
from config.logger import logger

class TestServerAuth():

    def test_server_auth(self, login, go_user_mag):
        server_auth = ServerAuth(login)
        server_auth.gene_server_qcode()
        actual = server_auth.assert_server_qcode()
        logger.info(f"✅ 实际结果：{actual}")
        expected = '授权码产生成功'
        logger.info(f"✅ 预期结果：{actual}")
        assert expected in actual, f"断言失败！实际结果：{actual}"

    def test_proxy_auth(self, login, go_user_mag):
        server_auth = ServerAuth(login)
        server_auth.proxy_auth()
        actual = server_auth.assert_back_gene()
        logger.info(f"实际结果：{actual}")
        expected = '代理授权码'
        logger.info(f"预期结果：{actual}")
        assert expected in actual, f"断言失败！实际结果：{actual}"

