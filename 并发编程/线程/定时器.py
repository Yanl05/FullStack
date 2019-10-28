# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-27 15:57
# @Author  : yanlei
# @FileName: 定时器.py

"""
# 每隔5秒，开启一个线程执行func中的代码。
from threading import Timer
import time


def func():
    print('时间同步相关code')


while True:
    Timer(5, func).start()
    time.sleep(5)
# 由于while True会一直快速执行以下的代码，需要在while True下面添加sleep(5)
# 这样就是完整的5秒，不多不少。 如果sleep(5)在func中添加，则会加上程序的运行时间，时间会超过5秒
