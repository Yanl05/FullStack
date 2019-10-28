# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-28 20:06
# @Author  : yanlei
# @FileName: 线程池

从concurrent.futures中导入线程池。（也可以导入进程池，用法一样）
"""
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time

def func(n):
    time.sleep(2)
    print(n)
    return n*n


def call_back(ret):
    print('结果是%s'%ret.result())


# t_list = []
# t_pool = ThreadPoolExecutor(max_workers=5)  # 设置线程池中线程的个数，不要超过cpu数*5
# for i in range(20):
#     t = t_pool.submit(func, i)  # 提交任务，submit可以取得返回值。 map不能获取返回值
#     t_list.append(t)
# t_pool.shutdown()  # shutdown 功能等于 t_pool.close() + t_pool.join()
# for t in t_list:  # 如果上面没有执行shutdown()，则一次执行5个线程后就输出5个结果
#     print('t的值', t.result())  # t.result() 从t对象中获取具体的值
#

# map
# t_pool = ThreadPoolExecutor(max_workers=5)
# t_pool.map(func, range(20))  # map拿不到func的返回值


# add_done_callback  回调函数
# 用法一：
# t_list = []
# t_pool = ThreadPoolExecutor(max_workers=5)  # 设置线程池中线程的个数，不要超过cpu数*5
# for i in range(20):
#     t_pool.submit(func, i).add_done_callback(call_back)


# 用法二：
# t_list = []
# t_pool = ThreadPoolExecutor(max_workers=5)  # 设置线程池中线程的个数，不要超过cpu数*5
# for i in range(20):
#     t = t_pool.submit(func, i)
#     t_list.append(t)
# t_pool.shutdown()
# for t in t_list:
#     t.add_done_callback(call_back)
