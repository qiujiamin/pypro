#! /usr/bin/env/python
# -*- coding:utf-8 -*-
#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import  requests
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

print(res)
print(type(res))
usercheck = res['info']['usercheck']
userid = res['info']['userid']
print(usercheck)
print(userid)

# url1 = "https://h5app-dev.multilotto.com/en/touch/dashboard/mygames/active/?version=2.9.0"
url1 = "https://h5app-dev.multilotto.com/en/touch/dashboard/mygames/active?isH5=1"
# data1 = {}
# url1 = "https://h5app-dev.multilotto.com/en/touch/auth/applogin/"+userid+"/"+usercheck+"?url=touch/dashboard/mygames/active/&version=2.6.1"
# print(url1)
# res1 = requests.get(url1)
# print(res1)