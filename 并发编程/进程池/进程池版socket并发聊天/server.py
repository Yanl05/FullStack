# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 17:14
# @Author  : yanlei
# @FileName: server.py
"""
import os
from socket import *
from multiprocessing import Pool

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)

def talk(conn):
    print('进程pid：%s'%os.getpid())
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:break
            print(msg.decode('utf-8'))
            conn.send(msg.upper())
        except Exception:
            break

p = Pool(4)
while True:
    conn, *_ = server.accept()
    p.apply_async(talk, args=(conn, ))