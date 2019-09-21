# GIL概念
# 由于GIL的存在，python中的多线程其实并不是真正的多线程，
# 如果想要充分的利用多核cpu资源，那么使用多进程
import threading
import time


def sum():
    sum = 0
    for i in range(100000000):
        sum += i
    print(sum)


def mul():
    mul = 1
    for i in range(1, 100):
        mul *= i
    print(mul)


t1 = threading.Thread(target=sum)
t2 = threading.Thread(target=mul)

list = []
list.append(t1)
list.append(t2)
start = time.time()

for t in list:
    t.start()
for t in list:
    t.join()

# sum()
# mul()
print('cost', time.time()-start)

# 问题：多核没用上
# GIL： global interpreter lock 全局解释锁
# 因为有GIL的存在，无论启多少个线程，有多少个cpu，
# python在执行的时候会淡定的在同一时刻只允许一个线程运行
# 任务：IO密集型，计算密集型。 sleep等同于IO操作，爬虫也属于IO密集型，使用多线程没问题
# 对于IO密集型的任务，python多线程是有意义的，可以采用多进程+协程
# 对于计算密集型的任务，python多线程就不推荐，python就不适用
