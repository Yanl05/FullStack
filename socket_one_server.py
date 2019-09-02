# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/9/2 
# @Author  : yanlei
# @FileName: socket_one_server.py
"""
# TCP服务端
# 1.创建套接字socket
# 2.绑定端口bind
# 3. 侦听客户请求listen
# 4. 接受客户连接accept
# 5. 接受/发送
# 6. 关闭套接字
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))  # bind('ip', port)
sk.listen()

conn, addr = sk.accept()  # connect 连接， address 地址

ret = conn.recv(1024)  # receive   revv(1024) 一次接受1024个字节
print(ret)
conn.send(b'hello')  # 只能发送bytes类型数据3

# 先关闭连接，再关闭套接字
conn.close()
sk.close()


