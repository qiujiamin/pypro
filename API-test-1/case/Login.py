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
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
    # 登录，提供读取用例excel第七行登录方式（请excelmm-07中写死登录）
    def get_logininfo_byrow(self,case_line=None):
        # 还需要处理写入表格
        filepath ='../dataconfig/logininfo.json'
        logininfojson = OperationJson(filepath)
        logininfo = logininfojson.get_data('logininfo')
        print("读取前的userjson文件信息")
        print(logininfo)
        url = self.data.request_url(case_line)
        # print(url)
        method = self.data.get_request_method(case_line)
        # print(method)
        header = self.data.is_header(case_line)
        # op_json = OperationJson('../dataconfig/cookie.json')
        # cookies = op_json.get_data('header')
        request_data = self.data.get_data_for_json(case_line)
        expect = self.data.get_expect_data(case_line)
        print(expect)
        # print(request_data)
        # res = self.run_method.run_main(method, url, request_data,cookies)
        res = self.run_method.run_main(method, url, request_data,header)
        if self.com_util.is_contain(expect, res):
            print("测试通过")
            self.data.write_result(case_line, 'pass')
        else:
            print("测试失败")
            # self.data.write_result(i, 'fail')
            self.data.write_result(case_line, res)
        res = json.loads(res)
        logininfo['usercheck'] = res['info']['usercheck']
        logininfo['userid'] = res['info']['userid']
        logininfo['verificationcode'] = res['info']['verificationcode']
        print("登录成功后的信息")
        print(logininfo)
        logininfojson.write_data(filepath, 'logininfo', logininfo)
        print('重新写入文件中信息')
        print(logininfojson.get_data('logininfo'))

        return logininfo
    # 登录，自定义，有时候可能需要其他账号登录，自己写一下参数，就不需要再改excel/json了
    def get_logininfo_hardcode(self):
        url = "https://h5app-dev.multilotto.net/api/user/login"
        data = {
            "pushproject": "curacao",
            "password": "Aa123456",
            "email": "de08@gmail.com",
            "userid": "",
            "uniq": "android_c5a219a3-9ee6-4b5f-9b18-c7dec9bc10f0_1570777588260",
            "useragent": "MI 6 ",
            "platform": "4000",
            "osversion": "5.1.1",
            "remote_addr": "172.17.100.15",
            "version": "3.0.0",
            "countryid": "EN",
            "resolution": "900x1600",
            "language": "EN",
            "pushid": "3679c083-b597-4112-b1bd-eced7d0f5b39",
            "subchannel": "10005",
            "usercheck": ""
        }
        header = {
            "accept": "*/*",
            "content-type": "application/json; charset=UTF-8",
            "content-length": "442",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.8.1",
            "XForwardedFor": "89.31.136.0",
        }
        res = requests.post(url, data, header).json()
        usercheck = res['info']['usercheck']
        userid = res['info']['userid']
        userinfolist = [usercheck, userid]
        return userinfolist
if __name__ == '__main__':
    # 使用方法1
    loginuser = GetLogininfo()
    userinfo = loginuser.get_logininfo_byrow(1)
    # 使用方法2
    # loginuser = GetLogininfo()
    # userinfo = loginuser.get_logininfo_hardcode()
    # print(userinfo)
