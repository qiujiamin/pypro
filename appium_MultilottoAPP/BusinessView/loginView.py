import logging
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginView(Common):
    # byxpath
    username_type = (By.ID,"//*[@resource-id='com.multilotto.lottery:id/ev_log_in_email']//*[@resource-id='com.multilotto.lottery:id/ev']")
    password_type = (By.ID,"//*[@resource-id='com.multilotto.lottery:id/ev_log_in_password']//*[@text='Password']")
    loginBtn = (By.ID,"com.multilotto.lottery:id/btn_login")

    # 打开时遇到弹框，待补充
    tip_commint= (By.ID,'')
    # 登录页校验元素
    button_myself= (By.ID,'')
    username= (By.ID,'')
    # 退出先点 me,menu,logout等按钮

    me_icon= (By.ID,'')
    menu_button= (By.ID,'')
    logout_button= (By.ID,'')
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
    def check_account_alert(self):
        # 假设打开时有弹框情况处理
        logging.info('==========check_account_alert===========')
        try:
            element = self.driver.find_element(self.tip_commint)
        except NoSuchElementException:
            pass
        else:
            logging.info('close tip_commit')
            element.click()
    def check_loginStatus(self):
        logging.info('=======check_loginStatus=======')
        self.check_account_alert()

        try:
            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login fail')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            logging.logout_action()
            return True
    def logout_action(self):
        logging.info('======logout_action======')
        self.driver.find_element(*self.me_icon).click()
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_button).click()
if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('de07@gmail.com','Aa123456')
    l.check_loginStatus()
