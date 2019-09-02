# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/9/2 
# @Author  : yanlei
# @FileName: socket_two_server.py
"""
# 话痨聊天
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
while True:
    ret = conn.recv(1024).decode('utf-8')
    if ret == 'bye':
        conn.send(bytes('bye', encoding='utf-8'))
        break
    print(ret)
    conn.send(bytes(input('>>>'), encoding='utf-8'))




conn.close()
sk.close()