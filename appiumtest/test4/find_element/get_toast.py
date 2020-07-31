#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# coding=utf-8
from test4.find_element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# # 首页登录按钮
# WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.multilotto.lottery:id/btn_login'))
# driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()
# 注册页面
def signup_page():
    print("注册页面")
    #     首页注册按钮
    driver.find_element_by_id('com.multilotto.lottery:id/btn_sign_up').click()
    #     注册页面
    driver.find_element_by_id('com.multilotto.lottery:id/btn_create_account').click()
    error_message = 'Invalid first name format'
    message = '//*[@text=\'{}\']'.format(error_message)
    toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
    print(toast_element.text)
# # 登录页面
# # def login_page():
# #     print('loginpage')
# #     try:
# #         # 登录email： com.multilotto.lottery:id/ev_log_in_email
# #         # root_email = driver.find_element_by_id('com.multilotto.lottery:id/ev_log_in_email')
# #         # email_edit = root_email.find_element_by_class_name('android.widget.EditText')
# #         # email_edit = driver.find_element_by_xpath("//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText[@resource-id='com.multilotto.lottery:id/ev']")
# #         email_xpath = "//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']//*[@resource-id='com.multilotto.lottery:id/ev']"
# #         # email_edit = driver.find_element_by_xpath("//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']//*[@resource-id='com.multilotto.lottery:id/ev']")
# #         WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath(email_xpath))
# #         email_edit = driver.find_element_by_xpath(email_xpath)
# #         # driver.implicitly_wait(3)
# #         email_edit.clear()
# #         email_edit.send_keys('de07@gmail.com')
# #         driver.implicitly_wait(2)
# #         print("email元素找到")
# #         password_xpath = "//*[@resource-id='com.multilotto.lottery:id/ev_log_in_password']//*[@text='Password']"
# #         WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath(password_xpath))
# #         # password_edit = driver.find_element_by_xpath(
# #         #     "//*[@resource-id='com.multilotto.lottery:id/ev_log_in_password']//*[@text='Password']")
# #         password_edit = driver.find_element_by_xpath(password_xpath)
# #         password_edit.send_keys('Aa123455')
# #         # 登录按钮
# #         driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()
# #
# #         # print("password元素找到")
# #     except NoSuchElementException:
# #         print("login page fail")
#
signup_page()