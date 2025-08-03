import time

from base.base import BasePage
from elements.user_mag_ele.invite_user_ele import InviteUser as invite


class UserManage(BasePage):

    def invite_user(self):
        time.sleep(2)
        self.click(*invite.user_mag_module, timeout=3)
        time.sleep(1)
        self.click(*invite.invite_user_button)
        self.click(*invite.invite_user)
        self.send_keys(2222,*invite.invite_user_id)
        self.click(*invite.user_quality)
        self.click(*invite.invite_user_out)
        self.send_keys("我邀请你",*invite.invite_cotent)
        self.click(*invite.invite_send)
    def assert_invite_success(self):
        return self.get_text(*invite.assert_invite_sucess)

    def invite_user_patch(self):
        # self.click(*invite.invite_user_button)
        # self.click(*invite.upload_file)
        # self.click(*invite.send_file)
        pass



    def gen_invite_url(self):
        self.click(*invite.invite_user_button)
        self.click(*invite.gene_invite_url)

        self.click(*invite.add_invite_url)
        self.click(*invite.user_quality_url)
        self.click(*invite.selected_com_user)
        self.send_keys("2025-09-09",*invite.select_day)
        self.tab(*invite.select_day)
        self.click(*invite.send_invite_url)
        self.send_keys("222@com",*invite.send_to_email)
        self.click(*invite.send_email_button)
    def assert_email_success(self):
        return self.get_text(*invite.assert_email_seccess)








