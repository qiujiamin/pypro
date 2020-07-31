#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from find_element.kyd_login import driver
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('元素id'))
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()