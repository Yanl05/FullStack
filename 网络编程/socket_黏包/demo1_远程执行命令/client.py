# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-09 10:28
# @Author  : yanlei
# @FileName: client.py

接受server端的命令后自己在机器上执行
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
    ret = subprocess.Popen(cmd, shell=True,  # shell=True 直接执行操作系统的命令
                     stdout=subprocess.PIPE,  # 从管道中提取输出信息与错误信息
                     stderr=subprocess.PIPE)
    sk.send(ret.stdout.read())
    sk.send(ret.stderr.read())

sk.close()