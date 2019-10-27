# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-27 14:43
# @Author  : yanlei
# @FileName: 事件.py

模拟数据库连接
"""
import time
import random
from threading import Thread, Event

def connect_db(e):
    try:
        count = 0  # 设置连接次数
        while count < 3:
            e.wait(0.5)  # 状态为false，阻塞状态只等待 timeout 参数的时间
            if e.is_set() == True:
                print('连接数据库成功')
                break
            else:
                count += 1
                print('第%s次连接失败'%count)
        else:
            raise TimeoutError('数据库连接失败')
    except TimeoutError as e:
        print(e)



def check_web(e):
    time.sleep(random.randint(0, 3))
    e.set()  # 将事件解除阻塞


e =Event()
t1 = Thread(target=check_web, args=(e, ))
t2 = Thread(target=connect_db, args=(e, ))
t1.start()
t2.start()

