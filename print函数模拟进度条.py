# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-12 11:42
# @Author  : yanlei
# @FileName: print函数模拟进度条.py

print 默认end为 \n，  将print的\n 替换为空，并且每次print，都用\r 先回车  会到行首
"""
import time


# def progress_bar():
#     progress = 0
#     while progress <= 100:
#         time.sleep(0.1)
#         ret = divmod(progress, 2)
#         consult = ret[0]
#         remainder = ret[1]
#         if remainder == 0:
#             print('\r'+ str(progress) + '%' + (consult * '*'), end=' ')
#         progress += 1
#
# progress_bar()

# 固定每次print的输出长度
def progress_bar():
    progress = 0
    lenbar = 60  # 每次print的输出长度
    while progress <= 100:
        time.sleep(0.01)
        ret = divmod(progress, 2)
        consult = ret[0]
        remainder = ret[1]
        if remainder == 0:
            bar = '\r'+ str(progress) + '%' + (consult * '*')
            print(bar + ' '*(lenbar-len(bar)), end=' ')

        progress += 1

progress_bar()
