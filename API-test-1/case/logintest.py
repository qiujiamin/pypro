#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import sys
import json
import  requests

sys.path.append("D:\pypro\API-test-1")
from base.runmethod import RunMethod
from data.get_data import GetData
from utilconf.common_util import CommonUtil
from utilconf.operation_json import OperationJson


class GetLogininfo:
    def __init__(self,case_line):
        self.run_method = RunMethod()
        self.data=GetData()
        self.com_util = CommonUtil()
        self.case_line = case_line
    def get_logininfo(self):
        userinfolist = []
        url = self.data.request_url(self.case_line)
        print(url)
        method = self.data.get_request_method(self.case_line)
        print(method)
        op_json = OperationJson('../dataconfig/cookie.json')
        cookies = op_json.get_data('header')
        # print(cookies)
        request_data = self.data.get_data_for_json(7)
        print(request_data)
        res = self.run_method.run_main(method, url, request_data,cookies)
        # print(type(res))
        res = json.loads(res)
        # print(type(res))
        usercheck = res['info']['usercheck']
        userid = res['info']['userid']
        userinfolist = [usercheck,userid]
        # print(userinfolist)
        return userinfolist

# res = requests.post(url,data).json()
#
# print(res)
# # print("=====================")
# usercheck = res['info']['usercheck']
# userid = res['info']['userid']
# print(usercheck)
# # url1 = "https://h5app-dev.multilotto.com/en/touch/dashboard/mygames/active/?version=2.9.0"
# # data1 = {}
# url1 = "https://h5app-dev.multilotto.com/en/touch/auth/applogin/"+userid+"/"+usercheck+"?url=touch/dashboard/mygames/active/&version=2.6.1"
# print(url1)
# res1 = requests.get(url1)
# print(res1)
if __name__ == '__main__':
    loginuser = GetLogininfo(7)
    userinfo = loginuser.get_logininfo()
    print(userinfo)
