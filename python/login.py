#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import sys
import json
import  requests
import datetime
import time
import urllib3,urllib
def login_android():
    # starttime = datetime.datetime.now()
    # start = time.clock()
    start = time.time()
    # url = "https://h5app-dev.multilotto.net/api/user/login"
    # print(url)
    url = "https://service.multilotto.net/api/user/login"
    data = {
        "pushproject": "curacao",
        "password": "Aa123456",
        # "email": "se90@gmail.com",
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
    header = {
            "accept": "*/*",
            "content-type": "application/json; charset=UTF-8",
            "content-length": "442",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.8.1",
            "XForwardedFor": "89.31.136.0",
            # "XForwardedFor": "217.227.25.30",
        }
    # header = {
    #     "Content-Length": "418",
    #     "Accept-Encoding": "gzip",
    #     "X-Forwarded-For": "89.31.136.0",
    #     "Host": "localhost:10288",
    #     "Connection": "close",
    #     "X-Forwarded-Proto": "https",
    #     "Cdn-Loop": "cloudflare",
    #     "Cf-Connecting-Ip": "89.31.136.0",
    #     "Cf-Ray": "4c09a00fee4b943f-AMS",
    #     "Cf-Ipcountry": "DE",
    #     "Content-Type": "application/json; charset=UTF-8"
    # }
    res = requests.post(url, data, header).json()
    print("android登录完成")
    usercheck = res['info']['usercheck']
    userid = res['info']['userid']
    # url1= 'https://h5app-dev.multilotto.net/api/user/accountcenter'
    # url2= 'https://h5app-dev.multilotto.net/api/user/logout'
    url1= 'https://service.multilotto.net/api/user/accountcenter'
    url2= 'https://service.multilotto.net/api/user/logout'
    data1 = {
        "useragent": "MI 6",
        "pushproject": "curacao",
        "platform": "4000",
        "osversion": "5.1.1",
        "remote_addr": "172.17.100.15",
        "version": "3.0.1",
        "resolution": "900x1600",
        "language": "SE",
        "pushid": "c7e0ae94-042b-415c-aaa3-6bbb02cf0d76",
        "subchannel": "10005",
        "uniq": "android_4fa2fa2d-d5eb-4498-9f6a-f1d66ad9e4c3_1573539888894",
        "userid":"",
        "usercheck":""
}
    data1['userid'] = userid
    data1['usercheck'] = usercheck

    res_accountcenter = requests.post(url1, data1, header).json()
    bonusid_list = res_accountcenter['info']['bonus']
    if len(bonusid_list) >2:
        print("可能有freeticket")
    else:
        print("个人中心还是那两个bonus")
    # if bonusid == 1552:
    #     print("有bonusid1552")
    res_logout = requests.post(url2, data1, header).json()
    # userinfolist = [usercheck, userid]
    # return userinfolist
    print('android退出')
    # endtime = datetime.datetime.now()
    # print((endtime - starttime).seconds)
    end = time.time()
    print(end - start)

def login_IOS():
    url = "https://h5app-dev.multilotto.net/api/user/login"
    data = {
		"access_token":"",
		"casinoversion":"3.0.0",
		"email":"se80@gmail.com",
		"external_identifier":"",
		"external_typeid":"",
		"hashstr":"",
		"language":"EN",
		"password":"Aa123456",
		"platform":"3000",
		"pushid":"a7b69ace-4b6d-49e4-8ef4-077c58a182b2",
		"pushproject":"curacao",
		"subchannel":"10004",
		"uniq":"D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
		"usercheck":"",
		"userid":"",
		"username":"",
		"version":"3.0.0"
		}
    header = {
            "accept": "*/*",
            "content-type": "application/json; charset=UTF-8",
            "content-length": "442",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.8.1",
            "XForwardedFor": "89.31.136.0",
            # "XForwardedFor": "217.227.25.30",
        }

    res = requests.post(url, data, header).json()
    print("IOS登录完成")
    usercheck = res['info']['usercheck']
    userid = res['info']['userid']
    url1= 'https://h5app-dev.multilotto.net/api/user/accountcenter'
    url2= 'https://h5app-dev.multilotto.net/api/user/logout'
    data1 = {
		"casinoversion":"3.0.0",
		"language":"EN",
		"platform":"3000",
		"pushid":"a7b69ace-4b6d-49e4-8ef4-077c58a182b2",
		"pushproject":"curacao",
		"subchannel":"10004",
		"uniq":"D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
		"usercheck":"",
		"userid":"",
		"username":"",
		"version":"3.0.0"
		}
    data1['userid'] = userid
    data1['usercheck'] = usercheck

    res_accountcenter = requests.post(url1, data1, header).json()
    bonusid_list = res_accountcenter['info']['bonus']
    if len(bonusid_list) >2:
        print("可能有freeticket")
    else:
        print("个人中心还是那两个bonus")
    # if bonusid == 1552:
    #     print("有bonusid1552")
    res_logout = requests.post(url2, data1, header).json()
    # userinfolist = [usercheck, userid]
    # return userinfolist
    print('IOS退出')

def online_android_login():
    url = "https://service.multilotto.net/api/user/login"
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
    header = {
        "accept": "*/*",
        "content-type": "application/json; charset=UTF-8",
        "content-length": "442",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.8.1",
        "X-Forward-For": "89.31.136.0",
        # "X-Forwarded-Proto": "https",
        # "Host": "localhost:10288"
        # "XForwardedFor": "217.227.25.30",
    }
    # header = {
    #     "Content-Length": "418",
    #     "Accept-Encoding": "gzip",
    #     "X-Forwarded-For": "89.31.136.0",
    #     "Host": "localhost:10288",
    #     "Connection": "close",
    #     "X-Forwarded-Proto": "https",
    #     "Cdn-Loop": "cloudflare",
    #     "Cf-Connecting-Ip": "89.31.136.0",
    #     "Cf-Ray": "4c09a00fee4b943f-AMS",
    #     "Cf-Ipcountry": "DE",
    #     "Content-Type": "application/json; charset=UTF-8"
    # }
    # ip = requests.getHeader("x-forwarded-for")
    # ip = urllib.request.urlopen(url)
    ip = requests.head(url)
    print("=====")
    print(ip)
    print("===")
    res = requests.post(url, data, header).json()
    print("android登录完成")
    print(res)
    usercheck = res['info']['usercheck']
    userid = res['info']['userid']
    print(usercheck)
    print(userid)
    # url1 = 'https://service.multilotto.net/api/user/accountcenter'
    # url2 = 'https://service.multilotto.net/api/user/logout'
    # data1 = {
    #     "useragent": "MI 6",
    #     "pushproject": "curacao",
    #     "platform": "4000",
    #     "osversion": "5.1.1",
    #     "remote_addr": "172.17.100.15",
    #     "version": "3.0.1",
    #     "resolution": "900x1600",
    #     "language": "SE",
    #     "pushid": "c7e0ae94-042b-415c-aaa3-6bbb02cf0d76",
    #     "subchannel": "10005",
    #     "uniq": "android_4fa2fa2d-d5eb-4498-9f6a-f1d66ad9e4c3_1573539888894",
    #     "userid": "",
    #     "usercheck": ""
    # }
    # data1['userid'] = userid
    # data1['usercheck'] = usercheck
    #
    # res_accountcenter = requests.post(url1, data1, header).json()
    # bonusid_list = res_accountcenter['info']['bonus']
    # if len(bonusid_list) > 2:
    #     print("可能有freeticket")
    # else:
    #     print("个人中心还是那两个bonus")
    # res_logout = requests.post(url2, data1, header).json()
    # print('android退出')
if __name__ == '__main__':
    # while 1:
    #     login_android()
    #     # login_IOS()
    # online_android_login()
    login_android()