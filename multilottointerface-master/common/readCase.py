from common.readConfig import ReadConfig
from common.readExcle import ReadExcle
import json

class ReadCase:
    def __init__(self, excle_name, sheet_name):
        self.excle_name = excle_name
        self.sheet_name = sheet_name
        self.readConfig = ReadConfig()
        self.readExcle = ReadExcle(excle_name, sheet_name)

    def set_excle_name(self, excle_name):
        self.excle_name = excle_name

    def set_sheet_name(self, sheet_name):
        self.sheet_name = sheet_name

    def get_sheet_name(self):
        return self.sheet_name

    def get_excle_name(self):
        return self.excle_name

    """根据用例名称获取接口地址 ， 协议 +host + port + path"""
    def get_interface_url(self, case_name, is_online=True):
        if is_online:
            try:
                new_url = self.readConfig.get_ml_h5app('scheme') + '://' + self.readConfig.get_ml_h5app('host') + ":" + self.readConfig.get_ml_h5app('port') + self.get_path(case_name)
                return new_url
            except Exception as e:
                print(e)
                print("用例名称不存在2，或输入错误，请检查！！！")
        else:
            try:
                new_url = self.readConfig.get_http('scheme') + '://' + self.readConfig.get_http('host') + ":" + self.readConfig.get_http('port') + self.get_path(case_name)
                return new_url
            except Exception as e:
                print(e)
                print("用例名称不存在1，或输入错误，请检查！！！")

    def get_interface_data(self, case_name):
        try:
            for i in range(0, self.readExcle.nrows):
                row_value = self.readExcle.get_excle()[i][0]
                if case_name == row_value:
                    return self.readExcle.get_excle()[i][2]
        except Exception as e:
            print(e)
            print("data对应用例名称不存在，或输入错误，请检查！！！")

    def get_intetface_headers(self, case_name):
        try:
            for i in range(0, self.readExcle.nrows):
                row_value = self.readExcle.get_excle()[i][0]
                if case_name == row_value:
                    headers = self.readExcle.get_excle()[i][3]
                    headers_dict = json.loads(headers)
                    return headers_dict
        except Exception as e:
            print(e)
            print("Headers用例名称不存在，或输入错误，请检查！！！")

    """根据用例名称返回这个用例所对应的path路径"""
    def get_path(self, case_name):
        for i in range(0, self.readExcle.nrows-1):
            row_value = self.readExcle.get_excle()[i][0]
            if case_name == row_value:
                return self.readExcle.get_excle()[i][1]

    def get_method(self, case_name):
        try:
            for i in range(0, self.readExcle.nrows):
                row_value = self.readExcle.get_excle()[i][0]
                if case_name == row_value:
                    return self.readExcle.get_excle()[i][4]
        except Exception as e:
            print(e)
            print("Method对应用例名称不存在，或输入错误，请检查！！！")


if __name__ == '__main__':
    r = ReadCase('mltest.xlsx', '工作表1')
    print(r.readExcle.nrows)
    print(r.readExcle.ncols)
    print(r.readExcle.get_excle())
    #print(r.get_excle_name())
   # print(r.get_interface_data('getnearbyplaces'))
    # print(r.get_interface_data('login_error'))
   # print(r.get_interface_url('getnearbyplaces', True))
    #s = r.get_intetface_headers('getvalidcountries')
    print(r.get_interface_url('getcountryidbyip'))
    print(r.get_intetface_headers("getnearbyplaces"))
    print(r.get_interface_data("getnearbyplaces"))
    print(r.get_method("getnearbyplaces"))
    #print(s)
    #s1 = json.loads(s, encoding='utf-8')
    #print(type(s))
   # print()
   # print(type(s1))

