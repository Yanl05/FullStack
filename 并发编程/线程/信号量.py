# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-27 14:43
# @Author  : yanlei
# @FileName: 信号量.py


"""
from threading import Semaphore, Thread
import time
def func(a, b, sem):
    sem.acquire()
    time.sleep(1)
    print(a+b)
    sem.release()

sem = Semaphore(4)
for i in range(10):
    Thread(target=func, args=(i, i+5, sem)).start()
