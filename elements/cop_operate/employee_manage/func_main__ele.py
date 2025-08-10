from selenium.webdriver.common.by import By


class FuncMainEle():

    func_main_button = (By.XPATH, "//span[text()='职能维护']")

    add_func = (By.XPATH, "//span[text()='新增职能']")
    add_func_id = (By.XPATH, "//input[@placeholder='请输入职能']")
    add_func_name = (By.XPATH, "//input[@placeholder='请输入职能名称']")
    add_func_save = (By.XPATH, "//span[text()='储存']")
    assert_add_func_success = (By.XPATH, "//span[text()='新增成功']")

    #修改
    edit_func = (By.XPATH, "(//a[text()='修改'])[1]")
    edit_func_name = (By.XPATH, "//input[@placeholder='请输入职能名称']")
    edit_func_save = (By.XPATH, "//span[text()='储存']")
    assert_edit_func_success = (By.XPATH, "//span[text()='修改成功']")


    #停用
    stop_func = (By.XPATH, "(//a[text()='停用'])[1]")
    stop_func_confirm = (By.XPATH, "//span[text()='确定']")
    assert_stop_func_success = (By.XPATH, "//span[text()='停用成功']")

    #启用
    start_func = (By.XPATH, "(//a[text()='启用'])[1]")
    assert_start_func_success = (By.XPATH, "//span[text()='启用成功']")

    #删除
    delete_func = (By.XPATH, "(//a[text()='删除'])[1]")
    delete_func_confirm = (By.XPATH, "//span[text()='确定']")
    assert_delete_func_success = (By.XPATH, "//span[text()='删除成功']")

