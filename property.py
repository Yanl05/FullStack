# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-26 10:20
# @Author  : yanlei
# @FileName: property.py
"""
# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def perimeter(self):
#         return 2*pi*self.r
#
#     def area(self):
#         return self.r**2*pi
#
# c1 = Circle(5)
# print(c1.perimeter())

# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     @property
#     def perimeter(self):
#         return 2*pi*self.r
#
#     @property
#     def area(self):
#         return self.r**2*pi
#
# c1 = Circle(5)
# print(c1.perimeter)

class Goods:
    discount = 0.8
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Goods.discount


apple = Goods('苹果', 5)
print(apple.price)


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):  # 1
        return self.__name

    @name.deleter    # 2
    def name(self):  # 3   1,2,3 三处名称应该一样
        del self.__name

wang = Person('王力宏')
print(wang.name) # 能够输出name
del wang.name   # 删除了__name属性
print(wang.name)  # 报错