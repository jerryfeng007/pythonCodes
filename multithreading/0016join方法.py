import threading
from time import sleep, ctime


def music():
    print('begin to listen', ctime())
    sleep(3)
    print('stop to listen', ctime())


def game():
    print('begin to play game', ctime())
    sleep(5)
    print('stop to play game', ctime())


t1 = threading.Thread(target=music)
t2 = threading.Thread(target=game)
t1.start()  # 线程1
t2.start()  # 线程2
# t1.join()  # t1不执行完，不往下执行
t2.join()  # t2不执行完，不往下执行
print('ending..........')  # 主线程
