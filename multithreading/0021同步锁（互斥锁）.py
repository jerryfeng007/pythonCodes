# 也叫互斥锁
import threading
from time import sleep


def sub():
    global num
    lock.acquire()  # 锁上
    num -= 1          # 锁上之后这部分就是串行了
    sleep(0.001)      # 锁上之后这部分就是串行了
    lock.release()  # 释放锁
    print(num)


num = 100
l = []
lock = threading.Lock()  # 创建线程锁对象

for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()

print('ending..........')
