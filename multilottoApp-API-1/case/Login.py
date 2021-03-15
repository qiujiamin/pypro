#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import sys
import json
import  requests

from base.runmethod import RunMethod
from data.get_data import GetData
from utilconf.common_util import CommonUtil
from utilconf.operation_json import OperationJson


class GetLogininfo:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
    def get_logininfo_byrow(self,case_line=None):
        """
        读取excel中接口中为登录/注册的接口，每次正常登录/注册成功（异常登录/注册不要写在excel中）,提取usercheck及userid,更新'../dataconfig/logininfo.json'文件，以提供其他接口使用
        原因说明：因为基本所有接口都需要登录，但每个接口前面都调用一次登录退出，会出现同一个账号登录频繁的问题，导致一些没必要报错，影响同一个excel中的执行效率
        故特殊处理。异常登录/注册会单独处理，其他均可使用该excel
        :param case_line:登录用例的行号
        :return:logininfo=[usercheck, userid,verificationcode],如后续需要用到其他，可再补充。
        """
        filepath ='../dataconfig/logininfo.json'
        logininfojson = OperationJson(filepath)
        logininfo = logininfojson.get_data('logininfo')
        print("读取前的userjson文dd件信息")
        print(logininfo)
        url = self.data.request_url(case_line)
        method = self.data.get_request_method(case_line)
        header = self.data.is_header(case_line)
        # request_data = self.data.get_data_for_json(case_line)
        request_data = self.data.opra_requestdata(case_line)
        expect = self.data.get_expect_data(case_line)
        try:
            res = self.run_method.run_main(method, url, request_data,header)
            if res:
                if self.com_util.is_contain(expect, res):
                    print("11登录/注册测试通过")
                    self.data.write_result(case_line, 'pass')
                    res = json.loads(res)
                    if res['info']['usercheck']:
                        logininfo['usercheck'] = res['info']['usercheck']
                        logininfo['userid'] = res['info']['userid']
                        logininfo['verificationcode'] = res['info']['verificationcode']
                        logininfo['email'] = res['info']['email']
                        print("登录成功后的信息是")
                        print(logininfo)
                        logininfojson.write_data(filepath, 'logininfo', logininfo)
                        # print('重新写入文件中信息')
                        # print(logininfojson.get_data('logininfo'))
                        return logininfo
                else:
                    print("登录/注册测试失败了了")
            # self.data.write_result(i, 'fail')
                    self.data.write_result(case_line, res)
                    return None
        except IndexError as e:
            print("该次登录/注册请求出错了")
            pass
    def get_logininfo_hardcode(self,type = None,server = None):
        """
        登录，自定义，有时候可能需要其他账号登录，自己写一下参数，就不需要再改excel/json了
        ps.暂时作为调试用，未更新
        :return:  userinfolist = [usercheck, userid]
        """
        url = "https://h5app-dev.multilotto.net/api/user/login"
        urlonline = "https://service.multilotto.net/api/user/login"
        data_android = {
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
        data_IOS = {
            "access_token": "",
            "casinoversion": "3.0.1",
            "email": "De08@gmail.com",
            "external_identifier": "",
            "external_typeid": "",
            "hashstr": "",
            "language": "EN",
            "password": "Aa123456",
            "platform": "3000",
            "pushid": "a7b69ace-4b6d-49e4-8ef4-077c58a182b2",
            "pushproject": "curacao",
            "subchannel": "10004",
            "uniq": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
            "usercheck": "",
            "userid": "",
            "username": "",
            "version": "3.0.1"
        }
        header_android = {
            "accept": "*/*",
            "content-type": "application/json; charset=UTF-8",
            "content-length": "442",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.8.1",
            "XForwardedFor": "89.31.136.0",
        }
        header_ios = {
        "AcceptLanguage": "zh-Hans-CN;q=1.0",
        "ContentType": "application/x-www-form-urlencoded;charset=utf-8",
        "AcceptEncoding"
        "": "gzip;q=1.0, compress;q=0.5",
        "User-Agent": "MultiLotto/2.6.1 CFNetwork/902.2 Darwin/17.7.0",
        "Accept": "/",
        "XForwardedFor": "89.31.136.0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d1c8a3cb521f1f4b72487b5dae55428f1545292386"
        }
        if server ==None:
            if type ==None:
                res = requests.post(url, data_android, header_android).json()
            else:
                res = requests.post(url, data_IOS, header_ios).json()
        usercheck = res['info']['usercheck']
        userid = res['info']['userid']
        useremail= res['info']['email']
        uservertificode= res['info']['verificationcode']
        if usercheck:
            filepath = '../dataconfig/logininfo.json'
            logininfojson = OperationJson(filepath)
            logininfo = logininfojson.get_data('logininfo')
            logininfo['usercheck'] = usercheck
            logininfo['userid'] = userid
            logininfo['email'] = useremail
            logininfo['verificationcode'] = uservertificode
            print("登录成功,本次是固定的登录调用，会写入loginjson，但不统计到执行用例总个数")
            print(logininfo)
            logininfojson.write_data(filepath, 'logininfo', logininfo)
            print('重新写入文件中信息')
            print(logininfojson.get_data('logininfo'))
            return logininfo
        else:
            print("固定登录失败，请检查")
        # userinfolist = [usercheck, userid]
        # return userinfolist
if __name__ == '__main__':
    # 使用方法1
    loginuser = GetLogininfo()
    userinfo = loginuser.get_logininfo_byrow(1)
    # 使用方法2
    # loginuser = GetLogininfo()
    # userinfo = loginuser.get_logininfo_hardcode()
    # print(userinfo)
