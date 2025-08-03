import os.path
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


# print(load_yaml('loginData.yaml'))

# to_dirname('testcase')