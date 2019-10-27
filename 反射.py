# -*- coding: UTF-8 -*-

"""
# @Time    : 2019-08-26 13:34
# @Author  : yanlei
# @FileName: 反射.py
"""
class Teacher:
    dic = {'查看学生信息':'show_student', '查看老师信息':'show_teacher'}
    def show_student(self):
        print('show_student')

    def show_teacher(self):
        print('show_teacher')

    @classmethod
    def func(cls):
        print('hahaha')

zhou = Teacher()
if hasattr(zhou, 'show_student'):
    ret = getattr(zhou, 'show_student')
    ret()