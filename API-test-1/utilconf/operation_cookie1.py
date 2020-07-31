#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import  requests
url = "http://m.imooc.com/passport/user/login"
data={
    "username":"15019498582",
    "password":"ssbx521qjm",
    "verify":"",
    "referer":"https://m.imooc.com"
}
res = requests.post(url,data).json()
response_url = res['dataconfig']['url'][0]
response_url = response_url+"&callback=jQuery210042712711583783314_1562582095923"
cookie = requests.get(response_url).cookies
# cookie = requests.utils.dict_from_cookiejar(cookie)
# print(cookie['apsid'])
url1 = "http://order.imooc.com/pay/submitorder?jsoncallback=jQuery210042712711583783314_1562582095923"
print(requests.get(url =url1,cookies =cookie).text)