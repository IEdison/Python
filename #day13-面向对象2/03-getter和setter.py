# -*- coding: utf-8 -*-

# @Time : 2018/8/1 13:48
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-getter和setter.py
# @Software : PyCharm

"""
属性假的私有化：声明对象属性的时候，在属性名前面加一个'_'，来告诉别人这个数次那个不可以直接使用
               要通过getter和setter来获取属性和修改属性的值


1.getter：获取属性的值
@property
def 属性名（去掉下划线）（self）：
    return 返回值

如果在获取对象的某个属性前需要再干点儿别的事情，就给属性添加getter


2.setter： 给属性赋值
一个属性必须要有getter，才能添加setter

@属性名（去掉下划线）.setter
def 属性名去掉下划线（self ，变量名）：
    给带下划线的属性赋值


如果再给对象的某个属相赋值前需要再干点儿别的事情，就给属性添加setter


"""


class Student:
    """学生类"""
    def  __init__(self):
        # 声明属性的时候前面加一个'_'是为了告诉别人这个属性不能直接使用
        self._name = ''
        self._score = 0
        self._age = 0

    # 给属性_name添加getter
    @property
    def name(self):
        return self._name

    # 给属性_name 添加setter
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def age(self):
        return str(self._age)+'岁'

    @age.setter
    def age(self, age):
        if age >= 150 or age <= 0:
            print('赋值错误')
            # raise 抛出异常 ：raise 错误类型
            raise ValueError
            self._age = None
            return
        self._age = age



if __name__ == '__main__':
    stu1 =Student()
    # 不添加getter和setter
    stu1._name = '张三'
    print(stu1._name)

    #添加getter和setter
    stu1.name = '李四'
    print(stu1.name)

    stu1.score = 95
    print(stu1.score)

    stu1.age = 100

    print(stu1.age)





