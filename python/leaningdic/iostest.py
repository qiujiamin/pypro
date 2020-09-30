#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import sys
import json
import  requests
sys.path.append("D:\pypro\API-test-1")



class Test:

    def get_countryid(self):
        url = "https://h5app-dev.multilotto.net/api/user/getcountryidbyip"
        data = {
            "casinoversion":"3.0.0",
            "language":"EN",
            "platform":"3000",
            "pushid":""	,
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
            "accept-encoding": "gzip;q=1.0, compress;q=0.5",
            "accept-language":"zh-Hans-US;q=1.0, en-US;q=0.9",
            "user-agent": "MultiLotto/3.0.0 (com.multiLotto.lottery; build:3.0.1; iOS 11.4.1) Alamofire/4.7.3",
            "XForwardedFor": "89.31.136.0",
        }
        res = requests.post(url, data, header).json()
        print(res)
        countryid = res['info']['countryid']
        print(countryid)
if __name__ == '__main__':
    # 使用方法1
    coutryid =  Test()
    coutryid.get_countryid()
    # 使用方法2
    # loginuser = GetLogininfo()
    # userinfo = loginuser.get_logininfo_hardcode()
    # print(userinfo)
