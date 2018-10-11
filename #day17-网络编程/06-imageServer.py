# -*- coding: utf-8 -*-

# @Time : 2018/8/7 18:46
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 06-imageServer.py
# @Software : PyCharm

import socket

if __name__ == '__main__':
    server = socket.socket()
    server.bind(('10.7.181.71', 8081))
    server.listen(10)

    while True:
        conversation, addr = server.accept()
        print(addr)

        # 发送一张图片
        with open('./image.jpeg', 'rb') as f:
            data = f.read()
        conversation.send(data)


        conversation.close()