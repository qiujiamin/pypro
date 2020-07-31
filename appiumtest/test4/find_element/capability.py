#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
# 模拟器设备-逍遥游模拟器
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['platforVersion']='7.1.2'
# 用于toast元素的识别
desired_caps['automationName']='uiautomator2'

desired_caps['app'] = r'E:\abak\mm_v3.3.1-2020-07-29-15-34.apk'
desired_caps['appPackage']='com.multilotto.lottery'
desired_caps['appActivity']='com.multilotto.lottery.module.splash.SplashActivity'

desired_caps['noReset']='True'
# 使用sendkey需要配置这两个
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)

def check_startBtn():
    print("check_startBtn")
    try:
        start_Btn = driver.find_element_by_id('com.multilotto.lottery:id/tv_start')
        # start_Btn = driver.find_element_by_xpath("//*[@class ='android.widget.TextView' and @index='3']")

    except NoSuchElementException:
        print("no start_Btn")
    else:
        start_Btn.click()
        driver.implicitly_wait(2)
def home_login_btn():
    print("check_loginBtn")
    try:
        login_Btn = driver.find_element_by_id('com.multilotto.lottery:id/btn_login')
        # login_Btn = driver.find_element_by_xpath('//*[@class="android.widget.Button" and @index="3"]')
        driver.implicitly_wait(3)
    except NoSuchElementException:
        print("homepage no login_Btn")
    else:
        login_Btn.click()
def login_page():
    print('loginpage')
    try:
        # 登录email： com.multilotto.lottery:id/ev_log_in_email
        # root_email = driver.find_element_by_id('com.multilotto.lottery:id/ev_log_in_email')
        # email_edit = root_email.find_element_by_class_name('android.widget.EditText')
        # email_edit = driver.find_element_by_xpath("//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText[@resource-id='com.multilotto.lottery:id/ev']")
        email_edit = driver.find_element_by_xpath("//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']//*[@resource-id='com.multilotto.lottery:id/ev']")
        # email_edit = driver.find_element_by_xpath(
        #     "//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']/following::android.widget.EditText[@resource-id='com.multilotto.lottery:id/ev']")

        # driver.implicitly_wait(3)
        email_edit.clear()
        email_edit.send_keys('de07@gmail.com')
        driver.implicitly_wait(2)
        print("email元素找到")
        # root_password = driver.find_element_by_id('com.multilotto.lottery:id/ev_log_in_password')
        # password_edit = root_password.find_element_by_xpath("//[@text='Password']")
        # password_edit = root_password.find_element_by_name('Password') #失败了
        # password_edit = root_password.find_element_by_id('com.multilotto.lottery:id/ev')

        password_edit = driver.find_element_by_xpath(
            "//*[@resource-id='com.multilotto.lottery:id/ev_log_in_password']//*[@text='Password']")
        password_edit.send_keys('Aa123456')
        driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()

        print("password元素找到")
    except NoSuchElementException:
        print("login page fail")
check_startBtn()
# home_login_btn()
# login_page()
# driver.quit()
