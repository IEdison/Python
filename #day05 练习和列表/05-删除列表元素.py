# 注意:不管是添加元素还是删除元素，都会重新分配下标！！！！

# 删除列表元素

films = ['肖申克的救赎','阿甘正传','触不可及','怦然心动']
# 1.del语句
'''
del可以删除任何数据

del 列表[下标]：删除列表中指定下标的元素

注意：这儿的下标不能越界
'''
del films[3]
print(films)


# 2.remove方法
'''
列表.remove(元素):删除列表中的指定的元素(如果有同一个元素，只删除最前面的那一个)
注意：如果要删除的元素不在列表中，会报错
'''
films.remove('阿甘正传')
print(films)

#3.pop方法
'''
列表.pop():将列表中最后一个元素取出来
列表.pop(下标):将列表中指定下标的元素取出来

注意：这儿的下标不能越界

'''
print(films)
film = films.pop()
print(films,film)
print('-----------------------')

film = films.pop(0)
print(films,film)


scores = [25,56,63,90,84,52,23]
scores2 = []
for _ in range(len(scores)):
	score = scores.pop()
	if score > 60:
		scores2.append(score)
print(scores2)



'''

new_score = scores[:]
for item in new_score
'''


scores = [25,56,63,90,84,52,23]
# score[:] = scores 

for item in scores[:]:
	if item < 60:
		scores.remove(item)
print(scores)