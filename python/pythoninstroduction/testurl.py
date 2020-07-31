#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import urllib.request
# url="https://www.baidu.com/"
# file=urllib.request.urlopen(url)
# print('获取当前url:',file.geturl() )
# print('file.getcode,HTTPResponse类型:',file.getcode )
#
# print('file.info 返回当前环境相关的信息：' ,file.info())

url = "https://service.multilotto.net/api/user/login"
# file=urllib.request.urlopen(url)

data = {
        "pushproject": "curacao",
        "password": "Aa123456",
        "email": "jiamin.qiu+se@themultigroup.com",
        "userid": "",
        "uniq": "android_4fa2fa2d-d5eb-4498-9f6a-f1d66ad9e4c3_1573539888894",
        "useragent": "MI 6",
        "platform": "4000",
        "osversion": "5.1.1",
        "remote_addr": "172.17.100.15",
        "version": "3.0.1",
        "countryid": "EN",
        "resolution": "900x1600",
        "language": "EN",
        "pushid": "c7e0ae94-042b-415c-aaa3-6bbb02cf0d76",
        "subchannel": "10005",
        "usercheck": ""
    }
file = urllib.request.urlopen(url,data)
print('获取当前url:',file.geturl() )
print('file.getcode,HTTPResponse类型:',file.getcode )

print('file.info 返回当前环境相关的信息：' ,file.info())