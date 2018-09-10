# 添加列表元素
skills = []
print(skills)


#1.append函数
"""
列表.append(元素)
在列表的末尾添加一个元素
"""

skills.append('气体源流')
print(skills)

skills.append('拘灵遣将')
print(skills)

# 2.insert函数
'''
列表.insert（下标，元素）
在列表的指定的下标前插入一个元素


注意：在这儿,下标可以越界，如果越界，就会插入到列表的最前面或者最后面
'''
skills.insert(1,'通天箓')
print(skills)

# 3.+
'''
列表1 + 列表2 
将列表2中的元素，添加到列表1中
'''
new_skills = skills + ['风后奇门','阿威十八式']
print(new_skills)


# 练习：从控制台输入10个学生的成绩，然后保存在一个列表中。
scores = []
for _ in range(10):
	score = int(input('输入成绩'))
	scores.append(score)
print(scores)

# 