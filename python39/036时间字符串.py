# 给定一个字符串的时间，将其转换为时间戳。
a1 = "2019-5-10 23:40:00"

import time

# 先转化为时间元组
t = time.strptime(a1, '%Y-%m-%d %H:%M:%S')
print(t)

# 再转化
tt = time.mktime(t)
print(tt)


# 转换为其他格式
# 先转换为时间元组
t1 = time.strptime(a1, '%Y-%m-%d %H:%M:%S')
print(t1)

# 再转换
t2 = time.strftime('%Y/%m/%d %H/%M/%S', t1)
print(t2)
