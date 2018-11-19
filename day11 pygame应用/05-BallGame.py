# -*- coding: utf-8 -*-

# @Time : 2018/7/30 15:39
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 05-BallGame.py
# @Software : PyCharm


import pygame

def draw_ball(place,color,pos):
    """
    画球
    """
    pygame.draw.circle(place, color, pos, 20)
Up = 273
Down = 274
Left = 276
Right = 275

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))

    pygame.display.flip()
    # 保存初始坐标
    ball_x = 100
    ball_y = 100
    x_speed = 1
    y_speed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        if event.type ==pygame.KEYDOWN:
            if event.key == Up:
                y_speed = -1
                x_speed = 0
            elif event.key == Down:
                x_speed = 0
                y_speed = 1
            elif event.key == Right:
                x_speed = 1
                y_speed = 0
            elif event.key == Left:
                x_speed = -1
                y_speed = 0


        # 刷新屏幕
        screen.fill((255, 255, 255))
        # 每次循环让球的x
        ball_x += x_speed
        ball_y += y_speed
        if ball_x + 20 >= 600 or ball_x -20 <= 0 or ball_y + 20 >= 400 or ball_y - 20 <= 0:
            print('游戏结束')
            break
        #     ball_x = 600 - 20
        #     x_speed *= -1
        # if ball_x - 20 <= 0:
        #     ball_x = 0 + 20
        #     x_speed *= -1
        draw_ball(screen, (255, 0, 0), (ball_x, ball_y))

        pygame.display.update()