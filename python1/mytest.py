from __future__ import  print_function
# num = input()
str = "A2c1b3"
numList = []
charList=[]
for tmp in str:
    if tmp.isdigit():
        numList.append(tmp)
    else:
        charList.append(tmp)
list = charList+numList
print("".join(list))