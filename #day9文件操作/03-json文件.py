# -*- coding: utf-8 -*-

# @Time : 2018/7/26 15:43
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-json文件.py
# @Software : PyCharm


'''
数据本地化：将数据保存到本地文件中

json文件（文本），就是文件后缀是.json的文件。内容必须是json格式的内容

json格式：
1.内容是字符串
2.最外层是字典，字典里面就必须是键值对
3.最外层是数组（列表），数组里面的内容必须是数组


'''
# json 是python中内值得一个模块，专门用来处理json数据的

import json

if __name__ == '__main__':
    pass
    """1.json文件的读操作"""
    with open('./files/test/test.json', 'r', encoding='utf-8') as f:

        #直接使用read（）去读，获取到的字符串数据，包含了json文件中的所有内容（包括所有注释部分）
        #content = f.read()
        #print(content,type(content))
        """
 !!!!!  load（文件对象）：获取json文件中的内容,返回值的类型是json文件最外层的对应的数据类型
        
        
        dict ----> dict
        array ----> list
        string ----> str
        number -----> int/float
        true/false ----> True/False
        null -----> None
        """
        content = json.load(f)
        print(content, type(content), content['成绩'][1])


    """2.json文件的写操作"""
    with open('./files/test/new.json', 'w', encoding='utf-8') as f:
        """
 !!!!!!  dump(写的内容，文件对象)
        
        """


        w_content =[
            {'name': 'a1', 'age': 18},
            {'name': 'a2', 'age': 20}
        ]
        json.dump(w_content, f)
        """
        3.json模块的其他操作
        loads(字符串，编码方式) ----》将指定的字符串，转化成json数据 
        将字符串转换成字典\将字符串转换成列表

        """
        # {"a":1,"b":2,"c":3}
        # ["a",100,{"a":1,"b":2,"c":3}]
        content = json.loads('{"a":1,"b":2,"c":3}', encoding='utf-8')
        print(content, type(content))

        """
        4.dumps(对象)
        将对象（字典或者列表）转换成json字符串
        字典/列表转换成json字符串
        """
        content = json.dumps(['aaa', 1, True])
        # content = '["aaa", 1, True]'
        content2 = str(['aaa', 1, True])
        # content2 = '['aaa', 1, True]'
        print(content, content2, type(content))


# 练习:输入学生的姓名和电话，保存到本地（要求下次启动程序，再添加学生的时候，之前添加的学生信息还在）
name = input('名字：')
tel = input('电话：')
student = {'name': name, 'tel': tel}

try:
    with open('./files/test/student.json', 'r', encoding='utf-8') as f:
        all_students = json.load(f)
except FileNotFoundError:

    with open('./files/test/student.json', 'w', encoding='utf-8') as f:
        all_students = {}

        all_students.append(student)
        json.dump(all_students, f)

