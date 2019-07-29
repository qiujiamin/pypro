import os
import configparser
from common.getpathInfo import get_path


class ReadConfig:

    path = get_path()
    config_path = os.path.join(path, '../testFile', 'config.ini')  # 配置文件的路径
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')  # 读取config.ini配置文件内容

    def get_http(self, name):
        try:
            return self.config.get('HTTP', name)
        except Exception as e:
            print(e, '请检查配置名称')

    def get_email(self, name):
        try:
            return self.config.get('EMAIL', name)
        except Exception as e:
            print(e, '请检查配置名称')

    def get_database(self, name):
        try:
            return self.config.get('DATABASE', name)
        except Exception as e:
            print(e, '请检查配置名称')

    def get_ml_h5app(self, name):
        try:
            return self.config.get('ML-h5app', name)
        except Exception as e:
            print(e, '请j检查配置情况')


if __name__ == '__main__':
    print("http配置中host的值为", ReadConfig().get_http('host'))
    print("email配置中，on_off的值为", ReadConfig().get_email('on_off3'))
    print('ML配置中，host的值为', ReadConfig().get_ml_h5app('port'))