# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-11 17:37
# @Author  : yanlei
# @FileName: client2.py
"""
import socket

ip_port = ('127.0.0.1', 8081)

sk = socket.socket()
sk.connect(ip_port)


while True:
    info = input('>>>')
    sk.send(('client2'+info).encode('utf-8'))
    msg = sk.recv(1024).decode('utf-8')
    if msg == 'q':
        break
    print(msg)


sk.close()