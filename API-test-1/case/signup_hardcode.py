#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import  requests
# url = "http://m.imooc.com/passport/user/login"
# dataconfig={
#     "username":"15019498582",
#     "password":"ssbx521qjm",
#     "verify":"",
#     "referer":"https://m.imooc.com"
#
# }
url = "https://h5app-dev.multilotto.net/api/jsuser/signup"
data = {
	"pushproject": "lite",
	"password": "Aa123456",
	"source": "",
	"email": "ku19@gmail.com",
	"userid": "",
	"uniq": "android_7a4193a1-0462-44f7-b2c3-7a1ac0c9361d_1568707560122",
	"useragent": "MI 6 ",
	"platform": "4000",
	"osversion": "5.1.1",
	"country": "KR",
	"affiliatecode": "",
	"remote_addr": "172.17.100.15",
	"version": "2.9.2",
	"resolution": "900x1600",
	"language": "EN",
	"currency": "CAD",
	"pushid": "fb26b96a-53e2-40ff-b20d-1cbecff49b79",
	"subchannel": "10051",
	"usercheck": ""
}
header = {
    "accept":"*/*",
    "content-type":"application/json; charset=UTF-8",
    "content-length":"442",
    "accept-encoding":"gzip",
    "user-agent":"okhttp/3.8.1"

}
res = requests.post(url,data,header).json()
print(res)


# url1 = "https://h5app-dev.multilotto.com/en/touch/dashboard/mygames/active/?version=2.9.0"
# data1 = {}
# url1 = "https://h5app-dev.multilotto.com/en/touch/auth/applogin/"+userid+"/"+usercheck+"?url=touch/dashboard/mygames/active/&version=2.6.1"
# print(url1)
# res1 = requests.get(url1)
# print(res1)