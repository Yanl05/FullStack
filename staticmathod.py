# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-26 13:06
# @Author  : yanlei
# @FileName: staticmathod.py
"""
class Goods:
    __discount = 0.8
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Goods.__discount

    @classmethod  # 把一个方法 变成一个类中的方法，这个方法就可以直接被类调用，不需要依托任何对象
    def change_discount(cls, new_discount):  # 修改折扣
        cls.__discount = new_discount


apple = Goods('苹果', 5)
print(apple.price)
Goods.change_discount(0.5)  # 直接被类调用，不用依托任何对象
print(apple.price)



class Login:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def login(self):
        pass

    @staticmethod  # 静态方法
    def get_usr_pwd():
        usr = input('username:')
        pwd = input('password:')
        Login(usr, pwd)

Login.get_usr_pwd()
# 在完全面向对象的程序中，如果一个函数，即和对象没有关系，也和类没有关系，那么就用staticmethod将这个函数变成一个静态方法
