# -*- coding: utf-8 -*-

# @Time : 2018/8/8 14:05
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 02-多线程技术2.py
# @Software : PyCharm
"""
方式2：写一个自己的线程类
1.写一个类，继承自Thread类
2.重写run方法，在里面规定需要在子线程中执行的任务
3.实现在子线程中执行的任务对应的功能，如果需要参数，通过类的对象属性来传值
"""
from threading import Thread
import requests
import re
# 下载数据
class DownloadThread(Thread):
    """下载类"""
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
    def run(self):
        """run方法"""
        """
        1.写在这个方法的内容就是在子线程中执行的内容
        2.这个方法不要直接调用
        """
        print('开始下载')
        response = requests.request('GET', self.file_path)
        data = response.content

        # 获取文件后缀
        suffix = re.search(r'\.\w+$', self.file_path).group()
        with open('./abc' + suffix, 'wb') as f:
            f.write(data)
        print('下载完成')

if __name__ == '__main__':
    print('=============')
    # t1 = DownloadThread()
    # 通过start间接调用run方法，run方法中的任务在子线程中执行
    # t1.start()
    # 直接调用run方法，run方法中的任务在当前线程中执行
    # t1.run()
    t2 = DownloadThread('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1533720058151&di=766b5c97653351e805c85881ecaa57d0&imgtype=0&src=http%3A%2F%2Fx.itunes123.com%2Fuploadfiles%2Fb2ab55461e6dc7a82895c7425fc89017.jpg')
    t2.start()
    print('!!!!!!!')

