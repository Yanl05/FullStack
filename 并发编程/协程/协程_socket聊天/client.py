# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-29 21:09
# @Author  : yanlei
# @FileName: client.py
"""
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

msg = sk.recv(1024).decode('utf-8')
print(msg)
send_msg = input('>>>')
sk.send(send_msg.encode('utf-8'))
sk.close()