#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['paltformName'] = 'Anddroid'
desired_caps['deviceName']= '127.0.0.1:62001'
desired_caps['platforVersion'] ='5.1.1'
desired_caps['automationName'] ='uiautomator2'

desired_caps['app'] = r'E:\abak\mm_v3.3.1-2020-07-28-10-08.apk'
desired_caps['appPackage'] ='com.multilotto.lottery'
desired_caps['appActivity']='com.multilotto.lottery.module.splash.SplashActivity'

desired_caps['noReset'] ='False'
desired_caps['unicodekeyboard'] = 'True'
desired_caps['resetkeyboard'] = 'True'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(2)

def check_startBtn():
    print("check_startBtn")
    try:
        start_Btn = driver.find_element_by_id('com.multilotto.lottery:id/tv_start')
    except NoSuchElementException:
        print("no staet_Btn")
    else:
        start_Btn.click()
def check_skipBtn():
    print('check skipBtn')
    try:
        # 待补充跳过的element
        skipBtn = driver.find_element_by_xpath()
    except NoSuchElementException:
        skipBtn.click()

def home_login_btn():
    print("check_loginBtn")
    try:
        login_Btn = driver.find_element_by_id('com.multilotto.lottery:id/btn_login')
    except NoSuchElementException:
        print("homepage no login_Btn")
    else:
        login_Btn.click()
check_startBtn()
home_login_btn()
