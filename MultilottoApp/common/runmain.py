#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import json
import requests

class RunMain:
    # 需要str类型的返回结果，则添加参数is_str = True,否则返回dict类型
    def post(self,url,header,data,is_str =False):
        result = requests.post(url=url,headers=header,data = data).json()
        if is_str:
            res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
            return res
        else:
            return result
    def get(self,url,header,data,is_str=False):
        result = requests.get(url,headers=header,params=data).json()
        if is_str:
            res = json.dumps(result,ensure_ascii=False,sort_keys=True,is_str=False)
            return res
        else :
            return result
    def run_main(self,method,url =None,header = None,data = None,is_str=False):
        result = None
        if method == 'post':
            result = self.post(url,header,data,is_str)
        elif method == 'get':
            result = self.get(url,header,data,is_str)
        else:
            print("不支持这种method方式")
        return result

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
    result =RunMain().run_main('post',url,'',data,False)
    result1 = RunMain().run_main('get',url,'','',False)
    print(result)
    print(result1)

