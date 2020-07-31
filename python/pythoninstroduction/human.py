#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from PIL import Image
import qrcode
class Human(object):
    """
    人类
    """
    let_num = 2
    hard_num = 2
    record = [1]

    @staticmethod
    def show_leg_num(cls):
        print("leg num is %s" %cls.leg_num)
def static_class_data_demo():
    """
    静态数据成员演示
    :return:
    """
    human1 = Human()
    human2 = Human
    print('human.hand_num :%s' %human1.hard_num)
    human1.hard_num = 3
    # human1.record.append(2)
    human1.record=[2,4]
    print('human.hand_num:%s,record:%s' %(Human.hard_num,str(Human.record)))
    print('human1.hand_num:%s,record:%s' %(human1.hard_num,str(human1.record)))
    print('human2.hand_num:%s,record:%s' %(human2.hard_num,str(human2.record)))
    human3 = Human()
    print('human3.hand_num:%s,record:%s' %(human3.hard_num,str(human3.record)))
    Human.hard_num = 4

    Human.record.append(3)
    print('human.hand_num:%s,record:%s' % (Human.hard_num, str(Human.record)))
    print('human1.hand_num:%s,record:%s' % (human1.hard_num, str(human1.record)))
    print('human2.hand_num:%s,record:%s' % (human2.hard_num, str(human2.record)))
    print('human3.hand_num:%s,record:%s' % (human3.hard_num, str(human3.record)))
    human2.record=[4,6]
    # 不确定为何使用过append，再赋值仍是改变所有？
    # human2s.record = [3,5,7]
    print('human.hand_num:%s,record:%s' %(Human.hard_num,str(Human.record)))
    print('human1.hand_num:%s,record:%s' %(human1.hard_num,str(human1.record)))
    print('human2.hand_num:%s,record:%s' %(human2.hard_num,str(human2.record)))
    print('human3.hand_num:%s,record:%s' %(human3.hard_num,str(human3.record)))
def qrcode_demo():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    url = 'http://www.jason-niu.com'
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('二维码.png')

    '''
    ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
    ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
    ROR_CORRECT_H：大约30%或更少的错误能被纠正。
    '''
def qrcode_color_demo():
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    qr.add_data("http://www.jason-niu.com")
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    # logo="D:/favicon.jpg"
    icon = Image.open("E:\\abak\\test2.png")

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    # img.show()
    img.save('E:\\abak\\test1.png')
if __name__ == '__main__':
    # static_class_data_demo()
    # qrcode_demo()
    qrcode_color_demo()