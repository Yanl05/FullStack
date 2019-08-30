# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/16 
# @Author  : yanlei
# @FileName: tmp.py
"""

# a = 5 + 6j
# print(type(a.real))
#
# b = range(100)
# print(type(b))
# print(list(b[0:3]))
# c = b
# print(c)
#
# dict = {'k':0}
# print('k' in dict)

# list=[]
# def extendlist(val,list):
#     list.append(val)
#     return list
#
# list1 = extendlist(10, list)
# print(list1)
# list2 = extendlist(123, [])
# list3 = extendlist('a', list)
# print(list1)
# print(list2)
# print(list3)

# l = [1, 2]
# l2 = ['a', 'b']
# for i in zip(l, l2):
#     print(list(i))
#     print(type(i))

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表

zip(a,c)              # 元素个数与最短的列表一致

# print(zip(*zipped))          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
for i in zip(*zipped):
    print(i)
    print(type(i))



