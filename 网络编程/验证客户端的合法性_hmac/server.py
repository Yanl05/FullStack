# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 17:47
# @Author  : yanlei
# @FileName: server.py
"""
import hmac
import socket

def check_conn(conn):
    pass

# 配置
ip_port = ('127.0.0.1', 8080)
secret_key = b'key'  # 设置hmac的密钥

# 开套接字
sk = socket.socket()
sk.bind(ip_port)
sk.listen()


