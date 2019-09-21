# 进程间通讯有3个方法
# 方法1：Queue 进程队列
import time
import multiprocessing


def foo(q):
    time.sleep(1)
    print('子', id(q))
    q.put(123)
    q.put('abc')


if __name__ == '__main__':
    # q = queue.Queue()  # 这是线程队列，不能用在多进程
    q = multiprocessing.Queue()
    print('主', id(q))
    p = multiprocessing.Process(target=foo, args=(q, )) # 把q传过去
    p.start()  # 运行子进程

    data = q.get()  # 运行主进程，取不到数据，会一直卡住，直到子进程把数据put进队列
    print(data)
    data = q.get()
    print(data)
