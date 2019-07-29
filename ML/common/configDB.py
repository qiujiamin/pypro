import configparser
import json
import pymysql
import sys


class ReadDBConfig:
    def __init__(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file)
        self.host = config['database1']['host']
        self.port = config['database1']['port']
        self.user = config['database1']['user']
        self.password = config['database1']['password']

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

    def set_username(self, user):
        self.username = user

    def get_username(self):
        return self.user

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def get_conn(self):
        try:
            db_conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, charset='utf-8')
            return db_conn
        except Exception as e:
            print("%s", e)
            sys.exit()
