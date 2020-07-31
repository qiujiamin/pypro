#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from test4.find_element.capability import driver
import random


def random_str(slen=10):
    seed = "abcdefghijklmnopqrstuvwxyz"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)
signup_btn = driver.find_element_by_id('com.multilotto.lottery:id/btn_sign_up')
signup_btn.click()
random_numstr = str(random.randint(100,99999))
signup_email = "af"+random_numstr+"@gmail.com"

print(signup_email)

firstname = driver.find_element_by_xpath("//*[@text ='First Name']")
firstname.send_keys(random_str(4))

lastname = driver.find_element_by_xpath("//*[@text ='Last Name']")
lastname.send_keys(random_str(4))

email = driver.find_element_by_xpath("//*[@text ='E-mail address']")
email.send_keys(signup_email)

password = driver.find_element_by_xpath("//*[@text ='Password']")
password.send_keys("Aa123456")

country = driver.find_element_by_id('com.multilotto.lottery:id/tv_country')
country.click()
# list元素，结合下标
countrylist = driver.find_elements_by_class_name('android.widget.RelativeLayout')
# print(countrylist)
print(countrylist[4])
countrylist[4].click()

signup_Btn1 = driver.find_element_by_id('com.multilotto.lottery:id/btn_create_account')
signup_Btn1.click()
confirm_btn = driver.find_element_by_id('	com.multilotto.lottery:id/btn_dialog')
confirm_btn.click()



