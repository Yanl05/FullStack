# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/21 
# @Author  : yanlei
# @FileName: 面向对象引入.py
"""


# 人狗大战
def Person(name, blood, aggr, sex):
    person = {
        'name': name,
        'blood': blood,
        'aggr': aggr,
        'sex': sex
    }

    def attack(dog):
        dog['blood'] -= person['aggr']
        print('%s被打了，掉了%s血' % (dog['name'], person['aggr']))

    person['attack'] = attack
    return person


def Dog(name, blood, aggr, kind):
    dog = {
        'name': name,
        'blood': blood,
        'aggr': aggr,
        'kind': kind
    }

    def bite(person):
        person['blood'] -= dog['aggr']
        print('%s被咬了，掉了%s血' % (person['name'], dog['aggr']))

    dog['bite'] = bite
    return dog


jia = Person('jia', 100, 10, 'man')
t = Dog('t', 1000, 50, 'teddy')
print(jia)
jia['attack'](t)
