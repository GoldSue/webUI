import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.log import clear
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.utils import to_dirname, get_file

from config.logger import logger

class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.logger = logger

        # self.driver.implicitly_wait(3)
        self.driver.maximize_window()
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

    def _wait_interactable(self, *locator, timeout=5, buffer=0.2):
        """等待元素可交互，并移动到可视区域"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: (
                        (el := d.find_element(*locator))
                        and el.is_displayed()
                        and el.is_enabled()
                        and el.size['height'] > 0
                        and el.size['width'] > 0
                )
            )
            element = self.driver.find_element(*locator)  # 等待完再重新获取
            ActionChains(self.driver).move_to_element(element).perform()
            if buffer:
                time.sleep(buffer)  # 给前端动画一点缓冲时间
            return element
        except TimeoutException:
            raise TimeoutException(f"元素等待超时: {locator}")
        except Exception as e:
            raise e

    def click(self, *locator, timeout=5, buffer=0.2, retry=3):
        for attempt in range(retry):
            try:
                element = self._wait_interactable(*locator, timeout=timeout, buffer=buffer)
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(0.2)
                element.click()
                return
            except StaleElementReferenceException:
                if attempt < retry - 1:
                    time.sleep(0.2)
                    continue
                raise
            except Exception as e:
                # 常规点击失败，不打大段堆栈，只简要提示
                self.logger.info(f"常规点击失败，尝试 JS 点击: {locator} )")
                try:
                    element = self.driver.find_element(*locator)
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                    self.driver.execute_script("arguments[0].click();", element)
                    self.logger.debug(f"JS 点击成功: {locator}")
                    return
                except Exception as e2:
                    # JS 兜底也失败 → 打完整异常方便排查
                    self.logger.error(f"JS 点击也失败: {locator}", exc_info=True)
                    raise

    def send_keys(self, text, *locator, timeout=5, buffer=0.2, retry=3):
        """智能输入：防 DOM 刷新 → 常规输入 → JS 兜底"""
        for attempt in range(retry):
            try:
                element = self._wait_interactable(*locator, timeout=timeout, buffer=buffer)
                element.click()
                element.clear()
                element.send_keys(text)
                time.sleep(0.1)
                return
            except StaleElementReferenceException:
                if attempt < retry - 1:
                    time.sleep(0.3)
                    continue
                raise
            except Exception as e:
                self.logger.error(f"常规输入失败，尝试 JS 输入: {locator}，原因: {e}")
                self.js_set_value(text, *locator)
                return

    def js_set_value(self, value, *locator):
        """JS 直接赋值并触发 input 事件"""
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("""
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            """, element, value)
        except Exception as e:
            raise Exception(f"JS 设置值失败: {locator}，原因: {e}")

    def get_text(self, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or 5).until(
                EC.visibility_of_element_located(locator)
            )
            return self.find_element(*locator).text
        except Exception as e:
            self.logger.error(f"[get_text] 元素获取失败: {locator}, 原因: {e}")
            return ""

    def send_keys_human_like(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(0.05)
        element.send_keys(Keys.TAB)

    def get_attribute(self, attribute, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or 3).until(
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

    def click_body(self):
        self.click(By.XPATH, "//body")

    def tab(self, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or 3).until(
                EC.visibility_of_element_located(locator)
            )
            element = self.find_element(*locator)
            element.send_keys(Keys.TAB)
        except Exception as e:
            self.logger.error(f"Tab键操作失败: {e}")
            raise

    def get_url(self):
        url = self.driver.current_url
        return url

    def ele_exist(self, *locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            ele = self.driver.find_element(*locator)
            return ele.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_mask_disappear(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-drawer-mask"))
            )
            # self.logger.info("遮罩层已完全消失")
        except TimeoutException:
            self.logger.warning("遮罩层未在预期时间内消失，继续执行点击")

    def upload_file(self, file_path,file_input_locator, file_name, timeout=10):
        """
        文件上传基础方法
        :param driver: WebDriver 实例
        :param file_input_locator: tuple, 文件输入框定位 (By.XPATH, "//input[@type='file']")
        :param file_path: str, 本地文件绝对路径
        :param timeout: 等待文件输入框可用的超时时间
        """
        file_path = get_file(file_path, file_name)
        try:
            # 等待文件输入框可见
            file_input = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(file_input_locator)
            )
            # 发送本地文件路径
            file_input.send_keys(file_path)
        except TimeoutException:
            raise TimeoutError(f"文件输入框 {file_input_locator} 未在 {timeout}s 内出现")
        except Exception as e:
            raise Exception(f"上传文件失败: {file_path}, 原因: {e}")



