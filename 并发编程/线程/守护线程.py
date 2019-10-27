# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-25 10:49
# @Author  : yanlei
# @FileName: 守护线程.py
"""
from threading import Thread
import time

def func():
    print('子线程 is running')
    time.sleep(5)
def func2():
    while True:
        print('守护线程 is running')
        time.sleep(1)



# 开启线程
t1 = Thread(target=func)
t1.start()
t2 = Thread(target=func2)
t2.daemon = True
t2.start()
print('主线程结束')

# 主线程会等待所有非守护线程结束后才算运行完毕。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收。
# 在主线程结束(其他非主线程非守护线程全部结束)后，守护线程会立即结束。

