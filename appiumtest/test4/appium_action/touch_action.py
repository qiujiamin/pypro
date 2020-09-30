#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from time import sleep
from test4.find_element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
# 个人中心 by id :com.multilotto.lottery:id/radio_me
# menu：com.multilotto.lottery:id/img_menu
# password设置 :com.multilotto.lottery:id/tv_my_lotto_games
# 手势密码开关：	com.multilotto.lottery:id/btn_gesture_switch
# 已设置弹窗：取消com.multilotto.lottery:id/btn_dialog_left
# 已设置弹窗：关闭 com.multilotto.lottery:id/btn_dialog_right
# com.multilotto.lottery:id/lockPatternView
# 按压：
# press(self, el=None, x=None, y=None)
#
# TouchAction(driver).press(x=0,y=308)

# 长按
# long_press(self, el=None, x=None, y=None, duration=1000)
# 点击
# tap(self, element=None, x=None, y=None, count=1)
# 暂停
# wait(self, ms=0)
# 释放
# release(self)
# 执行
# perform(self)
# 登录
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

# driver.save_screenshot('login.png')
# driver.save_screenshot('./images/login.png')
driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()

# 切换个人中心
driver.implicitly_wait(3)
driver.find_element_by_id("com.multilotto.lottery:id/radio_me").click()
driver.find_element_by_id("com.multilotto.lottery:id/img_menu").click()
# pattern login
# driver.find_element_by_id("com.multilotto.lottery:id/tv_my_lotto_games").click()
driver.find_element_by_id("com.multilotto.lottery:id/tv_cancel_withdraw").click()
WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.multilotto.lottery:id/btn_gesture_switch'))
driver.find_element_by_id("com.multilotto.lottery:id/btn_gesture_switch").click()
try:
    disable=driver.find_element_by_id("com.multilotto.lottery:id/btn_dialog_right")
except NoSuchElementException:
    pass
else:
    disable.click()
    driver.implicitly_wait(3)
    driver.find_element_by_id("com.multilotto.lottery:id/btn_gesture_switch").click()
# driver.find_element_by_id("com.multilotto.lottery:id/btn_gesture_switch").click()
driver.implicitly_wait(2)

for i in range(2):
     # x1 368 582
     # x2 716 582
     # x3:691 921
     TouchAction(driver).press(x=368,y=582).wait(2000)\
         .move_to(x=586,y=582).wait(1000)\
         .move_to(x=695,y=582).wait(1000) \
         .move_to(x=695,y=758).wait(1000) \
         .move_to(x=695,y=921).wait(1000)\
         .release().perform()
     # 退出按钮
driver.find_element_by_id("com.multilotto.lottery:id/img_menu").click()

quitBtn = driver.find_element_by_xpath("//*[@resource-id='com.multilotto.lottery:id/refresh_layout']//*[@resource-id=com.multilotto.lottery:id/img_bonus]")
quitBtn.click()
#      登录的一次
TouchAction(driver).press(x=364,y=507).wait(2000)\
         .move_to(x=527,y=507).wait(1000)\
         .move_to(x=699,y=507).wait(1000) \
         .move_to(x=699,y=674).wait(1000) \
         .move_to(x=699,y=841).wait(1000)\
         .release().perform()




