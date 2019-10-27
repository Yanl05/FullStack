# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 10:32
# @Author  : yanlei
# @FileName: client.py
"""
import socket
import subprocess
import struct

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
    cmd_len = len(cmd_out) + len(cmd_err)
    cmd_len_bytes = struct.pack('i', cmd_len)
    sk.send(cmd_len_bytes)
    sk.send(cmd_out)
    sk.send(cmd_err)

sk.close()