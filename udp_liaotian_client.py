# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-07 11:55
# @Author  : yanlei
# @FileName: udp_liaotian_client.py

利用udp连接编写聊天功能，客户端
"""
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

msg = input('客户端发送：>>>').encode('utf-8')
sk.sendto(msg, ip_port)
ret, addr = sk.recvfrom(1024)
print(ret.decode('utf-8'))

sk.close()