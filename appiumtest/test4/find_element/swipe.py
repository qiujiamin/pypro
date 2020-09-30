#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from time import sleep
from test4.find_element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait

# 获取屏幕尺寸
def get_size():
    x= driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y
# 显示屏幕尺寸（width,height）
l = get_size()
print(l)
# 左滑
def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[1]*0.5)
    x2 = int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)
def swipeRight():
    l=get_size()
    y1 = int(l[1] * 0.5)
    x1 = int(l[0] * 0.25)
    x2 = int(l[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)
def swipeDown():
    l= get_size()
    x1 = int(l[0]*0.5)
    y1 = int(l[1]* 0.35)
    y2 = int(l[1]* 0.85)
    driver.swipe(x1,y1,x1,y2,1000)
def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)
driver.find_element_by_id('com.multilotto.lottery:id/radio_lotteries').click()
driver.implicitly_wait(3)
swipeLeft()
swipeDown()
swipeUp()
swipeRight()


# # 向左滑动两次
for i in range(4):
    swipeUp()
    sleep(0.5)


