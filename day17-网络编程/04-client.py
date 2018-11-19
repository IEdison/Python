# -*- coding: utf-8 -*-

# @Time : 2018/8/7 14:38
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-client.py
# @Software : PyCharm

import socket
if __name__ == '__main__':
    # 1.创建套接字对象
    client = socket.socket()

    # 2.连接服务器
    client.connect(('10.7.181.118', 1025))

    while True:

        data = client.recv(1024)
        print(data.decode(encoding='utf-8'))

        message = input('>>>')
        client.send(message.encode())