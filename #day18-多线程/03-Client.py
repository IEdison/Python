# -*- coding: utf-8 -*-

# @Time : 2018/8/8 14:55
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-Client.py
# @Software : PyCharm

import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('10.7.181.117', 8080))

    while True:
        print(client.recv(1024).decode(encoding='utf-8'))
        message = input('>>>')
        client.send(message.encode())

