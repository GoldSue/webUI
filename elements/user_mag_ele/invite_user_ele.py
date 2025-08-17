import time

from selenium.webdriver.common.by import By


class InviteUser():

    user_mag_module = (By.XPATH, "//span[text()='用户管理']")
    invite_user_button = (By.XPATH, "//span[text()='邀请用户']")
    invite_user = (By.XPATH, "//a[@angularticscategory='用戶管理-邀請']")
    invite_user_id = (By.XPATH, "//input[@id='user']")
    user_quality = (By.XPATH, "//nz-select-item[@class='ant-select-selection-item ng-star-inserted'and (@title='一般用户' or @title='外部用户')]")
    invite_user_out = (By.XPATH, "//div[text()='外部用户' ]")
    invite_cotent = (By.ID,'content')
    invite_send = (By.XPATH, "//span[text()='送出']")
    assert_invite_sucess = (By.XPATH, "//span[text()='邀请发起成功' ]")

    invite_user_patch = (By.XPATH, "//span[text()='批量邀请']")
    upload_file = (By.XPATH, "//button[@angularticslabel='上傳批量模版資料']")
    send_file = (By.XPATH, "//button[@angularticslabel='送出用戶邀請訊息']")

    gene_invite_url = (By.XPATH, "//span[text()='产生邀请链接']")
    add_invite_url = (By.XPATH, "//span[text()='新增邀请链接']")
    user_quality_url = (By.XPATH, "//nz-select-item[@title='一般用户' or @title='外部用户用户']")
    selected_com_user = (By.XPATH, "//div[text()='一般用户' ]")
    select_day = (By.XPATH, "//input[@placeholder='请选择日期' ]")
    send_invite_url = (By.XPATH, "//span[text()='送出' ]")
    send_to_email = (By.XPATH, "//input[@formcontrolname='mails' ]")
    send_email_button = (By.XPATH, "//span[text()='发送邮件通知' ]")
    assert_email_seccess = (By.XPATH, "//span[text()='通知信件发送成功' ]")

    invite_user_batch = (By.XPATH, "//span[text()='批量邀请']")
    invite_user_file = (By.XPATH, "//input[@type='file']")
    invite_user_batch_button = (By.XPATH, "//button[@angularticsaction='點擊送出批量邀請' ]")
    assert_batch_success = (By.XPATH, "//span[text()='邀请发起成功' ]")


