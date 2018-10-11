# -*- coding: utf-8 -*-

# @Time : 2018/7/30 13:49
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-鼠标事件的应用2.py
# @Software : PyCharm

# 要求：先在屏幕上显示一张图片，鼠标按下移动的时候，拽着图片一起动，鼠标弹起就不动了
import pygame

# 写一个函数，判断一个点是否在图片上
def is_in_rect(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
        return True
    return False



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))

    screen.fill((255, 255, 255))
    pygame.display.set_caption('图片拖拽')

    #显示图片
    image = pygame.image.load('./image.jpeg')
    image = pygame.transform.scale(image, (100, 100))
    image_x = 100
    image_y = 100
    screen.blit(image, (image_x, image_y))



    pygame.display.flip()
    # 用来存储图片是否可以移动
    is_move = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # 鼠标按下，让状态变为可以移动;
            if event.type == pygame.MOUSEBUTTONDOWN:
                w, h = image.get_size()
                if is_in_rect(event.pos, (image_x, image_y, w, h)):
                    is_move = True

            # 鼠标弹起，让状态变为不可以移动：
            if event.type == pygame.MOUSEBUTTONUP:
                is_move = False
            if is_move:
                if event.type == pygame.MOUSEMOTION:
                        screen.fill((255, 255, 255))
                        x, y = event.pos
                        image_w, image_h = image.get_size()
                        # 保证鼠标在图片的中心
                        image_x = x - image_w/2
                        image_y = y - image_h/2
                        screen.blit(image, (image_x, image_y))
                        pygame.display.update()