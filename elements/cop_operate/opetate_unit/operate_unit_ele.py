from selenium.webdriver.common.by import By


class OperateUnit():

    cop_operate = (By.XPATH, "//span[text()='企业运营']")


    #新增公司
    add_cop_operate_unit = (By.XPATH, "//a[contains(text(),'新增公司别')]")
    cop_operate_unit_id = (By.XPATH, "//input[@placeholder='请输入ID']")
    cop_operate_unit_name = (By.XPATH, "//input[@placeholder='请输入公司别名称']")
    cop_operate_unit_type = (By.XPATH, "//nz-select-item[@title='公司' or @title='法人']")
    cop_operate_select_type = (By.XPATH, "//div[text()='公司']")
    add_cop_save = (By.XPATH, "//span[contains(text(),'储存')]")
    assert_add_operate_unit_success = (By.XPATH, "//span[text()='新增成功']")

    #修改公司
    edit_cop_operate_unit = (By.XPATH, "(//a[text()=' 修改 '])[1]")
    cop_operate_select_type2 = (By.XPATH, "//div[text()='法人']")
    # cop_operate_unit_id = (By.XPATH, "//input[@placeholder='请输入ID']")
    # cop_operate_unit_name = (By.XPATH, "//input[@placeholder='请输入公司别名称']")
    # cop_operate_unit_type = (By.XPATH, "//nz-select-item[@title='公司' or @title='法人']")
    # add_cop_save = (By.XPATH, "//span[text()='储存']")
    assert_edit_cop_success = (By.XPATH, "//span[text()='修改成功']")

    #删除
    delete_cop_operate_unit = (By.XPATH, "(//a[text()=' 删除 '])[1]")
    delete_cop_operate_confirm = (By.XPATH, "//span[text()=' 确定 ']")

    # assert_delete_success = (By.XPATH, "//span[text()='无法删除']")
    # delete_cop_confirm = (By.XPATH, "//span[text()=' 确定 ']")

    #工厂别设置
    cop_operate_unit_setting = (By.XPATH, "(//a[text()=' 工厂别设置 '])[1]")
    cop_operate_unit_setting_add = (By.XPATH, "//span[text()='新增']")
    cop_type = (By.XPATH, "(//nz-select-top-control[contains(@class,'ant-select-selector')])[2]")
    cop_type_select = (By.XPATH, "//div[text()='工厂']")
    cop_code = (By.XPATH, "(//input[@placeholder='请输入'])[1]")
    cop_name = (By.XPATH, "(//input[@placeholder='请输入'])[2]")
    cop_operate_unit_setting_save = (By.XPATH, "//span[contains(text(),'储存')]")
    assert_cop_setting_success = (By.XPATH, "//span[text()='操作成功']")







