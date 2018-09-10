# 1.输出函数：print（）
'''
1. 默认每一个print（）函数，输出完内容后都会输出一个换行
2.一个print（）函数输出多个内容的时候，内容之间使用空格隔开的
3.内容后边加end=来设置结束标志（默认是'\n')
4.通过设置sep的值，来设置多个内容之间的间隔符(默认是' ')
'''

print('aaa',100,end='',sep='-')
print('bbb')


#2.input()函数

'''
 1.input（）函数可以接受从控制台输入的内容（以回车为结束标志）
 2.input函数会阻塞线程，程序执行到input的时候会停下来，等待用户的输入，输入完成后才会执行下面的内容
 3.接收到的数据释义字符串的形式返回的（Python2.x中输入的是数字的时候，可能返回int类型或者浮点型数据）

'''
'''
value = input('请任意输入：')
print('name',value,type(value))

'''
# 练习：猜字游戏
'''
随机产生一个1-100的整数,
输入的数字如果一样就提示猜对了，并且游戏结束
如果输入的数大于或者小于随机数，就提示输入的数字偏大或偏小，让其重新输入
'''

import random
num = random.randint(1,100)
count = 0
while True:
	num1 = int(input('请输入一个整数：'))
	count += 1
	if num1 == num:
		print('猜对了')
		break	
	elif num1 < num:
		print('偏小')
	else:
		print('偏大')
	if count > 3:
		print('游戏结束')
		break
		
	