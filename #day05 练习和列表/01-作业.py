# 1.
number = 1
for i in range(0,20):
	number *= 2
print(number)
# for 循环中，如果for后面的变量在循环体中不需要，这个变量命名的时候可以用'_'命名
# for _ in range(20)

# 2的20次方

# 2.
# sum1 = 0
# num = 1
# while num <= 100:
#  	if ((num%3==0) or (num%7==0)) and (num%21 != 0):
#  		sum1 += 1
#  		num += 1
# print(num)


# 能被3或7整除 且不能被21整除得数

# 1.求1到100之间所有数的和，平均值
sum1 = 0
for x in range(1,101):
	sum1 += x
print(sum1,sum1/100)



sum1 = 0
count = 1
while count <= 100:
	sum1 += count
	count += 1
print(sum1,sum1/100)


# 2.计算1-100之间能被3整除的数的和
sum1 = 0
for x in range(1,101):
	if x % 3 == 0:
		sum1 += x
print(sum1)


sum1 = 0
count = 1
while count <= 100:
	count += 1
	if count % 3 ==0:
		sum1 += count
print(sum1)

# 3.计算1到100之间不能被7整除的数的和

sum1 = 0
for x in range(1,101):
	if x % 7 != 0:
		sum1 += x
print(sum1)


sum1 = 0 
count = 0
while count <= 100:
	# count += 1
	if count % 7 != 0:
		sum1 += count
	count += 1
print(sum1)


# 1.兔子问题 斐波那锲数
'''
a = 1
 = 1	
while count <= 7
'''	

# 2.判断101-200之间有多少个素数，并输出所有素数。
#判断素数的方法：用一个数分别除2到sqrt(这个数)，
#如果能被整除，则表明此数不是素数，反之是素数。

for x in range(101,201):
	flag = True
	for y in range(2,x):
		num = x % y
		if num == 0:
			flag = False #  只要在2~number-1之间有一个被num整除，那么这个num就确定不是素数
			break   # 循环嵌套的时候，遇到break和continue结束的是包含的最近的那个循环		
	if flag == True:
		print(x,end=' ')		
print()

#3.打印出所有的水仙花数,所谓水仙花数是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个水仙花数,因为153 = 1^3 + 5^3 + 3^3

for x in range(100,1000):
	a = x // 100
	b = x // 10 % 10
	c = x % 10
	if x == a**3 + b**3 + c**3:
		print(x,end=' ')
print()
#4.有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的第20个分数  
'''
1  2  1

2  3  2

3  5  3

4  8  5

分子：上一个分数的分子加分母   分母: 上一个分数的分子

fz = 2 fm = 1

fz+fm / fz
'''
a=1
b=2
for x in range(1,20):
	c = b
	b = b + a
	a = c
print('第20个分数是%d/%d' % (b,a))


# 5.给一个正整数，要求：1、求它是几位数 2.逆序打印出各位数字
import random
num = random.randint(1,1000)
print(num)


count = 1
while num // 10 != 0:
	count += 1
	print(num%10,end='') #逆序打印例如  789  打印89 剩下7，单独打印
	num //= 10
print(num)  #输出原数最高位7，即个位数
print(count)
