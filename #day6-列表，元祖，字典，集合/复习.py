# -*- coding: UTF-8 -*-

# @Time : 2018/7/24 8:52
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 复习.py
# @Software : PyCharm

'''
列表：[1,3,'a','12abc']
元素 in 列表
+：链接
*：列表重复
都是创建一个新的列表
'''

for item in [{'a':10}, {'b':100}, {'a':1}]:
    print(item)

'''
元祖：不可变，有序
（1，'yu'）
'''

a = (1, 2)
print(a, type(a))


b = (10,)  # 当元祖的元素只有一个的时候，需要在元素的后面加一个逗号表示这个值是一个元祖
print(b, type(b))

'''
字典:{key:value,key1:value}
字典的增，删，改，查

del 字典[key]
字典.pop(key)

key in 字典
字典1.update(字典2)

'''

for key in student_dict:
    print(key, student_dict[key])

'''
集合：{1，'ss'}无序，可变，不会重复
增删改查
集合.add(元素)
集合.update(集合)
集合.remove(元素)
集合.pop()

数学集合运算:1.包含（<=,>=） 2.并集（|），交集（&），差集（-），补集（^）

'''

