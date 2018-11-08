# 字符串相关方法的通用格式：字符串.函数（）

# 1.capitalize:将字符串的首字母转换成大写字母，并且创建一个新的字符返回
str1 = 'abc'
new_str = str1.capitalize()
print(new_str)

# 2.center(width,fillerchar):将原字符串变成指定长度并且内容居中，剩下的部分使用指定的（字符：长度为1的字符串）填充
new_str = str1.center(7,'！')
print(str1,new_str)


# 3.rjust(width,fillerchar)
new_str = str1.rjust(7,'*')
print(new_str)


number = 19 # py1805009

#str(数据)：将其他任何的数据转换成字符串
num_str = str(number)
print(num_str, type(num_str))
# 让字符串变成宽度为3，内容右对齐，剩下部分使用'0'填充
new_str = num_str.rjust(3, '0')
print(new_str)
new_str = 'py1805' + new_str
print(new_str) 

# 4.ljust(width,fillerchar):左对齐

str1 = 'py1805'
new_str = str1.ljust(10, '0')
print(new_str)
new_str = new_str + num_str
print(new_str)


# 5.字符串1.join(字符串2): 在字符串2中的每个字符间插入一个字符串1
new_str = '123'.join('bbb')
print(new_str)

print('---------------')
# 6.maketrans()
new_str = str.maketrans('abc', '123')
print(new_str)
