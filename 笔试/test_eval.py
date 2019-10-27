# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-17 13:48
# @Author  : yanlei
# @FileName: test_eval.py
"""
# a = "print('abc')"
# eval(a)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        print(self.a)
        return x

myclass = MyNumbers()
myiter = iter(myclass)
# myiter = myclass.__iter__()

# print(myiter)
print(next(myiter))
print(next(myiter))
# print(myclass)