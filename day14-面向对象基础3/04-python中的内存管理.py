# -*- coding: utf-8 -*-

# @Time : 2018/8/2 14:03
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-python中的内存管理.py
# @Software : PyCharm

"""
python内存管理原理
内存中有两个特殊的区域：栈，堆
栈：栈中的内存是系统自动管理的（内存的开辟和释放）---》作用域结束，内存就释放
堆：堆中的内存都是需要写程序去开辟和释放的（python中这个过程也已经自动化）

原理：堆中的数据到底是什么时候释放的
看一个值有几个引用，当一个值没有引用的时候，值对应的内存空间就会被释放
（引用计数机制）

引用：存储对象地址的变量

"""
class Person:
    def __init__(self, name):
        self.name = name
    def run(self):
        print(self.name,'人在跑')


if __name__ == '__main__':
    # 声明了一个Person对象，存到p中的
    p = Person('p')
    p.run()
    # 删除对象的唯一的引用，对象就会被销毁
    del p
    # p.run()

    # Person对象(0)，name='p1'  0+1+1-1-1
    p1 = Person('p1')
    p2 = p1
    del p2
    p1.run()
    p1 = 'a'

    # 注意：将对象添加到容器中，对象的引用会加1
    p3 = Person('p3')
    lists = [p3, 100]
    del p3

    lists[0].run()

    # del lists[0]
    # del lists
    lists[0] = None


