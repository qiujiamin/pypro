#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import unittest
class TestMethod(unittest.TestCase):
    # 只执行一次
    @classmethod
    def setUpClass(cls):
        print('类执行之前的方法\n')
    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法')
    # 每次方法之前执行
    def setUp(self):
        print('test-->setup')
    # 每次方法之后执行
    def tearDown(self):
        print('test-->teardown')
    def test_01(self):
        print('这个第1个是测试方法')
    def test_02(self):
        print('这个第2个是测试方法')
if __name__ == '__main__':
    unittest.main()
