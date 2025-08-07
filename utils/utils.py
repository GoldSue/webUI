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


def get_case_data(moudle_name,file_name, case_name):
    file_path = os.path.join(get_root(), 'data',moudle_name, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data_list = yaml.safe_load(file)

            for case in data_list:
                if case.get("case") == case_name:
                    return case.get("data")

            return None  # 如果没有找到匹配的 case

    except Exception as e:
        print(f'Error loading YAML file: {e}')
        return None
# print(random_digits(3))
# print(random_letters(3))
# print(random_letters_digits(8))
print(get_case_data('user_mag_data','add_cop_user.yaml', 'edit_cop_user'))