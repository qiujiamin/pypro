#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from MultilottoApp.MultilottoServiceInterface.BaseService import BaseService
from waitingToOptmize.configHttp import ConfigHttp

class Login(BaseService):
    """
    登录类，继承bashServicel类
    传入case_name名称，生成不同的登录对象，
    调用login——service方法去请求登录的接口，返回结果内容
    """

    def __init__(self,case_name):
        super().__init__(case_name)
    def login_service(self,result_type_is_str = False):
        result = self.request_service(result_type_is_str)
        return result
    # 带cookie的登录
    def login_cookie_service(self,case_name,resuly_type_is_str=False):
        service_header = self.add_cookie_header()
        service_data = str(self.case_excel.get_interface_data(case_name))+self.user_check()+self.userid()+self.username()
        service_url = self.case_excel.get_interface_url(case_name)
        service_method = self.case_excel.get_method(case_name)
        config_http = ConfigHttp(service_url,service_header,service_data,service_method)
        print("这次的headers："+str(service_header))
        print("这次的url："+str(service_url))
        print("这次的data："+str(service_data))
        print("这次的method："+str(service_method))

        result = config_http.request_result(resuly_type_is_str)
        return result

    # 获取当前登录用户的user_check
    def user_check(self):
        result = self.login_service()
        info = result["info"]
        user_check = info["usercheck"]
        return '&usercheck='+str(user_check)
    def userid(self):
        result = self.login_service()
        info = result["info"]
        userid = info['userid']
        return '&userid=' + str(userid)
    def username(self):
        result = self.login_service()
        info = result["info"]
        firstname = info['firstname']
        lastname = info['lastname']
        username = firstname + lastname
        return '&username=' + str(username)

    def login_status_code(self):
        return self.status_code()

    def login_cookies(self):
        return self.cookies()

    def login_cookie(self):
        return self.cookie()

    def add_cookie_header(self):
        return self.add_cookie(self.login_cookie())

if __name__ == '__main__':
    # lg_account = Login("login_by_account")
    lg_account = Login("login_de")
    # lg_vaild_country = Login("login_invaild_country")
    # lg_invaild_password = Login("login_invaild_password")
    # print(type(lg_account.login_service()))
    # print(lg_account.case_name)
    # print(lg_account.login_status_code())
    # print(lg_account.text())
    # print("*" * 30)
    # print(lg_invaild_password.login_service())
    # print(lg_account.login_cookies())
    # print(lg_account.login_cookie())
    # print(type(lg_account.login_cookie()))
    # print(lg_account.add_cookie_header())
    print(lg_account.login_service())
    # print(lg_account.login_cookie_service("getdeposit"))

