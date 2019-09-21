# # 生产者-消费者问题与queue模块（队列）
#
# 生产者-消费者模型
# queue
# 生产者 和 消费者 共享一个队列，生产的商品放在队列里面
# 队列操作不是原子操作，所以需要线程锁来保护这个队列，让他变成原子操作，否则会产生脏数据

from random import randrange
from time import ctime, sleep
from threading import Lock, Thread
from queue import Queue
lock = Lock()   # 创建线程锁对象


class MyThread(Thread):
    def __init__(self,func,args):
        super().__init__(target=func, args=args)
# 向队列中添加商品


def writeQ(queue):
    lock.acquire()
    print('生产了一个对象，并将其添加到队列中', end=' ')
    queue.put('商品')
    print('队列尺寸',queue.qsize())
    lock.release()
# 从队列中获取商品


def readQ(queue):
    lock.acquire()
    queue.get(1)
    print('消费了一个对象，队列尺寸：',queue.qsize())
    lock.release()
# 生成若干个生产者


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randrange(1,4))
# 生成若干个消费者


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randrange(2,6))


def main():
    nloops = randrange(2, 6)
    q = Queue(32)  # 创建队列，初始的尺寸是32
    t1 = MyThread(writer, (q, nloops))
    t2 = MyThread(reader, (q, nloops))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
main()
