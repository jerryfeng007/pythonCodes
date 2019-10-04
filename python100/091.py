# 时间函数

import time
t = time.time()
print(t)

t2 = time.ctime(t)
print(t2)

t3 = time.localtime(t)
print(t3)
t4 = time.asctime(time.localtime(t))
print(t4)
