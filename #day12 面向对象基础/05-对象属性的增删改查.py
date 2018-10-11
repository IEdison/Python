# -*- coding: utf-8 -*-

# @Time : 2018/7/31 13:53
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 05-对象属性的增删改查.py
# @Software : PyCharm

class Dog:
    """狗类"""
    def __init__(self, age = 0, color = 'white'):
        self.age = age
        self.color = color

class Student:
    def __init__(self, name='胡晨宇', sex='男', age='18'):
        self.name = name
        self.sex = sex
        self.age = age

    def study(self):
        print('%s学习' % self.name)


if __name__ == '__main__':

    # 1. 查（获取属性）
    """
    方法一： 对象.属性（如果属性不存在，会报错）
    方法二：对象.__getattribute__（属性名）和getattr（对象，属性名，默认值）
    """
    dog1 = Dog(age=3, color='red')
    print(dog1.age, dog1.color)

    print(dog1.__getattribute__('age'))
    print(getattr(dog1, 'age'))

    #如果设置了default的值，那么当属性不存在的时候不会报错，并且返回默认值
    print(getattr(dog1, 'abc', '无名氏'))
    # 2. 改（修改属性的值）
    """
    方法一：对象.属性 = 新值
    方法二：对象.__setattr__(属性名，新值)和setattr（对象，属性名，默认值）
    """
    dog1.age = 4
    print(dog1.age)

    dog1.__setattr__('color', 'black')
    print(dog1.color)

    setattr(dog1, 'color', 'blue')
    print(dog1.color)
    # 3.增加（增加对象属性）
    """
    对象.属性 = 值（属性不存在）
    注意：属性是添加给对象的，而不是类的
    """
    dog1.name ='大黄'
    print(dog1.name)

    dog1.__setattr__('type', '哈士奇')
    print(dog1.type)

    setattr(dog1, 'sex', '公')
    print(dog1.sex)

    # 4.删（删除对象属性）
    """
    方法一：del 对象.属性
    注意：删除属性也是删的具体某个对象的属性。不会影响到这个类的其他对象
    
    """
    # del dog1.age
    # print(dog1.age)

    dog1.__delattr__('age')
    # print(dog1.age)

    delattr(dog1, 'color')
    # print(dog1.color)


    # 练习：声明一个学生类，拥有属性：姓名，性别，年龄。方法：学习
    # 声明学生类的对象，声明的时候就给姓名，性别和年龄赋值
    # 通过三种方式分别获取姓名，性别和年龄，并且打印
    # 给学生添加一个对象
    # 修改学生的年龄
    # 删除学生的性别



    student1 = Student()
    print(student1.name, student1.sex, student1.age)

    print(student1.__getattribute__('name'))

    print(getattr(student1, 'sex'))

    student1.tel = '123456'
    print(student1.tel)
    student1.age = 22
    del student1.sex
    student1.study()