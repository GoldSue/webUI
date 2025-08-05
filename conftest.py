import os
import time

import pytest
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from utils.utils import to_dirname
from pages.loggin import LoginPage
from elements.loginEle import LoginEle
from utils.utils import load_yaml

login_data= load_yaml('loginData.yaml')



@pytest.fixture(scope="function")
def login_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()
@pytest.fixture(scope="session")
def login():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    prefs = {
        "credentials_enable_service": False,  # 禁用自动填充服务
        "profile.password_manager_enabled": False  # 禁用密码管理器
    }
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    login_page = LoginPage(driver)
    username = login_data[0]["username"]
    password = login_data[0]["password"]
    login_page.login(username, password)
    time.sleep(3)

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("/", "_")
            screenshot_dir = to_dirname("screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
            driver.save_screenshot(file_name)
            print(f"\n[截图] 用例失败截图已保存：{file_name}")

@pytest.fixture(scope="function")
def go_user_mag(login):
    from pages.user_mag.user_manage.invite_user import UserManage
    user_mag = UserManage(login)
    user_mag.module_user_mag()
    return user_mag



