# -*- coding: UTF-8 -*-

# @Time : 2018/7/26 10:25
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 01-模块管理函数和类.py
# @Software : PyCharm


'''
1.什么是模块：一个.py文件就是一个模块

2.import：可以通过import关键字导入其他的模块
import 模块名（.py文件名）

直接导入模块的时候，相当于把被导入模块里面的内容粘贴到了import的位置

3.怎么使用模块中的内容？什么内容是可以使用的？
import 模块名 ----》 导入模块中的所有的内容
模块名.的方式去使用模块中的内容


'''
print('=========')
import other
# 在模块中声明的的全局变量（普通变量，函数，类）

print(other.func_other(), other.abc)
print('---------')

print('=====', other.__name__)
'''
4.from 模块 import 内容1，内容2   ------》 导入模块中指定的内容
使用内容的时候，不用再被导入的变量或者函数或者类前加模块名
'''
print('**********************')
from other2 import func2
func2()



'''
5.阻止被导入的模块中的不必要的代码被粘贴到当前模块
一般情况下，除了函数的声明和累的声明意外，其他代码都放到这个if 里面
（执行时__name__ 就是__main__ 。调用它，不执行时就是other）
'''

# __name__：是每个模块自带的一个属性，是用来保存当前这个模块的名字的。
# 但是当正在执行当前模块的时候，这个属性的值是固定的'__main__'

print('==:', other.__name__)

print(__name__)

if __name__ == '__main__':
    # 这个里面的代码不会被其他模块使用
    pass

'''
# 使用as重命名
import 模块名 as 新的名字
from 模块名 import 函数名 as 新的函数
'''
import math as my_math
print(my_math.pi)

from random import randint as my_rand
print(my_rand(1, 10))


# 练习：使用一个模块，用来管理所有和形状有关的功能
# （求两点之间的距离，求圆的周长，求圆的面积，求矩形的周长和面积等）