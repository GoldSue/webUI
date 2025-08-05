import time

from base.base import BasePage
from elements.user_mag_ele.server_auth_ele import ServerAuthEle
from utils.utils import tomorrow


class ServerAuth(BasePage):

    def gene_server_qcode(self):
        self.click(*ServerAuthEle.server_auth_button)
        time.sleep(1)
        self.click(*ServerAuthEle.gene_server_qcode, timeout=2)
        # 如果是重复点击为展开窗口，可加注释
        if self.ele_exist(*ServerAuthEle.gene_code, timeout=3):
            self.logger.info("⚠️ 注意：已存在服务授权码")
            self.click(*ServerAuthEle.now_stop)
            self.click(*ServerAuthEle.stop_server_confirm)
        time.sleep(1)
        self.logger.info("✅ 开始选择有效时长并生成授权码")
        self.click(*ServerAuthEle.select_days)
        self.click(*ServerAuthEle.selected_days)
        self.click(*ServerAuthEle.gene_code)

        self.click_body()


    def assert_server_qcode(self):
        text = self.get_text(*ServerAuthEle.assert_server_qcode)
        return text

    def proxy_auth(self):
        self.click(*ServerAuthEle.server_auth_button)
        # self.click(*ServerAuthEle.gene_server_qcode)
        self.click(*ServerAuthEle.proxy_auth)
        self.click(*ServerAuthEle.long_time)
        tomorrow_date = tomorrow()
        self.send_keys(tomorrow_date,*ServerAuthEle.end_time)
        self.click(*ServerAuthEle.agree_agreement)
        self.click(*ServerAuthEle.gene_code_button)

    def assert_back_gene(self):
        text = self.get_text(*ServerAuthEle.assert_back_gene)
        return text




