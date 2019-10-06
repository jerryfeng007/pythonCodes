# 计算几天前并转换为指定格式。

from datetime import datetime, timedelta

t = datetime.now()
print(t)

# 3天前
t1 = timedelta(days=-3)

t2 = t + t1
print(t2)

print(datetime.strftime(t2, '%Y-%m-%d %H:%M:%S'))


# 给定一个时间戳
timeStamp = 1557502800

t = datetime.utcfromtimestamp(timeStamp)
print(t)

tt = t + timedelta(days=-3)
print(tt)
