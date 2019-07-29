from MultilottoServiceInterface.userService.login import Login

class GetPaymentMethods(Login):

    lg = Login('login_by_account')

    def getpaymentmethods_service(self, result_type_is_str=False):
        return self.lg.login_cookie_service("getpaymentmethods", result_type_is_str)


if __name__ == '__main__':
    gp = GetPaymentMethods('getpaymentmethods')
    print(gp.getpaymentmethods_service())
