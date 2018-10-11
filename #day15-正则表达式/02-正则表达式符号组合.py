# -*- coding: utf-8 -*-

# @Time : 2018/8/3 10:47
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 02-正则表达式符号组合.py
# @Software : PyCharm

import re
if __name__ == '__main__':
    # 1.[]匹配[]中出现的任意一个字符
    """匹配一个字符串，前三位是abc，第四位是1或a"""
    re_str = r'abc[1a，]'
    print(re.fullmatch(re_str, 'abc1'))
    print(re.match(re_str, 'abc1asd'))

    """第一位是数字或者下划线，后面是abc"""
    re_str = r'[\d_ ]abc'
    print(re.fullmatch(re_str, ' abc'))

    # 2.[^]匹配不在中括号中出现的任意一个字符
    """匹配一个字符串，前三位是abc，第四位不是数字也不是a"""
    re_str = r'abc[^\da]'
    print(re.fullmatch(re_str, 'abc '))

    # 3.*：匹配0次或者多次
    """匹配一个字符串，前面是0个后者多个数字字符，然后是abc"""
    re_str = r'\d*abc'
    print(re.fullmatch(re_str, '1234abc'))

    """
    [0-9]:匹配0到9中的任意一个字符
    [1-8]:匹配1到8
    [a-z]:匹配任意一个小写字母
    [A-Z]:匹配一个大写字母
    """
    re_str = r'[a-z,A-Z]'
    print(re.fullmatch(re_str, 'B'))

    # 写一个正则表达式，判断一个字符串是数字字符串（不能空串）

    re_str = r'\d\d*'
    re_str = r'[0-9][0-9]*'
    print(re.fullmatch(re_str, '123456'))

    # 写一个正则表达式，检测一个字符串是否是合格的标识符（字母数字下划线，数字不开头）
    re_str = r'[^0-9]\w*'
    print(re.fullmatch(re_str, '_abc'))

    # 4. + :匹配一次或者多次
    """匹配一个字符串开头出现一次或者多个数字字符，然后再有0次或者多次数字，字母，下划线"""
    re_str = r'\d+\w*'
    print(re.fullmatch(re_str, '123asd456'))

    # 5. ?：匹配0次或者1次
    """"""
    re_str = r'[a-z]?123'
    print(re.fullmatch(re_str, 'a123'))

    # 6.判断一个字符串是否是正整数字符串'123'-> 成功 '1234'-->成功 '0123'-->None
    re_str = r'[+]?[1-9]\d*'
    print(re.fullmatch(re_str, '+123'))

    # 7.{N} 匹配N次
    """前面5个数字，然后是abc"""
    re_str = r'\d{5}abc'

    # 前三位是12ab中的任意三次，例如11a，11b，aab，abb，aaa
    re_str = r'[12ab]{3}abc'
    print(re.fullmatch(re_str, '111abc'))


    # 8.{N，}匹配大于等于N次
    """前面至少三位数字，后面随意"""
    re_str = r'\d{3,}.*'
    print(re.fullmatch(re_str, '337biasd123nlmp;'))

    # 9.{M,N}匹配最少M次，最多N次
    """密码要求：数字，字母组成，并且8-16位"""
    re_str = r'[\da-zA-Z]{8,16}'
    print(re.fullmatch(re_str, 'ab1a5s6d1a6'))

    # 10.|：分之（运算等级低）
    # 匹配一个字符串，是三个数字字符或者是三个小写字母
    re_str = r'\d{3}|[a-z]{3}a'
    print(re.fullmatch(re_str, 'abca'))

    # 11.（）匹配的时候是分组，让括号中的正则条件变成一个整体
    re_str = r'(123){3}'  # （整体重复三次）
    print(re.fullmatch(re_str, '123123123'))

    re_str = r'(\d\w[0-3]){2}'
    print(re.fullmatch(re_str, '7b26a1'))

    """======以下了解======="""

    # 12.*? ： 重复任意次，尽可能少的重复
    re_str = r'ba*?b'
    print(re.match(re_str, 'baaab'))

    # 13.+?: 重复一次或多次，尽可能少的重复
    re_str = r'ba+?'
    print(re.match(re_str, 'baaaaaa'))

    # 14.？？：重复0次或者1次，尽可能少的重复
    re_str = r'ab??'
    print(re.match(re_str, 'abbbbbb'))

    # 15.{N,}？：重复至少N次，尽可能少的重复
    # 16.{M,N}？：重复M到N次，尽可能少的重复