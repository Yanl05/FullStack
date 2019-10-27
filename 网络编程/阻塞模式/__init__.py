# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-21 10:30
# @Author  : yanlei
# @FileName: __init__.py.py
"""
import socket
sk = socket.socket()
sk.setblocking(False)    # 如果设置为false 则accept没收到就pass了，不会一直等待
sk.bind(('127.0.0.1', 8080))
sk.listen()

try:
    conn, addr = sk.accept()
except BlockingIOError:
    pass
print('++++++++++++')
