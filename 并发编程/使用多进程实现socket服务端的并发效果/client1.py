# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 10:49
# @Author  : yanlei
# @FileName: client.py

多进程实现socket的并发效果 服务端
"""
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

msg = sk.recv(1024).decode('utf-8')
print(msg)
sendmsg = input('>>>').encode('utf-8')
sk.send(sendmsg)

sk.close()


