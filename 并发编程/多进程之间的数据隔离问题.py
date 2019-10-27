 # -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 10:38
# @Author  : yanlei
# @FileName: 多进程之间的数据隔离问题.py
"""
from multiprocessing import Process
import os


def func():
    global n
    n = 0
    print('子进程id：', os.getpid(), 'n=', n)

n = 100
p = Process(target=func)
p.start()
print('n=', n)