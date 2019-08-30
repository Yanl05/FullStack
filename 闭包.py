# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/13 
# @Author  : yanlei
# @FileName: 闭包.py
"""


# 闭包  内部函数调用外部函数的变量
# def outer():
#     a = 1
#     def inner():
#         print(a)
#     print(inner.__closure__)
# outer()

# def outer():
#     a = 1
#
#     def inner():
#         print(a)
#
#     print(inner.__closure__)
#     return inner
#
#
# inn = outer()
# inn()  # 每次调用不同重复生成a，a会保存在内存中


# from urllib.request import urlopen
# def get_url():
#     url = 'http://pianyuan.la/'
#     def get():
#         ret = urlopen(url).read()
#         print(ret)
#     return get
#
# get_func = get_url()
# get_func()


# 作用一 当闭包执行完后，仍然能够保持住当前的运行环境
origin = [0, 0]  # 坐标系统原点
legal_x = [0, 50]  # x, y 轴的合法坐标
legal_y = [0, 50]
def create(pos = origin):
    def player(direction, step):
        new_x = pos[0] + direction[0]*step
        new_y = pos[1] + direction[1]*step
        pos[0] = new_x
        pos[1] = new_y
        return pos
    return player

player = create()  # 创建棋子
print(player([1, 0], 10))
print(player([0, 1], 10))

# 作用二 闭包可以根据外部作用域的局部变量来得到不同的结果
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter
filter = make_filter('pass')
filter_result = filter('result.txt')