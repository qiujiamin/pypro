#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 10:59
# @Author  : dzw
# @File    : readImage.py
# @Software: win10 Tensorflow1.13.1 python3.6.3
import exifread
import re

def  imageread():
        GPS = {}
        date = ''
        f = open("F:\\原图.jpg",'rb')
        imagetext = exifread.process_file(f)
        for key in imagetext:                           #打印键值对
                print(key,":",imagetext[key])
        print('********************************************************\n********************************************************')
        for q in imagetext:                             #打印该图片的经纬度 以及拍摄的时间
                if q == "GPS GPSLongitude":
                        print("GPS经度 =", imagetext[q],imagetext['GPS GPSLatitudeRef'])
                elif q =="GPS GPSLatitude":
                        print("GPS纬度 =",imagetext[q],imagetext['GPS GPSLongitudeRef'])
                elif q =='Image DateTime':
                        print("拍摄时间 =",imagetext[q])

imageread()
