#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import json
# 加载文件基础
# with open('../dataconfig/logininfo.json','r') as f:
#     dataconfig = json.load(f)
# f = open('../dataconfig/logininfo.json',encoding='utf-8')
# dataconfig = json.load(f)
# print(dataconfig['login'])

class OperationJson:
    def __init__(self,file_path=None):
        if file_path ==None:
            self.file_path = '../dataconfig/login1.json'
        else:
            self.file_path = file_path
        self.data =self.read_data()

    # 读取json文件
    def read_data(self):
        # fp = open(path)
        # fp.close()
# 为了防止忘记关闭，使用with
#         with open('../dataconfig/login1.json') as fp:
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data
    # 根据关键字获取数据
    def get_data(self,id):
        print(type(self.data))
        return self.data[id]
#    写json
    def write_data(self,data):
        with open('../dataconfig/cookie.json','w') as fp:
            fp.write(json.dumps(data))
    #    获取coockie
    # def get_cookie(self):


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('login'))



