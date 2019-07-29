"""
列表是有序的对象集合
字典是 无序的对象集合
字典使用 键值对 存储数据，键值对之间使用 ， 分隔
键：key 是索引
值:value 是数据
键必须是唯一的
值可以是任何数据类型，但键只能使用 字符串，数字或元组
键和值之间使用:分隔
"""
# xiaoming_dict ={"name":"小明",
#            "age":18,
#            "height":1.75,
#            "weight":75.5
#            }
xiaoming_dict ={"name":"小明",
                "age":12}

print(xiaoming_dict)
# 1.、统计键值对数量
print(len(xiaoming_dict))

#合并字典
temp_dict ={"height":1.75,"age":20}
xiaoming_dict.update(temp_dict)
# 注意：如果被合并的字典中，包含已经存在的键值对，会覆盖原来的键值对

print(xiaoming_dict)

# 1.取值
print(xiaoming_dict["name"])
# print(xiaoming_dict["name1"])
# 2、增加/修改
# 如果key不存在，会新增键值对
# 如果key存在，则修改键值对
xiaoming_dict["age"] = 18
xiaoming_dict["name"]="小小明"
# xiaoming_dict["name"]=18
# 3、删除
# xiaoming_dict.pop("name")
# 删除指定键值对时，如果指定的key不存在，程序会报错
xiaoming_dict.pop("name")
print(xiaoming_dict)

# 字典的循环遍历

"""
字典的循环遍历
用的不多
"""
xm_dict = {"name":"xiaoming",
           "qq":"1232456",
           "phone":10086
           }
# 变量K是每次循环中，获取到的键值对的key
for k in xm_dict:
    print("%s- %s" %(k,xm_dict[k]))

# 3、清空字典
xiaoming_dict.clear()
print(xiaoming_dict)


# 字典及列表的应用场景
"""
列表是有序的数据集合；字典是无序的数据集合
两个字典放在同一个列表变量中
遍历
使用多个键值对，存储描述同一个物体的相关 信息--描述更复杂的数据信息
将多个字典放在同一个列表中，在进行变量，在循环体内部真的每一个字典进行相同的处理
"""
card_list = [
    {
        "name":"xiaoming",
        "age":19,
        "height":1.75,
        "number":998877
    },
    {
        "name": "huahua",
        "age": 18,
        "height": 1.60,
        "number":999888
    }
]

for card_info in card_list:
    print(card_info)