# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-27 15:57
# @Author  : yanlei
# @FileName: 条件.py
"""
from threading import Condition, Thread

def func(con, i):
    con.acquire()
    con.wait()
    print('当前在第%s个循环中'%i)
    con.release()


con = Condition()
for i in range(10):
    Thread(target=func, args=(con, i)).start()
while True:
    num = int(input('>>>'))
    con.acquire()
    con.notify(num)
    con.release()