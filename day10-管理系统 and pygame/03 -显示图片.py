# -*- coding: utf-8 -*-

# @Time : 2018/7/27 15:09
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03 -显示图片.py
# @Software : PyCharm

import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))

    # 1.获取图片对象
    image = pygame.image.load('./image/新图片.png')

    """
    a.获取图片大小
    get_size()
    """
    image_size = image.get_size()
    print(image_size)

    """
    b.形变：
    transform：形变包含缩放，旋转和平移
    scale(缩放对象，新的大小) --》 返回一个缩放后的新的对象
    """
    # image = pygame.transform.scale(image, (400, 400))

    """
    旋转
    rorate（旋转对象，旋转角度） ---- 角度是0-360对应的度数
    """

    # image = pygame.transform.rotate(image, 90)
    """
    def rotozoom(旋转对象，旋转角度，缩放比例)
    """
    image = pygame.transform.rotozoom(image, 0, 0.4)


    # 2.将图片对象渲染到窗口上(平移)
    screen.blit(image, (0, 0))
    # 3.展示在屏幕上
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()