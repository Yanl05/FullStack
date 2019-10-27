# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-09 10:28
# @Author  : yanlei
# @FileName: server.py

远程执行cmd命令
"""
import socket
sk = socket.socket()

sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
while True:
    cmd = input('>>>').encode('gbk')
    if cmd == b'q':
        conn.send(b'q')
        break
    conn.send(cmd)
    ret = conn.recv(1024).decode('gbk')
    print(ret)

conn.close()
sk.close()
