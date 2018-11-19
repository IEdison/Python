"""__author__ = 余婷"""

# 主要包含处理年月日时分秒对应的时间(着重时分秒)
import time

# 专门处理年月日
import datetime



if __name__ == '__main__':
    # 1.获取当前时间
    """
    时间戳：就是从格林威治时间(1970年1月1日0:0:0)到当前时间的时间差(单位是秒)
    # '2010-10-10 12:10:29'
    1. 存时间以时间戳的形式去存，可以节省内存空间(一个浮点数的内存是4/8个字节，存一个字符串一个字符占2个字节)
    2. 自带对时间加密的功能(加密更方便)
    """
    time1 = time.time()
    print(time1, type(time1))

    # 2. 将时间戳转换成struct_time
    """
    localtime(seconds)
    参数seconds：a.不传参，就是将当前时间对应的时间戳转换成struct_time
                b.传参，就是将指定的时间转换成struct_time
    """
    time1 = time.localtime()
    print(time1)

    """
    struct_time的结构:
    tm_year: 年
    tm_mon: 月
    tm_mday: 日
    tm_hour: 时
    tm_min：分
    tm_sec：秒
    tm_wday：星期(0-6 --> 周一 - 周天)
    tm_yday：当前是当年的第几天
    tm_isdst：是否是夏令时
    """
    print(time1.tm_year,time1.tm_mon, time1.tm_mday)

    # 将时间戳转换成struct_time
    struct1 = time.localtime(1000000000)
    print(struct1)


    # 2.1 将struct_time抓换成时间戳
    """
    mktime(结构时间)
    """
    """2018-12-31 23:30:40"""
    strc = time.strptime('2018-12-31 23:30:40','%Y-%m-%d %H:%M:%S')
    time1 = time.mktime(strc)

    # 时间加一个小时
    time1 += 60*60
    print('==',time.localtime(time1))



    # 3.时间的格式转换
    """
    strftime(时间格式,时间)
    将时间以指定的格式转换成字符串
    """
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(time_str)

    """
    strptime(需要转换的字符串,时间格式)
    将时间字符串转换成相应的struct_time
    """
    struct_time = time.strptime('今天是2018年8月5号', '今天是%Y年%m月%d号')
    struct_time = time.strptime('2018-7-20', '%Y-%m-%d')
    print(struct_time)

    # 4.延迟
    """
    sleep(秒)
    可以让线程阻塞指定的时间
    """
    time.sleep(10)











