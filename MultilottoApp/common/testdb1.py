#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import pymysql
connect = pymysql.connect(host='10.0.0.104',user='root',passwd ='Lotto@500.com',db='500lotto_dev',charset = 'utf8')
cur = connect.cursor()
select_sqli = 'select * from t_area;'
res = cur.execute(select_sqli)
print("查看语句的返回结果:", res)