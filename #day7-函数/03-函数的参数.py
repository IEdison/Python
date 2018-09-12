# -*- coding: UTF-8 -*-

# @Time : 2018/7/24 15:31
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-函数的参数.py
# @Software : PyCharm


"""
参数的作用：从函数的外面给函数传值
"""
# 1.位置参数
"""
传参的时候，实参按顺序给形参赋值
"""
def func1(a, b, c):
    print(a, b, c)

func1(10, 20, 30)

# 2.关键字参数
"""
调用函数的时候：
函数名（参数=值）
"""
print('===============')
func1(b=20, a=20, c=30)
def func11(a,b='cc',c='bb',d='a'):
    print(a,b,c,d)

func11(10,d='100')

print('============')
# 说明：未知参数和关键字参数可以混着来

# 3.参数的默认值
"""
在python中函数声明的时候的参数可以设置默认值,有默认值的参数必须放在参数列表的最后
调用参数有默认值的函数，有默认值的参数可以传参，也可以不传参

"""
def func2(a, b, c=100):
    print(a, b, c)
func2(10, 20, 30)
func2(10, 20)


# 4.参数个数不定
'''
函数参数的个数不确定的时候，就在声明函数的时候，形参的前面加一个*，将形参变成元祖
调用函数的时候，这个参数会将对应的实参作为元祖的元素保存起来

'''
# 写一个函数，求多个函数的和
def my_sum(*numbers):
    print(numbers)
    sum1 = 0
    for item in numbers:
        sum1 += item
    print(sum1)
my_sum(10, 20, 30, 40, 50)

# 参数个数不定，可以是形参中的一部分是不定的
# 个数不确定的参数要被放在最后
def func1(char, *numbers):
    print(char, numbers)
func1('a', 10, 20, 30)

# 参数个数不定，也可以不传参，对应的参数的值就是一个空的元祖
func1('a')
