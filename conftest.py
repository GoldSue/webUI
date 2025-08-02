import os
import time

import pytest
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from utils.utils import to_dirname
from pages.loggin import LoginPage
from elements.loginEle import LoginEle
from utils.utils import load_yaml

load_yaml= load_yaml('loginData.yaml')


@pytest.fixture(scope="session")
def driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()
@pytest.fixture(scope="function")
def login_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)
    yield driver
    driver.quit()

def login(driver):
    login_page = LoginPage(driver)
    username = load_yaml[0]['username']
    password = load_yaml[0]['password']
    login_page.login(username, password)


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







