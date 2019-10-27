# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 08:52
# @Author  : yanlei
# @FileName: server.py
"""
import socketserver
import json
from core import views
from conf import settings


class MyFTPServer(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.my_recv()
        func_str = msg['operation']
        if hasattr(views, func_str):
            func = getattr(views, func_str)
            ret = func(msg)
            self.my_send(ret)

        
        
    def my_recv(self):
        msg = self.request.recv(1024)
        msg = msg.decode(settings.code)
        msg = json.loads(msg)
        return msg

    def my_send(self, msg):
        msg = json.dumps(msg).encode(settings.code)
        self.request.send(msg)
    
    