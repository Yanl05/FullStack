# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-09 11:31
# @Author  : yanlei
# @FileName: client.py
"""
import socket
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)

sk.send(b'hello')
sk.send(b'world')

sk.close()