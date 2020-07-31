import unittest
from waitingToOptmize.log import Log
# from MultilottoServiceInterface.PaymentService.getdeposit import Deposit
from MultilottoServiceInterface.OthersService.feedback import Feedback


class DepositTest(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.log.info("用户反馈用例测试开始")

    def test_get_feedback(self):
        feedback = Feedback("feedback_login_ios")
        result = Feedback.feedback_unlogin(False)
        # result1 = Feedback.feedback_login('feedback_login_ios')
        print(result)
        self.log.info("feedback 的status code为:" + str(feedback.status_code()))
        "断言 'CODE': '1'和deposit字段是否在响应里" + str(self.assertIn('"CODE": "1"', result))


    def tearDown(self):
        self.log.info("用户反馈用例测试结束")


if __name__ == '__main__':
    unittest.main().runTests()
