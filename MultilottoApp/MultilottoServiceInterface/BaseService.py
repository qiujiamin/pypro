from common.readCase import *
from common.readConfig import *
from common.configHttp import ConfigHttp


"""
基础接口类 ，其他接口需继承该类，传入case_name生成对应的接口对象
具体请求直接实现request_service方法即可
"""
class BaseService:
    def __init__(self,case_name):
        self.config = ReadConfig()
        self.case_excel = ReadCase('mltest8.xlsx', '工作表1') #写死，作为这个excel接口测试的用例
        self.case_name = case_name
        # 这里可能需要改一下
        self.service_url = self.case_excel.get_interface_url(self.case_name,True,True)
        self.service_header = self.case_excel.get_interface_headers(self.case_name)
        self.service_data = self.case_excel.get_interface_data(self.case_name)
        self.service_method = self.case_excel.get_method(self.case_name)
        self.config_http = ConfigHttp(self.service_url,self.service_header,self.service_data,self.service_method)

    # 默认返回dict类型的result,如果需要，str类型的，设置str_format = True
    def set_case_name(self,case_name):
        self.case_name = case_name
    def get_case_name(self):
        return self.case_name

    # 传入result_typr_is_str字段，传入False返回dict类型，传入True返回Str类型
    def request_service(self,result_type_is_str):
        return  self.config_http.request_result(result_type_is_str)
    # 获取返回状态码
    def status_code(self):
        return self.config_http.status_code
    # 获取返回的text文本
    def text(self):
        return self.config_http.text
    # 获取返回的content
    def content(self):
        return  self.config_http.content
    # 返回一个cookiejar
    def cookies(self):
        return self.config_http.cookies
if __name__ == '__main__':
    # bs = BaseService("login_de_account")
    bs = BaseService("getcountryidbyip")
    print(bs.case_name)
    print(bs.request_service(False))
