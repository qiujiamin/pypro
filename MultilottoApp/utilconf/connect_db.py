#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# 链接数据库
import pymysql
conn = pymysql.Connect(
        host='10.0.0.104',
        port= 3306,
        user='root',
        password='Lotto@500.com',
        db='500lotto_dev',
        charset='utf8',
)
# 创建游标
cur = conn.cursor()
cur.execute("select * from t_area limit 5")
# 查看结果
print(cur.fetchone())

# malta这个数据库连不上
# host = '10.201.2.12',
# port = 3306,
# user = 'multilotto_dev_500',
# password = 't6E78gkrvSfvgkRt',
# db = 'multilotto_dev',
# charset = 'utf8',

#数据库：500lotto
# DB_CONNECTION=mysql
# DB_HOST=10.0.0.104
# DB_PORT=3306
# DB_DATABASE=500lotto_dev
# DB_USERNAME=root
# DB_PASSWORD=Lotto@500.com