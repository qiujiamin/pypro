"""
shebang符号直接运行python文件
#！知名执行这个脚本文件的解释
which python2
---   #! usr/bin/python3(完整路径)
在主程序中就可以，不需要解释器
"""

# import cards_tools
from python.hm_14名片管理系统 import cards_tools
# for循环遍历集合
#1、 while循环
while True:
    # TODO(名字) 显示功能菜单 --用来标记需要去做的工作
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是：【%s】" %action_str)

    #如果是1,2,3 针对名片的操作
    # 字符串操作
    if action_str in ["1","2","3"]:
        if action_str == "1":
            # 新增名片
            # 3、pass暂时不写逻辑
            cards_tools.new_card()
        elif action_str =="2":
            # 显示全部
            # pass
            cards_tools.show_all()
        elif action_str =="3":
            # 查询名片
            cards_tools.search_card()
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片系统】")
        break
        # 如果在开发环境时，不希望立刻编写分支内部的代码
        # 可以使用pass关键字  表示一个占位符，能够保证程序的代码结构正确
    # 其他内容提示输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")
