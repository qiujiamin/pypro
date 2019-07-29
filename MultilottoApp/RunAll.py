# -*- coding: utf-8 -*-
from result.testResult import TestResult
from testCase.testcase_login_null import LoginNull
from testCase.testcase_login import Login
from testCase.multilotto_get_config import TestML


def run():
    tests = [Login('test_login_error'), LoginNull('test_login_null'), TestML('testGetnearbyplace'), Login('test_login')]
    test_result = TestResult()
    test_result.suite.addTests(tests)
    #test_result.suite.addTest(Login('test_login'))
    test_result.get_html_report()
    #test_result.get_text_result()


run()
