"""__author__ = 余婷"""
import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('10.7.181.117', 8050))
    while True:
        # 接收服务器返回的信息
        re_message = client.recv(1024).decode(encoding='utf-8')
        print(re_message)

        # 发送消息
        message = input('>>>')
        # message = '好吧abc'
        client.send(message.encode())



