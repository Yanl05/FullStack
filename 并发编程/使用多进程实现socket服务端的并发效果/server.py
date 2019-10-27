# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 10:49
# @Author  : yanlei
# @FileName: server.py

多进程实现socket的并发效果 服务端
"""
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1', 8080))
# sk.listen()
#
# conn, addr = sk.accept()
# conn.send(('hello').encode('utf-8'))
# msg = conn.recv(1024).decode('utf-8')
# print(msg)
#
# conn.close()
# sk.close()


import socket
from multiprocessing import Process


def server(conn):
    conn.send(('hello').encode('utf-8'))
    msg = conn.recv(1024).decode('utf-8')
    print(msg)

    conn.close()


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
while True:
    conn, addr = sk.accept()  # 收到一个连接，就开启一个进程。
    p = Process(target=server, args=(conn, ))
    p.start()

sk.close()

