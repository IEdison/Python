# -*- coding: utf-8 -*-

# @Time : 2018/7/30 10:51
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 02-鼠标事件的应用.py
# @Software : PyCharm

import pygame
from random import randint
def rand_color():
    """
    产生随机颜色
    """
    return randint(0, 255), randint(0, 255), randint(0, 255)

def draw_ball(screen, pos):
    pygame.draw.circle(screen, rand_color(), pos, randint(10, 20))

    # 只要屏幕上的内容有更新。都需要调用下面这两个方法中的一个
    # pygame.display.flip()
    pygame.display.flip()

# 写一个函数，判断指定的点是否在指定的矩形范围内
def is_in_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
        return True
    return False

def draw_button(screen, bith_color, title_color):

    # 画个按钮
    """矩形框"""
    pygame.draw.rect(screen, bith_color, (100, 100, 100, 60))
    """文字"""
    font = pygame.font .SysFont('Times', 30)
    title = font.render('QCG', True, title_color)
    screen.blit(title, (120, 120))
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))

    screen.fill((255, 255, 255))
    pygame.display.set_caption('鼠标事件')

    pygame.display.flip()

    # 画个按钮
    # draw_button(screen, (0, 255, 0), (255, 0, 0))
    # """矩形框"""
    # pygame.draw.rect(screen, (0, 255, 0), (100, 100, 100, 60))
    #  """文字"""
    # font = pygame.font .SysFont('Times', 30)
    # title = font.render('QCG', True, (255, 0, 0))
    # screen.blit(title, (120, 120))
    # pygame.display.flip()



    while True:
        for event in pygame.event.get():

            # 退出
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
               # draw_ball(screen, event.pos)
                if is_in_rect(event.pos, (100, 100, 100, 60)):
                    draw_button(screen, (0, 0, 255), (0, 0, 0))
                    print('点中按钮')

            if event.type == pygame.MOUSEBUTTONUP:
                if is_in_rect(event.pos, (100, 100, 100, 60)):
                    draw_button(screen, (0, 255, 0), (255, 0, 0))
                    pygame.display.update()


            if event.type == pygame.MOUSEMOTION:
                screen.fill((255, 255, 255))
                draw_button(screen, (0, 255, 0), (255, 0, 0))
                draw_ball(screen, event.pos)