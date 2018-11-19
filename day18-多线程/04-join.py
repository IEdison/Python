# -*- coding: utf-8 -*-

# @Time : 2018/8/8 15:38
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-join.py
# @Software : PyCharm

from threading import Thread, currentThread
from random import randint
import time

class Download(Thread):
    def __init__(self, file):
        # 这儿的父类的init方法必须调用，否则当前这个创建的对象就没有新的线程
        super().__init__()
        self.file = file


    def run(self):
        print(currentThread())

        print('开始下载：%s' % self.file)
        time.sleep(randint(5, 10))
        print('%s下载结束' % self.file)

if __name__ == '__main__':
    # time.time():获取当前时间 --时间戳
    start_time = time.time()
    t1 = Download('最强Z.mp4')
    t1.start()

    t2 = Download('最强,mp4')
    t2.start()
    print('==========')
    # 获取当前线程
    """
    主线程：MainThread
    子线程：Thread - 数字（数字从1开始）
    """
    # 如果一个任务想要在另外一个子线程的任务执行完成后在执行，就在当前任务前用子线程对象调用join方法
    # 所以join也会阻塞线程，租的到对应的子线程中任务执行完为止
    t1.join()
    t2.join()
    print('==========')
    end_time = time.time()
    print('总共消耗时间：%.2f' % (end_time - start_time))
