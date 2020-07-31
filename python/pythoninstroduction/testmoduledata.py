#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# 会执行，影响效率
# print("you have a module on go")
# print(__name__)
author_name = "amo"
def print_author_name():
    """
    输出作者名称
    :return:
    """
    print("author name is %s" %author_name )

if __name__ == '__main__':
    print_author_name()