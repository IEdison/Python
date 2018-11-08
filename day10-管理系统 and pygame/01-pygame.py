# -*- coding: utf-8 -*-

# @Time : 2018/7/27 10:54
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 01-pygame.py
# @Software : PyCharm


import pygame


if __name__ == '__main__':
    # 1.初始化pygame
    pygame.init()

    # 2.创建游戏窗口
    # set_mode((宽度，高度))
    screen = pygame.display.set_mode((600, 400))

    # 3.游戏循环（死循环）
    while True:
        # 检测事件
        for event in pygame.event.get():
            # 检测窗口上的关闭按钮是否被点击
            if event.type == pygame.QUIT:
                # 退出游戏
                print('关闭按钮被点击')
                exit()