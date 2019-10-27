# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 11:41
# @Author  : yanlei
# @FileName: client.py

文件传输，从服务端下载文件到本地
"""
import os
import struct
import socket
import json

# 配置
buffer = 4096
ip_port = ('127.0.0.1', 8080)

# 开套接字
sk = socket.socket()
sk.connect(ip_port)

# 先获得报头长度
# 再接收报头
# 再接收file
head_size = sk.recv(4)
head_size = struct.unpack('i', head_size)[0]
json_head = sk.recv(head_size).decode('utf-8')
head = json.loads(json_head)
file_size = head['filesize']
with open(head['filename'], 'wb') as f:
    while file_size:
        if file_size >= buffer:
            content = sk.recv(buffer)
            f.write(content)
            file_size -= buffer
        else:
            content = sk.recv(file_size)
            f.write(content)
            break

sk.close()

