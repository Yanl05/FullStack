# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 08:16
# @Author  : yanlei
# @FileName: socket_client.py
"""
import socket
import json


class MySocketClient:
    __instance = None  # 设置为单例模式
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1', 8080))

    def mysend(self, msg):
        ret_json = json.dumps(msg)
        self.sk.send(ret_json.encode('utf-8'))

