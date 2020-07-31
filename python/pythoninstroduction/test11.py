#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import string
import copy
# a = [1]
# a= list(range(3))
# b = a
# print(a,b)
# print(id(a),id(b))
#
# a[0] = 3
# # print(a,b)
# print(id(a),id(b))
# a= [4]
# print(a,b)
# print(id(a),id(b))

# list1 = []
# print(list1)
# for i, x in enumerate(list1):
#     print(i, x)
# list1.append(2)
# print(list1)
# 即：空的list不能直接用角标赋值，会报错

# test
# 连接序列
# k={'a':'123','b':'456'}
# print('#'.join(k))
# a = ['1','3','4']
# print(''.join(a))
# # 大小写转换
# s= 'aaccNNm'
# print(s.lower())
# print(s.upper())

# c= [" ","11"]
c= "   aass  ff   "
# print(c.lstrip())
# print(c.rstrip())
print(c.strip())

# 格式化字符串
# a = "%d" %23.1
# print(a)
# 分隔成字符串
# b = '/sss/ddd/cccff/this-abc'
# b_arrays =b.split('/')
# print(b_arrays)

# l=['1',1.2,'hello']
# l1=['1','9','hello']
# print(l[1])
# print(l.pop())
# l1.sort()
# print(l1)
# l.reverse()
# print(l)
# l.remove('1')
# print(l)
# l.append('helloworld')
# print(l)
# # 字符串的
# s1 = 'asaa2jjj'
# # s1[0]='xx' 字符串不能这样赋值
# print(s1[3])
# print(s1)
# t = (1,2,3,['a','v','b'],'sss')
# # 元组不能这样赋值
# # t[0] =2
# # 元组中的列表下的元素可以赋值，因为列表元素存储的是地址
# t[3][0] ='cc'
# print(t)
# a1 =[1,2,3]
# a2 =a1.copy()
# print('a1,a2地址分别是%d %d ' %(id(a1),id(a2)))
# print(a2)
# a2[1]=22
# print(a2)
# print(a1)
#
# # 字典
# d = {}
# d['server'] = 'aliyun'
# d['client'] = 'android'
# d['list'] = [1,2,3]
# del d['list'][0]
# del d['server']


# print(d)

str_1='wo shi yi zhi da da niu/n'
str_list=list(str_1)
print(str_list)
nPos=str_list.index('/')
print(nPos)
str_list.insert(nPos,',')
print(str_list)
str_2="".join(str_list)
print(str_2)



