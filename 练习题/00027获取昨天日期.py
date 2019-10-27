import datetime

d1 = datetime.date.today()
print(d1)

# 昨天
d2 = d1 - datetime.timedelta(days=1)
print(d2)

# 7天后
d3 = d1 + datetime.timedelta(days=7)
print(d3)
