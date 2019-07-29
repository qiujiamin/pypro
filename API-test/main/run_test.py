#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# no module named base.runmethod
# import sys
# sys.path.append("D:\pypro\API-test")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.depend_data import DependentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
import xlrd
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data=GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()

    # 程序执行的主入口
    def go_on_run(self):
        # 10  0,1,2,3,
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        print(rows_count)
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                print(i,url)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expect_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                # res = self.run_method.run_main(method, url, data, header)
            # if is_run:
                # method,url,data=None,header=None
                if depend_case != None:
                    # self.depend_data = DependentData(depend_case)
                    print("depend_case is"+" --- "+depend_case)
                    self.depend_data = DependentData(depend_case)
                    # 获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                #     获取依赖的key
                    print(depend_response_data)
                    depend_key = self.data.get_depend_field(i)
                    print(depend_key)
                    request_data[depend_key] =depend_response_data
                if header == "write":
                    res = self.run_method.run_main(method,url,request_data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()
                elif header =='yes':
                    op_json = OperationJson('../dataconfig/cookie.json')
                    cookie = op_json.get_data('apsid')
                    cookies ={
                        'apsid':cookie
                    }
                    # cookie = op_header.get_data()
                    # cookie = ../dataconfig/cookie.json ../dataconfig/cookie.json
                    res = self.run_method.run_main(method,url,request_data,cookies)
                else:
                    res = self.run_method.run_main(method,url,request_data)

                # res = self.run_method.run_main(method,url,request_data,header)
                # print(res)
                if self.com_util.is_contain(expect,res):
                    # print("测试通过")
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    # print("测试失败")
                    # self.data.write_result(i, 'fail')
                    self.data.write_result(i,res)
                    fail_count.append(i)
        self.send_email.send_main(pass_count,fail_count)
        # print (len(pass_count))
        # print (len(fail_count))
if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
    # print(run.go_on_run())
# TypeError: list indices must be integers or slices, not str
#    return self.data[id]
# KeyError: None
# mlt://webview?suffix=promotions%3fisH5%3d1
# TypeError: 'in <string>' requires string as left operand, not NoneType