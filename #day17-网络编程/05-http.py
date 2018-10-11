# -*- coding: utf-8 -*-

# @Time : 2018/8/7 15:26
# @Author ：Hcy
# @Email : 297420160@qq.com
# @File : 05-http.py
# @Software : PyCharm

"""
服务器：python\java\php等等

HTTP：为了可以让客户端和服务器能够进行有效的数据交流
""
客户端：网页（js），IOS设备上的软件（oc/swift），Android设备上的软件(java)


python中访问网络的数据：第三方库requests

"""
from requests import request
if __name__ == '__main__':
    # https://www.apiopen.top/satinApi?type=1&page=1
    # GET请求：参数以？号的形式拼接到url地址后面。多个参数用&隔开
    # 1.确定url
    url = 'https://www.apiopen.top/satinApi?type=1&page=1'

    # 2.发送请求
    """
    resuest(请求方式，请求地址)
    返回值：响应
    """
    response = request('GET', url)
    print(type(response), response)

    # 1.以字符串的形式获取响应体（服务器返回的数据）
    text = response.text
    print(type(text), text)

    # 2.以json的形式获取响应体
    json = response.json()
    print(type(json), json)

    # 3.以二进制的形式获取响应体
    content = response.content
    print(type(content), content)
