#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header !=None:
            # res = requests.post(url =url,dataconfig=dataconfig,headers=header).json()
            res = requests.post(url =url,data=data,headers=header)
        else:
            # res = requests.post(url =url,dataconfig=dataconfig).json()
            res = requests.post(url =url,data=data)
        print(res.status_code)
        return res.json()
    def get_main(self,url,data=None,header=None):
        # 增加了Verify =
        res = None
        if header !=None:
            # res = requests.get(url =url,dataconfig=dataconfig,headers=header).json()
            res = requests.get(url =url,data=data,headers=header,verify=False)
        else:
            res = requests.get(url =url,data=data,verify=False)
        return res
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method  == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        # return res
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
#     self.opera_excel = op^
# global name 'self' is not defined





