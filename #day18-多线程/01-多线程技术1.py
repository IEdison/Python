# -*- coding: utf-8 -*-

# @Time : 2018/8/8 9:34
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 01-多线程技术1.py
# @Software : PyCharm

"""
python 内置的threading模块，可以支持多线程

所有的进程默认都有一个线程（一般叫这个线程为主线程），其他的线程叫子线程
如果想要在进程中添加其他的线程，就创建线程对象

"""
import threading
import time

def download(file, time1):
    print('开始下载', file)
    time.sleep(time1)
    print(file, '下载结束')


if __name__ == '__main__':
    print('abc')

    # 1.创建线程对象
    """
    target：需要在子线程中执行的函数
    args:调用函数的实参列表
    返回值:线程对象
    """

    t1 = threading.Thread(target=download, args=['爱情公寓', 10])

    # 2.在子线程中执行任务
    t1.start()

    t2 = threading.Thread(target=download, args=['狄仁杰', 5])
    t2.start()

    # download('爱情公寓')
    # download('狄仁杰')
    time.sleep(3)

    print('======')

    # value = input('>>>')
    # print('!!!!')