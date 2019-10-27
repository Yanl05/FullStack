# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 11:34
# @Author  : yanlei
# @FileName: 队列demo.py
"""
from multiprocessing import Queue, Process

def producer(q):
    q.put('hello')

def consumer(q):
    print(q.get())


q = Queue()
p = Process(target=producer, args=(q, ))
p.start()
c = Process(target=consumer, args=(q, ))
c.start()