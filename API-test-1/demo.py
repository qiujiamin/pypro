#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import  requests
import json

# data ={
#     'username':'mushishi',
#     'password':'111111'
# }
# # headers = {"Content-Type": "application/x-www-form-urlencoded"}
# # res 发送了，默认的情况下会有信息返回
# res = requests.post(url='http://127.0.0.1:8000/login/',data=data)
# # print (type(res.text))
# # print (type(res.text))
# # print (type(res.json()))
# print(res)
# print(res.json())
# # 为什么不正常？res.json()? 导入json错误？

# # Post方法
# url = ' https://h5app-dev.multilotto.net/api/user/getcountryidbyip'
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
# url = ' 127.0.0.1:8000/login/'
# data ={
#     'username':'mushishi',
#     'password':'111111'
# }
# # get 方法
# url = 'https://h5app-dev.multilotto.net/en/terms-and-conditions?isH5=1?version=2.6.1'
# url = 'http://test.baidu.com/mark/task/getList?type=test'
url = 'http://www.imooc.com/m/web/shizhanapi/loadmore'
data ={
    'cart': '11',
}
# 封装

# def send_post(url,data):
#     res = requests.post(url=url, data=data).json()
#     print(res.json())
# send_post(url,data)
def send_get(url,data):
    res = requests.get(url=url,data=data).json()
    # 格式化处理：json.dumps(indent=None(默认none,前面空格，sort_keys，按abcd排序))
    return json.dumps(res,indent=2,sort_keys=True)
    # print(res.json())
print(send_get(url,data))









