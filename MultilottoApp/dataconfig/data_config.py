#! /usr/bin/env/python
# -*- coding:utf-8 -*-
class global_var:
    #case_id
    Id = '0'
    request_name = '1'
    url_path = '2'
    run ='3'
    run_way = '4'
    header = '5'
    # case依赖，需要提前执行的caseid
    case_depend = '6'
    # 数据依赖 依赖的返回数据
    data_depend ='7'
    # 字段依赖
    field_depend ='8'
    data = '9'
    expect ='10'
    result='11'
# 获取caseid
def get_id():
    return global_var.Id
# 获取名称
def get_request_name():
    return global_var.request_name
# 获取url
def get_url_path():
    return global_var.url_path
# 获取是否执行
def get_run():
    return global_var.run
# 获取请求方式
def get_run_way():
    return global_var.run_way
# 获取头
def get_header():
    return global_var.header
# 获取用例数据依赖id
def get_case_depend():
    return global_var.case_depend
# 获取依赖数据
def get_data_depend():
    return global_var.data_depend
# 获取数据所属字段
def get_field_depend():
    return global_var.field_depend
# 获取请求数据
def get_data():
    return global_var.data
# 获取请求预期结果
def get_expect():
    return global_var.expect
# 获取实际结果
def get_result():
    return global_var.result
def get_header_value():
    # # 暂时写死
    # header = {
    #     "header":"1234",
    #     "cookie":"mushsi"
    # }
    header = {
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
    return header