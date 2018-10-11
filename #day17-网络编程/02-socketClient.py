# -*- coding: utf-8 -*-

# @Time : 2018/8/7 14:14
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 02-socketClient.py
# @Software : PyCharm
import socket
if __name__ == '__main__':

    # 1.创建套接字对象
    client = socket.socket()

    # 2.链接服务器
    client.connect(('10.7.181.71', 4568))

    # 3.接收信息
    data = client.recv(1024)
    print('接收服务器的数据：', data.decode(encoding='utf-8'))

    # 4.发送信息
    client.send('hello'.encode(encoding='utf-8'))
