# 由于GIL的存在，python中的多线程其实并不是真正的多线程，
# 如果想要充分的利用多核cpu资源，那么使用多进程
# 多进程 multiprocessing，主要就是解决GIL的问题
# 运行是真真正正的并行，不是并发
import multiprocessing
import time


def f(name):
    time.sleep(1)
    print('hello', name, time.ctime())


if __name__ == '__main__':  # 使用多进程，一定要有这句话，要不然执行报错
    p_list = []
    for i in range(3):  # 这是子进程
        p = multiprocessing.Process(target=f, args=('alvin',))  # 进程对象
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print('ending..........')  # 这是主进程
