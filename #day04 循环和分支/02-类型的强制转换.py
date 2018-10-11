# 数据类型的转换：类型名（）
# int float bool str

# 1.其他的数据类型转换成整型
'''
浮点型：只保留整数部分
布尔类型：True -> 1  , False -> 0
字符串：去掉字符串的引号后，剩下部分本身就是一个整型数据的字符串才能转换成整数
'''

print(int(12.9))
print(int(False))
print(int('-12'))


# 2.其他的数据类型转换成浮点型
'''
整型：在整数后面加一个'.0'
布尔：True -> 1.0  ,   False  -> 0.0
字符串：去掉字符串的引号后，剩下的部分本身就是一个整型或者浮点型数据的字符串才能转换成浮点型数据

'''
print(float(123))
print(float(False))
print(float('+100.23'))

# 3.其他类型的数据转换成布尔类型：bool（）
'''
不管什么类型的数据都能转换成布尔值
整数中，除了0会转换成False其他的都会转换成True

总结：所有为0,为空的值都会转换成False，其他的值都是True

'''

print(bool())

if 0:
	print('======')
else:
	print('!!!!!')


# 判断一个字符串是否是空串(字符串长度是0)
# 空串就是:'',""
# 方法1 
str1 = '12'
if str1 == '':
	print('空串')
else:
	print('不是空串')

# 方法2
if len(str1) == 0:
	print('空串')
else:
	print('不是空串')

# 方法3

if str1:
	print('不是空串')
else:
	print('空串') 

# 判断一个数字是否是0
number = 10

# 方法1
if number == 0:
	print('是零')
else:
	print('非零')

# 方法2
if number:
	print('非零')
else:
	print('是零')

# 4.其他类型的数据转换成字符串：str（）
'''

不管是什么类型的数据都可以转换成字符串,就是直接在数据的外层加引号
'''

print(str(120))


# 5. if语句是可以嵌套使用
'''
if 条件语句1：
	if 条件语句2：
		执行语句块2
	else：
		执行语句块3
else:
	执行语句块4
'''

# 给出一个数字，如果是偶数，就打印“xxx是偶数”  ， 是偶数并且还能被4整除就打印“xxx是4的倍数”，否则就打印“xxx是基数”

str1 = 456
if str1 % 2 == 0:
	print('%d是偶数'% str1)
	if str1 % 4 == 0:
		print('%d是4的倍数' % str1)	
else:
	print('%d是奇数'% str1)	


if str1 % 2:
	print('奇数')
else:
	print('偶数')

num = 45672
if isinstance(num,int):
	print('是整数')
	if num % 2:
		print('是奇数')
	else:
		print('是偶数')
		if not (num % 4):
			print('被4整除')

# 5.判断数据的类型
# isinstance(值，类型名)  ---> 判断指定的值是都是指定的类型，如果是结果是True，否则结果是False

print(isinstance(10,int))  # 判断10是否是int类型
print(isinstance(10.2,int))