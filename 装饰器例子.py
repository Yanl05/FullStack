# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-22 08:58
# @Author  : yanlei
# @FileName: 装饰器例子.py
"""
import functools  # from functools import wraps

def wrapper1(func1):
    @functools.wraps(func1)  # import functools是导入functools模块。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。
    def inner1(*args,**kwargs):
        print('wrapper1 ,before func')
        ret1 = func1() + ' 1111111111'
        print('wrapper1 ,after func')
        return ret1

    return inner1

def wrapper2(func):
    @functools.wraps(func)
    def inner2(*args,**kwargs):
        print('wrapper2 ,before func')
        ret2 = func() + ' 2222222222'
        print('wrapper2 ,after func')
        return ret2

    return inner2


@wrapper1
@wrapper2
def f():
    return 'in f'

ret = f()
print(ret)
print(f.__name__)  # 如果前面没有@function.wraps(),就会出现inner1