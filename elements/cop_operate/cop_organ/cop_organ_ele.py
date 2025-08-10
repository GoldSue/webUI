from selenium.webdriver.common.by import By


class CopOrganEle():

    cop_organ_button = (By.XPATH, "//div[text()='企业组织']")

    add_department_button = (By.XPATH, "//span[text()='新增部门']")
    select_cop_name = (By.XPATH, "//nz-select-placeholder[text()=' 请选择公司别名称 (ID) ']")
    selected_name = (By.XPATH, "(//div[@class='ant-select-item-option-content'])[1]")
    dep_id = (By.XPATH, "//input[@placeholder='请输入部门 ID']")
    dep_name = (By.XPATH, "//input[@placeholder='请输入部门名称']")
    dep_leader = (By.XPATH, "//input[@placeholder='请选择部门主管']")
    selected_leader_input = (By.XPATH, "(//input[@placeholder='请输入ID或名称'])[2]")
    selected_leader_search = (By.XPATH, "//span[@class='ant-input-group-addon ng-star-inserted']")
    selected_checkbox = (By.XPATH, "(//input[@type='checkbox'])[3]")
    selected_leader_confirm = (By.XPATH, "//span[text()='储存']")
    add_dep_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_add_dep_success = (By.XPATH, "//span[text()='新增成功']")


