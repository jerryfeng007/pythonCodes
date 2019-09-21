# 进程同步, 进程也有公用的资源，比如打印到屏幕上，在同一时刻，究竟是谁先打印
import multiprocessing


def f(l, i):
    with l:  # 使用with就不用写release了，注意这里是with l, 不是with l.acquire()
        print('hello world %s' % i)  # 只要加上锁，这里就是串行的了
    # l.release() 使用with就不用写release了


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for num in range(10):
        p = multiprocessing.Process(target=f, args=(lock, num,))
        p.start()
