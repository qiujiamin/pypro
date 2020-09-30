#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from test4.find_element.capability import driver

# # save_screenshot直接保存当前屏幕截图到当前脚本所在文件位置
# driver.save_screenshot('login.png')
# # 方法2：get_screenshot_as_file(self,filename)
# # 将截图保留到指定文件路径
# driver.get_screenshot_as_file('./images/login.png')
# 首页登录按钮
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

driver.save_screenshot('login.png')
driver.save_screenshot('./images/login.png')
driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()

