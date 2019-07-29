
# while
"""
while 条件（判断 计数器是否达到 目标次数）：
    条件满足时，做事1
    条件满足时，做的事2
    条件满足时，做的事3
    处理条件（计数器+1）
"""
# 定义一个整数变量，记录循环次数
# i=0
#
# # 2开始循环
# while i< 3:
#     # 1、希望在循环内执行的代码
#     print("hello python")
#     # 2、处理计数器
#     i+=1
#     # 3、观察一下，循环结束后，计数器i的数值是多少
# print("循环结束后，i是%d" %i)
#

# 计算0-100之间的所有数字的累计求和
# i=0
# sum=0
# while(i<=100):
#     sum+=i
#     i+=1
# print("1-100和值是%d" %sum)
# 0-100所有偶数求和
# i=0
# sum=0
# while i<=100:
#     if i%2==0:
#         sum+=i
#     i+=1
# print("1-100的所有偶数求和为%d" %sum)

# break 某一条件满足时，退出循环，不再执行后续重复的代码
# i=0
# sum=0
# while i<10:
#     print(i)
#     sum+=i
#     i += 1
#     if(i%4==0):
#         break
#
# i=0
# while i<10:
#     if i==3:
#         break
#     print(i)
#     i+=1


# continue 某个条件不满足时，不执行后续重复的代码
# i=0
# while i<10:
#     if i==3:
#         i+=1
#         continue
#     #     注意：在循环中，如果使用continue这个关键字，
#     # 在使用关键字之前，需要确认循环的计数是否修改 否则可能造成死循环
#     print(i)
#     i += 1

# 循环嵌套
# 使用字符串运算直接输出小星星
# 连续输出五行，每一行星星一次递增
# 1、定义一个计数器变量,从数字1开始循环
# row=1
# while row <=5:
#     print("*" * row)
#     row+=1

# print函数的拓展：在输出内容后，自动输出一个换行
# print("*",end="")
# print("*")
# 如果不希望在末尾增加换行，可以在print函数输出内容的后面增加，end=""

# 使用循环嵌套输出小星星
# row =1
# while row<=5:
#     # 每一行要打印的星星，与当前的行数一致
#     # 增加一个小的循环，专门负责当前行中，每一列的星星显示
#     col = 1
#     while col<=row:
#         print("*",end="")
#         col+=1
#     print("")
#
#     row+=1

# 九九乘法表
row=1
while row<=9:
    col = 1
    while col <=row:
        # print("*",end="")
        print("%d*%d= %d"%(col,row,col*row),end=" ")
        col+=1
    # print("%d" %row)
    print("")
    row+=1


