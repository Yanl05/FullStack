# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-29 21:09
# @Author  : yanlei
# @FileName: server.py

协程  tcp
"""
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

while True:
    conn, addr = sk.accept()
    conn.send(b'hello')
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    conn.close()

sk.close()
