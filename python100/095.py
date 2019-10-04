# 字符串日期转换为易读的日期格式。
import time
from datetime import datetime

t = time.localtime()
print(type(t))
print(t)

tt = time.asctime(t)
print(tt)

print(time.ctime())

d = datetime.now()
print(d)

dd = datetime.strftime(d, '%Y-%m-%d %H:%M:%S')
print(dd)
