
#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import requests,json
# post请求-安卓登录
url = "https://h5app-dev.multilotto.net/api/user/login"
headers = {
    'accept':'*/*',
    'content-type':'application/json; charset=UTF-8',
    'content-length':'400',
    'accept-encoding':'gzip',
    'user-agent':'okhttp/3.8.1'
}
request_param = {
	"pushproject": "curacao",
	"password": "Aa123456",
	"email": "nde05@gmail.com",
	"userid": "",
	"uniq": "android_4ff1bf2d-03f4-4938-8dba-cc7eff359444_1567411144203",
	"useragent": "MI 6 ",
	"platform": "4000",
	"osversion": "5.1.1",
	"remote_addr": "172.17.100.15",
	"version": "2.9.1",
	"countryid": "EN",
	"resolution": "900x1600",
	"language": "EN",
	"pushid": "1690137a-a583-4155-86a8-e6db370f3ab1",
	"subchannel": "10005",
	"usercheck": ""
}
response = requests.post(url,data =json.dumps(request_param),headers=headers)
# print(response.text)
print("---------------")
print(response.json()['info']['usercheck'])
print("---------------")

# get请求-获取powerball某期开奖结果
url1 = "https://h5app-dev.multilotto.net/en/lotto-results/usa-powerball/2019-09-07?isH5=1&version=2.9.1"
headers1 = {
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Linux; Android 5.1.1; MI 6  Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Google-Apps-Script',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding':'gzip, deflate',
    'accept-language':'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'x-requested-with':'com.multilotto.lottery',
}

response1 = requests.get(url1,headers=headers1)
print(response1.text)
# print(response1.text)