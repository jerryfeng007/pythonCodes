# 线程、进程、协程
# python多线程的特点：无法利用多核，无法实现真正的并行
# 协程---又叫微线程，协作式，非抢占式（进程、线程都是抢占式）
# 协程，可以按我们的需求，我们控制切换到哪； 进程和线程不是我们能控制的
# yield(是最底层的一个协程)
# 用户态的切换
# key：什么时候切换是关键
# 协程主要解决的也是IO操作
# 协程，本质上是一个线程
# 协程的优势：没有切换的消耗，没有锁的概念（本身就是一个线程，不会抢占）
# 存在的问题：本身就是一个线程，所以不能用多核-----但是可以利用多进程+协程 解决这个问题
# 多进程+协程，一个很好的解决并发的方案

# yield的简单实现 （yield是最底层的一个协程）
import time


def consumer(name):  # 这不是一个函数，是生成器， 因为有yield
    print('ready to eat baozi')
    while True:
        new_baozi = yield
        print('%s is eating baozi %s' % (name, new_baozi))


def producer():
    r = con.__next__()  # 切换
    r = con2.__next__()  # 切换
    n=0
    while 1:
        time.sleep(1)
        print('producer is making baozi %s and %s' % (n, n+1))
        con.send(n)  # 切换
        con2.send(n+1)  # 切换

        n+=2


if __name__ == '__main__':
    con = consumer('c1')   # 生成器对象
    con2 = consumer('c2')  # 生成器对象
    producer()
