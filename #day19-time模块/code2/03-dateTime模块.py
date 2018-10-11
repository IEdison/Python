"""__author__ = 余婷"""
import datetime

if __name__ == '__main__':

    # ============= 1.日期类(date) =========-- 只能表示年月日
    """1.类的字段"""
    # 最小日期
    print(datetime.date.min, type(datetime.date.min))
    # 最大日期
    print(datetime.date.max)
    # 最小单位
    print(datetime.date.resolution)

    """2.类方法"""
    # 获取当前日期
    today = datetime.date.today()
    print(today)

    # 将时间戳转换成日期
    today2 = datetime.date.fromtimestamp(0)
    print(today2)

    """2.对象属性"""
    # 年(year)、月(month)、日(day)属性
    print(today.year, type(today.year))
    print(today.month)
    print(today.day)

    """3.对象方法"""
    # 1. 获取指定日期对应的星期
    print(today.isoweekday())

    # 2. 将指定日期转换成指定格式的字符串日期
    print(today.strftime('%Y年%m月%d日 周%w'))

    # 3. 将日期转换成struct_time
    print(today.timetuple())


    """4.创建日期对象"""
    print(datetime.date(2017, 9, 10))

    # ========datetime类=========
    """1.类方法"""
    # 1. 将时间戳转换成datetime
    print(datetime.datetime.fromtimestamp(0))

    # 2. now(时区)： 获取当前时间
    print(datetime.datetime.now())
    now_dt = datetime.datetime.now()

    # 3. 将时间字符串按指定的格式转换成datetime对象
    print(datetime.datetime.strptime('2018-8-10 10:30:40', '%Y-%m-%d %H:%M:%S'))

    """2.对象方法"""
    # 1.将datatime对象转换成struct_time
    print(now_dt.timetuple())

    # 2.获取datatime中时分秒的部分
    print(now_dt.time())

    # 3.获取datetime中日期的部分
    print(now_dt.date())

    # 4.将datetime转换成时间戳
    print(now_dt.timestamp())

    # ============3.timedelta方法==========
    # 日期加一天
    print(today + datetime.timedelta(days=100))
    print(now_dt + datetime.timedelta(days=1))

    # 日期减两天
    print(today + datetime.timedelta(days=-2))
    print(now_dt + datetime.timedelta(days=-2))

    # 时间增加50分钟
    print(now_dt + datetime.timedelta(minutes=50))

    # 时间增加1000毫秒
    print(now_dt + datetime.timedelta(microseconds=1000))


















