import logging
from appium_advance.page_object.common_fun import Common
from appium_advance.page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):
    # byxpath
    username_type = (By.ID,"//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']//*[@resource-id='com.multilotto.lottery:id/ev']")
    password_type = (By.ID,"//*[@resource-id='com.multilotto.lottery:id/ev_log_in_password']//*[@text='Password']")
    loginBtn = (By.ID,"com.multilotto.lottery:id/btn_login")

    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_startBtn()

        logging.info('================login_action================')
        logging.info('username id :%s' %username)
        username_ele = self.driver.find_element(*self.username_type)
        username_ele.clear()
        username_ele.sendkeys(username)

        logging.info('password is %s' %password)
        self.driver.find_element(*self.password_type).sendkeys(password)

        logging.info('click loginBtn')

        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished')
if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('de07@gmail.com','Aa123456')
