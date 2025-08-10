from pages.user_mag.user_manage.server_auth import ServerAuth
from config.logger import logger

class TestServerAuth():

    def test_server_auth(self, assert_log,login, go_user_mag):
        server_auth = ServerAuth(login)
        server_auth.gene_server_qcode()
        actual = server_auth.assert_server_qcode()
        expected = '授权码产生成功'
        assert_log(expected, actual)

    def test_proxy_auth(self, assert_log,login, go_user_mag):
        server_auth = ServerAuth(login)
        server_auth.proxy_auth()
        actual = server_auth.assert_back_gene()
        expected = '代理授权码'
        assert_log(expected, actual)

