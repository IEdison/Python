# -*- coding: UTF-8 -*-

# @Time : 2018/7/25 11:17
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-匿名函数.py
# @Software : PyCharm

'''
匿名函数：本质函数，以另外一种简单的方式来声明

匿名函数的声明：
lambda 参数列表：返回值 ----> 结果是一个函数变量

'''

# 写一个函数计算两个数的和
def my_sum1(x, y):
    return x + y
print(my_sum1(10, 20))

my_sum2 = lambda x, y: x+y
print(my_sum2(10, 20))

#
funcs = []
for i in range(5):
    funcs.append(lambda x: x*i)

print(funcs[2](2))
print(funcs[4](2))