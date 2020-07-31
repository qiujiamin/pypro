# 字符串的切片，截取中间位置
# 字符串[开始索引：结束索引：步长]
# 列表和元组都是有序的集合，都能够通过 索引值获取到对应的数据
# 字典是一个无序的集合，是使用键值对保存数据
# 顺序：0 1 2 3 4
# 倒序 -1 -1
# 0 -1 无法截取到数据。如果要截取收尾，不要填写
num_list = [0,1,2,3,4,5]
num_tuple = (0,1,2,3,4,5)
fuhao_list = [",","%","#","^","&"]
t_str = "shduihsfhiucnhhferhfei"

# 字典不支持切片
str_dict = {"a":"z","b":"y","c":"x"}
print(num_list[0:4])
print(num_list[0:4:3])
print(num_tuple[0:4:3])
# print(str_dict[0:4]) 不可用

# 内置函数
"""
len(item) 计容器元素个数
del(item) 删除变量 del有两种方式：函数及关键字

"""

del num_list[1]
print(num_list)
del(num_list[1])
print(num_list)
print(max(t_str))
print(min(t_str))
print(min(num_list))
print(min(fuhao_list))
print(max(str_dict))
print(min(str_dict))

# B比较字符串
print("1"<"3")
print("aaaa"<"bbbb")
# 比较列表
print([1,1,1]<[2,2,2])
print((1,1,1)<(2,2,2))
# print({1:1,2:2}<{2:2,2:2})
# 字典只能针对key进行比较


# 算数运算符及对比列表追加方法
# print([1,2]+[3,4])
# print((1,2)+(3,4))
t_list = [1,2]
print(t_list.append(0))
print(t_list.append([8,9]))
t_list.extend([3,4])

print(t_list)

# print(t_list.append(1))



print(["H1!"*4])
print("a" not in "abcde")
print(3 in (1,2,3))
print(4 not in (1,2,3))
# print({1:1,2:2}<{2:2,2:2})
# in 找keyS
print("laowang" in {"a","laowang"})

print ([1,2]*2)
print ((1,2)*2)
# key 必须唯一

# print ({"1":"2"}*3)
# for  in
# 循环体
# else
# 没有通过break 退出循环，循环结束后，会执行的代码

for num in [1,2,3]:
    print(num)
    if num ==2:
        break
else:
    # 如果循环体内部使用break退出循环
    # else下方的代码就不会执行
    print("会执行么")
print("循环结束")
