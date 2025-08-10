from selenium.webdriver.common.by import By


class RoleManageEle():

    role_manage_button = (By.XPATH, "//div[text()='角色管理']")
    add_role_button = (By.XPATH, "//span[text()='新增角色']")
    role_id = (By.XPATH, "//input[@placeholder='请输入角色ID']")
    role_name = (By.XPATH, "//input[@placeholder='请输入角色名称']")
    role_description = (By.XPATH, "//textarea[@placeholder='请输入备注']")
    save_role_button = (By.XPATH, "//span[text()='储存']")
    assert_add_role_success = (By.XPATH, "//span[contains(text(),'新增成功')]")


    #编辑用户
    edit_user_button = (By.XPATH, "(//a[contains(text(),'编辑')])[1]")
    edit_user_name = (By.XPATH, "//input[@placeholder='请输入角色名称']")
    edit_user_save = (By.XPATH, "//span[text()='储存']")
    assert_edit_role_success = (By.XPATH, "//span[contains(text(),'修改成功')]")

    #删除用户
    delete_user_button = (By.XPATH, "(//a[contains(text(),'删除')])[1]")
    delete_user_confirm = (By.XPATH, "//span[contains(text(),'确定')]")
    assert_delete_role_success = (By.XPATH, "//span[contains(text(),'删除成功')]")

