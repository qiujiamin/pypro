#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from jsonpath_rw import jsonpath, parse
json_obj = {"student":[{"male":176,"female":162},{"male":174,"female":159}]}
jsonpath_expr = parse("student[*].male")
print(type(jsonpath_expr))
print(jsonpath_expr)
male = jsonpath_expr.find(json_obj)
item = [math.value for math in male][0]
print(male)
print(item)
print(type(item))
# print([match.value for match in male])
