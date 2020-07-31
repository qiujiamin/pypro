#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from find_element.capability import driver

lotteries_btn = driver.find_element_by_id('com.multilotto.lottery:id/radio_lotteries')
lotteries_btn.click()

lotto_pw = driver.find_element_by_xpath('//*[@text="powerball"]')
lotto_pw.click()
