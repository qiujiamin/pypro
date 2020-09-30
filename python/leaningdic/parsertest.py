
# https://www.cnblogs.com/wongbingming/p/6896886.html
from jsonpath_rw import parse

import  requests
dependata= "info.usercheck#info.userid"
url = "https://h5app-dev.multilotto.net/api/user/login"
data = {
	"pushproject": "curacao",
	"password": "Aa123456",
	"email": "de08@gmail.com",
	"userid": "",
	"uniq": "android_c5a219a3-9ee6-4b5f-9b18-c7dec9bc10f0_1570777588260",
	"useragent": "MI 6 ",
	"platform": "4000",
	"osversion": "5.1.1",
	"remote_addr": "172.17.100.15",
	"version": "3.0.0",
	"countryid": "EN",
	"resolution": "900x1600",
	"language": "EN",
	"pushid": "3679c083-b597-4112-b1bd-eced7d0f5b39",
	"subchannel": "10005",
	"usercheck": ""
}
header = {
    "accept":"*/*",
    "content-type":"application/json; charset=UTF-8",
    "content-length":"442",
    "accept-encoding":"gzip",
    "user-agent":"okhttp/3.8.1",
	"XForwardedFor": "89.31.136.0",
}
res = requests.post(url,data,header).json()
if '#' in dependata:
    depend_datalist = dependata.split("#")
    itemreslist=[]
    # depend_datalistlen = len(depend_datalist)
    for dpdata_item in depend_datalist:
        # json_exe = parse(dpdata_item)
        dpdata_item = parse(dpdata_item)
        print(dpdata_item)
        madle = dpdata_item.find(res)
        eachdata = [math.value for math in madle][0]
        itemreslist.append(eachdata)
        print(eachdata)
    print(itemreslist)
else:
    print("hahaha")
#
# male = dependata.find(res)
# item = [math.value for math in male][0]
# print(male)
# print(item)
# print(type(item))
# # ep
# from jsonpath_rw import jsonpath, parse
# json_obj = {"student":[{"male":176,"female":162},{"male":174,"female":159}]}
# jsonpath_expr = parse("student[*].male")
# print(type(jsonpath_expr))
# print(jsonpath_expr)
# male = jsonpath_expr.find(json_obj)



#         响应值为字符串，需要处理。根据层级关系去拿
#         json_exe = parse(depend_data)
#         madle = json_exe.find(response_data)
        # for i in madle: i是字段类型
        # i.value
        # course:[0]:out_trade_no
