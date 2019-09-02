# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/9/2 
# @Author  : yanlei
# @FileName: socket_two_client.py
"""
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    sk.send(bytes(input('>>>'), encoding='utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    if ret == 'bye':
        sk.send(b'bye')
        break
    print(ret)

sk.close()
