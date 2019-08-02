#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import unittest
import io
from demo2 import RunMain
import HTMLTestRunner
import json
import time
import os
import mock


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
    def test_01(self):
        url = 'https://h5app-dev.multilotto.net/api/user/getcountryidbyip'
        data ={
            	"language": "EN",
                "platform": "3000",
            	"remote_addr": "13.230.65.62",
            	"userid": "",
            	"subchannel": "10004",
            	"casinoversion": "2.7.0",
            	"version": "2.7.0",
            	"pushid": "a7b69ace-4b6d-49e4-8ef4-077 c58a182b2 ",
                "usercheck ": "",
                "username ": "",
                "pushproject ": "curacao ",
                "uniq ": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
            }
        # mock模拟这个返回值
        print('----------------------')
        mock_data = mock.Mock(return_value =data)
        # print(mock_data)
        print('----------------------')
        self.run.runmain = mock_data

        res = self.run.runmain(url,'POST',data)
        print(res)
        # print('----------------')
        # print(type(res))
        # # print(res['CODE'])
        # print('----------------')
        self.assertEqual(res['CODE'],'1',"测试失败")
        # 设置全局变量
        # globals()['userid']='100099'
        print('这是第一个case')
    # def test_02(self):
    #     # 使用别的用例返回的数据，但不推荐
    #     # print(self.userid)
    #     # print(userid)
    #     url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
    #     dataconfig = {
    #     'cart':'11'
    #     }
    #     res = self.run.runmain(url,'GET')
    #     # print(res)
    #     self.assertEqual(res['dataconfig']['errorCode'],1006,"测试失败")
    #     print("这是第二个case")

if __name__ == '__main__':
    # 1、获取当前时间，这样便于下面的使用。
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 2、html报告文件路径
    filepath = "../report/htmlReport.hmtl"
    # report_abspath = os.path.join(filepath, "result_" + now + ".html")
    # 创建资源流
    fp = open(filepath, 'wb')
    # 创建一个容器
    suite = unittest.TestSuite()
     # 往容器中添加case
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
#     结合htmllrunner及report
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
#     执行
    runner.run(suite)
    fp.close()

