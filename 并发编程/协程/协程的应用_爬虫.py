# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-10-29 19:36
# @Author  : yanlei
# @FileName: 协程的应用_爬虫.py
"""
# import requests
# def get_content(url):
#     content = requests.get(url)        # 通过request.get到的网页内容是无格式的
#     return content.content.decode('utf-8')
#
# url = 'http://www.baidu.com'
# print(get_content(url))


from gevent import monkey;monkey.patch_all()
import gevent
import ssl
from urllib.request import urlopen, Request
def get_content(url):
    context = ssl._create_unverified_context()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    get_url = Request(url=url, headers=headers)
    content = urlopen(get_url, context=context)        # urlopen到的网页内容是有格式的
    text = content.read().decode('utf-8')
    return len(text)

url_list = ['http://www.baidu.com',
            'http://www.jianshu.com',
            'http://www.csdn.com',
            'http://www.cctv.com',
            'http://www.sogou.com']
# 通过协程来并发获得网页内容的长度
g_list = []
for i in range(len(url_list)):
    g = gevent.spawn(get_content, url_list[i])
    g_list.append(g)
for g in g_list:g.join()
for g in g_list:print(g.value)
