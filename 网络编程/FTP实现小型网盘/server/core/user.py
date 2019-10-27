# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 09:52
# @Author  : yanlei
# @FileName: user.py
"""
from conf import settings
import os


class User:
    # 创建一个属于这个用户的家目录，并记录下来
    # 把用户名密码 写进userinfo文件里，记录用户名
    # 记录用户的初始磁盘配额
    # 记录用户当前所在的目录
    def __init__(self, msg):
        self.name = msg['username']
        self.home = os.path.join(settings.home_path, msg['username'])
        self.disk_space = settings.space
        self.file_num = 0  # 目录中的总文件数
        self.cur_path = self.home
        