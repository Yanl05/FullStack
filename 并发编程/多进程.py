# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 08:47
# @Author  : yanlei
# @FileName: 多进程.py
"""
from multiprocessing import Process
import time
import os

def func(args, args2):
    print(args, args2)
    time.sleep(1)
    print('子进程：', os.getpid())
    print('子进程的父进程：', os.getppid())
    print('func')


# 开启一个进程
p = Process(target=func, args=('参数一', '参数二'))  # register, p is a process object
p.start()  # start
print('*'*10)
print('父进程：', os.getpid())  # 查看当前进程的进程号
print('父进程的父进程：', os.getppid())  # 查看当前进程的父进程

