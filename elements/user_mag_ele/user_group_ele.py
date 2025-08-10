from selenium.webdriver.common.by import By


class UserGroupEle():
    user_group = (By.XPATH, "//div[text()='用户群组']")
    add_user_group = (By.XPATH, "//span[text()='新增用户群组']")
    add_user_group_id = (By.XPATH, "//input[@placeholder='请输入用户群组ID']")
    add_user_group_name = (By.XPATH, "//input[@placeholder='请输入用户群组名称']")
    add_user_group_save = (By.XPATH, "//span[text()='储存']")
    assert_add_user_group_success = (By.XPATH, "//span[text()='用户群组已新增']")

    #新增子用户群组
    add_child_user_group = (By.XPATH, "(//a[text()=' 新增子用户群组 '])[1]")
    add_child_user_group_id = (By.XPATH, "//input[@placeholder='请输入子用户群组ID']")
    add_child_user_group_name = (By.XPATH, "//input[@placeholder='请输入子用户群组名称']")
    assert_add_child_user_group_success = (By.XPATH, "//span[text()='用户群组已新增']")


    #修改用户群组
    edit_user_group = (By.XPATH, "(//a[text()=' 修改 '])[1]")
    edit_user_group_name = (By.XPATH, "//input[@placeholder='请输入用户群组名称']")
    edit_user_group_save = (By.XPATH, "//span[text()='储存']")
    assert_edit_user_group_success = (By.XPATH, "//span[text()='用户群组已修改']")

    #删除用户群组
    delete_user_group = (By.XPATH, "//a[text()=' 删除 '][1]")
    delete_user_group_confirm = (By.XPATH, "//span[text()=' 确定 ']")
    assert_delete_user_group_success = (By.XPATH, "//span[text()='用户群组已删除']")
