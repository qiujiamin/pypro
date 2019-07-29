import unittest
from common.log import Log
from MultilottoServiceInterface.userService.accountcenter import *
from MultilottoServiceInterface.userService.getcountryidbyip import GetCountryIdByIp
from MultilottoServiceInterface.userService.getnearbyplaces import GetNearByPlaces
from MultilottoServiceInterface.userService.getvaildcountries import GetVaildCountries


class GetInfo(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.log.info("获取信息测试用例开始")

    def test_get_account_center(self):
        account_center = AccountCenter("accountcenter")
        result = account_center.account_center_service()
        self.log.info("test_get_account_center 的status code为:" + str(account_center.status_code()))
        "断言 个人中心页username是否与登录账户一致" + str(self.assertEqual(result['info']['user_info']['firstname'], "dfdf"))

    def test_get_countryid_by_ip(self):
        getcountryid = GetCountryIdByIp("getcountryidbyip")
        result = getcountryid.countryidbyip_service(True)
        self.log.info("test_get_countryid_by_ip 的status code为:" + str(getcountryid.status_code()))
        "断言结果是否包含China " + str(self.assertIn("China", result))

    def test_get_near_by_places(self):
        getnearplace = GetNearByPlaces("getnearbyplaces")
        result = getnearplace.getnearbyplaces_service(True)
        self.log.info("test_get_near_by_places 的status code为:" + str(getnearplace.status_code()))
        "断言结果是否包含深圳市 " + str(self.assertIn("深圳市", result))

    def test_get_vaild_country(self):
        getvaildcountry = GetVaildCountries("getvalidcountries")
        result = getvaildcountry.vaildcountries_service(True)
        self.log.info("getvaildcountry 的status code为:" + str(getvaildcountry.status_code()))
        "断言结果是否包含深圳市 " + str(self.assertIn("popular", result)) #and str(self.assertIn("country: Germany", result))

    def tearDown(self):
        self.log.info("getinfo测试结束")


if __name__ == '__main__':
    unittest.main().runTests()
