# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 09:49
# @Author  : yanlei
# @FileName: 信号量.py
"""
from multiprocessing import Process
from multiprocessing import Semaphore
import time
import random

def ktv(i, sem):
    sem.acquire()  # 获取钥匙
    print('%s进了ktv'%i)
    time.sleep(random.randint(1, 5))
    print('%s走出了ktv'%i)
    sem.release()  # 归还钥匙

sem = Semaphore(4)  # 一次只能有4个人使用这一套资源
for i in range(20):
    p = Process(target=ktv, args=(i, sem))
    p.start()