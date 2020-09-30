#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import yaml
file = open('./familyInfo.yaml')
data = yaml.load(file,Loader=yaml.FullLoader)

print(data)
print(data['name'])
print(data['age'])

print(data['spouse'])

print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'][0]['name'])
print(data['children'][0]['age'])

print(data['children'][1]['name'])
print(data['children'][1]['age'])
# 不会修改文件
data['name'] = '5ffgg'
print(data['name'])

