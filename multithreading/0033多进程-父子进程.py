import os
import time
import multiprocessing


def info(title):
    print('title:', title)
    print('parent process:', os.getppid())  # ppid是pycharm的进程 爷爷
    print('process id:', os.getpid())   # 这里是当前运行的进程  父亲


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main process line')
    time.sleep(1)
    print('---------------------')
    p = multiprocessing.Process(target=info, args=('yuan',))  # 这里是当前进程创建的子进程  儿子
    p.start()
    p.join()
