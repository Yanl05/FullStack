# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-28 17:05
# @Author  : yanlei
# @FileName: 队列.py
"""
import queue

q = queue.Queue()
q.put_nowait(1)
value = q.get()
print(value)

q = queue.PriorityQueue()
q.put((20, 'a'))
q.put((10, 'b'))
q.put((30, 'c'))

print(q.get())