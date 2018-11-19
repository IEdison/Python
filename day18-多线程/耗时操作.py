# -*- coding: utf-8 -*-

# @Time : 2018/8/8 10:46
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 耗时操作.py
# @Software : PyCharm


from random import randint
import time

"""
1.耗时操作放到主线程中的问题：
耗时操作放到主线程中，会阻塞线程
多个耗时操作都放到一个线程中执行，最终执行的时间是两个耗时操作的时间和

2.怎么解决问题？
使用多线程(创建多个线程)
"""


def rand_color():
    return randint(0, 255),randint(0, 255),randint(0, 255)

def long_time():
    print('耗时操作开始')
    time.sleep(10)
    print('耗时操作结束')

def download(file):
    print('开始下载',file)
    time.sleep(10)
    print(file, '下载结束')

if __name__ == '__main__':
    print('====')
    print(time.time())
    download('狄仁杰')
    download('爱情公寓')
    print(time.time())
    print('!!!')


