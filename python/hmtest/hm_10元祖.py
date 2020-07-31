# tuple
# 元祖与列表类似，不同之处在于元祖的元素不可修改
"""
元组表示多个元素组成的序列
元组在ptrhon开发中，有特定的应用场景
用于存储一串信息，数据之间使用 ，分隔
元组用()定义
元组的索引从0开始

"""
info_tuple =("zhangshan",18,1.75)
print("%s 年龄是 %d 身高是 %.2f" %info_tuple)
# 使用格式化字符串，可以使用 一个元组，来拼接字符串
info_str ="%s 年龄是 %d 身高是 %.2f" %info_tuple
print(info_str)
print(type(info_tuple))
print(info_tuple[1])
# 在开发时，一般不会定义空元组
empty_tuple=()
print(type(empty_tuple))
# 一个元素的元组,需要加逗号
single_tuple =(5,)
print(type(single_tuple))

# 取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangshan"))

# 统计计数
print(info_tuple.count("zhangshan"))
print(len(info_tuple))

# 使用迭代遍历元组
for my_info in info_tuple:
    # 使用格式字符串
    print(my_info)

# 格式化字符串的后面的"()"，本质上时元组
print("%s 年龄是 %d 身高是 %.2f" %("小明",18,1.75))

# 元组与列表之间的转换
num_list =[1,2,3,4]
print(type(num_list))
num_tuple = tuple(num_list)
print(type(num_tuple))
num2_list = list(num_tuple)
print(type(num2_list))
