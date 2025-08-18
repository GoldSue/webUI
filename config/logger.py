import logging
import os
from datetime import datetime

if not os.path.exists("logs"):
    os.mkdir("logs")

log_file = os.path.join("logs", f"{datetime.now().strftime('%Y-%m-%d')}.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    file_handle = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handle.setFormatter(logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    console_handle = logging.StreamHandler()
    console_handle.setFormatter(logging.Formatter(
        fmt="%(asctime)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    # ✅ 这里要用 addHandler 而不是 addFilter
    logger.addHandler(file_handle)
    # logger.addHandler(console_handle)

# 直接使用 logger
logger.info("日志初始化完成")


