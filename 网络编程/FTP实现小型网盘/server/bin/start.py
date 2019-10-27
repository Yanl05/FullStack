# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 08:51
# @Author  : yanlei
# @FileName: start.py
"""
import os
import sys
from core.server import MyFTPServer
import socketserver
from conf import settings

sys.path.append(os.path.dirname(os.getcwd()))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(settings.addr, MyFTPServer)
    server.serve_forever()
