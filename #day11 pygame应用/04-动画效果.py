# -*- coding: utf-8 -*-

# @Time : 2018/7/30 14:43
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-动画效果.py
# @Software : PyCharm
"""
动画原理：不断刷新界面上的内容（一帧一帧的画）
"""

import pygame
from random import randint

def static_page(screen):
    font = pygame.font.SysFont('Times', 40)
    title = font.render('WELCOME!!!', True, (0, 0, 0))
    screen.blit(title, (100, 100))

def animation_title(screen):
    font = pygame.font.SysFont('Times', 40)
    title = font.render('PYTHON!!!', True, (randint(0, 255), randint(0, 255), randint(0, 255)))
    screen.blit(title, (200, 200))

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))


    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # 在下面写每一帧要显示的内容
            """程序执行到这个位置，cpu休息一段时间后自治性后面的代码（线程在这儿）"""
        pygame.time.delay(60)

        # 动画前要将原来的内容全部清空
        screen.fill((255, 255, 255))

        static_page(screen)
        animation_title(screen)

        pygame.display.flip()