#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from find_element.capability import driver

driver.find_element_by_class_name("android.widget.EditText").send_keys('自学网2018')
driver.find_element_by_class_name('android.widget.EditText').send_keys('zxc111')
driver.find_element_by_class_name('android.widget.Button').click()