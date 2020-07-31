#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import json,pickle #导入模块。
data = {
    'name' : "lixin",
    'sex' :"female",
    'height':1.58,
    'weight':82,
    'utterance':'奏是这么瘦,来打我啊'
}
jsondata = json.dumps(data) #转json数据
pythondata1 = json.loads(jsondata) #json数据转python
print(pythondata1)
pickledate = pickle.dumps(data)#转持久化数据
pythondata2 = pickle.loads(pickledate)#转回python
print(pythondata2)