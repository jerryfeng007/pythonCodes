# 信号量，也是锁的一种，用来控制线程并发数
# 到现在学习了三种锁：互斥锁（同步锁）、递归锁、semaphore
# 类似于停车场，有空位置时，同步锁只能允许一个车进入，但是信号量可以允许多个车进入
import threading
from time import sleep


class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():  # 同时有5个线程运行
            print(self.name)
            sleep(3)
            semaphore.release()


semaphore = threading.Semaphore(5)  # 创建锁对象，5 表示能有几个线程进去；
# ------------------------------------如果设置为1，就相当于同步锁

thrs = []

for i in range(100):
    thrs.append(MyThread())

for t in thrs:
    t.start()
