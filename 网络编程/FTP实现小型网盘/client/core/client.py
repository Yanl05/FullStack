# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-22 08:02
# @Author  : yanlei
# @FileName: client.py
"""
from core.auth_client import Auth


def main():
    auth_obj = None
    # 先选择 菜单功能： 登陆，注册，退出
    # 菜单，需要用到反射，如果使用字典的话，会使菜单无序
    start_l = [('登陆', 'login'), ('注册', 'register'), ('退出', 'quit')]
    for index, item in enumerate(start_l, 1):
        print(index, item[0])
    while True:
        try:
            num = int(input('>>>'))
            func_str = start_l[num-1][1]
        except:
            print('输入的信息有误')
            continue
        # 字符串数据类型的方法 login register quit

        if hasattr(Auth, func_str):  # 登陆 注册
            auth_obj = Auth()  # 未来防止总是生成新的auth对象，设置为单例模式
            func = getattr(auth_obj, func_str)
            ret = func()
            if ret:  # 如果登陆成功 或者 注册成功，跳出while循环
                break
        elif auth_obj:
            auth_obj.socket.sk.close()
            exit()
        else:
            exit()
