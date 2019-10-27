# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 10:05
# @Author  : yanlei
# @FileName: 事件.py

事件的一些简单操作

举例：红绿灯事件
"""
# from multiprocessing import Event
#
# e = Event()  # 实例化一个事件对象
# # 一个事件创建之后，默认是阻塞状态
# print(e.is_set())  # e.is_set() 查看当前事件是否阻塞，False为阻塞状态
# e.set()  # 将当前事件 解除阻塞
# print(e.is_set())
# e.clear()
# print(e.is_set())
# e.wait()  # 如果当前状态为阻塞，则会一直等待


# 红绿灯事件
from multiprocessing import Process, Event
import random, time

def traffic_light(e):
    while True:
        if not e.is_set():
            e.set()
            print('绿灯亮')
        else:
            e.clear()
            print('红灯亮')
        time.sleep(1)

def cars(e, i):
    if not e.is_set():
        print('%s号车在等红灯'%i)
        e.wait()
    print('%s号车通行'%i)





e = Event()
traffic = Process(target=traffic_light, args=(e, ))
traffic.start()
for i in range(20):
    car = Process(target=cars, args=(e, i))
    car.start()
    time.sleep(random.random())