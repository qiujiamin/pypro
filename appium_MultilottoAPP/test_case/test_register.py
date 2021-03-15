#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from common.myunit import StartEnd
from BusinessView.registerView import RegisterView
import logging
import random
import unittest

class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info('=======test_user_register=====')
        r= RegisterView(self.driver)

        username = 'jptest'+'fly'+str(random.randint(1000,90000))
        password = 'Aa123456.'
        email = 'appiumtest'+'cu'+str(random.randint(10000,90000))+'gmail.com'

        self.assertTrue(r.register_action(username,password,email))
if __name__ == '__main__':
    unittest.main()