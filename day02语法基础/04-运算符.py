# 数学运算符，比较运算符，逻辑运算符，赋值运算符，位运算符


# 1.数学运算符(+,-,*,/,%,**,//)
# +: 求和
# 注意：求和操作，+两边必须是数字类型
# True  --> 1 , False --> 0
print(10+20.4,True+1)
number = 100 + 11
print(number)

# - :求差
print(100-12)

# * : 求乘积
print('chengji:'+str(3.12*2))
number = 3 * 9

# / : 求商
print(4/2)
print(5/2)

# % : 取余
print(3%2)
print(101%10)

# ** : 幂运算
# x ** y ： 求x的y次方
# 浮点数在计算中存储的时候，有的时候会有一定的误差
number = 2 ** 3
print(number)

# // : 整除
# 求商,但是只取商的整数部分
print(5//2)
# 取一个二位整数的十位数（78）
print(78//10)

# 取2345中的4：
print(2345%100//10)
print(2345//10%10)

# 2.比较运算符
'''
>,<,==,!=,>=,<=

比较运算符的结果全是布尔值：True，False

'''
'''
1.>
x > y : 判断x是否大于y，如果是结果为True,否则是False
'''
result = 10 > 20 
print(result,100 > 20)

#2.<
print(10 < 20)


# 3. ==
# x == y: 如果x和y相等，结果九尾True，否则是False
number = 12.5
number2 = 12
print(number == number2)

# 4.>= ,<=
10 >= 5 	#True
10 >= 10	#True

# 5.!=
# x != y : 如果x和y不相等，结果是True，否则是False

#6.
number = 15
result = 10 < number <20 #判断number是否在10到20之间
print(result)


#3. 逻辑运算符

'''
与（and）， 或（or）， 非（not） 
逻辑运算符的运算数据是布尔值，结果也是布尔值

布尔1 and 布尔2 ：两个都为True结果才是True ,只要有一个是False，结果就是False  并且
需要两个或者多个条件同时满足，就是用逻辑与（and）


布尔1 or 布尔2 ：只要有一个是True，结果就是True。两个都是False结果才是False。   或者
需要两个或者多个条件满足一个就可以，就是用逻辑或（or）


not 布尔1： 如果是 False，结果就是True；如果是True，结果就是False。
需要不满足某个条件的时候才为True


# 写一个条件，判断一个人的年龄是否满足青年的条件（10<age<20）
'''
age = 30
print(age>18 and age<28 and age != 20)


#平均成绩大于90，或者操评分大于100，并且英语成绩还不能低于80分
score = 80 
score2 = 90
english = 70
print('===:',score > 90 or score2 > 100 and english >= 80)

#成绩不低于60分
score = 70
print(score >= 60)
print(not score < 60)

#4.赋值运算符
'''
=,+=,-=,*=,/=,%=,**=,//==

赋值运算符的作用，将赋值符号右边的表达式的值赋给左边的变量
表达式：有结果的语句，例如：10，'abc',10+20,30>10.5等
赋值符号的左边必须是变量

赋值符号，是先算右边的结果，然后再把结果赋给左边的变量
'''
number = 100 

number += 10 # 相当于number = number + 10
print(number)

number *= 2 # 相当于number = number *2
print(number)

#5.运算符的优先级
'''
10+20*3-5/2=10+60-2.5 ---数学运算顺序
优先级从低到高： 赋值运算符 < 逻辑运算符 < 比较运算符 < 算术运算符
算术运算符中：先幂运算在乘除取余取整再加减

如果你不确定运算顺序，可以通过添加括号来改变运算顺序。有括号就先算括号里边的
'''
result = 10 + 20 > 15 and 7 * 8 < 30 + 60 
#result 30>15 and 56< 90
#result	True and True 
#result = True
print(result)

print(10 + 20 * 3 / 2 - 10 % 3)
#10+30-1 
#39

print(10 + 20 * 3 / (2 - 10) % 3)