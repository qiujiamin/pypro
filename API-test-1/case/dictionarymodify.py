#! /usr/bin/env/python
# -*- coding:utf-8 -*-

dict1 = {'a':'1','b':'2','c':'3'}
dict2 = {'a':'4','b':'5','f':'7'}
print('字典1的值',dict1)
print('字典2的值',dict2)
for key in dict2.keys():
    dict1[key] = dict2[key]
print('dict1',dict1)
print('dict2',dict2)
