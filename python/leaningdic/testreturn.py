#! /usr/bin/env/python
# -*- coding:utf-8 -*-
a = ['a','b','c']
k = "p"
f="hhhhhh"
def getinfo():
    if '#' in f:
        print("返回a")
        print(type(a))
        return a
    else:
        print("返回b")
        print(type(k))

        return k
def listadd():
    response = {
        "usercheck":"",
        "userid":"",
        "username":""
    }
    a = ["usercheck","userid","username"]
    b = ["kkkkkk","123456","qiujiamin"]
    for i in range(len(a)):
        print(a[i])
        response[a[i]] = b[i]
    print(response)
def testadddict():
    flag = 0
    requestdata ={
        "name":"bb",
        "age":"18",
        "test":"oo"
    }
    modifydata ={
        "name": "aa",
        "age": "14"
    }
    if modifydata:
        flag =1
        for key in modifydata.keys():
            requestdata[key] = modifydata[key]
    return requestdata,flag
    # print(requestdata)

if __name__ == '__main__':
    # getinfo()
    # listadd()

    print(testadddict())