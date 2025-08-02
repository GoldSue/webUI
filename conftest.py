
import pytest
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)
    # return  driver
    yield driver
    driver.quit()




