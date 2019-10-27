# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-26 08:52
# @Author  : yanlei
# @FileName: 线程锁.py
"""
# GIL 全局解释锁
# import time
# from threading import Thread, Lock
#
# def func():
#     global n
#     temp = n
#     time.sleep(0.2)  # 线程阻塞
#     n = temp - 1
#
#
# n = 10
# t_list = []
# for i in range(10):
#     t = Thread(target=func)
#     t.start()
#     t_list.append(t)
# for t in t_list:t.join() # 等待所有线程执行完毕
# print(n)
# 运行结果： 9
# 没有加线程锁，只靠GIL,当线程阻塞时，线程会让出锁，让其他线程访问cpu。此时，无法保证数据安全


# 加线程锁  -- 互斥锁
# import time
# from threading import Thread, Lock
#
# def func(lock):
#     lock.acquire()
#     global n
#     temp = n
#     time.sleep(0.2)  # 线程阻塞
#     n = temp - 1
#     lock.release()
#
#
# n = 10
# t_list = []
# lock = Lock()
# for i in range(10):
#     t = Thread(target=func, args=(lock, ))
#     t.start()
#     t_list.append(t)
# for t in t_list:t.join() # 等待所有线程执行完毕
# print(n)

# 互斥锁 Lock
# 科学家吃面问题  需要 拿到 叉 和 面 才能吃到面
from threading import Lock, Thread
import time
fork_lock = Lock()
noodle_lock = Lock()
def eat1(name):
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    noodle_lock.acquire()
    print('%s拿到面条了'%name)
    print('%s开始吃面了'%name)
    noodle_lock.release()
    fork_lock.release()

def eat2(name):
    noodle_lock.acquire()
    print('%s拿到面条了' % name)
    time.sleep(1)
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    print('%s开始吃面了'%name)
    fork_lock.release()
    noodle_lock.release()

Thread(target=eat1, args=('jobs', )).start()
Thread(target=eat2, args=('steve', )).start()
Thread(target=eat1, args=('bob', )).start()
# 1. jobs先拿到叉子和面条，开始吃面，然后归还了锁
# 2. steve拿到面条，阻塞一秒，阻塞的同时 bob拿到了叉子， 由于需要同时拿到两把锁才能开始吃面，所以此时程序开始挂起进入死锁。



# 加线程锁 --- 递归锁 RLock   -> 在一个线程中可以被acquire多次  (相当于多个锁都在一起，拿到一个锁的时候就等于拿到了全部到锁，其他线程无法在拿到锁，解决了死锁问题)
from threading import RLock, Thread
import time
fork_lock = noodle_lock = RLock()
def eat1(name):
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    noodle_lock.acquire()
    print('%s拿到面条了'%name)
    print('%s开始吃面了'%name)
    noodle_lock.release()
    fork_lock.release()

def eat2(name):
    noodle_lock.acquire()
    print('%s拿到面条了' % name)
    time.sleep(1)
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    print('%s开始吃面了'%name)
    fork_lock.release()
    noodle_lock.release()

Thread(target=eat1, args=('jobs', )).start()
Thread(target=eat2, args=('steve', )).start()
Thread(target=eat1, args=('bob', )).start()