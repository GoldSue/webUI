import pytest

from config.logger import logger
from utils.utils import load_yaml
from pages.loggin import LoginPage
from config.logger import logger
login_data = load_yaml("loginData.yaml") or []


class TestLogin():

    @pytest.mark.parametrize("data",login_data,ids=[data["case"] for data in login_data])
    def test_login(self,data,driver):
        login_page = LoginPage(driver)
        login_page.login(data["username"],data["password"])

        expected_text = data["expected"]

        if data["case"] == "正常登录":
            assert expected_text in login_page.get_right_message()
        elif data["case"] == "密码错误":
            assert data["expected"] in login_page.get_error_message()
        elif data["case"] == "用户不存在":
            actual_text = login_page.get_error_message()
            print(f"获取到的值：{actual_text}")
            assert data["expected"] in actual_text



