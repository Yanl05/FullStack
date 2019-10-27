# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-11 20:57
# @Author  : yanlei
# @FileName: test.py
"""
class Base:
    def __init__(self, name):
        self.name = name
        self.Testfunc()  # self 是谁的对象就先从谁中找方法

    def Testfunc(self):
        print('do Base Testfunc')

class Son(Base):
    def Testfunc(self):
        print('do Son Testfunc')


sonobj = Son('zhang')
# 创建一个子类对象，先执行init方法，son中没有，从父类中找，执行父类中的init方法，其中self.Testfunc() Testfunc方法父类，子类中都有，
# 看self是谁的对象，self是创建的子类对象，现在子类Son中找该方法，如果没有再从父类中找

# 输出 do Son Testfunc
