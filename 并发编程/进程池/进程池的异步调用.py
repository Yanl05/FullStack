# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 17:06
# @Author  : yanlei
# @FileName: 进程池的异步调用.py
"""
import os, time
from multiprocessing import Pool

def work(n):
    print('%s run'%os.getpid())
    time.sleep(1)
    return n**2

p = Pool(3)
ret_l = []
for i in range(10):
    ret = p.apply_async(work, args=(i, )) # 异步调用
    ret_l.append(ret)
p.close()
p.join()
for ret in ret_l:
    print(ret.get())