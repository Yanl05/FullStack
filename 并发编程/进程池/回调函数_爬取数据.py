# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-23 22:05
# @Author  : yanlei
# @FileName: 回调函数_爬取数据.py
"""
import requests
from multiprocessing import Pool

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return url, response.content.decode('utf-8')

def call_back(args):
    url, content = args
    print(url, len(content))

url_list = [
    'https://www.baidu.com',
    'https://www.sohu.com',
    'https://www.sogou.com',
    'https://www.runoob.com',
    'https://leetcode-cn.com',
    'https://cn.bing.com',
]

p = Pool(2)
for url in url_list:
    p.apply_async(get_data, args=(url, ), callback=call_back)
p.close()
p.join()


