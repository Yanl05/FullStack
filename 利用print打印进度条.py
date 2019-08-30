# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/15 
# @Author  : yanlei
# @FileName: 利用print打印进度条.py
"""
# import time
#
# for i in range(0, 101, 2):
#     time.sleep(0.1)
#     char_num = i // 2  # 打印多少个'*'
#     per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s' % (i, '*' * char_num)
#     print(per_str, end='', flush=True)
# \r 可以把光标移动到行首但不换行


# \n	回车，光标在下一行
# \r	换行，光标在上一行

import re

list = ['1111', '0000', '1111', '0000', '000']

pattern = re.compile(r'^0000')
for i in list:
    print(re.match(pattern, i))
