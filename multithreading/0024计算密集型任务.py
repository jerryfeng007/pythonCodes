# 因为是计算密集型，不是IO密集型，所以使用多线程有可能比不使用还要慢
def sum():
    sum = 0
    for i in range(1000001):
        sum += i
    print(sum)


def mul():
    mul = 1
    for i in range(1,16):
        mul *=i
    print(mul)


import threading
t1 = threading.Thread(target=sum)
t2 = threading.Thread(target=mul)
t1.start()
t2.start()
t1.join()
t2.join()
print('ending...........')
