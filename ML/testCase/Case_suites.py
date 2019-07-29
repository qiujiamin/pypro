import unittest
from testCase.testcase_login import Login
from testCase.testcase_login_null import LoginNull


class Suites(unittest.TestSuite):

    def addTest(self, test):
        self.addTest(test)

    def addTests(self, tests):
        self.addTests(tests)


if __name__ == '__main__':
    login_suc = Login("test_login")
    login_error = Login("test_login_error")
    login_null = LoginNull("test_login_null")
    suite = unittest.TestSuite()
    suite.addTest(login_suc)
    suite.addTest(login_error)
    suite.addTest(login_null)




