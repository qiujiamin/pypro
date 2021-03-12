from appium_advance.unittest.myunit import StartEnd
from appium_advance.page_object.loginView import LoginView
import unittest
import logging

class TestLogin(StartEnd):
    def test_login_multilotto_curacao(self):
        logging.info('======test_login_multilotto_curacao=======')
        l = LoginView(self.driver)
        l.login_action('jp07@gmail.com','Aa123456')
    def test_login_multilotto_MGA(self):
        logging.info('======test_login_multilotto_MGA=======')
        l = LoginView(self.driver)
        l.login_action('de07@gmail.com','Aa123456')

    def test_login_multilotto_error(self):
        logging.info('======test_login_multilotto_error=======')
        l = LoginView(self.driver)
        l.login_action('ddhdhsh@gmail.com','Aa123456')