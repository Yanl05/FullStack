# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-22 15:22
# @Author  : yanlei
# @FileName: 继承.py
"""


class Animal:
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

    def eat(self):
        print('animal eating')


class Dog(Animal):
    def __init__(self, name, aggr, hp, kind):
        Animal.__init__(self, name, aggr, hp)
        self.kind = kind


zhao = Dog('zhaoritian', 100, 50, 'teddy')
print(zhao.name)
