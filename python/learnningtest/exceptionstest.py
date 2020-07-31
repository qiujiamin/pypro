#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# try:
#     fileName = input("please input fileNanme: ")
#     open("%s.txt" %fileName)
# except FileNotFoundError:
#     print("%s.txt file not found" %fileName)
# try:
#     stu = 'jack'
#     print(stu)
# #     编译器已报错
# except NameError:
#     print("stu not define!")
try:
   stu = 'jack'
   print(stu)
except BaseException:
    print("stu not define!")