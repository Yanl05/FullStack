# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-09-10 11:36
# @Author  : yanlei
# @FileName: 序列化.py
"""
import json
dic = {1:'a',2:'b序列化'}
f = open('file', 'w', encoding='utf-8')
# json.dump(dic, f)
json.dump(dic, f, ensure_ascii=False)   # ensure_ascii 设置为false可以在文件中显示中文，否则显示bytes
f.close()



f = open('file')
res = json.load(f)
f.close()
print(res)

dic = {1:'a',2:'b序列化'}
json_dic = json.dumps(dic, ensure_ascii=False)
print(json_dic)
