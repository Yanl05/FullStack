# # -*- coding: UTF-8 -*-
#
# """
# # @Time    : 2019-09-17 17:40
# # @Author  : yanlei
# # @FileName: test.py
# """
# import sys
# import collections
#
#
# def func(s):
#     count = collections.Counter(s)
#     stack = []
#     visited = collections.defaultdict(bool)
#     for num in s:
#         count[num] -= 1
#         if visited[num]:
#             continue
#         while stack and count[stack[-1]] and stack[-1] > num:
#             visited[stack[-1]] = False
#             stack.pop()
#         visited[num] = True
#         stack.append(num)
#     return "".join(stack)
#
#
# for line in sys.stdin:
#     print(func(line))

import sys
import math


# def func(num):
#     if -10 < num < 10:
#         return num
#     str_num = str(num)
#     if str_num[0] != "-":
#         str_num = str_num[::-1]
#         num = int(str_num)
#     else:
#         str_num = str_num[1:][::-1]
#         num = int(str_num)
#         num = -num
#     return num if -(2 ** 31) < num < (2 ** 31) - 1 else 0
#
#
# for line in sys.stdin:
#     print(func(int(line)))

# s = 'string'
# s[0] = 'a'
# print(s[0])

# tu = ('123', 122)
# # t2 = tu*2
# # print(type(t2))

# a = {'tom', 'jack'}
# print(a)
# print(type(a))

# dic = {}
# print(dic)
# print(type(dic))
# dic[('a',)] = 123
# print(dic)
# print(type(dic))

import copy
# a = {1: [1,2,3]}
# b = a
# b[0] = 456
# print(a)
# print(b)
# b = a.copy()
# print(id(a))
# print(id(b))
# x = a[1]
# x.append(4)
# print(a)
# print(b)

string = 'afasfhajifasfbfhaskfnqwihweruytuinzcvbnvzbvbxagsghlewtlqourpqurqpohbbzkziahiaiq'
alp_dict = {}
for i in string:
    keys = alp_dict.keys()
    if i not in keys:
        alp_dict[i] = 1
    else:
        alp_dict[i] += 1
print(alp_dict)
# 反转字典
# new_dict = dict(zip(alp_dict.values(), alp_dict.keys()))
new_dict = {}
for k,v in alp_dict.items():
    print(k,v)
    if v not in new_dict:
        new_dict[v] = k
    else:
        new_dict[v] = new_dict[v] + k
# print(alp_dict.items())
print(new_dict)
top10 = sorted(new_dict.keys(), reverse=True)[:3]
print(top10)
print(new_dict[top10[0]])
