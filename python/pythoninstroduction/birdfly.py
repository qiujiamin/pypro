#! /usr/bin/env/python
# -*- coding:utf-8 -*-
class Bullet(object):
    """
    定义子弹的这个
    """
    @staticmethod
    def fly():
        print("let me fly")

def let_bullet_fly_po():
    """
    面向过程：让子弹飞
    :return:
    """
    bullet_name ="polly"
    print("let %s fly" %bullet_name)
def let_bullet_fly_oo():
    """
    面向对象，让子弹飞
    :return:
    """
    bullet = Bullet()
    bullet.fly()
def po_vs_oo_demo():
    """
    去吧
    :return:
    """
    let_bullet_fly_po()
    let_bullet_fly_oo()

if __name__ == '__main__':
    po_vs_oo_demo()
