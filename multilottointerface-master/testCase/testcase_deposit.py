import unittest
from common.log import Log
from MultilottoServiceInterface.PaymentService.getdeposit import Deposit


class DepositTest(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.log.info("充值类用例测试开始")

    def test_get_deposit(self):
        deposit = Deposit("getdeposit")
        result = deposit.deposit_service(True)
        self.log.info("test_get_deposit 的status code为:" + str(deposit.status_code()))
        "断言 current_loss_limit和deposit字段是否在响应里" + str(self.assertIn("current_loss_limit", result) and self.assertIn("deposit_methods", result))

    def tearDown(self):
        self.log.info("充值类用例测试结束")


if __name__ == '__main__':
    unittest.main().runTests()
