# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 09:22
# @Author  : yanlei
# @FileName: views.py
"""
from core.user import User
from conf import settings
import os
import pickle


def login(msg):
    print(msg)


def register(msg):
    print(msg)
    # username password
    # 创建一个属于这个用户的家目录，并记录下来
    # 把用户名密码 写进userinfo文件里，记录用户名
    # 记录用户的初始磁盘配额
    # 记录用户当前所在的目录
    user_obj = User(msg)
    # 将用户信息写入文件，再将文件路径写到userinfo中
    pickle_path = os.path.join(settings.pickle_path, msg['username'])
    with open(pickle_path, 'wb') as f:
        pickle.dump(user_obj, f)
    with open(settings.user_info, 'a') as f:
        f.write('%s|%s|%s'%(msg['username'], msg['password'], pickle_path))
    os.mkdir(user_obj.home)  # 创建家目录
    
    return True


def Upload(msg):
    pass

def Downloads(msg):
    pass