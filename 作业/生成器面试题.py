# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/14 
# @Author  : yanlei
# @FileName: 生成器面试题.py
"""
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(g2.__next__())
# print(g2.__next__())
# print(g2.__next__())
# print(g2.__next__())

# print(list(g1))
# print(list(g2))





def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()
# print(list(g))
for n in [1,10]:
    g=(add(n,i) for i in g)

print(list(g))


