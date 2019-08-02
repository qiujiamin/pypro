#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from utilconf.operation_excel import OperationExcel
import data_config
from utilconf.operation_json import OperationJson
# 拿excel数据
class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()
    #     去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    # 获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return  flag
    # 是否携带header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row,col)
        if header == 'yes':
            # return 'header'
            return data_config.get_header_value()
        else:
            return None
    # 获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method
#     获取url
    def get_request_url(self,row):
        col= int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row,col)

        return url
#     获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row,col)
        if data =='':
            return None
        return data
#     通过获取关键字 拿到data数据
    def get_data_for_json(self,row):
        # 不在构造函数，而在这里实例化，因为有的data不需要json
        opera_json = OperationJson()
        # 数据来源-excel，可直接调用
        # request_data = opera_json.get_data(self.get_request_data())
        request_data = opera_json.get_data(self.get_request_data(row))
        return  request_data
#     获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        if expect =='':
            return None
        return expect
    # 写入结果
    def write_result(self,row,value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row,col,value)

#     获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key
# 判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_case_depend())
        depend_case_id= self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

#         获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_field_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            return data
# if __name__ == '__main__':
#     print("hello")




