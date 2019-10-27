# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 11:38
# @Author  : yanlei
# @FileName: 生产者消费者模型.py
"""
# from multiprocessing import Queue, Process
# import time, random
#
# def consumer(name, q):
#     while True:
#         food = q.get()
#         if not food:break
#         time.sleep(random.random())
#         print('\033[31m%s购买了%s\033[0m' % (name, food))
#
# def producer(name, food, q):
#     for i in range(10):
#         time.sleep(random.random())
#         print('%s生产了第%s个%s'%(name, i, food))
#         q.put(food)
#
# q = Queue()
# p1 = Process(target=producer, args=('Jobs', 'hamberger', q))
# p1.start()
# p2 = Process(target=producer, args=('Steve', 'cola', q))
# p2.start()
# c1 = Process(target=consumer, args=('kindle', q))
# c1.start()
# c2 = Process(target=consumer, args=('caps', q))
# c2.start()
# p1.join()
# p2.join()
# q.put(None)  # 通过给队列加None， 有几个消费者就需要添加几个None，比较蠢
# q.put(None)

# 通过JoinableQueue来实现生产者消费者模型。
from multiprocessing import JoinableQueue, Process
import time, random

def consumer(name, q):
    while True:
        food = q.get()
        time.sleep(random.random())
        print('\033[31m%s购买了%s\033[0m' % (name, food))
        q.task_done()

def producer(name, food, q):
    for i in range(10):
        time.sleep(random.random())
        print('%s生产了第%s个%s'%(name, i, food))
        q.put(food)
    # 当生产者生产完后，进程并没有马上结束。通过q.join()来阻塞，已延长生命周期
    q.join()  # 阻塞。直到一个队列中全部的数据 都被处理完毕。


q = JoinableQueue()
p1 = Process(target=producer, args=('Jobs', 'hamberger', q))
p1.start()
p2 = Process(target=producer, args=('Steve', 'cola', q))
p2.start()
c1 = Process(target=consumer, args=('kindle', q))
c2 = Process(target=consumer, args=('caps', q))
# 将消费者进程设置为守护进程。主进程代码执行完毕，就结束
c1.daemon = True
c2.daemon = True
c1.start()
c2.start()
p1.join()
p2.join()  # 主进程代码在此阻塞，等待生产者进程生命周期的结束（生产者进程被阻塞，需要等待消费者进程中q.task_done()来反馈已经全部处理完队列中的数据。）
## JoinableQueue 比 Queue 多了一个 q.task_done()的计数功能，当put进一个数据，队列中默认count+1，当get取出一个数据，并处理完后，q.task_done()会将默认的count-1，直到count=0，就将q.join()的阻塞状态改为非阻塞。
