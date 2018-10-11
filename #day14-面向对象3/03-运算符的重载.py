# -*- coding: utf-8 -*-

# @Time : 2018/8/2 11:22
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-运算符的重载.py
# @Software : PyCharm
"""
重载：一个类中可以有多个名字相同的方法，但是参数不一样，就叫重载。python中不支持

"""
class Student:

    #python不支持方法的重载
    # def run(self):
    #     print('人在跑')

    def run(self, name):
        print('%s在跑' % name)

"""
2.运算符重载(重新定义运算符运算的过程)
>,<
大于和小于符号只需要重载其中的一个，另外一个的结果，直接是重载的结果取反

+,-
"""
class Student2():
    def __init__(self, name='', age=0, height=0):
        self.name = name
        self.age = age
        self.height = height

    # 重载：>
    """
    self > other
    """
    def __gt__(self, other):
        # 比较对象1>对象2的时候是比较的他们的height属性
        return self.height > other.height

    # 重载：<
    """
    self > other
    """
    def __lt__(self, other):
        return self.age < other.age

    # 重载：+
    def __add__(self, other):
        return self.age + other.age

    # 重载：-
    def __sub__(self, other):
        return self.height - other.height

if __name__ == '__main__':
    stu = Student()
    stu.run('胡晨宇')


    stu1 = Student2('aa', 18, 170)
    stu2 = Student2('bb', 20, 140)

    if stu1 > stu2:
        print('学生1大于学生2')

    if stu1 < stu2:
        print('学生1小于学生2')

    print(stu1 + stu2)
    print(stu1 - stu2)