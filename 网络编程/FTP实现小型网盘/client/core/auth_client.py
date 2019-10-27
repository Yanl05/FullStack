# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 08:13
# @Author  : yanlei
# @FileName: auth_client.py
"""
from core.socket_client import MySocketClient

class Auth:
    def __init__(self):
        self.socket = MySocketClient()  # 组合：一个对象的属性是另一个类的对象
        self.username = None

    def login(self):
        username = input('username:')
        password = input('password:')
        # 基于TCP协议，保证发送的信息不为空
        if username.strip() and password.strip():
            # send
            msg = {'username': username, 'password': password, 'operation': 'login'}
            self.socket.mysend(msg)
        ret = self.socket.sk.recv(1024)
        return ret


    def register(self):
        username = input('username:')
        password1 = input('password:')
        password2 = input('password_ensure:')
        if username.strip() and password1.strip() and password1 == password2:
            # send
            msg = {'username': username, 'password': password1, 'operation': 'register'}
            self.socket.mysend(msg)
        ret = self.socket.sk.recv(1024)
        return ret
