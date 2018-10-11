'''
字典也是一种容器类型的数据类型（序列），存的数据是以键值对的形式出现的，字典中的元素全部都是键值对
字典是可变的（可以增删改），但是是无序的（不能使用下标）

键值对：键：值（key：value）：键值对中key是形式，值才是真正要存的内容
键：理论上可以是任何不可变的数据类型，但是实际开发的时候一般使用字符串作为key
值：可以是任意数据类型

'''

# 1.声明一个字典
'''a.创建一个字典变量

'''
dict1 = {} # 创建一个空的字典
print(type(dict1))

dict2 = {'a': 1, 'b': 'abc', 'c': 3}
print(dict2)
dict2 = {'a': 1, 'b': 'abc', 'a': 3}
print(dict2)



'''b.将其他数据类型转换成字典'''
dict3 = dict([(1, 2), (3, 4)]) # 了解
print(dict3) # 列表的每个元素是元祖

# 2. 字典的增删改查
'''a.查：获取字典的元素的值
字典获取元素的值是通过key来获取的
字典[key]
'''
person = {'name': '路飞', 'age': 17, 'face': 90}
print(person['name'], person['face'])
# print(person['aaa'])   如果key不存在，会报错 KeyError
'''

字典.get(key)

'''
print(person.get('name'))
print(person.get('aaa'))   # 如果key不存在，返回None



# 注意：如果key值确定存在，使用[]语法去获取值。不确定key值是否存在才使用get方法去获取值

'''
b.增加元素\修改元素
通过key获取字典元素，然后赋值。当key存在的时候，就是修改元素的值；不存在的时候就是给字典添加键值对
'''

person['height'] = 1.8
print(person)

person['age'] = 25
print(person)

'''
q.删除:删除的是键值对
del 字典[key]
'''
print('1------------------------------')
del person['face']
print(person)




age = person.pop('age')
print(person, age)

# 3.相关的数组属性
'''
字典.pop(key) --->会返回
字典.key（）获取字典中所有的key，返回值的类型是dict——key
字典.values（）获取字典中所有的值
字典.items（）将字典中所有的键值对转换成一个一个的元祖，key作为元祖的第一个元素，把value作为元祖的第二个元素
'''

student_dict = {'name': ' 张三', 'study_id': 'py1805', 'scores': 96}
keys = student_dict.keys()
print(keys, type(keys))
for key in keys:
    print(key)

print(student_dict.values())
print(student_dict.items())
print('-------------------------------------')

# 4.遍历字典
# a.直接遍历字典获取到的是所有的key（推荐使用）
for key in student_dict:
    print(key, student_dict[key])

# b.
for key, value in student_dict.items():
    print(key, value)


# 5.列表中有字典，字典中有字典，字典中有列表
'''
声明一个变量，作用是用来存储一个班级的学生的信息。其中包括姓名，性别，年龄，电话
'''

class1 = [
    {'name': 'zs', 'age': '17', 'sex': '男', 'tel': '123456'},
    {'name': 'ls', 'age': '18', 'sex': '女', 'tel': '123000456'},
    {'name': 'ww', 'age': '19', 'sex': '男', 'tel': '123456000'}
]

class1 = {
    'name': 'py1805',
    'address': '19-1',
    'student': [
        {'name': 'as', 'age': 18},
        {'name': 'ls', 'age': 19},
        {'name': 'ww', 'age': 20}
    ]

}


# 6.其他操作
'''
1.fromkeys()
dict.fromkeys(序列,value)：创建一个新的字典，序列中的元素作为key，value作为值

'''
new_dict = dict.fromkeys('abc', 100

                         )
print(new_dict)
new_dict = dict.fromkeys(range(5), '100')
print(new_dict)
new_dict = dict.fromkeys(['abc', 'bbb', 'ccc'], '100')
print(new_dict)


'''2. in
key in 字典：判断字典中是否存在指定的key
'''
dog_dict = {'color': 'yellow', 'age': 2, 'type': '土狗'}
print('color'in dog_dict)   # 判断的是键是否存在
print('yellow' in dog_dict)

'''
3.update
字典1.update（字典2）：使用字典2的键值对去更新字典1中的键值对。如果字典2中对应键值对在字典1中不存在，就添加。存在就更新
'''
print('-------------------------------')
dict1 = {'1': 'a', '2': 'b'}
dict1.update({'1': 'aaa', '3': 'bbb'})
print(dict1)