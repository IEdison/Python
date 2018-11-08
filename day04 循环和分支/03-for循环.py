# 需要重复执行某个过程，就可以使用循环
# python中的循环有for循环和while循环



# for循环：
'''
for 变量名 in 序列:
	循环体

for：关键字
变量名：和声明变量时的变量名要求是一样的，功能是存储值
in：关键字，在...里的意思
序列：容器类型的数据。字符串，列表，字典，元组，集合等
循环体：会重复执行的代码块

执行过程：使用变量去序列中取数据，一个一个的取，取完为止。每取一个值，执行一次循环体
'''
for char in 'abcd123':
	print(char,end='')
	print('!!!')
print('======')


# 打印 20次'abc'
# 2,。range函数
'''
xrange是python2.x中的函数，在python3.x只用range函数代替了

range功能是指产生指定范围的数字序列。一般用在for循环中，控制循环次数

range(n)：产生0 ~ n-1 的整数序列
range(m,n):产生m ~ n-1 的整数序列
range(m,n,step):从m开始，每次加step产生下一个数字，直到n前面那一个为止

'''

#range（10）：产生数字
for x in range(10):
	print(x)

# range(10,20):产生数字10~19
for x in range(10,20):
	print(x)

#
for x in range(0,10,2):
	print(x)

# 练习:计算1+2+3+.....+100
sum1 = 0
for x in range(1,100+1):
	sum1 += x
print(sum1)


# 练习：计算1*2*3*....*10
# 		计算2*4*6*..*10
sum1 = 1
sum2 = 1
for x in range(1,11):
	sum1 *= x
	if not x % 2:
		sum2 *= x
print(sum1)
print(sum2)

# 练习2： 有一个字符串“abcdef”，一次去除字符串中偶位，下标是偶数。

str1 = 'abcdef'
count = -1
for x in 'abcdef':
	count += 1
	if count % 2 == 0:
		print(x)

#方法1 循环取出所有偶数下标
str1 = 'abcdef'
for index in range(0,len(str1),2):
	print(str1[index])

#方法2 
for index in range(0,len(str1)):
	if index % 2 == 0:
		print(str1[index])

# 方法三
index = 0
for char in str1:
	if index % 2 == 0:
		print(char)
	index += 1