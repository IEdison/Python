"""__author__ = 余婷"""
import itchat

if __name__ == '__main__':
    # 1.登录
    itchat.auto_login(hotReload=True)

    all_friend = itchat.get_friends()
    for item in all_friend:
        itchat.send_msg('我结婚，请发份子钱给我', item['UserName'])
        # print(item)
        # print(item['NickName'])

    # while True:
    #     itchat.send_msg('你好吗', all_friend[1]['UserName'])

