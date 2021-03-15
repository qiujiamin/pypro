from utilconf.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from case.Login import GetLogininfo
from jsonpath_rw  import parse
import json
from utilconf.operation_json import OperationJson
class DependentData:
    def __init__(self,case_id):
        self.run_method = RunMethod()
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data =GetData()

    def get_case_line_data(self):
        """
        根据依赖caseid去获取该caseid整行数据
        :return:
        """
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
#     执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
#         拿到行号，获取get_data等需要行号获取
        row_num = self.opera_excel.get_row_num(self.case_id)
        print(row_num)
        # request_data = self.data.get_data_for_json(row_num)
        request_data = self.data.opra_requestdata(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.request_url(row_num)
        print(url)
        header = self.data.is_header(row_num)
        needlogin = self.data.get_needlogin(row_num)
        if needlogin:
            # 获取登录信息
            loginjson = OperationJson('../dataconfig/logininfo.json')
            logininfo = loginjson.get_data('logininfo')
            if logininfo['usercheck']:
                request_data['usercheck'] = logininfo['usercheck']
                request_data['userid'] = logininfo['userid']
                # print(request_data)
            else:
                # 登录如果没有信息，则重新登录
                loginuser = GetLogininfo()
                loginuser.get_logininfo_hardcode()
                logininfo = loginjson.get_data('logininfo')
                request_data['usercheck'] = logininfo['usercheck']
                request_data['userid'] = logininfo['userid']
                print(request_data)
        # if header == "write":
        #     res = self.run_method.run_main(method, url, request_data)
        #     op_header = OperationHeader(res)
        #     op_header.write_cookie()
        # elif header == 'yes':
        #     op_json = OperationJson('../dataconfig/cookie.json')
        #     cookies = op_json.get_data('header')
        #     # print(cookies)
        #     # cookie = ../dataconfig/cookie.json ../dataconfig/cookie.json
        #     res = self.run_method.run_main(method, url, request_data, cookies)
        #     # print(res)
        # else:
        #     res = self.run_method.run_main(method, url, request_data)
        res = run_method.run_main(method,url,request_data,header)
        print(res)
        return json.loads(res)
#     根据依赖的key去获取执行依赖测试case的响应，然后返回.
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        # print(depend_data)
        response_data = self.run_dependent()
        print(response_data)
        if '#' in depend_data:
            # 多个值以列表返回
            depend_datalist = depend_data.split("#")
            dpvaluelist = []
            for dpdata_item in depend_datalist:
                dpdata_item = parse(dpdata_item)
                madle = dpdata_item.find(response_data)
                eachdata = [math.value for math in madle][0]
                dpvaluelist.append(eachdata)
            return dpvaluelist
        else:
            # 一个值以字符串返回
            depend_data = parse(depend_data)
            print(depend_data)
            madle = depend_data.find(response_data)
            dpvaluestr = [math.value for math in madle][0]
            return dpvaluestr








