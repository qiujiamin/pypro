#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import random
import string
import  requests
# import time
from  time import ctime,sleep

from python.pythoninstroduction.testmoduledata import author_name, print_author_name
# import pythoninstroduction.testmoduledata

def get_last_name_count():
    name_list = ['张数','张思','李四']
    name_cnt = 0
    for name in name_list:
        if "张" in name:
            print(name)
            name_cnt+=1
    print(name_cnt)
def share_msg():
    """
    生成短信模板提示
    :return:
    """
    seeds = string.digits
    random_str = random.sample(seeds, k=4)
    code_num = int("".join(random_str))
    msg_str = '[招商银行]提醒您，您本次的验证码为 %d,请不要告诉其他人以防引起财务损失' %code_num
    return msg_str
def get_path():
    """
    根据文件路径，获取文件名称
    :return:
    """
    path = "/home/result/my.doc"
    alist = path.split('/')
    print(alist[-1])

def changefunctionname(s):
    """
    传入有大小写的字符串函数名，转换为linux函数名称：大写转小写且用_分隔
    pass in the case-sencitive string function name and convert it to "Linux" style function-name:String case conversion from uppercase to lowercase and split them by '_'
    :param s: A string of uppercase and lowercase letters
    :return: A string of lowercase and  field separation character of '_'
    """
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i].isupper():
            s_list[i] = s_list[i].lower()
            if i!=0:
                s_list[i] = "_"+s_list[i]
            print(s_list[i])
    s_str = ''.join(s_list)
    print(s_str)
    return s_str

def if_demo(a):
    """
    完整的if示例
    :param a:
    :return:
    """
    if a<= 1:
        print('a<=1')
    elif 1<a<=2:
        print('1<a<=2')
    else:
        print('a>2')
def while_forever():
    """
    不会自己挺固执的定时程序
    每一秒定时请求百度服务器是否能正常访问
    :return:
    """
    while True:
        res = requests.get('http://www.baidu.com')

        print(res.status_code)
        sleep(1)
        # time.sleep(1)
def for_demo():
    """
    for语句示范
    :return:
    """
    name_list = ['catu','terry','joe','matter']
    print('序列项迭代')
    for eachname in name_list:
        print(eachname)
    print('序列索引迭代')
    for index in range(len(name_list)):
        print(index)
        print(name_list[index])

def break_demo():
    """

    :return:
    """
    fly_num = 10
    for index in range(10):
        is_alive = True #苍蝇存活状态
        print("start kill fly no :%s" %index)
        print("use no.1 drug")
        if  is_alive:
            # continue
            break
        print('use no.2 drug')
        is_alive = False
        if not is_alive:
            break
        print("开始写报告")
def pass_demo():
    """
    先做结构
    :return:
    """
    a = True
    if a:
        pass
    else:
        pass
def exception_demo():
    """
    异常捕捉演示
    :return:
    """
    while True:
        try:
            print('run in try')
            a = 1
            b = a/0
            c = 2
            print(c)
        except BaseException as e:
            print('run in except')
        finally:
            print('finally')
        # time.sleep(1)
        sleep(1)
def assert_test():

    my_list = [1,2,3,4,5,6]
    assert len(my_list) <10
    print("mylist小于1")
def fun_demo_0():
    """
    返回一个对象
    :return:
    """
    print('return 0 object')

def fun_demo_1():
    """
    返回一个对象,该对象类型
    :return:
    """
    a=[1,2]
    b="sss"
    print('return 1 object')
    return 1
    # return b
def fun_demo_more():
    """
    返回多个对象，是元组
    :return:
    """
    a =[1,2]
    b='sjsjd'
    print('return more object')
    # return 1,2,3
    return a,b
def parameter_keyword(a,b):
    """
    位置参数传值
    :return:
    """
    print('a is %s' % a)
    print('b is %s' % b)
def parameter_keyword_demo():
    """
    关键字参数函数演示
    :return:
    """
    parameter_keyword(1,2)
    parameter_keyword(b=1,a=2)
def parameter_default(a=100):
    """
    默认值传参
    :param a:
    :return:
    """
    print("a is %s" %a)
    # a=300
    # print("a is %s" % a)
def parameter_default_demo():
    """
    默认值参数演示
    :return:
    """
    parameter_default()#不指定参数
    parameter_default(200)#指定参数
def parameter_args(*args):
    """
    单星号传值,元组作为参数，比较好
    :param args:
    :return:
    """
    print('*args')
    print(len(args))
    for item in args:
        print(item)
def parameter_kwargs(**kwargs):
    """
    双星号参数，字典作为参数
    :param kwargs:
    :return:
    """
    print("**kwargs")
    name = kwargs.get('name',None)
    # 获取字典中name的值，如果那么有值，则赋值给变量，没有就讲None赋值给变量
    age = kwargs.get('age',None)
    print('name is %s,age is %s'%(name,age))
    pass
def parameter_group_demo():
    """
    参数组演示
    :return:
    """
    atuple = (1,2,3,4,5)
    parameter_args(*atuple)#正确的调用方式
    # 有星号对元组进行变量，传入传出都有
    # 直接传进去，指向元组的指针的指针，长度始终是1
    parameter_args(atuple)#错误的调用方式

    adict = {'name':'jin','age':25}
    parameter_kwargs(**adict)
    parameter_kwargs(name = 'jim',age=26)
#     与直接传字典是一样的
def deco(method):
    """
    :param method:
    :return:
    """
    def wrapper():
        print('[%s][%s] called' %(ctime(),method.__name__))
        return method()
    return wrapper()

@deco  #等价于 mydemo_fun = warp(mtdemo_fun)
def mydeco_fun():
    """

    被装饰的函数
    :return:
    """
    print("mydeco fun")
def mydeco_fun_demo():
    """
    一般装饰器演示
    :return:
    """
    mydeco_fun

def module_demo():
    """
    模块引用
    :return:
    """
    print('auther name is :%s'%author_name)

    print_author_name()
if __name__ == '__main__':

    # get_last_name_count()

    # print(share_msg())
    # get_path()
    # s='iLoveSpirit'
    # s=input('输入有大小写的一串字符：')
    # changefunctionname(s)
    # n = int(input('输入一个数字：'))
    # if_demo(n)
    # while_forever()
    # for_demo()
    # break_demo()
    # exception_demo()
    # assert_test()
    # print(fun_demo_0())
    # print(fun_demo_1())
    # print(fun_demo_more())
    # a = input('请输入a:')
    # b = input('请输入b:')
    # parameter_keyword(a,b)
    # parameter_keyword_demo()
    # parameter_default_demo()
    # parameter_group_demo()
    # mydeco_fun_demo()
    module_demo()