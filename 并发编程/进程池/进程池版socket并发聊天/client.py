# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 17:14
# @Author  : yanlei
# @FileName: client.py
"""
from socket import *
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>>').strip()
    if not msg:break

    client.send(msg.encode('utf-8'))
    msg = client.recv(1024)
    print(msg.decode('utf-8'))