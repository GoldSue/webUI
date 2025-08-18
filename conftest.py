import os
import time

import allure
import pytest


from config.logger import logger
from utils.utils import to_dirname
from pages.loggin import LoginPage
from elements.loginEle import LoginEle
from utils.utils import load_yaml

login_data= load_yaml('loginData.yaml')



# import pytest
# import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(headless=True):
    """
    创建并返回 Chrome Driver (webdriver_manager 管理版本)
    :param headless: 是否无头模式
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--log-level=3")  # 0=INFO, 1=WARNING, 2=LOG_ERROR, 3=FATAL

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    # webdriver_manager 检查缓存 → 自动匹配 Chrome 版本 → 返回 driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# ==================== fixture 定义 ====================

@pytest.fixture(scope="function")
def login_driver():
    """不登录的浏览器实例（每次用例单独启动）"""
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login():
    """已登录的浏览器实例（会话级别共用）"""
    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.login(login_data[0]["username"], login_data[0]["password"])
    time.sleep(2)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def go_user_mag(login):
    from pages.user_mag.user_manage.invite_user import UserManage
    user_mag = UserManage(login)
    user_mag.module_user_mag()
    return user_mag


@pytest.fixture(scope="function")
def go_cop_operate(login):
    from pages.cop_operate.operate_unit import OperateUnit
    cop_operate = OperateUnit(login)
    cop_operate.module_cop_operate()
    return cop_operate

def assert_with_log(expected, actual):
    """
    通用断言：
    - expected: 预期值（字符串）
    - actual: 实际值（字符串）
    """
    if expected in actual:
        logger.info(f"✅ expected: {expected} | actual: {actual}")
    else:
        logger.error(f"❌ expected: {expected} | actual: {actual}")
        raise AssertionError(f"❌ expected: {expected} | actual: {actual}")


@pytest.fixture
def assert_log():
    """pytest fixture 方式使用断言（可选）"""
    return assert_with_log

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 兼容 driver 名称
        driver = item.funcargs.get("login_driver") or item.funcargs.get("login")

        if driver:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_dir = to_dirname("screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = os.path.join(screenshot_dir, f"{timestamp}_{item.name}.png")

            # 保存到文件
            driver.save_screenshot(file_name)
            logger.error(f"[截图] 用例失败截图已保存：{file_name}")

            # 同时附加到 Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"失败截图_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )
