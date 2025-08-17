from conftest import assert_with_log
from pages.user_mag.user_manage.server_auth import ServerAuth
from config.logger import logger

class TestServerAuth():

    def test_server_auth(self,login, go_user_mag):
        server_auth = ServerAuth(login)
        server_auth.gene_server_qcode()
        actual = server_auth.assert_server_qcode()
        assert_with_log("授权码产生成功", actual)

    def test_proxy_auth(self,login, go_user_mag):
        server_auth = ServerAuth(login)
        server_auth.proxy_auth()
        actual = server_auth.assert_back_gene()
        assert_with_log("代理授权码", actual)

