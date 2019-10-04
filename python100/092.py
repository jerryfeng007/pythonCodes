# 时间函数2
import time
t1 = time.time()

for i in range(300000):
    print(i)

t2 = time.time()

print(t2 - t1)
