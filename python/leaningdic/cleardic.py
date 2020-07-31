#! /usr/bin/env/python
# -*- coding:utf-8 -*-
a = {"logininfo": {"usercheck": "111", "userid": "333", "verificationcode": "555"}}
print(a)
print("-------------")
# a = a['logininfo'].clear()
for i in a['logininfo']:
    a['logininfo'][i] = ""
print(a)
