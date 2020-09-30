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
url = "https://h5app-dev.multilotto.net/api/user/login"
data = {
    "access_token": "",
    "casinoversion": "2.6.1",
    "email": "se20@gmail.com",
    "external_identiﬁer": "",
    "external_typeid": "",
    "hashstr": "",
    "language": "EN",
    "password": "Aa123456",
    "platform": "3000",
    "pushid": "a7b69ace-4b6d-49e4-8ef4-077c58a182b3",
    "pushproject": "curacao",
    "remote_addr": "192.168.22.151",
    "subchannel": "1004",
    "uniq": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE62",
    "usercheck": "",
    "userid": "",
    "username": "",
    "version": "2.6.1"
}
res = requests.post(url,data).json()

print(res)
# print("=====================")
usercheck = res['info']['usercheck']
userid = res['info']['userid']
print(usercheck)
# url1 = "https://h5app-dev.multilotto.com/en/touch/dashboard/mygames/active/?version=2.9.0"
# data1 = {}
url1 = "https://h5app-dev.multilotto.com/en/touch/auth/applogin/"+userid+"/"+usercheck+"?url=touch/dashboard/mygames/active/&version=2.6.1"
print(url1)
res1 = requests.get(url1)
print(res1)