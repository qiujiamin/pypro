#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from test4.find_element.capability import driver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# # 强制等待
# sleep(5)
#
# # 隐形等待
# # 全部元素设置一个等待时间
# driver.implicitly_wait(20)

# 显示等待
# 对特定元素进行等待
# WebDriverWait(driver,timeout=2,poll_frequency=0.5,ignored_exceptions=None)
# WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('elementID'))

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.multilotto.lottery:id/btn_login'))
driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()