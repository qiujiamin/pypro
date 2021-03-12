#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from unittest import unittest


class TestMethod(unittest.TestCase):
    def test_01(self):
        print('testcase1')

    def test_02(self):
        print('testcase2')
if __name__ == '__main__':
    unittest.main()
