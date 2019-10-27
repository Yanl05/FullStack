# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-22 09:59
# @Author  : yanlei
# @FileName: 开启多进程的第二种方式.py

通过继承Process类（自定义类）
必须实现一个run方法，run方法中是在子进程中执行的代码
"""
# import os
# from multiprocessing import Process
#
# class MyProcess(Process):
#     def run(self) -> None:
#         print(self.pid)
#         print(self.name)
#         print('子进程的id', os.getpid())
#
#
# print('主进程的id：', os.getpid())
# p1 = MyProcess()
# p1.start()
# p2 = MyProcess()
# p2.start()


# 如何传参？
# --> 通过 __init__
from multiprocessing import Process
import os


class MyProcess(Process):
    def __init__(self, arg1, arg2):  # 继承了Process， __init__也要继承父类的__init__
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self) -> None:
        print(self.pid)
        print(self.name)
        print(self.arg1)


print('主进程的id：', os.getpid())
p1 = MyProcess(1, 3)
p1.start()


