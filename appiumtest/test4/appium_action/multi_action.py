#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from appium import webdriver
from time  import sleep
from appium.webdriver.common.touch_action import  TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['platforVersion']='7.1.2'

desired_caps['app']=r'E:\abak\baiduditu.apk'
desired_caps['appPackage']='com.baidu.BaiduMap'
desired_caps['appActivity']='com.baidu.baidumaps.WelcomeScreen'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


# 同意按钮
# com.baidu.BaiduMap:id/ok_btn
# 跳过 ：com.baidu.BaiduMap:id/skip
# 新手引导：我知道了
# email_edit = driver.find_element_by_xpath("//*[@resource-id='android:id/content']//*[@text='知道了'])
# 弹窗关闭：com.baidu.BaiduMap:id/guide_close
driver.implicitly_wait(5)
driver.find_element_by_id('com.baidu.BaiduMap:id/ok_btn').click()
driver.implicitly_wait(3)
driver.find_element_by_id('com.baidu.BaiduMap:id/skip').click()
# driver.implicitly_wait(10)
# /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView
# "//*[@resource-id='android:id/content']//*[@text='知道了']"
# know = "//*[@resource-id='android:id/content']//*[@className = 'android.widget.TextView']"
# know = "//*[@resource-id='android:id/content']//*android.widget.RelativeLayout/android.widget.TextView]"
# know = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView"
know = "//*[@resource-id='android:id/content']//*[@text='知道了']"
WebDriverWait(driver,20).until(lambda x:x.find_element_by_xpath(know))
driver.find_element_by_xpath(know).click()
guide = 'com.baidu.BaiduMap:id/guide_close'
WebDriverWait(driver,10).until(lambda x:x.find_element_by_id(guide))
driver.find_element_by_id(guide).click()
x= driver.get_window_size()['width']
y = driver.get_window_size()['height']

def pinch():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x = x*0.2,y = y*0.2).wait(1000).move_to(x = x*0.4,y = y*0.4).wait(4000).release()
    action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000).release()

    print('start pinch...')
    zoom_action.add(action1,action2)
    zoom_action.perform()
def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()

    print('start zoom...')
    zoom_action.add(action1, action2)
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        pinch()
    for i in range(3):
        zoom()