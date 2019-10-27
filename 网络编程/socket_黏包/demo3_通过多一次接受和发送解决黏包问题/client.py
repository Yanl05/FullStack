# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 10:11
# @Author  : yanlei
# @FileName: client.py


"""
import socket
import subprocess

sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)

while True:
    cmd = sk.recv(1024).decode('gbk')
    if cmd == 'q':
        break
    ret = subprocess.Popen(cmd, shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    cmd_out = ret.stdout.read()
    cmd_err = ret.stderr.read()
    cmd_len = str(len(cmd_out) + len(cmd_err)).encode('gbk')
    sk.send(cmd_len)
    sk.recv(1024)  # 用来接收服务端发送的ok。只是为了隔离上面发送的数据包的大小与下面发送的具体的数据包内容，防止tcp优化算法将其一起发送过去
    sk.send(cmd_out)
    sk.send(cmd_err)

sk.close()