# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 17:02
# @Author  : yanlei
# @FileName: 进程池的同步调用.py
"""
import os, time
from multiprocessing import Pool

def work(n):
    print('%s run'%os.getpid())
    time.sleep(1)
    return n**2

p = Pool(3)
res_l = []
for i in range(10):
    res = p.apply(work, args=(i, )) # 同步调用，直到本次任务执行完毕拿到res，等待任务work执行的过程中可能有阻塞也可能没有阻塞
    res_l.append(res)
print(res_l)