import pytest

from config.logger import logger
from utils.utils import load_yaml
from pages.loggin import LoginPage
from config.logger import logger
login_data = load_yaml("loginData.yaml") or []


class TestLogin:
    @pytest.mark.parametrize("data", login_data, ids=[data["case"] for data in login_data])
    def test_login(self, assert_log, data, login_driver):
        login_page = LoginPage(login_driver)
        login_page.open()
        login_page.login(data["username"], data["password"])

        case = data["case"]
        expected = data["expected"]
        actual = (
            login_page.get_right_message()
            if case == "login_success"
            else login_page.get_error_message()
        )

        assert_log(expected, actual)  # 内部会自动打印 PASS/FAIL 并断言





