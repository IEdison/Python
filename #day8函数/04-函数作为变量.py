# -*- coding: UTF-8 -*-

# @Time : 2018/7/25 13:53
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-函数作为变量.py
# @Software : PyCharm


'''
声明一个函数就是在声明一个变量。函数名可以当成变量来使用。
    可以打印，可以赋值，可以作为函数的参数，可以作为函数的返回值
'''

a = 10
a = 'a'
print(a)

# 函数名func1可以当成变量使用
def func1(a):
    print(a)
    return 10
print(func1, type(func1))


# 将函数func1赋给变量a，这个时候a就是一个函数
a = func1
b = func1(10) + 100
a('aaa')
print(b)
print('------------------------------------------')
# ***加括号拿的是返回值，不加括号就是函数本身

# 将函数func1作为列表的元素
functions = [func1, func1(10)]
functions[0]('123')
print(functions[0])

# 1.将函数作为参数
def my_sum(*numbers):
    '''
    numbers = (10, 20, 30)

    '''
    sum1 = 0
    for item in numbers:
        sum1 += item
    return sum1


def my_mul(*numbers):
    sum1 = 1
    for item in numbers:
        sum1 *= item
    return sum1

def operation(method,*numbers):
    '''
    method = my_sum
    number = (10, 20, 30)
    return my_sum((10, 20, 30))
    '''
    a = ('a', 100, 'c')
    return method(*numbers)

# 求10+20
result = operation(my_sum, 10, 20)

# 求10*20
result2 = operation(my_mul, 10, 20)

# 判断10是否大于20
result3 = operation(lambda x, y: x < y, 10, 20)

# 找出两个数中的最大值
result4 = operation(lambda x, y: x if x > y else y, 10, 20)

a = 10 if 10 > 20 else 20
print('-------111111111111------------')

print(result, result2, result3, result4)

'''
python 中三目运算符( ?: )
表达式？值1：值2
值1 if 表达式 else 值2 ----->判断表达式是否为True，为True整个表达式的结果是‘值1’，否则是‘值2’
'''


'''3.将函数作为函数的返回值'''
# 写一个函数有个参数，要求传入一个运算符号（+，-，*，>,<）返回符号对应的功能
# + -----》 求和功能
# - -----》 求差功能

def get_method(char):
    if char == '+':
        return lambda x, y: x+y
    elif char == '-':
        def func(x, y):
            return x - y
        return func
    elif char == '*':
        return lambda x, y: x*y
    elif char == '>':
        return lambda x, y: x>y
    elif char == '<':
        return lambda x, y: x<y


print(get_method('+')(10, 20))
print(get_method('-')(10, 20))
print(get_method('>')(10, 20))

