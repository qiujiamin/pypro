#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import logging
from appium_advance.page_object.common_fun import Common
from appium_advance.page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):
    username_type = (By.ID,'')
