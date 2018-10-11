# -*- coding: utf-8 -*-

# @Time : 2018/8/1 17:05
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 练习2.py
# @Software : PyCharm

import json

def download_data():
    with open('./data.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
        return content['data']

print(download_data())

