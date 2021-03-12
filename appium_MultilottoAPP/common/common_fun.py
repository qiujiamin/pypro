from  baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

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
            logging.info("close cancel btn")
            cancelBtn.click()

    def get_screenSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now
    def getScreenShot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
    def check_startBtn(self):
        logging.info("====================check_startBtn==================")
        try:
            start_Btn = self.driver.find_element(*self.startBtn)
        except NoSuchElementException:
            logging.info('no start_Btn')
        else:
            start_Btn.click()
            self.driver.implicitly_wait(2)
    def get_csv_data(self,csv_file,line):
        logging.info('========get_csv_data=======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index == line:
                    return row

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    com.startBtn()
    com.swipeLeft('startApp')

    # list1 = ["这", "是", "一个", "测试", "数据"]
    # for index, item in enumerate(list1):
    #     print(index, item)

    # def get_csv_data(csv_file,line):
    #     with open(csv_file,'r',encoding='utf-8-sig') as file:
    #         reader=csv.reader(file)
    #         for index,row in enumerate(reader,1):
    #             if index == line:
    #                 return row
    # csv_file = '../data/account.csv'
    # data = get_csv_data(csv_file,1)
    # print(data[0])
    # print(data[1])