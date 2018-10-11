# -*- coding: utf-8 -*-

# @Time : 2018/7/30 8:54
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : recode.py
# @Software : PyCharm


"""
1.字典，集合，元祖
字典：{key：value}，key是唯一的，key值是不可变的

元祖：不可变的，有序的
（元素，）

集合： 可变，无序
{元素}
数学相关的集合运算

dict1 = {'a'：12，‘b’：[
        {'aa':1,'bb':2},
        {'aa':1,'bb':200}

]}
dict1['b'].append
dict['b].remove
dict['b'][]

dict1[''b][1]['bb']

怎么选用字典还是列表？
1.同时存储多个信息 --》 考虑使用容器的数据列行
2.是否可以对数据进行增删改查查 --》 是：列表字典   否：元祖，集合
3.看存储的数据是否是统一类数据 ---》是：列表   否：



2.函数
（1.怎么声明函数
def 函数名（参数列表）：

（2.参数
参数的功能是从函数外面给函数传值

传参：位置参数，关键参数（保证每个参数都要有值）

参数可以有默认值：1.有默认值的参数要放在没有默认值的参数后面
                2.可以不用传参

参数个数不定：参数名加*，参数就变成元祖

补充：容器类型前面加‘*’，就是将容器中的所有元素全部取出

（3.返回值
returm后面的表达式的值（没有遇到return，默认是None）

凡是函数功能会产生数据吗，或者想要给调用者返回信息的时候，都需要

(4.函数的调用过程
a.回到函数声明的位置
b.用实参给形参赋值
c.执行函数体
d.遇到return 或者函数体执行完，将返回值返回给调用者
e.回到函数调用的位置(调用表达式的值是返回值),接着往下执行

(5.函数作为变量

(6.匿名函数
函数名 = lambda 参数列表:返回值(不需要return)
函数名(实参)

(7.递归（了解）

(8.yeild函数（迭代器和生成器）


3.文件操作
打开文件-操作文件-关闭文件
open()、colse() \ with open() as
read()
wirte()

打开方式：'r','rb'\ 'w','wr','a'

json文件的操作
json内置模块，load,drump
loads\drumps

4.异常捕获
try:
    需要捕获异常的代码
except: -- 捕获所有的异常
    出现异常执行的代码


try:
    需要捕获异常的代码
except(异常类型1,异常类型2):
    出现异常执行的代码

try:
    需要捕获异常的代码
except 异常类型1:
    代码块1
except 异常类型2:
    代码块2
except:
    代码块3

try-except-finally
"""


def func2(*nums):

    print(sum(nums))

def func1(*numbers):

    print(numbers)
    func2(*numbers)


if __name__ == '__main__':

    func1(1, 2, 3)

    number = {11, 21, 33}
    print(number, *number)

    dict1 = {'a': 12, 'b': [
        {'aa': 1, 'bb': 2},
        {'aa': 100, 'bb': 200}
    ]}
    # 这个是个列表
    list_b = dict1['b']
    # 这个是一个字典
    dict_1 = list_b[1]
    # dict1['b'].append
    # dict1['b'].remove
    # dict1['b'][]
    print(dict1['b'][1]['bb'])