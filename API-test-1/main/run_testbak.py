#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# no module named base.runmethod
import sys
sys.path.append("D:\pypro\API-test-1")
from base.runmethod import RunMethod
from data.get_data import GetData
from utilconf.common_util import CommonUtil
from data.depend_data import DependentData
from utilconf.send_email import SendEmail
from python.leaningdic import OperationHeader
from utilconf.operation_json import OperationJson
from case.Login import GetLogininfo

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data=GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()
        # self.getlotinfo = GetLogininfo()
    # 程序执行的主入口
    def go_on_run(self):
        # 10  0,1,2,3,
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        print('1----case数量')
        print(rows_count)
        for i in range(1,rows_count):
            caseid = self.data.get_case_id(i)
            # 登录的caseid 固定写为'mm-01'
            if caseid == 'mm-07':
                loginid = i
                print("登录行号为 %d" %loginid)
                # 不传行号可以调用自定义的登录，自定义方法参考logininfo中修改
                loginuser = GetLogininfo(loginid)
                userinfo = loginuser.get_logininfo_byrow()
                # print(request_data)
                print(userinfo)
            else:
                is_run = self.data.get_is_run(i)
                if is_run:
                    url = self.data.request_url(i)
                    # print('2---case行号，url拼接')
                    print(i,url)
                    method = self.data.get_request_method(i)
                    # print('3---方法')
                    # print(method)
                    request_data = self.data.get_data_for_json(i)
                    # print('4---请求数据')
                    # print(request_data)
                    expect = self.data.get_expect_data(i)
                    # print('5---预期值')
                    # print(expect)
                    header = self.data.is_header(i)
                    # print('6----头信息')
                    # print(header)
                    depend_case = self.data.is_depend(i)
                    # print('7---依赖用例id')
                    # print(depend_case)
                    needlogin = self.data.get_needlogin(i)
                    print(needlogin)
                    # res = self.run_method.run_main(method, url, data, header)
                    # 第七行写死登录
                    if needlogin:
                        if userinfo:
                            request_data['usercheck'] = userinfo[0]
                            request_data['userid'] = userinfo[1]
                            print(request_data)
                        else:
                            loginuser = GetLogininfo(7)
                            userinfo = loginuser.get_logininfo_line7()
                            request_data['usercheck'] = userinfo[0]
                            request_data['userid'] =userinfo[1]
                            print(request_data)
                    if depend_case != None:
                        # self.depend_data = DependentData(depend_case)
                        print("depend_case is"+" --- "+depend_case)
                        self.depend_data = DependentData(
                            depend_case)
                        # 获取的依赖响应数据
                        depend_response_data = self.depend_data.get_data_for_key(i)
                        if isinstance(depend_response_data, str):
                            depend_key = self.data.get_depend_field(i)
                            request_data[depend_key] = depend_response_data
                            print("只有一个依赖数据，以str处理")
                        elif isinstance(depend_response_data, list):
                            # list
                            depend_key_list = self.data.get_depend_field(i)
                            for item in range(len(depend_key_list)):
                                request_data[depend_key_list[item]] = depend_response_data[item]
                            print("依赖数据后的request_data")
                            print(request_data)
                        else:
                            print('依赖出错了')
                    if header == "write":
                    # 这里后面再调试，目前不需要写
                        res = self.run_method.run_main(method,url,request_data)
                        op_header = OperationHeader(res)
                        op_header.write_cookie()
                    elif header =='yes':
                        op_json = OperationJson('../dataconfig/cookie.json')
                        # cookie = op_json.get_data('header')
                        cookies = op_json.get_data('header')
                        # print(cookies)
                        # cookie = ../dataconfig/cookie.json ../dataconfig/cookie.json
                        res = self.run_method.run_main(method,url,request_data,cookies)
                        # print(res)
                    else:
                        res = self.run_method.run_main(method,url,request_data)
                    # if header =='yes':
                    # res = self.run_method.run_main(method,url,request_data,header)
                    # print('----打印返回值')
                    # print(res)
                    if self.com_util.is_contain(expect,res):
                        print("测试通过")
                        self.data.write_result(i,'pass')
                        pass_count.append(i)
                    else:
                        print("测试失败")
                        # self.data.write_result(i, 'fail')
                        self.data.write_result(i,res)
                        fail_count.append(i)
        # self.send_email.send_main(pass_count,fail_count)
        # print (len(pass_count))
        # print (len(fail_count))
if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
