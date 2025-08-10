from selenium.webdriver.common.by import By


class TitleMainEle():
    employee_manage_button = (By.XPATH, "//div[text()='员工管理']")


    title_main = (By.XPATH, "//span[contains(text(),'职称维护')]")
    add_title = (By.XPATH, "//span[contains(text(),'新增职称')]")
    add_title_id = (By.XPATH, "//input[@placeholder='请输入职称ID']")
    add_title_name = (By.XPATH, "//input[@placeholder='请输入职称名称']")
    add_title_save = (By.XPATH, "//span[text()='储存']")
    assert_add_title_success = (By.XPATH, "//span[text()='新增成功']")

    #修改
    edit_title = (By.XPATH, "(//a[text()='修改'])[1]")
    edit_title_name = (By.XPATH, "//input[@placeholder='请输入职称名称']")
    edit_title_save = (By.XPATH, "//span[text()='储存']")
    assert_edit_title_success = (By.XPATH, "//span[text()='修改成功']")

    #删除
    delete_title = (By.XPATH, "(//a[text()='删除'])[1]")
    delete_title_confirm = (By.XPATH, "//span[text()=' 确定 ']")
    assert_delete_title_success = (By.XPATH, "//span[text()='删除成功']")



