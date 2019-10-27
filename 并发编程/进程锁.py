# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 21:28
# @Author  : yanlei
# @FileName: 进程锁.py

通过买票问题，来理解进程锁
"""
from multiprocessing import Process
import time
import json
from multiprocessing import Lock  # 导入进程锁

def query(i):
    with open('ticket') as f:
        dic = json.load(f)
    print('%s查询到余票还有 ：%s 张'%(i, dic['ticket']))

def buy(i, lock):
    lock.acquire()  # 拿到锁  只有拿到锁的才能对数据库进行修改，数据库一次只能由一个对象进行修改
    with open('ticket') as f:
        dic = json.load(f)
    time.sleep(0.1)  # 模拟查询时的网络延迟
    if dic['ticket'] > 0:
        print('\033[0;31;0m %s买到票了\033[0m'%i)
        dic['ticket'] -= 1
    else:
        print('%s没有买到票'%i)
    time.sleep(0.1)
    with open('ticket', 'w') as f:
        json.dump(dic, f)

    lock.release()  # 归还锁


for i in range(10):
    p = Process(target=query, args=(i, ))  # 开启1买票0个查询线程，模拟并发
    p.start()

# 开启10个买票线程对一张票进行购买，模拟并发
lock = Lock()  # 先实例化一个锁的对象
for i in range(10):
    p = Process(target=buy, args=(i, lock))  # 将锁对象一并传递给buy
    p.start()
