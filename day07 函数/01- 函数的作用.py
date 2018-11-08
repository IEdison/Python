# -*- coding: UTF-8 -*-

# @Time : 2018/7/24 14:01
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 01- 函数的作用.py
# @Software : PyCharm

'''
左移，右移，发射子弹

'''

'''
问题在哪儿？
1.同样一个功能的代码需要重复的写多次
2.当功能发生改变的时候，需要修改多个地方


怎么解决这个问题？
  使用函数
'''
'''左移-右移-左移-左移-右移-右移'''
# 发射子弹
print('上弹')
print('瞄准')
print('扣扳机')

# 左移
def left():
    print('看后视镜')
    print('向左打方向盘')
    print('踩油门')
    print('回正方向盘')
    print('==========')

# 右移
def right():
    print('看后视镜')
    print('向右打方向盘')
    print('踩油门')
    print('回正方向盘')
    print('==========')

# 左移
left()
# print('看后视镜')
# print('向左打方向盘')
# print('踩油门')
# print('回正方向盘')
# print('==========')

# 左移
left()
# print('看后视镜')
# print('向左打方向盘')
# print('踩油门')
# print('回正方向盘')
# print('==========')

# 右移
right()
# print('看后视镜')
# print('向右打方向盘')
# print('踩油门')
# print('回正方向盘')
# print('==========')

# 右移
right()
# print('看后视镜')
# print('向右打方向盘')
# print('踩油门')
# print('回正方向盘')
# print('==========')
