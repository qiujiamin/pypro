#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import requests
import json
class ConfigHttp:
    def __init__(self,method,url=None,header=None,data=None):
        if method =="get":
            self.request = requests.get(url=url,headers = header,params=data)
            self.result = self.request.json()
            self.status_code = self.request.status_code
            self.text = self.request.text
            self.content = self.request.content
            self.cookies = self.request.cookies
        elif method =='post':
            self.request = requests.post(url=url,headers = header,data =data)
            self.result = self.request.json()
            self.status_code = self.request.status_code
            self.text = self.request.text
            self.content = self.request.content
            self.cookies = self.request.cookies
        else:
            print("新建confighttp对象失败，请确认传入的参数")
    # 需要str类型的返回结果，则添加参数is_str=True,否则返回dict类型
    def request_result(self,result_type_is_str = False):
        if result_type_is_str:
            res = json.dumps(self.result,ensure_ascii=False,sort_keys=True,indent=2)
            return res
        else:
            return self.result
    def request_status_code(self):
        return self.status_code
    def get_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.cookies)
        return cookie
if __name__ == '__main__':
    url = 'https://h5app-dev.multilotto.net/api/user/getcountryidbyip'
    data = {
        "language": "EN",
        "platform": "3000",
        "remote_addr": "13.230.65.62",
        "userid": "",
        "subchannel": "10004",
        "casinoversion": "2.7.0",
        "version": "2.7.0",
        "pushid": "a7b69ace-4b6d-49e4-8ef4-077 c58a182b2 ",
        "usercheck ": "",
        "username ": "",
        "pushproject ": "curacao ",
        "uniq ": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
    }
    url1 = 'https://h5app-dev.multilotto.net/en/lotto-results/usa-powerball/2019-07-20?isH5=1'
    result =ConfigHttp('post',url,'',data)
    print(result.request_result(False))
    # print(request_result(True))