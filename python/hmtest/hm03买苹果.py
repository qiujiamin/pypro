#!/usr/bin/python
#codeing=utf-8
import keyword
# import关键字，能把keyword加入工具包
print(keyword)
print(keyword.kwlist)

# 标识符区分大小写
# 起名套路：=号左右各保留两个空格
# 变量名由多个：梅哥单词使用小写，单词单词直接使用 下划线 first_name

# 驼峰命名法 userName FirstName

# 1、输入苹果单价
# price_str =float(input("苹果单价："))
#
# # 2、输入苹果重量
# weightstr = float(input("苹果重量："))
#
# # 计算支付的总金额
# money = price_str*weightstr
# print(money)

# 格式化字符串
# %f %d %s %%,变量之间用,号分隔
name ="大小明"
print("我的名字叫%s,请多多关照" %name)

studert_no = 10011
print("我的学号是 %06d" %studert_no)
#06表示位数，以0来占位，大于6位的照常输出
#%.2 表示小数点后线上2位
price = 8.5
weight = 7.5

money =price*weight
print("苹果单价 %.2f 元/斤，购买了 %.3f 斤，需要支付 %.4f 元" %(price,weight,money))

scale =0.25
# print("数据比例是%.2f%%" %scale *10)
# print中使用乘号，会将重复指令输出,处理方式是加括号
print("数据比例是%.2f%%" %(scale*100))

