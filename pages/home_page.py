from urllib.parse import urlparse

from base.base import BasePage
from config.env_config import EnvConfig


class HomePage(BasePage):

    def get_home_page(self):
        """如果当前不在首页，则跳转首页"""
        url = EnvConfig.get_base_url()
        if not self.is_on_page(url):
            self.logger.info(f"🔄 跳转到首页")
            self.driver.get(url)
        else:
            self.logger.info("✅ 当前已在首页")

    def go_to_module(self, *nav_locator, module_name="模块"):
        """点击左侧导航栏模块按钮"""
        try:
            self.click(*nav_locator, timeout=3)
            self.logger.info(f"✅ 已跳转到 [{module_name}] ")
        except Exception as e:
            self.logger.error(f"❌ 跳转到 [{module_name}] 模块失败: {e}")
            raise

    def is_on_page(self, url):
        """判断当前 URL 是否在指定页面"""
        current_url = self.get_url()
        return urlparse(self.get_url()).path.rstrip("/") == urlparse(url).path.rstrip("/")
