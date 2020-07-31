from test4.find_element.capability import driver
# 首页登录按钮
# by id:
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().resourceId("com.multilotto.lottery:id/btn_login")').click()
# driver.implicitly_wait(3)
# by text
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("Log in")').click()
# # by classname
# driver.find_element_by_android_uiautomator\
#     ("new UiSelector().className('android.widget.Button')")
# 登录页id
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().resourceid("com.multilotto.lottery:id/ev_log_in_email")').send_keys('de07@Gmail.com')
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector')
