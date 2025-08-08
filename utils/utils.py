import os.path
import random
import string
from datetime import datetime, timedelta

import yaml


def get_root():
    current_path = os.path.abspath(__file__)

    # 逐级向上查找直到找到main.py
    while current_path != os.path.dirname(current_path):
        if os.path.exists(os.path.join(current_path, 'main.py')):
            return current_path
        current_path = os.path.dirname(current_path)
    print(current_path)
    raise FileNotFoundError("找不到包含main.py的项目根目录")
def to_dirname(file_name):
    root = get_root()
    return os.path.join(root, file_name)

def load_yaml(file_name):
    file_path = os.path.join(get_root(), 'data', file_name)

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                return data
        except Exception as e:
            print(f'Error loading YAML file: {e}')

def tomorrow():
    return (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
def month_later():
    return (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

def random_digits(n=6):
    return ''.join(random.choices(string.digits, k=n))

def random_letters(n=6):
    return ''.join(random.choices(string.ascii_letters, k=n))

def random_letters_digits(n=8):
    if n < 3:
        raise ValueError("长度必须 >= 3，才能包含大小写字母和数字各至少一位")

    # 至少各1位
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)

    # 剩下的位数，从混合池中选择
    remaining = random.choices(string.ascii_letters + string.digits, k=n - 3)
    # 合并并打乱顺序
    password_list = list(lower + upper + digit + ''.join(remaining))
    random.shuffle(password_list)
    return ''.join(password_list)


def get_case_data(module_name, file_name, case_name=None, return_list=False):
    """
    从 data/<module_name>/<file_name> 中读取测试数据。
    - 如果 YAML 是列表形式（多数用例文件会是这种），按 "case" 字段匹配并返回对应的 "data"。
    - case_name 为 None 时，返回该文件中所有 case 的 data（列表）。
    - 如果 return_list=True，总是返回匹配项的列表（可能为空）。
    - 返回单项时，若找不到匹配返回 None。
    """
    file_path = os.path.join(get_root(), 'data', module_name, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)

        # 空文件或解析为 None
        if content is None:
            return [] if return_list else None

        # 情形 A: YAML 顶层是 list（最常见）
        if isinstance(content, list):
            # 收集所有匹配 case 的 data（注意 data 可能是 dict 或 list）
            matches = []
            for item in content:
                if not isinstance(item, dict):
                    continue
                if case_name is None:
                    # 收集所有 case 的 data
                    matches.append(item.get('data'))
                else:
                    if item.get('case') == case_name:
                        matches.append(item.get('data'))
            if return_list:
                return matches
            # 若要求单条，返回第一个匹配或全部中的第一项
            if case_name is None:
                return matches  # 当 case_name==None 时直接返回所有 data 列表
            return matches[0] if matches else None

        # 情形 B: YAML 顶层是 dict（少见，但兼容）
        if isinstance(content, dict):
            if case_name is None:
                return content
            # 直接取 keyed dict 的值（兼容你原来的写法）
            return content.get(case_name)

        # 其它类型不支持
        return None

    except Exception as e:
        # 日志打印或抛出，根据项目约定处理
        print(f'Error loading YAML file: {e}')
        return None
# print(random_digits(3))
# print(random_letters(3))
# print(random_letters_digits(8))
# print(get_case_data('user_mag_data','add_cop_user.yaml', 'add_cop_user'))