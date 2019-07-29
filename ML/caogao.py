import requests
import json
# GET请求参数
param = {'name': 'ide', 'city': 'New York'}
# 传递参数params
print(type(param))
param1 = json.dumps(param)
print(type(param1))
response = requests.get('http://httpbin.org/get',data=param1)
print(response.text)