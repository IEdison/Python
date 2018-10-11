# 1. +： 字符串拼接
str1 = 'hello' + ' ' + 'Python'
print(str1)

# 注意： + 号两边要么都是数字，要么都是字符串。不能使一个数字和一个字符串

# 2. *：让字符串重复
# 字符串*整数
str1 = 'abc' * 3
print(str1)

str2 = 'a' * 10
print(str2)


# 3. in
# 字符串1 in 字符串2 ： 判断字符串1是否在字符串2中
result = 'aa' in 'aaabbb'
print(result)


# 4. not in
# 字符串1 not in 字符串2 ：判断字符串1是否在字符串2中 ---->不在是True，在就是False

result = '123' not in 'abc'
print(result)

# 5.格式字符串
# 格式：'占位符1占位符2'%(值1，值2)
str1 = 'abc%s15%s23' % ('>>>','Python')
print(str1)

# 	%s  --> 字符串占位符（格式）
# 	%d  --> 整数占位符（格式符）
# 	%f  --> 浮点数占位符
# 	%c  --> 长度是1的字符串占位符----可以给一个字符，也可以给字符的编码值

str2 = '-%s-%d-%f-%c' % ('我是字符串',123 + 5,12.4,'k')
print(str2)


# %.nf : 使用n限制小数点后面的小数的位数（默认六位小数）
str3 = '金额：%.2f' % (100)
print(str3)

# 如果后面没有加%，那么这个字符串只是一个普通的字符串
str3 = '金额：%f元'
print(str3)

# %x和%X  ---> 十六进制数据占位符
number = 100
# XXX的十六进制是XXXXX
str4 = '%d的十六进制是:%x' % (number,number)
print(str4)


# 6.格式化输出
name = '十四'
age = 18
# xx今年xx岁
print('%s今年%d岁' % (name,age))


str1 = 654.23
print('%x' % id(str1))


