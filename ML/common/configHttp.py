import json
import requests


class RunMain:
    # 需要str类型的返回结果，则添加参数is_str =True，否则返回dict类型
    def post(self, url, header, data, is_str=False):
        result = requests.post(url=url, headers=header, data=data).json()
        if is_str:
            res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
            return res
        else:
            return result

    def get(self, url, header, data, is_str=False):
        result = requests.get(url=url, headers=header, params=data).json()
        if is_str:
            res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)  # 将result的dict类型转换成str格式
            return res
        else:
            return result

    def run_main(self, method, url=None, header=None, data=None, is_str=False):
        result = None
        if method == 'post':
            result = self.post(url, header, data, is_str)
        elif method == 'get':
            result = self.get(url, header, data, is_str)
        else:
            print("不支持这种method方式")
        return result


if __name__ == '__main__':
    result1 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', '', 'name=xiaoming&pwd=111', True)
    print(type(result1))
 #   result2 = json.loads(result1)
  #  print(type(result2))