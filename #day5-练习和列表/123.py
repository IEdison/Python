# -*- coding: utf-8 -*-

# @Time : 2018/8/10 15:42
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 123.py
# @Software : PyCharm
import re
str = 'a1b2c3567d'
re_str = r'\d{1}'
list = re.findall(re_str,str)
print(list)
sum = 0
for index in range(len(str)):
    if str[index] in list:
        sum += index
print(sum)