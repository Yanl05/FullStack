# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 09:38
# @Author  : yanlei
# @FileName: 开启多个子进程.py
"""
from multiprocessing import Process
import os

def func(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# 开启十个进程，同时开始写，等待全部写完后，展示文件夹中的所有文件
p_list = []
for i in range(10):
    p = Process(target=func, args=('info%s'%i, 'content%s'%i))
    p_list.append(p)
    p.start()
[p.join() for p in p_list]  # p.join()  是感知一个子进程的结束，将异步的程序改为同步
print([i for i in os.walk('/Users/yanl/PycharmProjects/FullStack/并发编程')])