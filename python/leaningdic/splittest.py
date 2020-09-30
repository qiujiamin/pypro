#! /usr/bin/env/python
# -*- coding:utf-8 -*-

str = "info.usercheck#info.userid#info.userhaha"
# print str.split( )
# for i in str:

# print(str)
if '#' in str:
    str_list = str.split("#")
    len = len(str_list)
    print(type(str_list))
    print(len)
    for listnum in str_list:
        print(listnum)
else:
    print('不需要分隔')
# i=0


# print (str.split('#',3))
# print