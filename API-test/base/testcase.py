#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import unittest
import io
from demo2 import RunMain
import HTMLTestRunner
import json
import time
import os
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
        # 这种方法虽然可以，但如果参数较多，则不可行；且case间是相互独立的，不应该这么操作
        # self.userid =self.test_01(

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
        # self.userid=10002
        # run = RunMain()
        # res = self.setUp() 当前问题，只能这样调用，不能传参？
        # 要在setup中也加self

        res = self.run.runmain(url,'POST',data)
        print(res)
        print('----------------')
        print(type(res))
        # print(res['CODE'])
        print('----------------')
        self.assertEqual(res['CODE'],'1',"测试失败")
        # 设置全局变量
        # globals()['userid']='100099'
        #TO DO
        # 这个报错我暂不知
        # print(userid)
        print('这是第一个case')
        # 跳过执行某个用例
    # @unittest.skip('test_02')

        # 返回到setup中，给其他用例用--但不推荐
        # return self.userid

        # self.assertNotEqual()
        # self.assertTrue()
        #
        # if res['CODE'] == '1':
        #     print('testcase1 测试通过')
        # else:
        #     print('testcase1 测试失败')

        # unitest中，会按字母顺序来执行的，所以要注意执行顺序
    def test_02(self):
        # 使用别的用例返回的数据，但不推荐
        # print(self.userid)
        # print(userid)
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
        data = {
        'cart':'11'
        }
        res = self.run.runmain(url,'GET')
        # print(res)
        self.assertEqual(res['data']['errorCode'],1006,"测试失败")
        print("这是第二个case")

if __name__ == '__main__':
    # 执行所有的testcase
    # unittest.main()
#     其他方式的执行方法？
#     文件创建一个放报告的位置及文件
    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 2、html报告文件路径

#     report_path = os.path.join(os.getcwd(), "report.html")
    filepath = "../report/"
    report_abspath = os.path.join(filepath, "result_" + now + ".html")

    # 创建资源流
    # python2的写法
    # fp = file(filepath,'wb')
    # python3的写法
    fp = open(report_abspath, 'wb')
    # fp = open(report_abspath, 'wb')

# # 创建一个容器
    suite = unittest.TestSuite()
#     # 往容器中添加case
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
#     结合htmllrunner及report
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
#     执行
#     unittest.TextTestRunner().run(suite)
    runner.run(suite)
    fp.close()

