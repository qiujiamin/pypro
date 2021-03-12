#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import unittest
from BSTestRunner import BSTestRunner
import time,logging
import sys
path='E:\\pypro\\appium_MultilottoAPP'
sys.path.append(path)

test_dir='../test_case'
report_dir='../reports'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_report.html'

with open(report_name,'wb') as f:
    runner = BSTestRunner(stram = f,title='multilotto Test Report',description=',multilottoApp test report')
    logging.info('start run test case...')
    runner.run(discover)
    # 用例执行顺序，按字母顺序