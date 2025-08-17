from conftest import assert_with_log
from pages.cop_operate.cop_organ import CopOrgan


class TestCopOrgan():

    def test_add_dep(self, login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_dep()
        actual = cop_organ.assert_add_dep_success()
        assert_with_log('新增成功', actual)

    def test_add_sub_dep(self, login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_sub_dep()
        actual = cop_organ.assert_add_sub_dep_success()
        assert_with_log('新增成功', actual)

    def test_edit_sub_dep(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.edit_sub_dep()
        actual = cop_organ.assert_edit_sub_dep_success()
        assert_with_log('修改成功', actual)
    # #

    def test_delete_sub_dep(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.delete_sub_dep()
        actual = cop_organ.assert_delete_sub_dep()
        assert_with_log('删除成功', actual)

    def test_add_dep_member(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_dep_member()
        actual = cop_organ.assert_add_dep_member_success()
        assert_with_log('新增成功', actual)

    def test_edit_dep_member(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.edit_dep_member()
        actual = cop_organ.assert_edit_dep_member_success()
        assert_with_log('修改成功', actual)

    def test_delete_dep_member(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.delete_dep_member()
        actual = cop_organ.assert_delete_dep_member_success()
        assert_with_log('删除成功', actual)

    def test_add_derter_level(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.add_derter_level()
        actual = cop_organ.assert_add_deter_level_success()
        assert_with_log('新增成功', actual)

    def test_edit_derter_level(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.edit_derter_level()
        actual = cop_organ.assert_edit_deter_level()
        assert_with_log('修改成功', actual)

    def test_delete_derter_level(self,login,go_cop_operate):
        cop_organ = CopOrgan(login)
        cop_organ.delete_derter_level()
        actual = cop_organ.assert_delete_deter_level()
        assert_with_log('删除成功', actual)