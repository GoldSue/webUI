
# config/env_config.py

class EnvConfig:
    # 当前环境：dev / staging / prod
    ENV = "dev"

    # 各环境对应的 base_url
    BASE_URLS = {
        "dev": "https://console-paas.digiwincloud.com.cn"
    }

    @classmethod
    def get_base_url(cls):
        return cls.BASE_URLS.get(cls.ENV, cls.BASE_URLS["dev"])



