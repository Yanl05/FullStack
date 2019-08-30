# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/13 
# @Author  : yanlei
# @FileName: 生成器.py

生成器  ： 本质还是迭代器   自己写的迭代器
"""
def generator():  # 生成器函数
    for i in range(200):
        yield 'yan%s号'%i

g = generator()  # g为一个生成器
print(g.__next__())

for i in g:
    print(i)