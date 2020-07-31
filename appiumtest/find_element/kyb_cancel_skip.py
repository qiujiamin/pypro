#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['automationName']='uiautomator2'

desired_caps['app'] = r'E:\abak\mm_v3.1.1-2020-01-14-16-18.apk'
desired_caps['appPackage']='com.multilotto.lottery'
desired_caps['appActivity']='com.multilotto.lottery.module.splash.SplashActivity'

desired_caps['noReset']='False'
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(2)

def check_cancelBtn():
    print('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print('check skipBtn')
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
check_skipBtn()