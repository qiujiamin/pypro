#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from test4.find_element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait
import yaml

login_Btn = driver.find_element_by_id('com.multilotto.lottery:id/btn_login')
login_Btn.click()
driver.implicitly_wait(3)

print('loginpage')
email_edit = driver.find_element_by_xpath("//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']//*[@resource-id='com.multilotto.lottery:id/ev']")
email_edit.clear()
email_edit.send_keys('de07@gmail.com')
driver.implicitly_wait(2)
password_edit = driver.find_element_by_xpath(
            "//*[@resource-id='com.multilotto.lottery:id/ev_log_in_password']//*[@text='Password']")
password_edit.send_keys('Aa123456')
driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()
print("登录完成")
driver.implicitly_wait(3)

driver.implicitly_wait(2)
print("点击个人中心")
driver.find_element_by_id("com.multilotto.lottery:id/radio_me").click()

# 提现按钮，点击进去就是h5网页
# driver.find_element_by_id("com.multilotto.lottery:id/btn_withdraw").click()
# driver.find_element_by_id("com.multilotto.lottery:id/tv_active_game").click()
# active_game，点进去就是h5页面
driver.implicitly_wait(2)
driver.find_element_by_id("com.multilotto.lottery:id/tv_active_game_desc").click()

ele_group = "//*[@resource-id='body']//*[@text='Group Play']"
contexts=driver.contexts
print(contexts)
driver.switch_to.context('WEBVIEW_com.multilotto.lottery')
# https://h5app-dev.multilotto.com/en/touch/dashboard/mygames/active?isH5=1
# WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.multilotto.lottery:id/webview_top'))
WebDriverWait(driver,30).until(lambda x:x.find_element_by_xpath(ele_group))
driver.find_element_by_xpath(ele_group).click()
driver.switch_to.context('NATIVE_APP')
# print('switch conetext')
# contexts=driver.contexts
# ['NATIVE_APP', 'WEBVIEW_chrome', 'WEBVIEW_com.multilotto.lottery']
# print(contexts)
# driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
# print('edit email')
# email_edit = driver.find_element_by_xpath(
#     "//*[@resource-id='body']//*[@text='Group Play']")
