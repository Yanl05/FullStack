# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 16:50
# @Author  : yanlei
# @FileName: 进程池的返回值.py
"""
import time
from multiprocessing import Pool
def func(i):
    time.sleep(2)
    return i*i

p = Pool(5)
res_l = []
for i in range(10):
    res = p.apply_async(func,args=(i, ))
    res_l.append(res)
for res in res_l:
    print(res.get())  # 等待func的计算结果
