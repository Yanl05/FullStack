# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-11 17:37
# @Author  : yanlei
# @FileName: server.py

使用多线程，同时接收多个客户端的连接并接收与发送信息
"""
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print(self.client_address)
            msg = self.request.recv(1024).decode('utf-8')  # 根据源码可以了解 self.request 等价于 conn
            if msg == 'q':
                break
            print(msg)
            info = input('>>>')
            self.request.send(info.encode('utf-8'))


if __name__ == '__main__':
    # 根据源码可知道这一句等价于 起套接字socket.socket() 和 bind 和 listen()
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8081), MyServer)
    server.serve_forever()  # 相当于 accept()
