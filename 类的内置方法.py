# -*- coding: UTF-8 -*-

"""
# @Time    : 2019/8/29 
# @Author  : yanlei
# @FileName: 类的内置方法.py
"""
# class A:
#     # pass
#     def __str__(self):
#         return 'A'
# a = A()
# print(str(a))  # str(a) == a.__str__
# print(a.__str__())  # str(a) == a.__str__()
# # 类中不重写__str__方法时输出 <__main__.A object at 0x0000027016CAF0B8>
# # 类中写了__str__方法时输出  A
# print(a)  # 打印一个对象的时候，就是调用__str__()
#
# # object 里有一个__str__，一旦被调用，就返回调用这个方法的对象的内存地址
# print('%s:%s'%('A', a))
# # 输出 A:A
#
# # %s str() 直接打印一个对象  三种方法实际上都是走的__str__ 方法

# class Teacher:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def __str__(self):
#         return "Teacher's object : %s"%self.name
#     def __repr__(self):
#         return str(self.__dict__)  # __repr__ 必须返回字符串类型
#
# zhangsan = Teacher('张三', 1000)
# print(zhangsan)  # 直接打印一个对象 是 调用 __str__ 方法
# print(repr(zhangsan))  # repr函数 是 调用 __repr__ 方法
# print('%r'%zhangsan)  # %r 是 调用 __repr__ 方法
# Teacher's object : 张三
# {'name': '张三', 'salary': 1000}
# {'name': '张三', 'salary': 1000}



# 如果类中没有自定义__repr__方法，则打印对象的内存地址
# 会自动寻找父类中的__repr__方法。（返回该对象的内存地址）
# class Teacher:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def __str__(self):
#         return "Teacher's object : %s"%self.name
#     # def __repr__(self):
#     #     return str(self.__dict__)  # __repr__ 必须返回字符串类型
#
# zhangsan = Teacher('张三', 1000)
# print(zhangsan)  # 直接打印一个对象 是 调用 __str__ 方法
# print(repr(zhangsan))  # repr函数 是 调用 __repr__ 方法
# print('%r'%zhangsan)  # %r 是 调用 __repr__ 方法
# Teacher's object : 张三
# <__main__.Teacher object at 0x00000217BB91EAC8>
# <__main__.Teacher object at 0x00000217BB91EAC8>

# Teacher's object : 张三
# <__main__.Teacher object at 0x0000019290CBFA20>
# <__main__.Teacher object at 0x0000019290CBFA20>


# 如果类中没有__str__方法，又有直接打印 or str() or __str__ 调用该方法，则使用__repr__方法代替__str__方法
# 在没有__str__ 时  -->  __repr__方法 可以 代替__str__方法
# 在没有__repr__ 时  -->  __str__方法 不可以  代替__repr__方法 （会直接寻找父类中的__repr__方法（也就是直接打印对象的内存地址））
# class Teacher:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     # def __str__(self):
#     #     return "Teacher's object : %s"%self.name
#     # def __repr__(self):
#     #     return str(self.__dict__)  # __repr__ 必须返回字符串类型
#
# zhangsan = Teacher('张三', 1000)
# print(zhangsan)  # 直接打印一个对象 是 调用 __str__ 方法
# print(repr(zhangsan))  # repr函数 是 调用 __repr__ 方法
# print('%r'%zhangsan)  # %r 是 调用 __repr__ 方法


# __del__  析构函数  在程序结束时，会自动删除变量
# class A:
#     def __del__(self):
#         print('执行我了。')
#
# a = A()
# print(a)
# del a  # del 即执行了这个__del__方法，又删除了变量
# print(a)


# __call__
# class A:
#     def __init__(self, name):
#         self.name = name
#     def __call__(self, *args, **kwargs):
#         print('执行了call方法')
#
# a = A('Taylor')
# a()
#
# a = A('Taylor')()  # 在对象名后面加()， 则会执行类中的__call__方法

# __item__
# class Foo:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __getitem__(self, item):
#         if hasattr(self, item):
#             return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
# f = Foo('Taylor', 18, '女')
# print(f['name'])  # f['name'] 默认将对象后的参数传给类中的item  调用__getitem__方法
# f['hobby'] = 'sing'
# print(f.hobby, f['hobby'])  # f.hobby --> 通过类的属性获得hobby的内容  f['hobby'] --> 通过__getitem__获得
# # del f.hobby
# # print(f.__dict__)
# del f['name']  # 通过__delitem__方法来删除对象的属性
# print(f.__dict__)


# __new__
# class A:
#     def __init__(self):
#         self.x = 1
#         print("in init function")
#     def __new__(cls, *args, **kwargs):
#         print('in new function')
#         return object.__new__(A)
#
# a = A()
# print(a.x)
# in new function
# in init function
# 1
# 在执行__init__方法之前 会先执行__new__方法（单例模式就是基于__new__方法的）

# 单例模式
# 一个类始终只有一个 实例
# class A:
#     __isinstance = False
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#     def __new__(cls, *args, **kwargs):  # 重写__new__方法 用来实现单例模式
#         if cls.__isinstance:
#             return cls.__isinstance
#         cls.__isinstance = object.__new__(A)
#         return cls.__isinstance
#
#
# a = A('taylor', '男')
# b = A('swift', '女')
# print(a.__dict__)
# print(b.__dict__)

# __eq__
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     # == 触发 __eq__方法
#     # __eq__方法默认比较内存地址，内存地址一致，返回True，否则返回False
#     # 可以自定义重写__eq__方法，判断想要判断的东西来得到 == 的结果
#     def __eq__(self, other):
#         if self.name == other.name:
#             return True
#         else:
#             return False
#
# obj1 = A('taylor')
# obj2 = A('taylor')
# print(obj1 == obj2)


# hash() __hash__
class A:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

a = A('taylor')
b = A('taylor')
print(hash(a))
print(hash(b))
