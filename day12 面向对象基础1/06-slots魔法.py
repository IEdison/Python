# -*- coding: utf-8 -*-

# @Time : 2018/7/31 14:45
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 06-slots魔法.py
# @Software : PyCharm

class Person:
    # __slots__的功能：就是约束类中的对象的属性
    __slots__ = ('name', 'age', 'sex')
    def __init__(self,name='',age=0):
        self.name = name
        self.age = age

    # 自定义对象的打印格式
    def __str__(self):
        return self.name + ','+str(self.age)

if __name__ == '__main__':
    p1 = Person('小王', 20)
    # p1.names = '老王'
    print(p1)
