#! /usr/bin/env/python
# -*- coding:utf-8 -*-

class Student():
    def __init__(self,name,city):
        self.name = name
        self.city = city
        print("My name is %s and come from %s" %(name,city))
    def talk(self):
        print("hello jasmine")
stu1 = Student('jack','beijing')
stu1.talk()