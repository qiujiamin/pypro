#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import  requests
import json

# Post方法
# url = 'https://h5app-dev.multilotto.net/api/user/getcountryidbyip'
# data ={
# 	"language": "EN",
#     "platform": "3000",
# 	"remote_addr": "13.230.65.62",
# 	"userid": "",
# 	"subchannel": "10004",
# 	"casinoversion": "2.7.0",
# 	"version": "2.7.0",
# 	"pushid": "a7b69ace-4b6d-49e4-8ef4-077 c58a182b2 ",
#     "usercheck ": "",
#     "username ": "",
#     "pushproject ": "curacao ",
#     "uniq ": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
# }
# 封装

# def send_post(url,data):
#     res = requests.post(url=url, data=data).json()
#     print(res.json())
# send_post(url,data)
# url = 'https://h5app-dev.multilotto.net/api/user/getcountryidbyip'
# data ={
# 	"language": "EN",
#     "platform": "3000",
# 	"remote_addr": "13.230.65.62",
# 	"userid": "",
# 	"subchannel": "10004",
# 	"casinoversion": "2.7.0",
# 	"version": "2.7.0",
# 	"pushid": "a7b69ace-4b6d-49e4-8ef4-077 c58a182b2 ",
#     "usercheck ": "",
#     "username ": "",
#     "pushproject ": "curacao ",
#     "uniq ": "D69DE874-EA21-40A7-8DA3-8FDE0BC5DE61",
# }
# url = 'http://test.baidu.com/mark/task/getList'
# data ={
#     'type':'test'
# }
# get方法
url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
data ={
    # 'cart':'11'
}

def send_post(url,data):
    res = requests.post(url=url,data=data).json()
    # print(res.json())
    # 格式化处理：json.dumps(indent=None(默认none,前面空格，sort_keys，按abcd排序))
    return json.dumps(res,indent=2,sort_keys=True)
def send_get(url,data):
    res = requests.get(url=url,data=data).json()
    return json.dumps(res,indent=2,sort_keys=True)
def runmain(url,method,data=None):
    res =None
    if method =='GET':
      res = send_get(url,data)
    else:
      res =  send_post(url,data)
    return res
# }
print(runmain(url,'GET'))
# print(send_get(url,data))
# send_post(url,data)









