
"""
定义：单引号或双引号。尽量用双引号


"""

# str1 ="hello python hello hello"
# str2='我的外号叫"大西瓜"'
# print(str2)
# print(str1[6])

# for char in str2:
#     print(char)

#1、 统计字符串长度
# print(len(str1))
# 2、统计某个小字符串出现的次数
# print(str1.count("hel"))
# print(str1.count("yyy"))
# 大字符串的儿子，称为子字符串
# 3、某个子字符串出现的位置
#
# print(str1.index("llo"))
# print(str1.index("abc"))
# 不存在的会报错：valueerror

# 字符串的常用操作
# 字符串的转义：
# \t 制表符号，协助文本垂直对齐；\n 换行符  \\转义 \' 单引号 \"双引号 \r 回车
str3 = "hhhh"
# 1、判断类型
# space_str ="a1\t\n\r"
space_str ="aA"
# 判断空白字符
# print(space_str.isspace())
# print(space_str.isalnum())
# 判断数字:判断字符串中包含数字
# 这个三个，都不能判断小数；
# num_str = "1.1"
# unicode 字符串 后两个能判断
# num_str = "\u00b2"
# 中文数字 最后一个能判断
num_str = "一千零一"
print(num_str.isdecimal())
# 尽量使用这个
print(num_str.isdigit())
print(num_str.isnumeric())

# 2、查找和替换
# hello_str = "hello world"
# # 判断是否以该字符串开始
# print(hello_str.startswith("hello"))
# # 判断是否以指定字符串结束
# print(hello_str.endswith("world"))
# # 查找指定字符串
# # index 如果指定的字符串不存在，会报错
# # find如果指定的字符串不存在，会返回 -1
# print(hello_str.find("llo"))
# print(hello_str.find("abc"))
# # 替换字符串
# # replace方法执行完成之后，会返回一个新的字符串
# print(hello_str.replace("world","python"))
# print(hello_str)

# 3、字符串对齐
"""
假设：以下内容是从网络随意抓取的
要求：顺序并居中对齐，输出以下内容
"""
# poem = [
#     "\t\n登鹳雀楼",
#     "王之涣",
#     "白日依山尽",
#     "黄河入海流\t\n",
#     "欲穷千里目",
#     "更上一层楼"
# ]
# 中文空格，要全角
# 去除空白字符
# 先使用strip方法去除字符串中的空白字符
# 再使用center方法居中显示文本
# for poem_str in poem:
#     print("|%s|" %poem_str.strip().center(10,"　"))
    # print("|%s|" %poem_str.center(10,"　"))
#     print("|%s|" %poem_str.ljust(10,"　"))
#     print("|%s|" %poem_str.rjust(10,"　"))


# 字符串拆分及拼接

poem_str1= "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流\t\n 欲穷千里目\t\n 更上一层楼\t\n"


print(poem_str1)
# 拆分
poem_list = poem_str1.split()
print(poem_list)
# 合并
result = " ".join(poem_list)
print(result)

# 字符串的切片，截取中间位置
# 字符串[开始索引：结束索引：步长]
# 列表和元组都是有序的集合，都能够通过 索引值获取到对应的数据
# 字典是一个无序的集合，是使用键值对保存数据
# 顺序：0 1 2 3 4
# 倒序 -1 -1
# 0 -1 无法截取到数据。如果要截取收尾，不要填写
