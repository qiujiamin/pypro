#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import configparser
import json
import pymysql
import sys

class ReadDBConfig:
    def __init__(self,ini_file=None):
        if ini_file:
            self.ini_file = ini_file
        else:
            self.ini_file = '../dataconfig/dbconfig.ini'
        config =configparser.ConfigParser()
        config.read(self.ini_file,encoding='utf-8')
        self.host = config['DATABASE-500dev']['host']
        # self.port = config['DATABASE-500dev']['port']
        self.user = config['DATABASE-500dev']['user']
        self.password = config['DATABASE-500dev']['password']
        self.db = config['DATABASE-500dev']['database']

    def get_conn(self):
        try:
            db_conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db,
                                      charset='utf8')
            return db_conn
            # cur = db_conn.cursor()
            # return cur
        except Exception as e:
            print("%s",e)
            sys.exit()
    def select_sql(self,itemname,table,condition=None):
        if condition != None:
            select_sqli = "select " + itemname + " from " + table + " where " + condition + ";"

        else:
            select_sqli = "select " + itemname + " from " + table + ";"
        return select_sqli
    def update_sql(self,table,itemname,condition):
        update_sqli = 'update '+table +' set ' + itemname + ' where ' +condition + ';'
        return update_sqli

if __name__ == '__main__':
    db500 = ReadDBConfig('../dataconfig/dbconfig.ini')
    conn = db500.get_conn()
    cur = conn.cursor()
    # select_sqli = db500.select_sql('*','t_area','id=1')
    select_sqli = db500.select_sql('*','t_area')
    # print(select_sqli)
    res = cur.execute(select_sqli)
    print("查看语句的返回结果:", res)
    cur.close()
    conn.close()

#     待调试

