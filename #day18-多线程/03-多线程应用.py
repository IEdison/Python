# -*- coding: utf-8 -*-

# @Time : 2018/8/8 14:51
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-多线程应用.py
# @Software : PyCharm

import socket
from threading import Thread

class ConversationThread(Thread):
    """在西线程中处理不同的客户端"""
    """
    python中可以在函数参数的后面加一个冒号，来对参数的类型进行说明
    """
    def __init__(self, conversation:socket.socket, address):
        super.__init__()
        self.conversation = conversation
        self.address = address

    def run(self):
        while True:
            self.conversation.send('你好！'.encode())
            print(self.conversation.recv(1024).decode(encoding='utf-8'))



if __name__ == '__main__':
    server = socket.socket()
    server.bind(('10.7.181.117', 8080))
    server.listen(10)

    while True:
        conversation, addr = server.accept()

        t = ConversationThread(conversation, addr)
        t.start()

