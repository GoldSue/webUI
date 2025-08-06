from selenium.webdriver.common.by import By

from base.base import BasePage


class AddCopUser(BasePage):
    add_cop_button = (By.XPATH, "//span[text()='添加企业用户']")
    add_cop = (By.XPATH, "(//span[text()='添加企业用户'])[2]")
    add_new_cop = (By.XPATH, "//span[text()='新增']")
    user_id = (By.XPATH, "(//input[@placeholder='请输入'])[2]")
    user_name = (By.XPATH, "(//input[@placeholder='请输入'])[3]")
    user_pwd = (By.XPATH, "(//input[@placeholder='请输入'])[4]")
    add_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_add_cop_success = (By.XPATH, "//span[text()='新增成功']")
    close_add = (By.XPATH, "//button[@aria-label='Close']")

    #批量添加企业用户


