#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from test4.find_element.capability import driver
login_Btn = driver.find_element_by_id('com.multilotto.lottery:id/btn_login')
login_Btn.click()
driver.implicitly_wait(3)