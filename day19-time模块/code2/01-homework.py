"""__author__ = 余婷"""

"""
注意：
1.想要结束一个进程就是让它里面的所有的线程都结束，进程才会结束
2.想要关闭一个子线程，就是想方设法让子线程中的任务结束(就是让run方法结束)
3.如果一个线程崩溃(发生异常)，不会影响其他线程
"""


"""
写一个服务器，可以和多个客户端同时通信，并且把接收到的消息显示在屏幕上
"""

import socket
import pygame
from random import randint
from color import Color
import myThread


def creat_server():
    """创建服务器"""
    server = socket.socket()
    server.bind(('10.7.181.117', 8050))
    server.listen(512)

    # 在一个子线程中去监听客户端的请求
    server_thread = myThread.AcceptThread(server)
    server_thread.start()
    
    return server_thread


if __name__ == '__main__':

    # 0. 创建服务器
    t1 = creat_server()

    # 1.准备显示信息的屏幕
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill(Color.white)
    pygame.display.flip()

    # 2.让屏幕可以一直存在
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # 获取每条信息，显示在屏幕上
        screen.fill(Color.white)
        for message in myThread.ConversationThread.all_message[:]:
            if message.alive:
                # 显示信息
                font = pygame.font.SysFont('Times', 30)
                text = font.render(message.text, True, message.color)
                screen.blit(text, (message.x, message.y))
                # 动起来
                message.move()
            else:
                myThread.ConversationThread.all_message.remove(message)


        pygame.display.update()


    print('退出1')








