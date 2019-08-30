# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/16 
# @Author  : yanlei
# @FileName: 匿名函数.py
"""

# add = lambda x, y: x + y
# print(add(1, 2))
#
# dict = {'k1': 10, 'k2': 100, 'k3': 50}
# print(max(dict, key=lambda y:dict[y]))
# l = ['12','123','1']
# l.sort(key=len)
# print(l)

# 现有两元组(('a'),('b')),(('c'),('d')),请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]

# x = (('a'),('b')),(('c'),('d'))
# def func(k):
#     return {k[0]:k[1]}
#
# new_list = lambda x:map(func, zip(x[0],x[1]))
# for i in new_list(x):
#     print(i)
# print(list(new_list(x)))

# 以下代码的输出是什么？请给出答案并解释。
def multipliers():
    return [lambda x:i*x for i in range(4)]

print([m(2) for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果。
