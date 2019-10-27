# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 07:56
# @Author  : yanlei
# @FileName: start.py
"""
import os
import sys

# print(sys.path)
# print(os.path.dirname(os.getcwd()))  # 获取当前目录的父目录
sys.path.append(os.path.dirname(os.getcwd()))  # 将当前客户端根目录放到系统路径下，方便导入模块
print(sys.path)


from core import client
if __name__ == '__main__':
    client.main()

