#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from MultilottoServiceInterface.BaseService import BaseService
from MultilottoServiceInterface.userService.login import Login

class  Feedback(BaseService):

    def feedback_unlogin(self, result_type_is_str=False):
        result = self.request_service(result_type_is_str)
        return result

    lg = Login("login_de")
    def feedback_login(self, reslut_type_is_str=False):

        return self.lg.login_cookie_service("feedback_login_ios",reslut_type_is_str)

if __name__ == '__main__':
    # feedback0 = Feedback('feedback_unlogin_IOS')
    # print(feedback0.feedback_unlogin('feedback_unlogin_IOS'))
    # 登录用户提交feedback
    feedback = Feedback('feedback_login_ios')
    print(feedback.feedback_login('feedback_login_ios'))
