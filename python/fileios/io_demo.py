#! /usr/bin/env/python
# -*- coding:utf-8 -*-


def cli_io_demo():
    """
    控制台的输入输出
    :return:
    """
    a = input()
    print("输入的字符： %s" %a)
def file_io_demo():
    """
    文件的输入输出
    :return:
    """
    str_temp = ''
    input_file = open('input.txt',mode = 'r',encoding='utf-8')
    for line in input_file.readlines():
        # 每一行作为可迭代对象
        print(line)
        str_temp = line
    # print(str_temp)

#     读取到的信息输出到文件中
    output_file = open('output.txt',mode='w',encoding='utf-8')
    output_file.writelines(str_temp)

    # 写100个数字
    for i in range(10):
        output_file.writelines(str(i)+'\n')
    output_file.writelines("这是输出到文件的操作")

    input_file.close()
    output_file.close()
def add():
    a= 0
    a += 1
    print(a)
def etc_demo(car_num):
    """
    if语句判断：ETC
    :return:
    """
    # 假设今天是6号，只允许尾号为6的通过
    if car_num ==6:
        print("今天不扣分")
    else:
        print('扣分')
def while_demo():
    """
    while循环
    :return:
    """
    counter = 0
    while counter <3:
        print("in loop:%d" %counter)
        counter += 1
def for_demo():
    """
    range:可迭代对象，如列表
    :return:
    """
    for i in range(10):
        print(i)
    a = 'hello world'
    for item in a:
        print(item)
if __name__ == '__main__':
    # file_io_demo()
    # add()
    # car_num_tail = 6
    # etc_demo(car_num_tail)
    # while_demo()
    for_demo()