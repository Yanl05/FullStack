# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/14 
# @Author  : yanlei
# @FileName: 生成器进阶_send.py

send注意事项：
 1.第一次使用生成器，使用next获取下一个值
 2.最后一个yield不能接受外部的值
 3.获取下一个值得时候，是给上一个yield的位置传值
"""
def generator():
    print(123)
    content = yield 1
    print('=========', content)
    print(456)
    yield 2
    print(789)
    yield

g = generator()  # 生成一个生成器
ret = g.__next__()
print(ret)
# ret = g.send(None)  # send的效果和next一样。 但是可以传值到函数中，如果不传值 要send(None)
ret = g.send('hello')
print(ret)
ret = g.__next__()
print(ret)


# send使用实例
# 移动平均数

# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum / count
#
# avg_g = average()
# avg_g.__next__()
# avg_1 = avg_g.send(10)
# print(avg_1)
# avg_2 = avg_g.send(20)
# print(avg_2)

# 装饰器 预激活版
def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()
        return g
    return inner

@init
def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count

avg_g = average()
avg_1 = avg_g.send(10)
print(avg_1)
avg_2 = avg_g.send(20)
print(avg_2)

