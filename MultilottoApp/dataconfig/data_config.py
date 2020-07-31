#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# test
class global_var:
    #case_id
    Id = '0'
    # 用例名称，只用于用户查看，无功能
    case_name ='1'
    # 请求名称，待定
    request_name = '2'
    # 域名，分辨dev或线上，如修改可统一变更（后面可能补一个文件直接读）。当前APP需区分dev_python,dev_h5app,线上等
    domain = '3'
    # 除了域名外的请求地址，会组合domain作为请求url
    url_path = '4'
    # 是否执行
    run ='5'
    # 请求类型，目前仅配置post及get,其他暂时报错
    run_way = '6'
    # 请求头，暂时写死,yes时调用，无需头文件则不填写。后面会改为，类似json的定制处理
    header = '7'
    # case依赖，填写需要提前执行的caseid，当前仅支持一个，如需多个，请多写几个用例叠加，当前用在需登录的情况较多
    case_depend = '8'
    # 数据依赖 依赖的返回数据。填写提取正则。当前写一个，依赖多个暂未补充
    data_depend ='9'
    # 字段依赖
    field_depend ='10'
    # 请求数据，写个关键字，细节到json中写，为解决excel加密，且排版漂亮
    data = '11'
    # 预期结果，一般写错误码
    expect ='12'
    # 实际运行结果，初始不需要填写。与预期匹配正确，写入pass;与预期有异常，写入返回结果
    result='13'
# 获取caseid
def get_id():
    return global_var.Id
# 获取用例名称
def get_case_name():
    return global_var.case_name
# 获取名称
def get_request_name():
    return global_var.request_name
# 获取域名
def get_domain():
    return global_var.domain
# 获取url_path
def get_url_path():
    return global_var.url_path
def get_url():
    domain = get_domain()
    path = get_url_path()
    url = domain + path
    return url
# 获取是否执行
def get_run():
    return global_var.run
# 获取请求方式
def get_run_way():
    return global_var.run_way
# 获取头
def get_header():
    return global_var.header
# 暂时用下面写死的
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
