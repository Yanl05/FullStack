# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 20:52
# @Author  : yanlei
# @FileName: 守护进程.py
"""
# 单一子进程
# from multiprocessing import Process
# import time
#
#
# def func():
#     while True:
#         time.sleep(0.2)
#         print('func 进程还在运行')
#
#
# p = Process(target=func)
# p.daemon = True  # 将子进程设置为守护进程
# p.start()
# i = 0
# while i < 5:
#     print('主进程还在运行')
#     time.sleep(0.3)
#     i += 1

# 多个子进程
from multiprocessing import Process
import time


def func():
    while True:
        time.sleep(0.2)
        print('守护 进程还在运行')


def func2():
    time.sleep(6)
    print('非守护进程 刚刚执行完')


p = Process(target=func)
p.daemon = True  # 将子进程设置为守护进程
p.start()
p2 = Process(target=func2).start()

i = 0
while i < 5:
    print('主进程还在运行')
    time.sleep(0.1)
    i += 1

# 守护进程会在主进程代码执行完毕的时候立即结束其生命周期。
# 主进程代码执行完毕后，不会立即结束(但此时，守护进程已经结束)，主进程此时需要等待其他进程全部执行完毕后才会结束其生命周期。
