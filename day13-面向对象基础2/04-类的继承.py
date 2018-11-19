# -*- coding: utf-8 -*-

# @Time : 2018/8/1 15:52
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-类的继承.py
# @Software : PyCharm

"""
子类：继承者
父类（超类）：被继承者


1.怎么继承
python中类是可以继承的，并且支持多继承

class 类名（父类列表）：
    '''类的说明文档'''
    属性
    方法

说明：python中所有的类默认继承Python中的基类：object

2.能继承哪些内容
继承:直接拥有父类的属性和方法（继承父类的属性和方法还是存在的）
a.对象的属性和方法，类的字段和类的方法，静态方法都可以继承（私有的继承无意义---不能继承）
b.__slots__的值不会被继承
c.getter 和setter 会被继承
"""
class Person:
    """人类"""
    def __init__(self):
        self.name = ''
        self.age = 0
        self.sex = '男'
        self.__lenght = 0
        self._face = 0


    def eat(self):
        print('%s在吃饭' % self.name)

    # 类字段
    number = 61

    @classmethod
    def get_number(cls):
        print('人类数量%s' % cls.number)

    @staticmethod
    def hurt_earth():
        print('人类破坏地球')

class Student(Person):
    """学生类"""
    def study(self):
        pass




if __name__ == '__main__':

    stu = Student()
    stu.name = '张三'
    print(stu.name, stu.age, stu.sex)

    stu.eat()
    print(stu.__dict__)

    print(Student.number)
    Student.get_number()
    Student.hurt_earth()

