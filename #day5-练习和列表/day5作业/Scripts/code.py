#10.输⼊一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

intCount = 0  #用来记录列表中的int元素个数
strCount = 0 #记录str元素个数
otherCount = 0
a = raw_input("plz input a string:")
# 使用for循环遍历字符串，每次循环判断当前获取的元素的类型，并给对应计数器计数
for i in a:
    if i.isdigit(): #判断i是不是int
        intCount += 1
    elif i.isalpha(): #判断i是不是str
        strCount += 1
    else:
        otherCount += 1
print ("数字=%d，字母=%d，其他=%d" % (intCount,strCount,otherCount))