import allure

from conftest import assert_with_log
from pages.cop_operate.cop_organ import CopOrgan

@allure.feature('企业运营')
class TestCopOrgan():
    @allure.story('企业组织')
    @allure.title('新增部门')
    def test_add_dep(self, login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_dep()
        actual = cop_organ.assert_add_dep_success()
        assert_with_log('新增成功', actual)

    @allure.story('企业组织')
    @allure.title('新增子部门')
    def test_add_sub_dep(self, login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_sub_dep()
        actual = cop_organ.assert_add_sub_dep_success()
        assert_with_log('新增成功', actual)

    @allure.story('企业组织')
    @allure.title('编辑子部门')
    def test_edit_sub_dep(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.edit_sub_dep()
        actual = cop_organ.assert_edit_sub_dep_success()
        assert_with_log('修改成功', actual)
    # #
    @allure.story('企业组织')
    @allure.title('删除子部门')
    def test_delete_sub_dep(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.delete_sub_dep()
        actual = cop_organ.assert_delete_sub_dep()
        assert_with_log('删除成功', actual)

    @allure.story('企业组织')
    @allure.title('新增部门成员')
    def test_add_dep_member(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_dep_member()
        actual = cop_organ.assert_add_dep_member_success()
        assert_with_log('新增成功', actual)

    @allure.story('企业组织')
    @allure.title('修改部门成员')
    def test_edit_dep_member(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.edit_dep_member()
        actual = cop_organ.assert_edit_dep_member_success()
        assert_with_log('修改成功', actual)

    @allure.story('企业组织')
    @allure.title('删除部门成员')
    def test_delete_dep_member(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.delete_dep_member()
        actual = cop_organ.assert_delete_dep_member_success()
        assert_with_log('删除成功', actual)

    @allure.story('企业组织')
    @allure.title('新增人员核决层级')
    def test_add_derter_level(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_derter_level()
        actual = cop_organ.assert_add_deter_level_success()
        assert_with_log('新增成功', actual)

    @allure.story('企业组织')
    @allure.title('修改人员核决层级')
    def test_edit_derter_level(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.edit_derter_level()
        actual = cop_organ.assert_edit_deter_level()
        assert_with_log('修改成功', actual)

    @allure.story('企业组织')
    @allure.title('删除人员核决层级')
    def test_delete_derter_level(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.delete_derter_level()
        actual = cop_organ.assert_delete_deter_level()
        assert_with_log('删除成功', actual)