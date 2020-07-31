#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
sys.path.append("D:\pypro\API-test-1")
from base.runmethod import RunMethod
from data.get_data import GetData
from utilconf.common_util import CommonUtil
from data.depend_data import DependentData
from utilconf.send_email import SendEmail
from utilconf.operation_json import OperationJson
from case.Login import GetLogininfo

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data=GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()
    # 程序执行的主入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url_path = self.data.get_urlpath(i)
            if url_path == '/api/user/login' or url_path =="/api/user/signup":
                # 登录特殊处理，按表中数据执行，但当前暂时不会记录结果：遇到登录需要更新信息loginingo.json，提供给后续传入行号来调用。登录失败暂不处理，手势及其他第三方登录暂未知
                print("本次登录/注册行号为 %d" % i)
                # 自定义登錄方法在logininfo中修改
                loginuser = GetLogininfo()
                loginuser.get_logininfo_byrow(i)
            else:
                is_run = self.data.get_is_run(i)
                if is_run:
                    url = self.data.request_url(i)
                    print(i, url)
                    method = self.data.get_request_method(i)
                    request_data = self.data.opra_request_data(i)
                    header = self.data.is_header(i)
                    expect = self.data.get_expect_data(i)
                    depend_case = self.data.is_depend(i)
                    needlogin = self.data.get_needlogin(i)
                    if needlogin:
                        # 获取登录信息
                        loginjson = OperationJson('../dataconfig/logininfo.json')
                        logininfo = loginjson.get_data('logininfo')
                        if logininfo['usercheck']:
                            request_data['usercheck'] = logininfo['usercheck']
                            request_data['userid'] = logininfo['userid']
                            print(request_data)
                        else:
                            # 登录如果没有信息，则重新登录并写入json文件
                            loginuser = GetLogininfo()
                            loginuser.get_logininfo_byrow(7)
                            logininfo = loginjson.get_data('logininfo')
                            request_data['usercheck'] = logininfo['usercheck']
                            request_data['userid'] = logininfo['userid']
                            print(request_data)
                    if depend_case != None:
                        print("depend_case is"+" --- "+depend_case)
                        depend_data = DependentData(depend_case)
                            # 获取的依赖响应数据
                        print(i)
                        depend_response_data = depend_data.get_data_for_key(i)
                        print("依赖的响应数据")
                        print(depend_response_data)
                        print("======")
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
                            # if header == "write":
                            # # 这里后面再调试，目前不需要写
                            #     res = self.run_method.run_main(method,url,request_data)
                            #     op_header = OperationHeader(res)
                            #     op_header.write_cookie()
                            # elif header =='yes':
                            #     op_json = OperationJson('../dataconfig/cookie.json')
                            #     cookies = op_json.get_data('header')
                            #     res = self.run_method.run_main(method,url,request_data,cookies)
                            # else:
                            #     res = self.run_method.run_main(method,url,request_data)
                    res = self.run_method.run_main(method,url,request_data,header)
                    print(res)
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
