from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.logger import logger

class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.logger = logger

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://console-paas.digiwincloud.com.cn/login")

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def js_click(self, *locator):
        try:
            element = self.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"JS 点击成功: {locator}")
        except Exception as e:
            self.logger.error(f"JS 点击失败: {locator}, 原因: {e}")
            raise

    def click(self, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or 10).until(
                EC.element_to_be_clickable(locator)  # 注意：不解包
            )
            self.find_element(*locator).click()
        except Exception as e:
            self.logger.warning(f"常规点击失败，使用 JS 点击: {locator}, 原因: {e}")
            self.js_click(*locator)

    def send_keys(self, text, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or 10).until(
                EC.visibility_of_element_located(locator)
            )
            self.find_element(*locator).send_keys(text)
        except NoSuchElementException:
            self.logger.error(f"该元素未找到: {locator}")
        except TimeoutException:
            self.logger.error(f"元素定位超时: {locator}")
        except Exception as e:
            self.logger.error(f"send_keys 失败: {locator}, 原因: {e}")
            raise

    def get_text(self, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or 10).until(
                EC.visibility_of_element_located(locator)
            )
            return self.find_element(*locator).text
        except Exception as e:
            self.logger.error(f"[get_text] 元素获取失败: {locator}, 原因: {e}")
            return ""

    def get_attribute(self, attribute, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or 10).until(
                EC.visibility_of_element_located(locator)
            )
            return self.find_element(*locator).get_attribute(attribute)
        except NoSuchElementException:
            self.logger.error(f"该元素未找到: {locator}")
        except TimeoutException:
            self.logger.error(f"元素定位超时: {locator}")
        except Exception as e:
            self.logger.error(f"获取属性失败: {locator}, 原因: {e}")
            raise
