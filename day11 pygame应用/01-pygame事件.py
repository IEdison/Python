# -*- coding: utf-8 -*-

# @Time : 2018/7/30 9:52
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 01-pygame事件.py
# @Software : PyCharm

import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))

    #设置窗口标题
    pygame.display.set_caption('游戏事件')

    pygame.display.flip()

    while True:
        # 每次循环检测有没有事件发生
        for event in pygame.event.get():
            #不同类型的事件对应的type值不一样
            if event.type == pygame.QUIT:
                exit()

            # 鼠标相关事件
            # pos属性：获取鼠标事件产生的位置
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('鼠标按下', event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                print('鼠标弹起', event.pos)

            if event.type == pygame.MOUSEMOTION:
                print('鼠标移动', event.pos)

            # 键盘相关事件
            # key属性，被按的按键对应的值得编码
            if event.type == pygame.KEYDOWN:
                print('键盘按键被按下', chr(event.key))

            if event.type == pygame.KEYUP:
                print('键盘按键弹起', chr(event.key))