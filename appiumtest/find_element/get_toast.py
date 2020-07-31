#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from find_element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait

# 登录email： com.multilotto.lottery:id/ev_log_in_email
root_email = driver.find_element_by_id('com.multilotto.lottery:id/ev_log_in_email')
email_edit = root_email.find_element_by_class_name('android.widget.EditText')
# id  com.multilotto.lottery:id/ev
email_edit.clear()
email_edit.send_keys('de07@gmail.com')
# 密码元素
root_password = driver.find_element_by_id('com.multilotto.lottery:id/ev_log_in_password')
# password_edit = root_password.find_element_by_name('Password') #失败了
password_edit = root_password.find_element_by_id('com.multilotto.lottery:id/ev')

# id  com.multilotto.lottery:id/ev
password_edit.send_keys('Aa123456')
driver.find_element_by_id('com.multilotto.lottery:id/btn_login').click()

error_message="用户名或密码错误，还可以尝试四次"
limit_message="验证失败次数过多，请15分钟后再试"

message='//*[@text=\'{}\']'.format(error_message)
# message='//*[@text=\'{}\']'.format(limit_message)

toast_element=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)