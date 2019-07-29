import unittest
from common.log import Log
from MultilottoServiceInterface.OrderService.getpaymentmethods import GetPaymentMethods

class Payment(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.log.info("OrderService类用例测试开始")

    def test_get_payment_method(self):
        payment_method = GetPaymentMethods("getpaymentmethods")
        result = payment_method.getpaymentmethods_service(True)
        self.log.info("test_get_payment_method 的status code为:" + str(payment_method.status_code()))
        "断言 未传号码订单获取支付方式返回error" + str(self.assertIn("Verified lines with error", result))

    def tearDown(self):
        self.log.info("OrderService类用例测试结束")
