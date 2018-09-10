"""
--hcy
"""
a = int(input('请输入一个自然数：'))
print(a**2)

sum1 = 0
for x in range(1, 101):
    sum1 += x
print('和：%d 平均值：%.2f' % (sum1, sum1 / 100))


# 5.求斐波那锲数列的第n个数是多少
n = int(input('请输入一个整数：'))
a = 1
b = 1
c = 1
for x in range(1, n+1):
    if n < 3:
        continue
    a = b
    b = c
    c = a + b
print('第%d个数是：%d' % (n, c))
