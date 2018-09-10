'''
列表，字典，元组，集合都是序列，都是容器类型的数据类型


列表(list)：用来存储多个数据的一种容器类型
特点：
1.有序的  2.可变的(可变指的是容器中的内容的个数和值可变)
3.元素可以是任何类型的数据 
列表的值：用[]将了列表中的元素括起来，多个元素之间用逗号隔开。[] --> 空列表


'''

# 1.怎么声明一个列表

list1 = [] #创建一个空的列表 
print(type(list1))

list2 = [1,12.9,'abc',[1,2,3,'a'],{'a':1}]
print(list2,type(list2))


# 2.将其他的数据类型转换成列表
list3 = list('abc1234')
print(list3)


list4 = list(i*2 for i in range(100) if i % 3 ==0)
print(list4)


list5 = list(i*2 for i in range(10))
print(list5)

# 2.获取列表元素
# 列表中的每一个元素都对应的一个下标：0 ~ 列表长度-1； -1 ~ -列表长度
names = ['路飞','索隆','娜美','桃之助']

# a.获取单个元素：列表名[下标]
print(names[2])
print(names[-2])

#print(names[5])  # IndexError: list out of range 

# b.获取部分元素(切片)
'''
列表名[起始下标:结束下标]：获取从起始下标开始，到结束下标前的所有元素。结果是一个列表
列表名[起始下标：结束下标：步进]：从起始下标开始，每次下标值加步进获取下一个元素，直到结束下标前位置
起始下标和结束下标都可以缺省：
			如果步进是正数，起始下标缺省就是从第一个元素开始获取
			如果步进是负数，就从最后一个元素开始获取
			如果下标缺省，步进是正数，获取到最后一个元素，
			步进是负数，从后往前获取到第一个元素

'''
names = ['路飞','索隆','娜美','桃之助']
print(names[1:4])
print(names[-4:-1])
print(names[0:4:2])
print(names[:])  #获取列表中的所有元素，从新创建一个新的列表


#c.一个一个的获取列表的元素（遍历列表）
scores = [12,45,79,36]
# for 循环遍历
for item in scores[:]:
	print(item)
print('=====')



#while 循环
index = 0
while index < len(scores):
	print(scores[index])
	index += 1

# 3.获取列表的长度（)
# len(scores)


