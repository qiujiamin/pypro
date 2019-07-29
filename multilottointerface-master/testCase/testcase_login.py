import unittest
from MultilottoServiceInterface.userService.login import Login
import json
from common.log import Log
from MultilottoServiceInterface.userService.logout import LogOut


class LoginTest(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.log.info("登录测试开始")

    def test_login_suc(self):
        """登入测试用例!!!!"""
        lg_suc = Login('login_by_account')
        result = lg_suc.login_service()
        self.log.info("test_login_suc 登录的status code为:" + str(lg_suc.status_code()))
        "断言二：登录的国家是否是jp" + str(self.assertEqual(result['info']['countryid'], 'JP'))

    def test_login_invaild_password(self):
        """密码错误登录"""
        lg_invaild_password = Login("login_invaild_password")
        result = lg_invaild_password.login_service(True)
        self.log.info("test_login_invaild_password 登录的status code 为:" + str(lg_invaild_password.status_code()))
        "断言 是否是密码错误的提示：" + str(self.assertIn("password", result))

    def test_logout(self):
        """登出测试用例"""
        lgout = LogOut("logout")
        result = lgout.logout_service()
        self.log.info("test_logout 的status code 为： " + str(lgout.status_code()))
        "断言： 是否登出：" + str(self.assertEqual(result['CODE'], "1"))

    def tearDown(self):
        self.log.info('登录测试结束')


if __name__ == '__main__':
    unittest.main().runTests()
