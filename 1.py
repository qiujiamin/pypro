#coding=utf-8
from selenium import  webdriver

dr = webdriver.Firefox()
# dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
input
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
dr.quit()