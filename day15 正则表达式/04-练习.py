# -*- coding: utf-8 -*-

# @Time : 2018/8/3 15:04
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 04-练习.py
# @Software : PyCharm


import re

if __name__ == '__main__':
    re_str = r'/w{6,20}'
    re_str = r'[1-9]\d{4,11}'


    # 练习 IP地址是否合法
    """
    X.X.X.X
    X:0-255
    """
    re_str = r'(([1-9]|[1-9]\d|1\d{2}|2[0-4]/d|25[0-5])\.){3}([1-9]|[1-9]\d|1\d{2}|2[0-4]/d|25[0-5])'

    print(re.fullmatch(re_str, '255.7.181.111'))
