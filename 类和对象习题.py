# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-22 09:51
# @Author  : yanlei
# @FileName: 类和对象习题.py

创建一个类，每实例化一个对象就计数
最终所有的对象共享这个数据
"""

class Foo:
    count = 0
    def __init__(self):
        Foo.count += 1

a = Foo()
a = Foo()
a = Foo()
print(a.count)