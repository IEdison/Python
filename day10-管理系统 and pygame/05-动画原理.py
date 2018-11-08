# -*- coding: utf-8 -*-

# @Time : 2018/7/27 16:42
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 05-动画原理.py
# @Software : PyCharm


import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))
    x = 0
    y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        x += 1
        y += 1
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x,y), 80)
        pygame.display.flip()

