#!/usr/bin/python
#codeing=utf-8
import random

# age = int(input("请输入年龄："))
# if age >=18:
#     print("可以到网吧嗨皮")
#     print("热烈欢迎！")
# else:
#     print("回家写作业")
# print("无论条件是否成立都会执行")
# # 逻辑运算符
# 与或非：and or not
# 定义证书变量age ，编写代码判断年龄是否正确：在【0-120】
# age = int(input("请输入年龄："))
# if age >=0 and age <=120:
#     print("您的年龄正常")
# else:
#     print("妖精")
# name = input("请输入姓名：")
# age=int(input("请输入年龄："))
# score = int(input("请输入score:"))
# if age>0 and age<120 and score>90:
#     print("%s，您的年龄是%d岁，分数是%score,很优秀" %(name,age,score))
# else:
#     print("不符合条件")
# python_score =int(input("请输入python的成绩："))
# c_score =int(input("请输入C语言的成绩："))
# if python_score>=60 and c_score >=60:
#     print("考试通过")
# else:
#     print("考试失败，继续努力")
# is_employee = True
# is_employee = False
# if not is_employee:
#     print("非本公司人员，请勿入内")
# 如果不是提示不允许入内
# 在开发中，通常希望在某个条件不满足时，执行一些代码，可以使用not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到

# elif

# holiday_name ="元旦";
# if holiday_name =="情人节":
#     print("玫瑰红酒香烛")
# elif holiday_name =="元旦":
#     print("跨年逛街")
# elif holiday_name =="国庆":
#     print("庆祝国家诞辰")
# else:
#     print("买礼物")

# 嵌套
# has_ticket = True
# knife_length =10
# if has_ticket:
#     print("车票检查通过，准备开始安检")
#     if knife_length>=30:
#         print("刀的长度是%d厘米,不允许上车" %knife_length)
#     elif knife_length >=20:
#         print("你携带的道具有%d公分，需要拿出来检查" %knife_length)
#     else:
#         print("安检已经通过，祝你旅途愉快 ")
#
# else:
#     print("大哥请先买票")

# 石头剪刀布

player = int(input("请输入您要出的拳 石头1/剪刀2/布3:"))
# computer = 1
computer = random.randint(1,3)
print("玩家选择的拳头是%d - 电脑出的拳是 %d" %(player,computer))
# 玩家胜利
if((player==1 and computer ==2)
        or (player==2 and computer==3)
        or (player==3 and computer==1)):

    print("欧耶，电脑弱爆了")
# 平局
elif player == computer:
    print("真是心有灵犀呀")
# 其他的情况就是电脑获胜
else:
    print("不服气，我们决战到天明")

