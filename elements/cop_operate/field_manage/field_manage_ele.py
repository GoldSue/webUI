from selenium.webdriver.common.by import By


class FieldManageEle():

    field_manage_button = (By.XPATH, "//div[text()='场域管理']")


    # 新增场域
    add_field = (By.XPATH, "//a[text()='新增场域 ']")
    add_field_type = (By.XPATH, "(//nz-select-top-control)[2]")
    add_field_type_selected = (By.XPATH, "//div[text()='营运域']")
    add_field_id = (By.XPATH, "//input[@placeholder='请输入ID']")
    add_field_name = (By.XPATH, "//input[@placeholder='请输入场域名称']")
    add_field_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_add_field_success = (By.XPATH, "//span[text()='新增成功']")

    # 修改场域
    edit_search_input = (By.XPATH, "//input[@placeholder='请输入ID或名称']")
    edit_search_button = (By.XPATH, "//span[text()='查询']")
    edit_field = (By.XPATH, "//a[text()='修改']")
    edit_field_name = (By.XPATH, "//input[@placeholder='请输入场域名称']")
    edit_field_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_edit_field_success = (By.XPATH, "//span[text()='修改成功']")

    #删除场域
    delete_search_input = (By.XPATH, "//input[@placeholder='请输入ID或名称']")
    delete_search_button = (By.XPATH, "//span[text()='查询']")
    delete_field = (By.XPATH, "//a[text()='删除']")
    delete_field_confirm = (By.XPATH, "//span[text()=' 确定 ']")
    assert_delete_field_success = (By.XPATH, "//span[text()='删除成功']")

    # 导入场域
    import_file_button = (By.XPATH, "//span[text()='导入']")
    import_file_select = (By.XPATH, "//a[text()='场域工厂']")
    import_file_up = (By.XPATH, "//input[@type='file']")
    import_file = (By.XPATH, "//span[text()='导入场域工厂']")
    assert_import_file_success = (By.XPATH, "//span[text()='导入成功']")



