import threading
from time import sleep
# 多线程利器：队列
# 队列是一种数据结构（list、dict也是数据结构）
# 列表是不安全的数据结构
# 以下是列表的一个例子，运行会报错，可以用同步锁或者信号量来解决，但是也可以用队列，不用列表
list1 = [1, 2, 3, 4, 5]


def a():
    # lock.acquire()
    while len(list1):
        # print(t.name)
        b = list1[-1]
        print(t.name)
        print(b)
        sleep(1)
        list1.remove(b)
    # lock.release()


list2 = []
# lock = threading.Semaphore(1)
# lock = threading.Lock()
for i in range(2):
    t = threading.Thread(target=a)
    t.start()
    list2.append(t)

for t in list2:
    t.join()
