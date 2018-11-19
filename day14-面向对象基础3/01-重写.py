# -*- coding: utf-8 -*-

# @Time : 2018/8/2 9:29
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 01-重写.py
# @Software : PyCharm

"""
继承后，子类可以拥有除父类继承的内容以外的其他的内容


1.关于方法
1）.在子类中可以直接添加其他的方法
2）.重写：
a.完全重写
重新实现从父类继承下来的方法，重写后，子类再调用这个方法的时候，就调用子类的
b.保留父类实现在的功能，再添加新功能


对对象和类的调用方法的过程：先看当前类是否存在这个方法，没有才看父类有没有这个方法，
                          如果父类没有就看父类的父类有没有，直到找到基类（object）为止
"""

class Animal(object):
    def __init__(self):
        self.age = 0
        self.color = ''

    def eat(self):
        print('吃东西')

    def shout(self):
        print('叫唤')

    def get_numbe(self):
        return 100

class Dog(Animal):
    def look_dog(self):
        print('看家')
# 重写父类的shout
    def shout(self):
        print('汪汪汪')

    # 重写父类的eat方法
    def eat(self):
        # 保留父类的eat的功能
        super().eat()
        print('吃骨头')

    # 保留父类的类方法的功能的时候，还有super（）的功能
    @classmethod
    def get_number(cls):
        print(super().get_number())

if __name__ == '__main__':
    dog = Dog()
    dog.age = 3
    dog.color = 'blue'
    print(dog.color)
    dog.shout()
    dog.look_dog()


    an = Animal

   # 继承后，父类不能使用子类中添加的属性和方法
    
