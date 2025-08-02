from selenium.webdriver.common.by import By


class LoginEle():
    username = (By.XPATH, "//input[@formcontrolname='userId']")
    password = (By.XPATH, "//input[@formcontrolname='password']")
    login_button = (By.XPATH, "//button[@class='login-form-button ant-btn ant-btn-primary']")
    error_message = (By.XPATH, "//span[contains(text(),'用户账户或密码错误')]")
    right_message = (By.XPATH, "//span[text()='我的首页']")
