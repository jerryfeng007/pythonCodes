# 获取几天前的时间

from datetime import datetime, timedelta

t = datetime.now()
print(t)

t1 = t - timedelta(days=3)
print(t1)


# 转化为指定的格式
t2 = datetime.ctime(t1)
print(t2)

t3 = datetime.strftime(t1, '%Y-%m-%d %H:%M:%S')
print(t3)
