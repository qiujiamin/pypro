#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from utilconf.operation_excel import OperationExcel
from base.runmethod import RunMethod
from dataconfig.get_data import GetData
from jsonpath_rw  import jsonpath,parse
import json
class DependentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data =GetData()
    # 根据依赖caseid去获取该caseid整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
#     执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
#         拿到行号，获取get_data等需要行号获取
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        # header = self.dataconfig.is_header(row_num)
        # if header == 'yes':

        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method,url,request_data,header)
        # return res
        return json.loads(res)
#     根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        # print("------------->>>>>>")
        # print(depend_data)
        # print(response_data)
#         响应值为字符串，需要处理。根据层级关系去拿
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        # for i in madle: i是字段类型
        # i.value
        # course:[0]:out_trade_no
        return [math.value for math in madle][0]






