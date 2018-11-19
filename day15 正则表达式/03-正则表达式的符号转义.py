# -*- coding: utf-8 -*-

# @Time : 2018/8/3 14:33
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 03-正则表达式的符号转义.py
# @Software : PyCharm

"""
正则中：. \ [] {} () * $ + ? ^ | 这些字符有特殊意义，
所以在正则表达式中，如果想要单纯表达这些字符，需要在前面加'\'；

注意：1.-，[],^ ,\在中括号中可能是特殊的符号,需要在前面加\
      2.  . {} () * + ? $ |在中括号中可以不用加\,用来表示字符
"""
import re
if __name__ == '__main__':
    re_str = r'\d+\.\d+'
    print(re.fullmatch(re_str, '12.89'))

    re_str = r'[+*$?|^\.]'
    print(re.fullmatch(re_str, '+'))

    re_str = r'[\^]'    # 匹配 字符^
    re_str = r'[\\]'    # 匹配 字符\
    re_str = r'[$]'
    re_str = r'[\[]]'
    print(re.fullmatch(re_str, '[]'))


    # 1. \数字 ----> 匹配前面第N个组中匹配到的内容
    re_str = r'([0-9][a-z]{2})\d\1'
    print(re.fullmatch(re_str, '1hu21hu'))
