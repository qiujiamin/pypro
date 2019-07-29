from MultilottoServiceInterface.userService.login import Login


class LogOut(Login):

    lg = Login('login_by_account')

    def logout_service(self):
        return self.lg.login_cookie_service("logout")


if __name__ == '__main__':

    gp = LogOut('logout')
    print(gp.logout_service())