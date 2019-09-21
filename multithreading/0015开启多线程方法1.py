import threading
from time import sleep


def hi(num):
    print('hello %s' % num)
    sleep(3)


t1 = threading.Thread(target=hi, args=(8,))  # 创建了一个线程的对象t1
t1.start()  # 线程1

t2 = threading.Thread(target=hi, args=(9,))  # 创建了一个线程的对象t2
t2.start()  # 线程2

print('ending..........')  # 主线程

# 2个子线程、一个主线程， 3个线程同时执行！！！！！！！！！！！！！！！！！！！！！！
# 等3秒
# 结束
