# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-25 15:03
# @Author  : yanlei
# @FileName: 封装.py
"""
class Person:
    __key = 123  # 静态私有属性
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd  # 私有属性

    def __get_pwd(self):  # 私有方法
        print(self.__dict__)
        return self.__passwd  # 只要在类的内部调用私有属性，都会自动加上 _类名

    def login(self):
        return self.__get_pwd()


test1 = Person('yan', '123456')
print(test1._Person__passwd)  # _类名__属性名
test1.__one = 1  # 在类的外部不能创建私有属性，此处创建的并不是私有静态属性
print(test1.__one)
print(test1.login())
print(test1.__get_pwd())  # 在类的外面不能调用私有方法