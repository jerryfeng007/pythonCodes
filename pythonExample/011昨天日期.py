# 获取昨天日期
import datetime

d = datetime.datetime.now()
print('现在：', d)

d1 = datetime.timedelta(days=1)  # 可以为负数
d2 = datetime.timedelta(days=-1)  # 可以为负数

d3 = d + d1
print('明天：', d3)

d4 = d + d2
print('昨天：', d4)
