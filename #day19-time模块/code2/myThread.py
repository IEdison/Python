"""__author__ = 余婷"""

from threading import Thread
import socket
from random import randint
from color import Color



class Massage:
    """文字信息类"""
    def __init__(self, text):
        self.text = text
        self.x = -50
        self.y = randint(0, 380)
        self.color = Color.rand_color()
        self.speed = randint(2, 5)
        self.alive = True

    def move(self):
        self.x += self.speed
        # 越界处理
        if self.x > 600 + 50:
            self.alive = False




class ConversationThread(Thread):
    """处理不同的客户端信息"""
    all_message = []

    def __init__(self, conversation:socket.socket):
        super().__init__()
        self.conversation = conversation

    def run(self):
        """让服务器和客户端一直保持通话"""
        while True:
            # 接收客户端发来的消息
            try:
                re_message = self.conversation.recv(1024).decode(encoding='utf-8')
                # 接收到一条消息就创建一个消息对象
                message = Massage(re_message)
                # 保存所有的消息
                ConversationThread.all_message.append(message)
                print('=====')

            except ConnectionResetError:
                print('[XXX已下线]')
                break

            # 给客户端发送消息
            self.conversation.send(' '.encode())









class AcceptThread(Thread):
    """接收请求的线程类"""
    all_client = []   # 保存所有的客户端
    def __init__(self, server:socket.socket):
        super().__init__()
        self.server = server
        self.flag = True

    def run(self):
        """不断接收客户端的请求"""
        while self.flag:
            conversation, addr = self.server.accept()
            # print('接收到客户端的请求')

            # 来了一个客户端请求，就给他创建一个子线程，来处理对应的消息
            t1 = ConversationThread(conversation)
            t1.start()
            AcceptThread.all_client.append(t1)

        # 在关闭服务器之前，给所有的客户端发送消息
        for tt in AcceptThread.all_client:
            try:
                tt.conversation.send('exit'.encode())
            except:
                pass
        print('退出2')






