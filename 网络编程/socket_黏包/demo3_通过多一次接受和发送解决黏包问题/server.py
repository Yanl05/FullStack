# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 10:04
# @Author  : yanlei
# @FileName: server.py

通过多一次recv与send先发送数据包的大小，然后确定第二次recv的数据包大小
"""
# 1. 开套接字
# 2. 绑定ip and 端口
# 3. 开始监听
# 4. 接收 连接 与 地址
# 5. 发送信息/接收信息
# 6. 关闭连接 and 关闭端口
import socket
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
    cmd_len = conn.recv(1024).decode('gbk')
    print(cmd_len)
    conn.send(b'ok')  # 为了防止tcp的优化算法，将几个小的连续的send的数据包一起发送产生黏包问题。发送一个ok已用来隔离客户端中数据包大小的send与数据包内容的send
    cmd_detail = conn.recv(int(cmd_len)).decode('gbk')
    print(cmd_detail)

conn.close()
sk.close()
