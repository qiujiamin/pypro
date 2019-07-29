import keyword
# name_list =["张三","李四","王五","李四","刘六","周七"]
name_list =["zz","xx","bb","xs","ed","周七","1"]
# len(length 长度)函数可以统计列表中元素的总数
num_list =[6,8,9,1,2,10]
# count 方法可以统计列表中某个数据出现的次数
list_len = len(name_list)
print(name_list.__len__())
print("列表中包含 %d 个元素" %list_len)

count = name_list.count("李四")
print("李四有 %d 个"%count)

# 从列表中删除数据 ctrl Q
# name_list.remove("李四")


# 升序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)
# 降序
name_list.sort(reverse = True)
print(name_list)
num_list.sort(reverse = True)
print(num_list)
# 逆序
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)
# 关键字，函数与方法的区别
# 查看关键字 import keyword
# 关键字是python内置的，具有特殊含义的标识符。后面不需要使用括号
# 函数封装了独立的功能，可以直接调用
# 方法和函数类似，同样封装了独立的功能
# 函数名（参数）
# 方法可以通过对象调用，表示针对这个对象要做的操作
# 对象.方法名(参数)

# print(keyword)


# 列表的循环遍历
# 遍历就是从头到尾依次从列表中获取数据
# 在循环体内部，针对每一个元素，执行相同的操作
# python中为了提高列表的遍历效率，专门提供的迭代iteration遍历
# 使用for就能实现迭代遍历
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在my_name这个变量中，
在循环体内部可以访问到当前这次获取到的数据
列表常用功能：
1、列表存储相同类型的数据
2、通过迭代遍历。在循环体内部，真的列表中的每一项元素，执行相同的操作
"""
list=["zhangshan",1,1.72]
for my_name in name_list:
    print("我的名字叫 %s" %my_name)
# print(keyword.kwlist)
print(num_list)

