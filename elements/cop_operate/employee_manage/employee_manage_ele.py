from selenium.webdriver.common.by import By


class EmployeManage():
    employee_manage_button = (By.XPATH, "//div[text()='员工管理']")

    add_employee = (By.XPATH, "//span[text()='新增员工']")
    add_employee_id = (By.XPATH, "//input[@formcontrolname='employeeID']")
    add_employee_name = (By.XPATH, "//input[@formcontrolname='employeeName']")
    add_employ_save = (By.XPATH, "//span[text()=' 储存']")
    add_employee_confirm = (By.XPATH, "//span[text()=' 确定保存 ']")
    assert_add_employee_success = (By.XPATH, "//span[text()='新增成功']")

    #员工修改
    edit_employee = (By.XPATH, "(//a[text()='修改'])[1]")
    edit_employee_name = (By.XPATH, "//input[@formcontrolname='employeeName']")
    edit_employ_save = (By.XPATH, "//span[text()=' 储存']")
    edit_employee_confirm = (By.XPATH, "//span[text()=' 确定保存 ']")
    assert_edit_employee_success = (By.XPATH, "//span[text()='修改成功']")

    #员工停用
    stop_employee = (By.XPATH, "(//a[text()='停用'])[1]")
    assert_stop_employee_success = (By.XPATH, "//span[contains(text(),'停用成功')]")

    #员工启用
    start_employee = (By.XPATH, "(//a[text()='启用'])[1]")
    assert_start_employee_success = (By.XPATH, "//span[contains(text(),'启用成功')]")

    #删除员工
    delete_employee = (By.XPATH, "(//a[text()='删除'])[1]")
    delete_employee_confirm = (By.XPATH, "//span[text()=' 确定 ']")
    assert_delete_employee_success = (By.XPATH, "//span[contains(text(),'删除成功')]")
