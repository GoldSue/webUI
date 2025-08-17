import time
from functools import wraps
from datetime import datetime


def log_and_time(_func=None, *, log_func=print):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_func(f"{func.__name__}() | 开始执行")

            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time

            log_func(f"{func.__name__}() | 执行结束 | 耗时: {elapsed:.3f} 秒")
            return result

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)
