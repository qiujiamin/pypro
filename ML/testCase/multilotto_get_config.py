import unittest
from testFile.readCase import ReadCase
from common.runmain import RunMain


class TestML(unittest.TestCase):

    def setUp(self):
        case_excle = ReadCase('mltest.xlsx', '工作表1')
        self.getnearbyplaces_url = case_excle.get_interface_url('getnearbyplaces', True)
        self.getnearbyplaces_data = case_excle.get_interface_data('getnearbyplaces')
        self.getnearbyplaces_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    def testGetnearbyplace(self):
        result = RunMain().run_main('get', self.getnearbyplaces_url, self.getnearbyplaces_headers, self.getnearbyplaces_data,True)
        "断言一：结果地址是否包含深圳市" + str(self.assertIn('Shenzhen', result))
       # "断言二: 结果地址是否包括深圳市12345" + str(self.assertIn('Shenzhen123', result))

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main().runTests()
