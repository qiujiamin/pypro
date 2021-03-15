#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from common.myunit import StartEnd
from BusinessView.loginView import LoginView
import unittest
import logging

class LoginTest(StartEnd):
    csv_file = '../data/account.csv'

    # @unittest.skip('test_login_jp')
    def test_login_jp(self):
        logging.info('======test_login_jp======')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())
        # @unittest.skip('skip test_login_zxw2018')

    def test_login_zxw2018(self):
        logging.info('=========test_login_zxw2018============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

        # @unittest.skip("test_login_error")

    def test_login_erro(self):
        logging.info('=======test_login_erro=========')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus(), msg='login fail!')
if __name__ == '__main__':
    unittest.main()