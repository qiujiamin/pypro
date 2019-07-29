from MultilottoServiceInterface.userService.login import Login


class Deposit(Login):

    # lg = Login("login_de")
    lg = Login("login_by_account")

    def deposit_service(self, reslut_type_is_str=False):
        return self.lg.login_cookie_service("getdeposit",reslut_type_is_str)


if __name__ == '__main__':
    dp = Deposit("getdeposit")
    print(dp.deposit_service())
