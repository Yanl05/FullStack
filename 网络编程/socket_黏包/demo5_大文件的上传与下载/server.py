# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 11:41
# @Author  : yanlei
# @FileName: server.py

文件传输服务端，提供文件 供客户端下载
"""
import socket
import os
import struct
import json

# 配置
ip_port = ('127.0.0.1', 8080)
buffer = 4096

# 开套接字
sk = socket.socket()
sk.bind(ip_port)
sk.listen()
conn, addr = sk.accept()

# 文件报头
head = {'filename':'轮到你了 反击篇.Anata.no.Ban.Desu.Hangeki.hen.Ep20.Final.Chi_Jap.HDTVrip.1280X720.mp4',
        'filesize':None,  # 文件大小暂时未知，需要计算
        'filetype':None,
        'filepath':'/Users/yanl/Downloads/rrshare/轮到你了 反击篇'}
file_path = os.path.join(head['filepath'], head['filename'])
file_size = os.path.getsize(file_path)
head['filesize'] = file_size
# 获取文件后缀
file_type = os.path.splitext(file_path)  # os.path.splitext(path)	分割路径，返回路径名和文件扩展名的元组
file_type = file_type[1][1:]  # splitext返回一个元组，第一项为文件的绝对路径，第二项为 .mp4   去掉第一个点就是文件的后缀
head['filetype'] = file_type
# 转换成json格式，在网络上传输
json_head = json.dumps(head)  # 字典转换成字符串
bytes_head = json_head.encode('utf-8')  # 字符串转换成bytes

bytes_head_len = struct.pack('i', len(bytes_head))
conn.send(bytes_head_len)  # 先将报头的长度传输过去
conn.send(bytes_head)  # 再传送报头字典
with open(file_path, 'rb') as f:  # 再传输文件
    while file_size:
        if file_size >= buffer:
            content = f.read(buffer)
            conn.send(content)
            file_size -= buffer
        else:
            content = f.read(file_size)
            conn.send(content)
            break

conn.close()
sk.close()
