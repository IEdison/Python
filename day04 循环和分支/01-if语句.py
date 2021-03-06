# if语句
'''
结构：
1.
if 条件语句：
	条件语句为True执行的代码块

 执行过程：先判断条件语句是否为True，
如果为True就执行if语句后：后面对应的一个缩进的所有代码块
如果为False，就不执行冒号后面的一个缩进中的代码块，直接执行后续的其他语句

条件语句：可以使任何有值的表达式，但是一般是布尔值


if : 关键字
'''


if True:
	print('代码1')
	print('代码2')
	print('代码3')
print('代码4')



# 练习：用一个变量保存时间（50米短跑），如果时间小于8秒，打印及格
time = 7
if time < 8:
	print('及格') # 只有条件成立的时候才会执行
print(time)		#不管if语句的条件是否，这个语句都会执行 


'''
if 条件语句：
	语句块1
else:
	语句块2

执行过程：先判断条件语句是否为True，如果为True就执行语句块1，否则就执行语句块2
练习：用一个变量保存成绩，如果成绩大于等于60，打印及格，否则打印不及格
'''
score = 70
if score >= 60:
	print('及格')
else:
	print('不及格')

# 3.if-elif-elif...else
'''
if 条件语句1：
	代码块1
elif 条件语句2：
	代码块2
else
	代码块3

执行过程：先判断条件语句1是否为True，如果为True就执行代码块1 ，执行完代码块1在执行其他语句
		 如果条件语句1是False，就判断条件语句2是否为True：
		 如果条件语句2是True就执行代码块2，执行完代码块2再执行其他语句
		 如果条件语句2是False就执行代码块3，执行完代码块3再执行其他语句

'''

print("第一次打印",end=" ")
print("第二次打印")
print("第三次打印")
print(123,"aaa",sep = "--")

# 给一个学生的成绩，判断成绩是优秀（90-100），良好（70-89），及格（60-69），不及格（0-59）

grade = 18
if 90 <= grade <= 100:
	print('优秀')
elif 70 < grade <= 89:
	print('良好')
elif 60 < grade <= 69:
	print('及格')
elif 0 <= grade <= 60:
	print('不及格')
else:
	print('成绩有误！！！')

