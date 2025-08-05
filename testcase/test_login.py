import pytest

from config.logger import logger
from utils.utils import load_yaml
from pages.loggin import LoginPage
from config.logger import logger
login_data = load_yaml("loginData.yaml") or []


class TestLogin():

    @pytest.mark.parametrize("data", login_data, ids=[data["case"] for data in login_data])
    def test_login(self, data, login_driver):
        login_page = LoginPage(login_driver)
        login_page.open()
        login_page.login(data["username"], data["password"])

        case: str = data["case"]
        expected: str = data["expected"]
        actual = (login_page.get_right_message() if case == "login_success"
                  else login_page.get_error_message())

        logger.info(f"[{case}] ✅ 预期: {expected}")
        logger.info(f"[{case}] ✅ 实际: {actual}")

        if expected not in actual:
            raise AssertionError(f"[{case}] ❌ 断言失败：预期 '{expected}'，实际 '{actual}'")




