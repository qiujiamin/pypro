#!/usr/bin/python
#codeing=utf-8
# 变量
# price = 8.5
# weight =7.5
# money = weight* price
#
# # 返回5元
# money = money-5
# print(money)
# 变量类型
# 在python中，定义变量是不需要制定变量类型的
# 在运行的时候，python解释器，会根据赋值语句等号右侧的数据，
# 自动推倒出变量只能保存数据的准确类型
# str,bool,int,float
name ='小明'
age = 18
gender =True
height = 1.75
weight =60
mi = 2**64
print(type(name))
print(mi)
print(type(mi))
print(name,age,gender,height,weight)
# 不同变量的计算
# 数字型可以直接计算，true以1参数，false以0计算
shuzi = age+gender+height
shuzi1 = age-gender-height
print(shuzi)
print(shuzi1)
# 拼接字符串
firstname ="三"
lastname ="张"
print(firstname*2+lastname+'是一个好孩子')
# 数字型与非数字型无法计算
# 变量的输入
# input("请输入银行密码：")
# 类型转换
# float()
# int("123")
# age=int(input("请输入一个整数:"))
# print(age)
# print(type(age))
# 买苹果综合版本

# 循环
# for i in range(1,10):
#     print(i)
# range(start,end,scan)
# for i in range(1, 10,2):
#         print(i)
# 数组
shuzu =[1,2,3,'a',5]
print(shuzu)
print(shuzu[2])
# 字典
zidian = {"password":"111222","gender":"man","age":"56"}
print(zidian.keys())
print(zidian.values())
print(zidian.items())
print(type(zidian))
print(type(shuzu))
# 函数
def add(a,b):
    print(a+b)
add(3,5)