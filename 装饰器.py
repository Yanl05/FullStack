# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/13 
# @Author  : yanlei
# @FileName: 装饰器.py

闭包与装饰器
简单的装饰器 -> 装饰器的固定模式
"""
# import time
# def func():
#     time.sleep(0.01)
#     print('this is test sentence')
#
# def timmer(f):  #装饰器函数
#     def inner():
#         start = time.time()
#         f()  # 被装饰的函数
#         end = time.time()
#         print(end - start)
#     return inner
#
# func = timmer(func)
# func()

# 装饰器的形成过程： 最简单的装饰器 -> 有返回值的 -> 有一个参数的 -> 万能参数的
import time

# 写装饰器函数
# 1.最简单的装饰器
# def timmer(f):
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print(end - start)
#     return inner

# 2.带返回值的装饰器
# def timmer(f):
#     def inner():
#         start = time.time()
#         ret = f()
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
# 3. 带参数的装饰器函数
# def timmer(f):
#     def inner(*args):
#         start = time.time()
#         ret = f(*args)
#         end = time.time()
#         print(end - start)
#         return ret
#     return inner
# 4. 万能参数的装饰器函数
def timmer(f):
    def inner(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        print(end - start)
        return ret
    return inner

@timmer  # 语法糖
# 1.最简单的装饰器装饰的函数
# def func():
#     time.sleep(0.01)
#     print('this is a sentence')
# 2.带返回值的装饰器装饰的函数
# def func():
#     time.sleep(0.01)
#     print('this is a sentence')
#     return 'hello world'
# 3.带参数的装饰器装饰的函数
# def func(a):
#     time.sleep(0.01)
#     print('this is a sentence', a)
#     return 'hello world'
# 4. 万能参数的装饰器装饰的函数
def func(a,b):
    time.sleep(0.01)
    print('this is a sentence', a, b)
    return 'hello world'


# func = timmer(func) == @timmer
# func = timmer(func)
ret = func(1, b=100)
print(ret)


# 装饰器的固定模式
# 1.先写装饰器函数
def wrapper(f):
    def inner(*args, **kwargs):
        '''在执行被装饰函数之前要做的事'''
        ret = f(*args, **kwargs)  # 被装饰的函数
        '''在执行被装饰函数之后要做的事'''
        return ret
    return inner

# 2.给被装饰函数加语法糖
@wrapper
def func():
    '''被装饰的函数'''
    print('this is a sentence')
    return 'acc'
print(func())

