# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/29 
# @Author  : yanlei
# @FileName: 类的内置方法进阶.py
"""
# 卡牌游戏
# from collections import namedtuple
#
#
# Card = namedtuple('Card', ['rank', 'suit'])
#
#
# class FrankDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = ['红心', '方块', '梅花', '黑桃']
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for rank in FrankDeck.ranks for suit in FrankDeck.suits]
#
#     def __str__(self):  # 必须返回字符串类型
#         return str(self._cards)
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return self._cards[item]
#
#     def __setitem__(self, key, value):
#         self._cards[key] = value
#
# deck = FrankDeck()
# print(deck)  # 如果不重写__str__方法，则返回deck的内存地址。可以重写__str__方法，使其输出所有的卡片
# print(deck[0])
# # 随机抽牌
# from random import choice
# print(choice(deck))  # choice依赖类中的__getitem__方法
# # 洗牌
# from random import shuffle
# shuffle(deck)  # shuffle 依赖类中的__setitem__方法
# print(deck[0])


# 面试题  从100个对象中，根据name，sex去重（nema与sex相同，age可能不同）
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
        return False

    def __hash__(self):
        return hash(self.name + self.sex)

p1 = Person('taylor', 'female', 18)
p2 = Person('taylor', 'female', 20)
p3 = Person('seift', 'male', 20)
print(set((p1, p2, p3)))
ret = set((p1, p2, p3))
for item in ret:
    print(item.name)