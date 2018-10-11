# 1.for 和 while 的选择

'''
for循环的循环次数是确定的，while循环的循环次数可以不确定

1.循环次数不确定的时候选择while循环。次数确定一般使用for循环
2.通过循环遍历一个序列中的值，使用for循环
'''



# 2.input()
# 接收从控制台输入的数据（输入的数据以回车结束）
# 程序中遇到input()函数，程序会阻塞，等待用户输入完成后，才会接着执行后面的代码
# 使用value去保存控制台输入的数据

# value = int(input())
# print('====')


#3.产生随机数
# python中有一个内置模块，可以产生随机数：random
'''
randint(m,n):产生一个m~n的随机数(整数)
'''
import random
number = random.randint(0,10)
print(number)
