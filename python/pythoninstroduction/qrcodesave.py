#! /usr/bin/env/python
# -*-

# 文件io操作
import qrcode
from PIL import Image

import os

def new_vcf1():
    vstr_start ="BEGIN:VCARD" \
          "VERSIPM:2.1"+"\n"
    vstr_end ="END:VCARD""\n"
    filename = "5-课后习题-员工联系方式列表.txt"
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line_list = line.split(',')
            str1 = "FN:"+line_list[0]+"\n"
            str2 = "TEL;CELL:86"+line_list[1]
            line_allstr = vstr_start+str1+str2+vstr_end
            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=2,
                    border=20,
                )
            # 将vCard数据填入qr
            qr.add_data(line_allstr)
            qr.make(fit=True)
            # 生成图片
            img = qr.make_image()
            # 将图片存入指定路径文件
            # img.save('qr%d.jpg'%(line+1))
            img.save('qr'+line_list[0]+'.jpg')

def new_vcf():
    filename = "5-课后习题-员工联系方式列表.txt"
    with open(filename,encoding='utf-8') as f:
        res = f.readlines()
    with open("new.vcf","w") as file_vcf:
        for line in res:
            # print(line.rstrip())
            line_list = line.split(',')
            print(line_list[0])
            print(line_list[1])
            file_vcf.write("BEGIN:VCARD"+"\n")
            file_vcf.write("VERSIPM:2.1"+"\n")
            file_vcf.write("FN:"+line_list[0]+"\n")
            file_vcf.write("TEL;CELL:86"+line_list[1])
            file_vcf.write("END:VCARD"+"\n")

            # print(line.split(','))
        # res = f.readlines()
def qrtest():
#     vcard内容

    vstr = """
        BEGIN:VCARD
        VERSIPM:2.1
        FN:张10 
        TEL;CELL:86 13409871110
        END:VCARD
        """
    qr = qrcode.QRCode(
        # version值为1~40的整数,控制二维码的大小,(最小值是1,是个12*12的矩阵)
        # 如果想让程序自动确定,将值设置为 None 并使用 fit 参数即可
        version=1,
        # error_correction: 控制二维码的错误纠正功能,可取值下列4个常量
        #   ERROR_CORRECT_L: 大约7%或更少的错误能被纠正
        #   ERROR_CORRECT_M(默认): 大约15%或更少的错误能被纠正
        #   ERROR_CORRECT_Q: 大约25%或更少的错误能被纠正
        #   ERROR_CORRECT_H: 大约30%或更少的错误能被纠正
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        # 控制二维码中每个小格子包含的像素数
        box_size=2,
        # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4,是相关标准规定的最小值)
        border=20,
    )

    # 将vCard数据填入qr
    qr.add_data(vstr)

    qr.make(fit=True)

    # 生成图片
    img = qr.make_image()

    # 将图片存入指定路径文件
    img.save('dtong.jpg')


def openfile():
    f = open("5-课后习题-员工联系方式列表.txt","r")
    # 1.读取文件，姓名和电话分离
    # 2、VCard编码成字符串
    # 3、 qr库，将字符串编码成二维码

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
    # qrtest()
    # new_vcf()
    new_vcf1()