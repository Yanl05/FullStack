# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-22 10:37
# @Author  : yanlei
# @FileName: 组合练习.py
"""
from math import pi
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r**2*pi
    def perimeter(self):
        return 2*pi*self.r

class Ring:
    def __init__(self, outside_r, inside_r):
        self.outside_c = Circle(outside_r)
        self.inside_c =Circle(inside_r)

    def area(self): return self.outside_c.area() - self.inside_c.area()
    def perimeter(self): return self.outside_c.perimeter() + self.inside_c.perimeter()

ring = Ring(20, 10)
print(ring.area())
print(ring.perimeter())