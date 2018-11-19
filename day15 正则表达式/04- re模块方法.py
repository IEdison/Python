# -*- coding: utf-8 -*-

# @Time : 2018/8/3 15:42
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04- re模块方法.py
# @Software : PyCharm
import re

if __name__ == '__main__':

    # 1.compile(正则字符串) 将正则表达式字符串转换成正则表达式对象
    re_obct = re.compile(r'\w{6,12}')
    print(re.fullmatch(r'\w{6,12}', 'asdasd'))

    # 2.fullmatch（正则表达式，字符串）完全匹配，从字符串开头匹配到结尾
    # 返回值是匹配对象
    match = re.fullmatch(r'\w{3}', 'asd')
    print(match)
    # a.获取匹配到的结果
    print(match.group())
    # b.获取匹配到的范围
    print(match.span())
    # c.获取匹配到的开始下标和结束下标
    print(match.start(), match.end())
    # d.获取被匹配的字符串（原字符串）
    print(match.string)
    # 应用：判断一个字符串是否是某种字符串

    # 3.match(正则表达式，字符串)不完全匹配，从字符串开头开始匹配，匹配到正则表达式对应的范围为止
    # 返回值是匹配对象，如果匹配是失败返回None

    match = re.match(r'\w{3}', 'qweasdasdad')
    print(match)
    print(match.group())
    print(match.string)

    # 应用：判断一个字符串是否以某种字符串开头


    # 4.search(正则表达式，字符串) 在制定的字符串中查找某种字符串（以正则表达式来描述）
    # 如果有多个符合条件的，只返回第一个
    # 返回值是匹配对象，如果找不到符合要求的返回None
    print(re.search(r'\d{2,}[a-z]', '1asd2asd==asd156as'))

    # 应用：判断一个字符串是否包含某种字符串

    # 5.findall（正则表达式，字符串）：去获取指定字符串中满足正则条件的所有的子串
    # 返回值是列表，列表中是符合要求的字符串，没有满足要求的字符串就返回空列表
    result = re.findall(r'[a-zA-z](\d+)', '12a123ababab=123bc456c')
    print(result)

    # 注意：在通过正则表达式获取子串的时候，可以通过正则表达式中添加括号，来约束获取的内容（只捕获括号中匹配到的内容）
    # 匹配的时候还是按原正则表达式去查找

    # 应用：字符串提取


    # 6.finditer(正则表达式，字符串)用法和findall一样，只是返回值的类型不一样
    # 返回一个迭代器
    # 注意：（）捕获部分无效，迭代器中的内容是匹配对象
    result = re.finditer(r'[a-zA-z](\d+)', '12a123ababab=123bc456c')
    for match in result:
        print(match)

    print('fasdqw4d65a4d89w'.split('a'))

    # 7.split(正则表达式，字符串)按正则表达式匹配到的字符串进行切割
    # 返回值是列表，列表元素就是切割后被分段的字符串
    result = re.split(r'[\[\]*\-]', 'asd4[456asd]5-f*64a6sd')
    print(result)

    # 8.sub(正则表达式，新字符串，原字符串) 在原字符串中查找符合正则的子串，替换成新的字符串

    """将指定字符串中所有的sb替换成****"""
    str1 = '你好sb，你全家都是sb'
    result = re.sub(r'sb|shabi|SB', '*', str1)
    print(str1, result)

