# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/9/2 
# @Author  : yanlei
# @FileName: hashlib初识.py
"""
# 登录验证
# 加密 ->  解密
# 摘要算法
import hashlib
md5 = hashlib.md5()  # md5 可以替换为其他摘要算法
# md5.update(b'yanlei')  # 此处需要二进制格式
md5.update(bytes('951105', encoding='utf-8'))
print(md5.hexdigest())


import hashlib
md5 = hashlib.md5()  # md5 可以替换为其他摘要算法
# md5.update(b'yanlei')  # 此处需要二进制格式
# md5.update(bytes('951105', encoding='utf-8'))
md5.update(b'95')
md5.update(b'1105')
print(md5.hexdigest())
# md5 可以替换为其他摘要算法
# sha 算法 随着算法复杂程度的增加 ，摘要的时间成本和空间成本都会增加


# 摘要算法
# 密码的密文存储
# 文件的一致性验证
    # 在下载的时候，检查我们下载的文件和远程服务器上的文件是否一致
    # 两台机器上的两个文件，检验是否相等

# 模拟用户的登录
# import hashlib
# usr = input('username: ')
# pwd = input('password: ')
# with open('userinfo') as f:
#     for line in f:
#         user, passwd = line.split('|')
#         md5 = hashlib.md5()
#         md5.update(bytes(pwd, encoding='utf-8'))
#         md5_pwd = md5.hexdigest()
#         if user == usr and md5_pwd == passwd:
#             print('登录成功')

import hashlib
def check_file(filename):
    md5 = hashlib.md5()
    with open(filename, encoding='utf-8') as f:
        ch = f.read(10)
        while ch:
            md5.update(bytes(ch, encoding='utf-8'))
            ch = f.read(10)
    ret = md5.hexdigest()
    return ret

ret1 = check_file('userinfo')
ret2 = check_file('userinfo2')
print(ret1, '\n', ret2, sep='')

