#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
# 模拟器设备-逍遥游模拟器
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['platforVersion']='7.1.2'

# 真机模拟--必须有udid
# desired_caps['platformName'] = 'MX4'
# desired_caps['platforVersion']= '5.1'
# desired_caps['udid'] = '750BBKL22GDN'

desired_caps['app'] = r'E:\abak\mm_v3.3.0-2020-07-16-11-40.apk'

desired_caps['appPackage'] = 'com.multilotto.lottery'
desired_caps['appActivity'] = 'com.multilotto.lottery.module.splash.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)