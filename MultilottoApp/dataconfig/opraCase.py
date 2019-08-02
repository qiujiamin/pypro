#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from common.readConfig import ReadConfig
from utilconf.operation_json import OperationJson
from dataconfig import data_config
from common.opraExcel import  OpraExcel
import json
class OpraCase:
    def __init__(self,excel_name,sheet_id):
        self.excel_name = excel_name
        self.sheet_name = sheet_id
        self.readConfig = ReadConfig()
        self.opraExcel = OpraExcel(excel_name,sheet_id)
    # 获取excel行数，即case个数
    def set_excel_name(self,excel_name):
        self.excel_name = excel_name
    def get_excel_name(self):
        return self.excel_name
    def set_sheet_name(self,sheet_name):
        self.sheet_name = sheet_name
    def get_sheet_name(self):
        return  self.sheet_name

    def get_case_lines(self):
        return self.opraExcel.get_lines()
    # 获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opraExcel.get_cell_value(row,col)
        if run_model =="yes":
            flag = True
        else:
            flag = False
        return  flag
    # 获取是否携带header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.opraExcel.get_cell_value(row,col)
        if header =="yes":
            return data_config.get_header_value()
        else:
            return None
    # 获取请求方式
    def get_request_method(self,row):
        try:
            col = int(data_config.get_run_way())
            request_method = self.opraExcel.get_cell_value(row,col)
            return request_method
        except Exception as e:
            print(e)
            print("method不存在或输入错误，请检查")
    # 获取url_path
    def get_request_url(self, row,is_dev=True,is_serv=True):
        col= int(data_config.get_url_path())
        url_path = self.opera_excel.get_cell_value(row,col)
        if is_dev and is_serv:
            try:
                url = self.readConfig.get_service_dev('scheme') + '://' + self.readConfig.get_service_dev(
                    'host') + ':' + self.readConfig.get_service_dev(
                    'port') + self.get_path(case_name)
            return new_url

        return url

    # 拼接url
    # 根据用例名称获取接口地址，协议+host+port+path
    def get_interface_url(self,case_name,is_dev=True,is_serv=True):
        if is_dev and is_serv:
            try:
                new_url = self.readConfig.get_service_dev('scheme') + '://' + self.readConfig.get_service_dev(
                    'host') + ':' + self.readConfig.get_service_dev(
                    'port') + self.get_path(case_name)
                return new_url
            except Exception as e:
                print(e)
                print("dev服务用例名称不存在或输入错误，请检查")
        elif is_dev and is_serv==False:
            try:
                new_url = self.readConfig.get_h5app_dev('scheme') + '://' + self.readConfig.get_h5app_dev(
                    'host') + ':' + self.readConfig.get_h5app_dev(
                    'port') + self.get_path(case_name)
                return new_url
            except Exception as e:
                print(e)
                print("devh5app用例名称不存在或输入错误，请检查")
        elif is_dev==False and is_serv:
            try:
                new_url = self.readConfig.get_service_online('scheme') + '://' + self.readConfig.get_service_online(
                    'host') + ':' + self.readConfig.get_service_online('port') + self.get_path(case_name)
                return new_url
            except Exception as e:
                print(e)
                print("online服务用例名称不存在或输入错误，请检查")
        elif is_dev==False and is_serv==False:
            try:
                new_url = self.readConfig.get_h5app_online('scheme') + '://' + self.readConfig.get_h5app_online(
                    'host') + ':' + self.readConfig.get_h5app_online('port') + self.get_path(case_name)
                return new_url
            except Exception as e:
                print(e)
                print("onlineh5app用例名称不存在或输入错误，请检查")
        else:
            print('未知错误')

    # def get_interface_url(self, case_name, is_online=True):
    #         if is_online:
    #             try:
    #                 new_url = self.readConfig.get_h5app_dev('scheme') + '://' + self.readConfig.get_h5app_dev('host') + ":" + self.readConfig.get_h5app_dev('port') + self.get_path(case_name)
    #                 # print(new_url)
    #                 return new_url
    #             except Exception as e:
    #                 print(e)
    #                 print("用例名称不存在2，或输入错误，请检查！！！")
    #         else:
    #             try:
    #                 new_url = self.readConfig.get_http('scheme') + '://' + self.readConfig.get_http('host') + ":" + self.readConfig.get_http('port') + self.get_path(case_name)
    #                 return new_url
    #             except Exception as e:
    #                 print(e)
    #                 print("用例名称不存在1，或输入错误，请检查！！！")

    def get_interface_data(self,case_name):
        try:
            for i in range(0,self.readExcel.nrows):
                row_value = self.readExcel.get_excel()[i][0]
                if case_name ==row_value:
                    return self.readExcel.get_excel()[i][2]
        except Exception as e:
            print(e)
            print("data对应用例名称不存在，或输入错误，请检查")
    # def get_interface_headers(self,case_name):
    #     try:
    #         for i in range(0,self.readExcel.nrows):
    #             row_value = self.readExcel.get_excel()[i][0]
    #             if case_name == row_value:
    #                 headers = self.readExcel.get_excel()[i][3]
    #                 headers_dict = json.loads(headers)
    #                 return headers_dict
    #     except Exception as e:
    #         print(e)
    #         print("Headers不存在或输入错误，请检查")
#     根据用例名称返回这个用例所对应的path路径
    def get_path(self,case_name):
        for i in range(0,self.readExcel.nrows-1):
            row_value = self.readExcel.get_excel()[i][0]
            if case_name == row_value:
                return self.readExcel.get_excel()[i][1]
    def get_method(self,case_name):
        try:
            for i in range(0,self.readExcel.nrows):
                row_value = self.readExcel.get_excel()[i][0]
                if case_name == row_value:
                    return self.readExcel.get_excel()[i][4]
        except Exception as e:
            print(e)
            print("method对应用例名称不存在或输入错误，请检查")
if __name__ == '__main__':
    r = ReadCase('mltest(4).xlsx', '工作表1')
    # print(r.readExcel.nrows)
    # print(r.readExcel.ncols)
    # print(r.get_excel_name())
    # print(r.get_interface_data('getnearbyplaces'))
    # print(r.get_interface_data('login_error'))
    print(r.get_interface_url('getnearbyplaces',True,False))
    print(r.get_interface_url('getnearbyplaces',True,True))
    print(r.get_interface_url('getnearbyplaces',False,False))
    print(r.get_interface_url('getnearbyplaces',False,True))
    print(r.get_method('getnearbyplaces'))
    #s = r.get_intetface_headers('getvalidcountries')
    # print(r.get_interface_url('getcountryidbyip'))
    # print(r.get_intetface_headers("getnearbyplaces"))
    # print(r.get_interface_data("getnearbyplaces"))
    #print(s)
    #s1 = json.loads(s, encoding='utf-8')
    #print(type(s))
   # print()
   # print(type(s1))



