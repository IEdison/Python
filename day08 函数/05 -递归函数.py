# -*- coding: UTF-8 -*-

# @Time : 2018/7/25 15:33
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 05 -递归函数.py
# @Software : PyCharm


# 这个函数就是递归函数

# def func1():
#     print('=====')
#     func1()
#
# func1()

'''
1.什么是递归
递归函数： 在函数的函数体重调用本身

理论上循环能做的事情，递归都可以做

对递归的要求，能不用就用
函数调用的过程是一个压栈的过程（每调用一次函数，系统都要为其分配内存空间，
用来存储函数中声明变量和参数等，这个内存在函数调用结束后会自动销毁）

2.怎么写一个递归函数
a.找临界值（跳出循环--- return）
b.找关系：假设当前函数对应的功能已经实现，找到f(n) 和 f(n-1) 的关系
c.通过使用f（n-1） 与 b中找到的关系去实现f（n）的功能

'''

# 1+2+3+4+...+n
# 普通函数

def my_sum(n):
    sum1 = 0
    for x in range(1,n+1):
        sum1 += x
    return  sum1

print(my_sum(10))

# 递归函数
def my_sum2(n):
    # 1.找到临界值
    if n == 1:
        return 1
    # 2.找到my_sum2（n）和 my_sum（n-1）的关系：
    '''
    关系： my_sum2(n) = my_sum2(n-1)+n
    
    '''
    # 3.使用my_sum2(n-1)去实现my_sum2(n)的关系：
    return my_sum2(n-1) + n
print(my_sum2(5))

# 用递归求2*4*6*....*n(n是偶数)

def my_mul3(n):
    # 1.找临界值
    if n == 2:
        return 2
    return my_mul3(n-2) * n
print(my_mul3(8))

'''
用递归函数实现以下功能
n = 3
***
**
*

n=4
****
***
**
*
'''

def print_star(n):
    if n == 1:
        print('*')
        return None

    # 2.找关系
    '''
    关系:先打印n个* 然后f（n-1）
    '''
    print('*'* n)
    return print_star(n-1)

print_star(4)
print('=============================')
'''
n = 4
****
***
**
*
'''



def print_star(n):
    if n == 1:
        print('*')
        return None

    # 2.找关系
    '''
    关系:先f（n-1） 然后打印n个*
    '''
    print_star(n-1)
    print('*'* n)

print_star(4)
