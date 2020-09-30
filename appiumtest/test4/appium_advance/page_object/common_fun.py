#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By

class Common(BaseView):
    cancelBtn = (By.ID,"android:id/button2")
    startBtn = (By.ID,'com.multilotto.lottery:id/tv_start')

    def check_cancelBtn(self):
        logging.info("================check cancelBtn======================")
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def check_startBtn(self):
        logging.info("====================check_startBtn==================")
        try:
            start_Btn = self.driver.find_element(*self.startBtn)
        except NoSuchElementException:
            logging.info('no start_Btn')
        else:
            start_Btn.click()
            self.driver.implicitly_wait(2)
if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    com.startBtn()

