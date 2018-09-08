# while循环
'''
while 条件语句：
	循环体
其他语句

while：关键字
条件语句： 结果是True，或者False
循环体：重复执行的代码段

执行过程：判断条件语句是否为True，如果为True就执行循环体。
		 执行完循环体，再判断条件语句是否为True，如果为True就在执行循环体....
		 直到条件语句的值为False，循环结束，直接执行while循环后面的语句

注意：如果条件语句一直都是True，就会造成死循环。所以在循环体要有让循环可以结束的操作
 
python 中没有do-while 循环
'''
# 死循环
# while True:
# 	print('aaa')


flag = True
while flag:
	print('aaa')
	flag = False

#使用while 循环计算1到100的和：
sum1 = 0
count = 1
while count <= 100:
	sum1 += count
	count += 1
print(sum1)	


#练习： 计算100以内偶数的和

sum1 = 0
count = 0
while count <= 100:
	sum1 += count
	count += 2
print(sum1)


#




