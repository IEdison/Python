
'''
1.什么是元祖
元祖就是不可变的列表，列表中除了可变的操作以外，其他的操作都说使用于元祖
元祖值：a.使用（）将元素包含起来，多个元素之间用逗号隔开，比如：（1,2,‘abc’）
        b.元素的类型可以是任何类型


2. 增删改，相关操作不能作用于元祖。查可以
'''
colors = ('red', 'green', 'yellow', 'purple')
# 1.查（和列表的查一模一样，没有任何区别）
print(colors[1])
print(colors[0:3])
print(colors[0::2])
for item in colors:
    print(item)

# 2.len
print(len(colors))

# 3.in ,not in
print('red' in colors)

# 4 +和*
print((1, 2) + (3, 4))
print((1, 2) * 2)

# 5.元祖补充：
'''
1.获取元祖的元素
'''
names = ('1', '2', '3')
x, y, z = names  # 通过多个变量分别获取元祖的元素(变量个数和元素个数一样)
print(x, y)

names = ('name1', 'name2', 'name2_2', 'name2_3', 'name3')
first, *mid, last = names  # 通过变量名前加*可以把变量变成列表，获取多个元素
print(first, mid, last)

*name1, name = names
print(name1, name)

name, *name1 =names
print(name, name1)


