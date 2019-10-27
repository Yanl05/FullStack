# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-07 11:49
# @Author  : yanlei
# @FileName: udp_tiaolian_server.py

利用upd实现聊天功能
服务端
"""
import socket
# 1. 创建udp连接
sk = socket.socket(type=socket.SOCK_DGRAM)  # datagram 数据报文
# 2. 起服务
sk.bind(('127.0.0.1', 8080))

# 3. 等待客户端来连接
msg, addr = sk.recvfrom(1024)  # 通过recvfrom设定一个报文的大小，并获得一个数据报文与客户端地址
print(msg.decode('utf-8'))
sk.sendto(input('服务端回复：>>>').encode('utf-8'), addr)

sk.close()
