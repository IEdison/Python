# -*- coding: utf-8 -*-

# @Time : 2018/8/2 15:30
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 05-包的使用.py
# @Software : PyCharm
"""
封装：
对功能的封装 ---》 用函数
对多个功能的封装 ---》 模块和类
对数据进行封装 ----》 类，字典
对多个类进行封装 ----》 模块
对多个模块进行封装 ---》 包（文件夹）

"""
# 导入包
import package1
# 到入某个包中的某个模块
from package1 import my_math
# 导入某个包的某个模块中的某个函数和类
from package1.my_math import sum,Math



if __name__ == '__main__':
    pass

