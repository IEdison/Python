# -*- coding: utf-8 -*-

# @Time : 2018/8/7 18:46
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 07-iamgeClient.py
# @Software : PyCharm

import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('10.7.181.71', 8081))

    # 接收数据，因为图片数据较大，可能会分多次发送
    image_data = bytes()  # 创建一个空的bytes用来保存整个图片数据
    data = client.recv(1024)
    while data:
        image_data += data
        data = client.recv(1024)

    # 保存图片到本地
    with open('./bbb.jpeg', 'wb') as f:
        f.write(image_data)

    client.close()