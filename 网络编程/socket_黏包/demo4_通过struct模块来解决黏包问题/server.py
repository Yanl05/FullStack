# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 10:30
# @Author  : yanlei
# @FileName: server.py

"""
# 1. 开套接字
# 2. 绑定ip and 端口
# 3. 开始监听
# 4. 接收 连接 与 地址
# 5. 发送信息/接收信息
# 6. 关闭连接 and 关闭端口
import socket
import struct
sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.bind(ip_port)
sk.listen()

conn, addr = sk.accept()
while True:
    cmd = input('>>>请输入命令：')
    if cmd == 'q':
        conn.send(b'q')
        break
    conn.send(cmd.encode('gbk'))
    cmd_len_bytes = conn.recv(4)  # 将数据包的大小转换成了长度为4的bytes类型，直接接受长度为4的数据就是数据包的长度了
    cmd_len = struct.unpack('i', cmd_len_bytes)[0]  # unpack 解压缩后得到一个元组，元组中的第一个元素就是要获得的数据包的大小-int型
    cmd_detail = conn.recv(cmd_len).decode('gbk')
    print(cmd_detail)

conn.close()
sk.close()
