# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/13 
# @Author  : yanlei
# @FileName: 利用生成器监听文件输入.py

利用生成器监听文件的输入
"""
def tail(filename):
    f = open(filename, encoding='utf-8')
    while True:
        line = f.readline()
        if line.strip():
            yield line.strip()

g = tail('input_generator')
for i in g:
    if 'yan' in i:
        print(i)