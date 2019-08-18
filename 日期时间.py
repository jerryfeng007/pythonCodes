print('-----------------------------------------time模块------------------------------------------------------')

# time模块
import time

# 获取当前时间戳
t1 = time.time()
print(t1)

# 获取当前时间元组
t2 = time.localtime()
print(t2)

t22 = time.localtime(t1)  # 获取某个时间戳的时间元组
print(t22)

# 格式化时间
t3 = time.ctime(t1)  # 格式化时间戳
print(t3)

t4 = time.asctime(t2)  # 格式化时间元组
print(t4)


# 自定义格式化时间   （格式字符串,时间元组）
t5 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(t5)

#                    （日期字符串，格式字符串） 转化后结果为一个时间元组
t6 = time.strptime('2019-08-11 08:36:50', '%Y-%m-%d %H:%M:%S')
print(t6)

# 把以上的时间元组转化为时间戳
t7 = time.mktime(t6)
print(t7)


# 获取cpu时间  ----统计一段程序代码的耗时
t1 = time.process_time()
for i in range(10):
    print(i)
t2 = time.process_time()
print(t2-t1)

# 休眠n秒
print('这是开始')
time.sleep(1)
print('这是结束')

print('-----------------------------------------datetime模块------------------------------------------------------')
# datetime模块有3个类：datetime类、date类、time类

import datetime
t1 = datetime.datetime.today()
print(t1)
print(t1.date(), t1.time(), t1.year, t1.month, t1.day, t1.hour, t1.minute, t1.second)

t2 = datetime.datetime.now()
print(t2)
print(t2.date(), t2.time(), t2.year, t2.month, t2.day, t2.hour, t2.minute, t2.second)

# 计算n天之后的日期
t1 = datetime.datetime.now()
print(t1)

t2 = t1 + datetime.timedelta(days=7)
print(t2)

# 获取两个日期时间的时间差
first = datetime.datetime(2018, 8, 11, 20, 30, 40)
print(first)

second = datetime.datetime(2019, 8, 11, 20, 30, 40)
print(second)

delta = second-first
print(delta)
print(delta.total_seconds())
