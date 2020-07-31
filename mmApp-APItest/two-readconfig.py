#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import os
import configparser
# 项目路径，分隔出路径及文件，从各个路径到目的文件的相对路径
# rootdir = os.path.split(os.path.relpath(__file__))[0]
# print('---1---')
# print(rootdir)
# print('---2---')
# # conf.ini文件路径，把目录和文件名合成一个文件
# confpath = os.path.join(rootdir,'conf.ini')
# def get_conf():
#     # 实例化一个名为congigParser对象
#     conf = configparser.ConfigParser()
#     # 读取文件
#     conf.read(confpath)
#     return conf.get("HTTP","url")
# print(get_conf())

class ConfigUtil:

    prop = {}

def get_prop(self, key_type, key):
    return ConfigUtil.prop[key_type][key]


def set_prop(self, path, file_name):
    os.chdir(path)
    config = configparser.ConfigParser()
    config.read(file_name, encoding="utf-8")
    db_items = config.items("db")
    hdfs_items = config.items("hdfs")

    db_dict = {}
    hdfs_dict = {}
    for x in db_items:
        key = x[0]
        db_dict[key] = x[1]
    #
    for x in hdfs_items:
        key = x[0]
        hdfs_dict[key] = x[1]

    ConfigUtil.prop['db'] = db_dict
    ConfigUtil.prop['hdfs'] = hdfs_dict

