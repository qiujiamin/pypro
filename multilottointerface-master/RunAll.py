# -*- coding: utf-8 -*-
from result.testResult import TestResult
from testCase.testcase_login import LoginTest
from testCase.testcase_deposit import *
from testCase.testcase_payment import *
from testCase.testcase_getinfo import *


def run():

    test_result = TestResult()
    # 把LoginTest类里面的testloginsuc,test_login_invaild_password用例加载到test1用例集中
    test_login = [LoginTest('test_login_suc'), LoginTest("test_login_invaild_password")] #LoginTest("test_logout")]
    test_deposit = [DepositTest("test_get_deposit")]
    test_info = [GetInfo("test_get_account_center"), GetInfo("test_get_countryid_by_ip"), GetInfo("test_get_near_by_places"), GetInfo("test_get_vaild_country")]
    test_payment = [Payment("test_get_payment_method")]
    test_result.suite.addTests(test_info)
    test_result.suite.addTests(test_deposit)
    test_result.suite.addTests(test_payment)
    test_result.suite.addTests(test_login)

    test_result.get_html_report()   #输出测试结果报告


run()
