import os


# 获取当前目录的绝对路径
def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == "__main__":
    print('测试路径是否OK,路径为:', get_path())
    print(type(get_path()))
