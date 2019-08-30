# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/13 
# @Author  : yanlei
# @FileName: 装饰器修复技术.py

修复inner函数，使被修饰函数不改变__name__  __doc__ 等属性
"""
from functools import wraps
def wrapper(func):
    @wraps(func)  # 装饰器修复技术  括号中要写被装饰的函数  该语法糖放在inner前
    def inner(*args, **kwargs):
        print('在被修饰的函数执行之前做的事')
        ret = func(*args, **kwargs)
        print('在被修饰的函数执行之后做的事')
        return ret
    return inner

@wrapper
def MyName(name):
    """
    is mu name
    :param name:
    :return:
    """
    print('my name is ', name)
    return 'this is my name'


print(MyName('yanlei'))
print(MyName.__doc__)
