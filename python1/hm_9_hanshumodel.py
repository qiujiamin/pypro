# import hm_9_hanshu
from python1 import hm_9_hanshu与列表


# hm_9_hanshu.print_lines("-",5,20)

print(hm_9_hanshu与列表.name)

name_list = ["zhangshan","lisi","wangwu"]
print(name_list.index("wangwu"))
print(name_list[2])

# 修改
name_list[2]="liuliu"
print(name_list[2])
# 增加
name_list.append("wangxiaoer")
name_list.insert(1,"苏梅")
temp_list =["孙悟空","猪二哥","沙思娣"]
name_list.extend(temp_list)

print(name_list)
# 删除  remove pop clear方法  +delete关键字
# remove方法，可以从列表中删除数据
# name_list.remove("沙思娣")

# pop方法默认可以把最后一个去掉? 当前需要传index
name_list.pop() #去掉最后一个
# name_list.pop(1)

# clear 方法清空列表
# name_list.clear()
#提示：在日常开发中，要从列表中删除数据，建议使用列表提供的方法

# delete 使用del 关键字（delete）删除列表元素
# 本质上时用来将一个变量从内存中删除的
name ="小明"
del name
# 注意如果使用 del关键字将变量从内存中删除，后续的代码就不能再使用这个变量
del name_list[1]
print(name_list)