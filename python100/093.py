# 时间函数3
import time
t1 = time.process_time()

for i in range(300000):
    print(i)

t2 = time.process_time()

print(t2 - t1)
