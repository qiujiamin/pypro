import unittest
from common.readCase import ReadCase
from common.configHttp import ConfigHttp
import json
from common.log import Log


class LoginNull(unittest.TestCase):

    def setUp(self):
        self.log = Log()
        self.log.info('loginnull测试开始')
        case_excle = ReadCase('mltest.xlsx', '工作表1')
        self.login_url_null = case_excle.get_interface_url('login_null')
        self.login_data_null = case_excle.get_interface_data('login_null')
        self.login_headers_null = case_excle.get_intetface_headers('login_null')

    def test_login_null(self):
        result = ConfigHttp().run_main('get', self.login_url_null, self.login_headers_null, self.login_data_null, True)
        # result为str类型的返回结果
        s = json.loads(result)  # s为dict类型的返回结果
        print(result)
        ("断言一：结果是否包含200字段：" + str(self.assertIn(str(10001), result)))
        ("断言二：结果msg信息是否是登录成功" + str(self.assertEqual(s['message'], '参数不能为空！')))
        (self.assertEqual(s['code'], 10001))

    def tearDown(self):
        print('login null测试结束')


if __name__ == '__main__':
    unittest.main().runTests()
