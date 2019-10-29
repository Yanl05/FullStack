# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-29 10:09
# @Author  : yanlei
# @FileName: 协程.py


"""
# 多任务之间切换的方法 greenlet模块   （协程）
# from greenlet import greenlet
# def eat():
#     print('eating start')
#     g2.switch()  # 切换到对应的方法，接着执行
#     print('eating end')
#
#
# def play():
#     print('playing start')
#
# g2 = greenlet(play)
# g1 = greenlet(eat)
# g1.switch()

from gevent import monkey;monkey.patch_all()
import time
import gevent
def eat(i):
    print('eating start')
    time.sleep(2)  # gevent 感知不到其他模块（time或其他阻塞）的阻塞。只能用gevent.sleep()
    # 不过可以通过打补丁实现感知time 、 socket的阻塞  from gevent import monkey:monkey.patch_all()
    print('eating end')
    return '%send'%i


def play():
    print('playing start')
    time.sleep(2)
    print('playing end')

# g1 = gevent.spawn(eat)  # 将func注册在协程中
# g2 = gevent.spawn(play)
# g1.join()  # 等待协程执行完毕
# g2.join()

g_list = []
ge_list = []
for i in range(10):
    ge = gevent.spawn(play)
    ge_list.append(ge)


for i in range(20):
    g = gevent.spawn(eat, i)
    g_list.append(g)

for ge in ge_list: ge.join()  # 等待所有协程执行完毕的 方法一
gevent.joinall(g_list)        # 等待所有协程执行完毕的 方法二

for g in g_list:print(g.value)  # 获得func的返回值

