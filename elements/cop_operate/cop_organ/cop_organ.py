from selenium.webdriver.common.by import By


class CopOrganEle():
    wait_mask_dis = (By.XPATH, "//button[contains(@class,'ant-drawer-close')]")
    cop_organ_moudle = (By.XPATH, "//div[text()='企业组织']")

    add_dep = (By.XPATH, "//span[contains(text(),'新增部门')]")
    # add_dep_title = (By.XPATH, '//input[@class="ant-select-selection-search-input ng-pristine ng-valid ng-touched"]')
    add_dep_select = (By.XPATH, '(//nz-select-top-control)[2]')
    add_dep_selected = (By.XPATH, "(//div[@class='ant-select-item-option-content'])[1]")
    add_dep_id = (By.XPATH, "//input[@placeholder='请输入部门 ID']")
    add_dep_name = (By.XPATH, "//input[@placeholder='请输入部门名称']")
    add_dep_leader_select = (By.XPATH, "//input[@placeholder='请选择部门主管']")
    add_dep_leader_search = (By.XPATH, "(//input[@placeholder='请输入ID或名称'])[2]")
    add_dep_leader_search_button = (By.XPATH, "//i[@nztype='search']")
    add_dep_leader_selected = (By.XPATH, "(//label)[last()]")
    add_dep_confirm = (By.XPATH, "//span[text()='确定']")
    # add_deter_level = (By.XPATH, "//span[text()=' 新增 ']")
    # add_deter_level_id = (By.XPATH, "//input[@placeholder='请输入层级 ID']")
    # add_deter_level_name = (By.XPATH, "//input[@placeholder='请输入层级名称']")
    # add_deter_level_order = (By.XPATH, "//input[@placeholder='请输入层级顺序']")
    # add_deter_level_save = (By.XPATH, "(//span[text()=' 储存 '])[2]")
    add_dep_level = (By.XPATH, "//input[@class='ant-select-selection-search-input ng-pristine ng-valid ng-touched']")
    add_dep_level_selected = (By.XPATH, "(//div[@class='ant-select-item-option-content'])[1]")
    add_dep_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_add_dep_success = (By.XPATH, "//span[text()='新增成功']")

    #添加子部门
    add_sub_befor = (By.XPATH, "(//button)[3]")
    add_sub_dep_selected = (By.XPATH, "(//button[contains(@class,'table-row')])[1]")
    add_sub_dep = (By.XPATH, "(//a[text()=' 新增子部门 '])[1]")
    add_sub_dep_id = (By.XPATH, "//input[@placeholder='请输入子部门 ID']")
    add_sub_dep_name = (By.XPATH, "//input[@placeholder='请输入子部门名称']")
    add_sub_dep_leader_select = (By.XPATH, "//input[@placeholder='请选择子部门主管']")
    add_sub_dep_leader_search = (By.XPATH, "(//input[@placeholder='请输入ID或名称'])[2]")
    add_sub_dep_leader_search_button = (By.XPATH, "//i[@nztype='search']")
    add_sub_dep_leader_selected = (By.XPATH, "(//label)[last()]")
    add_sub_dep_confirm = (By.XPATH, "//span[text()='确定']")
    add_sub_dep_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_add_sub_dep_success = (By.XPATH, "//span[text()='新增成功']")

    #编辑子部门
    edit_cop_type = (By.XPATH, "//nz-select-item[@title='公司别']")
    edit_cop_type_selected = (By.XPATH, "//div[text()='部门名称']")
    edit_sub_dep_search_input = (By.XPATH, "//input[@placeholder='请输入ID或名称']")
    edit_sub_dep_search_button = (By.XPATH, "//span[text()='查询']")
    edit_cop_befor = (By.XPATH, "(//button)[3]")
    edit_sub_dep_more = (By.XPATH, "//a[text()=' 更多 ']")
    edit_sub_dep = (By.XPATH, "//span[text()=' 修改 ']")
    edit_sub_dep_name = (By.XPATH, "//input[@placeholder='请输入部门名称']")
    edit_sub_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_edit_sub_dep_success = (By.XPATH, "//span[text()='修改成功']")

    #删除子部门
    delete_cop_type = (By.XPATH, "//nz-select-item[@title='公司别']")
    delete_cop_type_selected = (By.XPATH, "//div[text()='部门名称']")
    delete_sub_dep_search_input = (By.XPATH, "//input[@placeholder='请输入ID或名称']")
    delete_sub_dep_search_button = (By.XPATH, "//span[text()='查询']")
    delete_sub_dep_more = (By.XPATH, "//a[text()=' 更多 ']")
    delete_sub_dep = (By.XPATH, "//span[text()=' 删除 ']")
    delete_sub_dep_confirm = (By.XPATH, "//span[text()=' 确定 ']")
    assert_delete_sub_dep_success = (By.XPATH, "//span[text()='删除成功']")


    #新增部门成员
    dep_member = (By.XPATH, "(//a[text()=' 部门成员 '])[1]")
    is_member_exit = (By.XPATH, "//td[text()='我才是主管(9999)']")
    add_member = (By.XPATH, "//span[text()=' 新增 ']")
    add_member_name = (By.XPATH, "//input[@placeholder='请选择员工名称']")
    add_member_search = (By.XPATH, "(//input[@placeholder='请输入ID或名称'])[3]")
    add_member_search_button = (By.XPATH, "(//i[@nztype='search'])[2]")
    add_member_selected = (By.XPATH, '(//label)[last()]')
    add_member_confirm = (By.XPATH, "//span[text()='确定']")
    add_member_deter = (By.XPATH, "(//nz-select-search[contains(@class,'inserte')])[last()]")
    add_member_deter_selected = (By.XPATH, "(//nz-option-item)[1]")
    add_member_save = (By.XPATH, "//span[contains(text(),'储存')]")
    assert_add_member_success = (By.XPATH, "//span[text()='新增成功']")

    #编辑部门成员
    # dep_member = (By.XPATH, "(//a[text()=' 部门成员 '])[1]")
    # edit_search_input = (By.XPATH, "(//input[@placeholder='请输入ID或名称'])[2]")
    # edit_search_button = (By.XPATH, "//i[@class='anticon anticon-search']")
    edit_member_selected = (By.XPATH, "(//label)[last()]")
    edit_member_edit = (By.XPATH, "//span[text()=' 编辑 ']")
    edit_member_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_edit_member_success = (By.XPATH, "//span[text()='修改成功']")

    #删除员工
    # delete_member = (By.XPATH, "(//a[text()=' 部门成员 '])[1]")
    # delete_search_input = (By.XPATH, "(//span[@class='ant-checkbox-inner'])[2]")
    # delete_member_button = (By.XPATH, "//i[@class='anticon anticon-search']")
    delete_search_selected = (By.XPATH, "(//label)[last()]")
    delete_member_delete = (By.XPATH, "//span[text()=' 删除 ']")
    delete_member_confirm = (By.XPATH, "//span[text()=' 确定 ']")
    assert_delete_member_success = (By.XPATH, "//span[text()='删除成功']")

    #人员核决层级
    #新增层级
    member_derter_level = (By.XPATH, "//span[text()='人员核决层级']")
    add_deter_level = (By.XPATH, "//span[text()='新建层级']")
    add_deter_level_id = (By.XPATH, "//input[@placeholder='请输入层级 ID']")
    add_deter_level_name = (By.XPATH, "//input[@placeholder='请输入层级名称']")
    add_deter_level_order = (By.XPATH, "//input[@placeholder='请输入层级顺序']")
    add_deter_level_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_add_deter_level_success = (By.XPATH, "//span[text()='新增成功']")

    #编辑层级
    edit_derter_level = (By.XPATH, "//span[text()='人员核决层级']")
    edit_deter_level = (By.XPATH, "(//a[text()='修改'])[1]")
    edit_deter_level_name = (By.XPATH, "//input[@placeholder='请输入层级名称']")
    edit_deter_level_order = (By.XPATH, "//input[@placeholder='请输入层级顺序']")
    edit_deter_level_save = (By.XPATH, "//span[text()=' 储存 ']")
    assert_edit_deter_level_success = (By.XPATH, "//span[text()='修改成功']")

    #删除层级
    delete_derter_level = (By.XPATH, "//span[text()='人员核决层级']")
    delete_deter_level = (By.XPATH, "(//a[text()='删除'])[last()]")
    delete_deter_level_confirm = (By.XPATH, "//span[text()=' 确定 ']")
    assert_delete_deter_level_success = (By.XPATH, "//span[text()='删除成功']")



