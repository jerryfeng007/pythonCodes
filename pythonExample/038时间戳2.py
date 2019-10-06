# 给定一个时间戳，将其转换为指定格式的时间。

import time
from datetime import datetime, timedelta

# 获取当前时间戳-----------------------------------------------------------------------
now = time.time()
# 转为时间元组
t = time.localtime(now)
print(t)
# 再转为其他格式
tt = time.strftime('%Y-%m-%d %H:%M:%S', t)
print(tt)


# 利用datetime-----------------------------------------------------------------
t = datetime.now()
print(t)

# 转换格式
tt = t.strftime('%Y-%m-%d')
print(tt)


# 指定时间戳-------------------------------------------------------------------
timeStamp = 1557502800
t = time.localtime(timeStamp)
print(t)
# 再转为其他格式
tt = time.strftime('%Y-%m-%d %H:%M:%S', t)
print(tt)


# 指定时间戳-------------------------------------------------差8小时？？？？？？？？------------------
timeStamp = 1557502800
t0 = datetime.utcfromtimestamp(timeStamp)
print(t0)
tt = t0.strftime('%Y-%m-%d %H:%M')
print(tt)
