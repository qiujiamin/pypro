from MultilottoServiceInterface.userService.login import Login


class AccountCenter(Login):

    lg = Login('login_by_account')

    def account_center_service(self):
        return self.lg.login_cookie_service("accountcenter")


if __name__ == '__main__':

    gp = AccountCenter('accountcenter')
    print(gp.account_center_service())
