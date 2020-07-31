#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import configparser
import json
import pymysql
import sys

class ReadDBConfig:
    def __init__(self,ini_file):
        config =configparser.ConfigParser()
        config.read(ini_file,encoding='utf-8')
        self.host = config['DATABASE-500dev']['host']
        # self.port = config['DATABASE-500dev']['port']
        self.user = config['DATABASE-500dev']['user']
        self.password = config['DATABASE-500dev']['password']
        self.db = config['DATABASE-500dev']['database']
        if ini_file != None:
            self.ini_file = ini_file
        else:
            self.ini_file = '../configfiles/config.ini'
    # def set_host(self,host):
    #     self.host = host
    # def get_host(self):
    #     return self.host
    # def set_port(self,port):
    #     self.port = port
    # def get_port(self):
    #     return self.port
    # def set_username(self,user):
    #     self.username = user
    # def get_username(self):
    #     return self.user
    # def set_password(self,password):
    #     self.password = password
    # def get_password(self):
    #     return self.password
    # def set_db(self,db):
    #     self.db = db
    # def get_db(self):
    #     return self.db
    def get_conn(self):
        # db_conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db,
        #                           charset='utf8')
        try:
            db_conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db,
                                      charset='utf8')
            # return db_conn
            cur = db_conn.cursor()
            return cur
        except Exception as e:
            print("%s",e)
            sys.exit()
    def get_select(self,itemname,table,condition=None):
        if condition != None:
            select_sqli = "select " + itemname + " from " + table + " where " + condition + ";"

        else:
            select_sqli = "select " + itemname + " from " + table + ";"
        return select_sqli
if __name__ == '__main__':
    db500 = ReadDBConfig('../configfiles/config.ini')
    cur = db500.get_conn()
    # cur=conn.cursor()

    select_sqli = db500.get_select('*','t_area')
    print(select_sqli)
    # res = cur.execute(select_sqli)
    # print(cur)
    # res = cur.get_select('*','t_area','')
    # cur = conn.cursor()
    # print(cur)
    # select_sqli = 'select * from t_area;'
    # res = cur.execute(select_sqli)
    # print("查看语句的返回结果:", res)

#     待调试

