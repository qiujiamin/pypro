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

def check_startBtn():
    print("check_startBtn")
    try:
        start_Btn = driver.find_element_by_id('com.multilotto.lottery:id/tv_start')
    except NoSuchElementException:
        print("no start_Btn")
    else:
        start_Btn.click()
def home_login_btn():
    print("check_loginBtn")
    try:
        login_Btn = driver.find_element_by_id('com.multilotto.lottery:id/btn_login')
    except NoSuchElementException:
        print("homepage no login_Btn")
    else:
        login_Btn.click()
def login_page():
    print('loginpage')
    try:
        # 登录email： com.multilotto.lottery:id/ev_log_in_email
        root_email = driver.find_element_by_id('com.multilotto.lottery:id/ev_log_in_email')
        email_edit = root_email.find_element_by_class_name('android.widget.EditText')
        # id  com.multilotto.lottery:id/ev
        email_edit.clear()
        email_edit.send_keys('de07@gmail.com')

        root_password = driver.find_element_by_id('com.multilotto.lottery:id/ev_log_in_password')
        # password_edit = root_password.find_element_by_name('Password') #失败了
        password_edit = root_password.find_element_by_id('com.multilotto.lottery:id/ev')

        # id  com.multilotto.lottery:id/ev
        password_edit.send_keys('Aa123456')
        driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()
    except NoSuchElementException:
        print("login page fail")
check_startBtn()
home_login_btn()
login_page()
