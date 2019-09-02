# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/9/2 
# @Author  : yanlei
# @FileName: socket_one_client.py
"""
# TCP客户端
# 1. 创建套接字
# 2. 连接服务器
# 3. 发送/接受
# 4. 关闭套接字
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

sk.send(b'hi')
ret = sk.recv(1024)
print(ret)

sk.close()
