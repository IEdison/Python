# -*- coding: utf-8 -*-

# @Time : 2018/7/26 18:55
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04 异常捕获.py
# @Software : PyCharm



"""
出现异常（错误）不想让程序崩溃，就可以进行异常捕获
try:
    需要捕获异常的代码
except：
    出现异常会执行的代码


try：
    需要捕获异常的代码
except 错误类型：
    捕获到指定的错误类型，才执行的代码



"""


if __name__ == '__main__':
    try:
        with open('./aaa.txt') as ff:
            print('打开成功')
    except FileNotFoundError:
        print('==============')
        open('./aaa.txt', 'w')

