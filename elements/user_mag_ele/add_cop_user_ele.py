from selenium.webdriver.common.by import By

from pages.base_page import BasePage


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
    add_cop_batch = (By.XPATH, "//span[text()='批量导入企业用户']")
    add_cop_batch_file = (By.XPATH, "//input[@type='file']")
    add_cop_batch_button = (By.XPATH, "//span[text()='导入企业用户']")
    assert_add_cop_batch_success = (By.XPATH, "//span[text()='导入成功']")

    #搜索
    input_user_id= (By.XPATH, "//input[@placeholder='请输入']")
    search_user = (By.XPATH, "//span[text()='查询']")
    assert_search_cop_success = (By.XPATH, "//li[contains(text(),'共1笔记录')]")

    #编辑企业用户
    edit_user = (By.XPATH, "//a[text()=' 编辑 ']")
    edit_user_name = (By.XPATH, "//input[@formcontrolname='userName']")
    edit_save = (By.XPATH, "//span[text()=' 保存 ']")
    assert_edit_success = (By.XPATH, "//span[contains(text(),'修改成功')]")

    #停用企业用户
    stop_user = (By.XPATH, "//a[contains(text(),'停用')]")
    stop_user_confirm = (By.XPATH, "//span[contains(text(),'确定')]")
    assert_stop_success = (By.XPATH, "//span[contains(text(),'停用成功')]")

    #启用企业用户
    start_user = (By.XPATH, "//a[contains(text(),'启用')]")
    assert_start_success = (By.XPATH, "//span[contains(text(),'启用成功')]")

    #安删除企业用户
    delete_user = (By.XPATH, "//a[contains(text(),'删除')]")
    delete_user_confirm = (By.XPATH, "//span[contains(text(),'确定')]")
    assert_delete_success = (By.XPATH, "//span[contains(text(),'用户已删除')]")




