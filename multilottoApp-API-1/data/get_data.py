from utilconf.operation_excel import OperationExcel
from data import data_config
from utilconf.operation_json import OperationJson
# 拿excel数据
class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    def get_case_lines(self):
        """
        获取excel行数，就是我们的case个数
        :return: case数
        """
        return self.opera_excel.get_lines()
    def get_case_id(self,row):
        """
        获取用例id（excel第一行）
        :param row: 行号
        :return: caseid
        """
        col = int(data_config.get_id())
        caseid= self.opera_excel.get_cell_value(row,col)
        return caseid
    # 获取casename,当前暂无用
    def get_case_name(self,row):
        col = int(data_config.get_case_name())
        casename= self.opera_excel.get_cell_value(row,col)
        return casename
    # 获取域名key，当前固定写死：dev python域名，dev h5app域名，线上python域名，线上h5app服务
    def get_domain(self,row):
        col = int(data_config.get_domain())
        domain_flag = self.opera_excel.get_cell_value(row,col)
        if domain_flag == 'dev_service':
            domain = 'https://h5app-dev.multilotto.net'
        elif domain_flag == 'dev_h5app':
            domain ='https://h5app-dev.multilotto.com'
        elif domain_flag == 'online_service':
            domain = 'https://service.multilotto.net'
        elif domain_flag =='online_h5app':
            domain = 'https://h5app.multilotto.net'
        else :
            print('域名错误或域名为空，将填充dev_service,请检查')
            domain = 'https://h5app-dev.multilotto.net'
        return domain
    # 获取请求路径
    def get_urlpath(self,row):
        col = int(data_config.get_url_path())
        urlpath = self.opera_excel.get_cell_value(row,col)
        return urlpath
    def request_url(self,row):
        """
        处理域名+路径，组合url
        :return: 请求url
        """
        domain = self.get_domain(row)
        urlpath = self.get_urlpath(row)
        request_url = domain+urlpath
        return request_url
    def get_is_run(self,row):
        """
        是否执行该用例
        :param row: 行号
        :return: yes（执行）；其他，不执行
        """
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self,row):
        """
         是否需要header.当前区分ios（当前写死）/安卓（当前写死）/write（暂未处理）/无
        :param row:
        :return:
        """
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row,col)
        # IOS
        iosHeader = {
        "AcceptLanguage": "zh-Hans-CN;q=1.0",
        "ContentType": "application/x-www-form-urlencoded;charset=utf-8",
        "AcceptEncoding"
        "": "gzip;q=1.0, compress;q=0.5",
        "User-Agent": "MultiLotto/2.6.1 CFNetwork/902.2 Darwin/17.7.0",
        "Accept": "/",
        "XForwardedFor": "89.31.136.0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d1c8a3cb521f1f4b72487b5dae55428f1545292386"
        }
        # andoid
        androidHeader = {
        "AcceptLanguage": "zh-Hans-CN;q=1.0",
        "ContentType": "application/x-www-form-urlencoded;charset=utf-8",
        "AcceptEncoding": "gzip;q=1.0, compress;q=0.5",
        "User-Agent": "okhttp/3.8.1",
        "Accept": "/",
        "XForwardedFor": "89.31.136.0",
        "Connection": "keep-alive",
        }
        if header == "iosHeader":
            return iosHeader
        elif header =="androidHeader":
            return androidHeader
        elif header =="write":
            # 需要写请求头的，到时候在主函数中处理，可能根据用例有实时性，暂不处理
            return header
        else:
            print("没有请求头")
            return None
    # 获取请求方式，仅区分post/get（当前未用到）
    def get_request_method(self,row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method
    def get_requestdata(self,row):
        """
        excel-data列，主请求参数，读取json文件处理。必填，尽量写key
        :param row:
        :return:
        """
        col = int(data_config.get_data())
        exceldata = self.opera_excel.get_cell_value(row, col)
        if exceldata == '':
            return None
        elif exceldata:
            opera_json = OperationJson()
            request_data = opera_json.get_data(exceldata)
            if request_data == None:
                print("当前使用excel中请求data")
                return exceldata
            return request_data
        else:
            print("请求数据格式可能出错了")
    def get_modifyrequestdata(self,row):
        """
        选填。将modifydata中变化值，添加到请求data中。用于同一用例多参数组合。
        :param row:
        :return:
        """
        col = int(data_config.get_modifydata())
        modifydata = self.opera_excel.get_cell_value(row,col)
        if modifydata =='':
            return None
        else:
            # 不在构造函数，而在这里实例化，因为有的data不需要json
            opera_json = OperationJson("../dataconfig/modifyrequestdata.json")
            modify_request_data = opera_json.get_data(modifydata)
            # 数据来源-excel，可直接调用
            if modify_request_data ==None:
                print("当前使用excel中请求modifydata")
                return modifydata
            return modify_request_data
    def opra_requestdata(self,row):
        """
        请求参数调用。
        :param row:
        :return:处理后的请求数据.如有modifyrequestdata，则当前条件需要requestdata有填写。
        """
        requestdata = self.get_requestdata(row)
        modifydata = self.get_modifyrequestdata(row)
        if requestdata !=None and modifydata != None:
            for key in modifydata.keys():
                    requestdata[key] = modifydata[key]
        return requestdata
##     获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        if expect =='':
            return None
        return expect
    # 写入结果
    def write_result(self,row,value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row,col,value)

#     获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key
# 判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_case_depend())
        depend_case_id= self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id
#         获取数据依赖字段
    def get_depend_field(self,row):
        # 等会要处理出列表
        col = int(data_config.get_field_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            if "#" in data:
                datalist = data.split("#")
                return datalist
            else:
                return data
    # 获取是否需要登录
    def get_needlogin(self,row):
        flag = None
        col = int(data_config.get_needlogin())
        needlogin = self.opera_excel.get_cell_value(row,col)
        if needlogin == 'yes':
            flag = True
        else:
            flag = False
        return flag
if __name__ == '__main__':
    data = GetData()
    print(data.get_data_for_json(1))





