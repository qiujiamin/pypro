import unittest
from common.readCase import ReadCase
from common.runmain import RunMain
import json


class Login(unittest.TestCase):


    def setUp(self):
        print("测试准备，比如链接数据库，获取配置文件内容等操作")
        case_excle = ReadCase('mltest.xlsx', '工作表1')
        self.login_url = case_excle.get_interface_url('login')
        self.login_data = case_excle.get_interface_data('login')
        self.login_headers = case_excle.get_intetface_headers('login')
        self.login_data_error = case_excle.get_interface_data('login_error')
        self.login_url_error = case_excle.get_interface_url('login_error')
        self.login_headers_error = case_excle.get_intetface_headers('login_error')

    def test_login(self):
        """登入测试用例!!!!"""
        result = RunMain().run_main('get', self.login_url, self.login_headers, self.login_data, True)   # r为str类型的返回结果
        s = json.loads(result)  # s为dict类型的返回结果
        print(type(result))
        print(type(s))
        ("断言一：结果是否包含200字段："+ str(self.assertIn(str(300), result)))
        ("断言二：结果msg信息是否是登录成功" + str(self.assertEqual(s['message'], '登录成功')))
        (self.assertEqual(s['code'], 200))

    def test_login_error(self):
        """登入错误的测试用例"""
        s = RunMain().run_main('get', self.login_url_error, self.login_headers_error, self.login_data_error)
        self.assertEqual(s['code'], -1)
        self.assertEqual(s['message'], '账号密码错误')

    def tearDown(self):
        print('测试结束123')


if __name__ == '__main__':
    unittest.main().runTests()
