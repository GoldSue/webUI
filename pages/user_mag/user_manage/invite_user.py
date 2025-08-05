import time

from base.base import BasePage
from elements.user_mag_ele.invite_user_ele import InviteUser as invite
from pages.home_page import HomePage

class UserManage(BasePage):

    def module_user_mag(self):
        home_page = HomePage(self.driver)

        home_page.get_home_page()
        home_page.go_to_module(*invite.user_mag_module,module_name="用户管理")


    def invite_user(self):
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








