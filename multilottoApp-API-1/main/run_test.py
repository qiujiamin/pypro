from base.runmethod import RunMethod
from data.get_data import GetData
from utilconf.common_util import CommonUtil
from data.depend_data import DependentData
from utilconf.send_email import SendEmail
from utilconf.operation_json import OperationJson
from case.Login import GetLogininfo

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data=GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()
    # 程序执行的主入口
    def go_on_run(self):
        res = None
        # 基础邮件通知，统计成功及失败用例数
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url_path = self.data.get_urlpath(i)
            is_run = self.data.get_is_run(i)
            if is_run:
            # 对会登录注册用例特殊处理，与其他用例区分开。不管是否is_run，均会执行
                if url_path == '/api/user/login' or url_path =="/api/user/signup":
                    # 登录特殊处理，按表中数据执行，但当前暂时不会记录结果：遇到登录需要更新信息loginingo.json，提供给后续传入行号来调用。登录失败暂不处理，手势及其他第三方登录暂未知
                    print("本次登录/注册行号为 %d" % i)
                    # 自定义登錄方法在logininfo中修改
                    loginuser = GetLogininfo()
                    logininfo= loginuser.get_logininfo_byrow(i)
                    if logininfo ==None:
                        fail_count.append(i)
                        print("本次登录/注册失败")
                    else:
                        pass_count.append(i)
                        print("本次登录/注册成功.")
                else:
                    url = self.data.request_url(i)
                    print(i, url)
                    method = self.data.get_request_method(i)
                    request_data = self.data.opra_requestdata(i)
                    header = self.data.is_header(i)
                    expect = self.data.get_expect_data(i)
                    depend_case = self.data.is_depend(i)
                    needlogin = self.data.get_needlogin(i)
                    if needlogin:
                        # 其他非登录/注册用例，获取登录信息
                        loginjson = OperationJson('../dataconfig/logininfo.json')
                        logininfo = loginjson.get_data('logininfo')
                        # 如果logininfo有内容，说明是最新登录，直接读取
                        if logininfo['usercheck']:
                            request_data['usercheck'] = logininfo['usercheck']
                            request_data['userid'] = logininfo['userid']
                            request_data['email'] = logininfo['email']
                            request_data['verificationcode'] = logininfo['verificationcode']
                            # 如果遇到logout,需要清除logininfo，等待下一次登录/注册更新
                            if url_path == '/api/user/logout':
                                filepath_logininfo = '../dataconfig/logininfo.json'
                                print("本次退出清除登录信息，行号为 %d" % i)
                                for i in logininfo:
                                    logininfo[i] = ""
                                # logininfo['usercheck'] = ""
                                # logininfo['userid'] = ""
                                # logininfo['verificationcode'] = ""
                                # logininfo['email'] = ""
                                loginjson.write_data(filepath_logininfo, 'logininfo', logininfo)
                        # 如果logininfo无内容，则重新登录并写入json，这里调用的是固定的登录。也可以调用使用行号的登录，注意传入能登录的行号
                        elif logininfo['usercheck'] =="" :
                            # 登录如果没有信息，则重新登录并写入json文件
                            loginuser = GetLogininfo()
                            logininfo = loginuser.get_logininfo_hardcode()
                            request_data['usercheck'] = logininfo['usercheck']
                            request_data['userid'] = logininfo['userid']
                            print(request_data['usercheck'])
                            print("重新登录后的requestdata")
                            print(request_data)
                        else:
                            print("异常登录/注册")
                    if depend_case != None:
                        print("depend_case is"+" --- "+depend_case)
                        depend_data = DependentData(depend_case)
                            # 获取的依赖响应数据
                        print(i)
                        depend_response_data = depend_data.get_data_for_key(i)
                        print("依赖的响应数据")
                        print(depend_response_data)
                        if isinstance(depend_response_data, str):
                            depend_key = self.data.get_depend_field(i)
                            request_data[depend_key] = depend_response_data
                            print("本次有依赖用例的最终请求数据")
                            print(request_data)
                            print("只有一个依赖数据，以str处理")
                        elif isinstance(depend_response_data, list):
                            # list
                            depend_key_list = self.data.get_depend_field(i)
                            for item in range(len(depend_key_list)):
                                request_data[depend_key_list[item]] = depend_response_data[item]
                            print("依赖数据后的request_data")
                            print(request_data)
                        else:
                            print('依赖出错了')
                    try:
                        res = self.run_method.run_main(method, url, request_data, header)
                        # print(res)
                        if self.com_util.is_contain(expect, res):
                            print("测试通过")
                            self.data.write_result(i, 'pass')
                            pass_count.append(i)
                        else:
                            print("测试失败")
                            # self.data.write_result(i, 'fail')
                            self.data.write_result(i, res)
                            fail_count.append(i)
                    except IndexError as e:
                        print("该次请求出错了")
                        pass
        #             输入密码后再调用该行
        self.send_email.send_main(pass_count, fail_count)
        print(len(pass_count))
        print(len(fail_count))
if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
