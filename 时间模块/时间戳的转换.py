# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-28 20:41
# @Author  : yanlei
# @FileName: 时间戳的转换.py
"""
import time

now_time = time.time()
print(now_time)
print(int(now_time))
print(time.localtime(now_time))
print(time.strftime("%Y-%m-%d %X", time.localtime(now_time)))
