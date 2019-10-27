# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-09 11:31
# @Author  : yanlei
# @FileName: server.py
"""
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()

ret1 = conn.recv(12)
ret2 = conn.recv(2)  # ret1将客户端发送过来的两个数据包都接受了，由于tcp的优化算法，ret2只会接受到一个空字符串
print(ret1)
print(ret2)
'''
b'helloworld'
b''
'''
conn.close()
sk.close()
