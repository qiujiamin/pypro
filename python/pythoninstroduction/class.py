#! /usr/bin/env/python
# -*- coding:utf-8 -*-
class Bird(object):
    """
    鸟类
    """
    def __init__(self):
        self.leg = 4
        self.wing = 2
    def show_leg_num(self):
        print("I have %s legs" %self.leg)

    def show_wing_num(self):
        # 非静态需要一个实例指针传入
        print("I have %s wings" % self.wing)
    @staticmethod
    def fly():
        """
        飞行
        :return:
        """
        # 静态方法需要加修饰器
        print("now i am flying")
    @staticmethod
    def sleep():
        """
        睡觉
        :return:
        """
        print("now i am sleeping")
class Parrot(Bird):
    """
    鹦鹉
    """
    @staticmethod
    def fly():
        print("I can fly slowly")
class Eagle(Bird):
    """
    老鹰
    """
    @staticmethod
    def fly():
        print("T can fly quickly")
def inherit_demo():
    """
    继承演示
    """
    parrot = Parrot()
    parrot.show_leg_num()
    parrot.fly()

    eagle = Eagle()
    eagle.show_wing_num()
    eagle.fly()

# def bird_instance_demo():
#     """
#     实例
#     """
if __name__ == '__main__':
    inherit_demo()