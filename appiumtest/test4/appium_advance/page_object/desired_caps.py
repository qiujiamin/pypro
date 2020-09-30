from appium import webdriver
import yaml
import logging
import logging.config
from selenium.common.exceptions import NoSuchElementException

CON_LOG = '../log/log.conf'
logging.config.fileConfig(CON_LOG)
# 采集器
logging=logging.getLogger()

def appium_desired():
    file = open('./desired_caps.yaml', 'r')
    data = yaml.load(file, Loader=yaml.FullLoader)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['noReset'] = data['noReset']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActicity'] = data['appActicity']
    desired_caps['ip'] = data['ip']
    desired_caps['port'] = data['port']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver
if __name__ == '__main__':
    appium_desired()
# def check_startBtn():
#     logging.info('check cancelBtn')
#
#     try:
#         cancelBtn = driver.find_element_by_id('android:id/button2')
#     except NoSuchElementException:
#         logging.info('no cancelBtn')
#     else:
#         cancelBtn.click()
# def check_startBtn():
#     logging.info("check_startBtn")
#     try:
#         start_Btn = driver.find_element_by_id('com.multilotto.lottery:id/tv_start')
#         # start_Btn = driver.find_element_by_xpath("//*[@class ='android.widget.TextView' and @index='3']")
#
#     except NoSuchElementException:
#         # print("no start_Btn")
#         logging.info('no start_Btn')
#     else:
#         start_Btn.click()
#         driver.implicitly_wait(2)