# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/13 
# @Author  : yanlei
# @FileName: 装饰器作业.py

编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
要求登录成功一次，后续的函数都无需再输入用户名和密码
"""
# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码

# from functools import wraps
# # 设置一个flag，实现 登录成功一次，后续的函数都无需再输入用户名和密码 的功能
# FLAG = False
# def login(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         global FLAG
#         '''登录验证'''
#         if FLAG == False:
#             username = input('username:')
#             password = input('password:')
#             if username == 'yan' and password == '123':
#                 FLAG = True
#                 ret = func(*args, **kwargs)
#                 return ret
#             else:
#                 print('登录失败')
#         else:
#             ret = func(*args, **kwargs)
#             return ret
#     return inner
#
# @login
# def shopping_add():
#     print('增加一件物品')
#
# @login
# def shopping_del():
#     print('删除一件物品')
#
# shopping_add()
# shopping_del()


# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
# def log(func):
#     def inner(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         '''调用函数后执行的事'''
#         with open('file', 'a+', encoding='utf-8') as f:
#             f.write(func.__name__+'\n')
#         return ret
#     return inner
#
# @log
# def shopping_add():
#     print('增加一件物品')
#
# @log
# def shopping_del():
#     print('删除一件物品')
#
# shopping_add()
# shopping_del()

# 进阶作业(选做)：
# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中