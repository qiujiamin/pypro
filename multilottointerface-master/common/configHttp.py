import json
import requests


class ConfigHttp:
    def __init__(self, url, header, data, method):
        if method == "get":
            self.request = requests.get(url=url, headers=header, params=data)
            self.result = self.request.json()
            self.status_code = self.request.status_code
            self.text = self.request.text
            self.content = self.request.content
            self.cookies = self.request.cookies
        elif method == 'post':
            self.request = requests.post(url=url, headers=header, data=data)
            self.result = self.request.json()
            self.status_code = self.request.status_code
            self.text = self.request.text
            self.content = self.request.content
            self.cookies = self.request.cookies

        else:
            print("新建confighttp对象失败，请确认传入的参数")

    # 需要str类型的返回结果，则添加参数is_str =True，否则返回dict类型
    def request_result(self, result_type_is_str=False):
        if result_type_is_str:
            res = json.dumps(self.result, ensure_ascii=False, sort_keys=True, indent=2)
            return res
        else:
            return self.result

    def request_status_code(self):
        return self.status_code

    def get_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.cookies)
        return cookie


