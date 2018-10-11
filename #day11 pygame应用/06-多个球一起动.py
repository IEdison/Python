# -*- coding: utf-8 -*-

# @Time : 2018/7/30 16:18
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 06-多个球一起动.py
# @Software : PyCharm

import pygame
import random
from math import sqrt
# random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


all_balls = []
radius = 'radius'
center = 'pos'
color = 'color'
x_speed = 'x_speed'
y_speed = 'y_speed'

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))
    pygame.display.flip()
    random_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # all_balls中保存多个球
    # 每个球要保存：半径，圆心坐标，颜色，x速度，y速度
    all_balls = [
        {'r': random.randint(10, 20),
         'pos': (100, 100),
         'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
         'x_speed': random.randint(-1, 1),
         'y_speed': random.randint(-1, 1)
        },
        {'r': random.randint(10, 20),
         'pos': (10, 50),
         'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
         'x_speed': random.randint(-1, 1),
         'y_speed': random.randint(-1, 1)
         },
        {'r': random.randint(10, 20),
         'pos': (200, 200),
         'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
         'x_speed': random.randint(-1, 1),
         'y_speed': random.randint(-1, 1)
         },

    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
            # 点一下鼠标创建一个球
                ball = {
                          'r': random.randint(10, 25),
                          'pos': event.pos,
                          'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                          'x_speed': random.randint(-1, 1),
                          'y_speed': random.randint(-1, 1)
                        }

                all_balls.append(ball)

        # 刷新界面
        screen.fill((255, 255, 255))
        for ball_dict in all_balls:
            # 取出原来的x坐标和y坐标以及他们的速度
            x, y = ball_dict['pos']
            if x_speed == 0 and y_speed == 0:
                x_speed = 1
                y_speed = 1
                pass

            x_speed = ball_dict['x_speed']
            y_speed = ball_dict['y_speed']

            x += x_speed
            y += y_speed

            pygame.draw.circle(screen, ball_dict['color'], (x, y), ball_dict['r'])

            if x_speed == 0 and y_speed == 0:
                x_speed = 1
                y_speed = 1
                pass
            x += x_speed
            y += y_speed
            pygame.draw.circle(screen, ball_dict['color'], (x, y), ball_dict['r'])




            # 更新对应的坐标
            ball_dict['pos'] = x, y



            # pygame.display.flip()
            if x + ball_dict['r'] >= 600:

                x = 600 - ball_dict['r']
                x_speed *= -1
                ball_dict['x_speed'] = x_speed

            if x - ball_dict['r'] <= 0:
                x = 0 + ball_dict['r']
                x_speed *= -1
                ball_dict['x_speed'] = x_speed

            if y + ball_dict['r'] >= 400:
                y = 400 -ball_dict['r']
                y_speed *= -1
                ball_dict['y_speed'] = y_speed

            if y -ball_dict['r'] <= 0:
                y = 0 + ball_dict['r']
                y_speed *= -1
                ball_dict['y_speed'] = y_speed

            for ball1 in all_balls:
                for ball2 in all_balls:
                    if ball1 == ball2:
                        continue
                    else:
                        x1, y1 = ball1['pos']
                        x2, y2 = ball2['pos']
                        if sqrt((x1 - x2)**2 + (y1 - y2)**2) <= ball1['r'] + ball2['r']:
                            if ball1['r'] < ball2['r']:
                                ball2['r'] += int(ball1['r']/15)
                                all_balls.remove(ball1)
                            else:
                                ball1['r'] += int(ball2['r']/15)
                                all_balls.remove(ball2)



            # ball_dict['pos'] = x, y
            pygame.draw.circle(screen, ball_dict['color'], (x, y), ball_dict['r'])


        pygame.time.delay(10)


        pygame.display.update()