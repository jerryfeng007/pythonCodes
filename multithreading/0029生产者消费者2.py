# 需要注意的是，q.task_done和q.join()是成对出现的，要不然么意义

import threading
import queue
import time
import random
q = queue.Queue()


def producer(name):
    count = 0
    while count < 10:
        print('making......')   # 制作包子
        time.sleep(random.randrange(4, 10))  # 制作包子需要时间，1或2秒
        q.put(count)
        print('生产者 %s has produced %s 包子' % (name, count))
        count += 1
        q.task_done()  # 通知队列，放了一个包子
        # q.join()  # 顾客取了包子给队列发的信号，这里收到信号，才往下执行，要不然卡在这里
        print('ok......')


def customer(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(1))  # 吃包子需要时间
        print('waiting......')
        q.join()  # 收到队列放包子的信号，然后再去取包子，要不然就会卡在这里等，类似于t.join()
        data = q.get()
        # q.task_done()  # 取了包子，然后给队列发一个信号
        print('顾客 %s has eaten %s 包子' % (name, data))
        count += 1


p1 = threading.Thread(target=producer, args=('A君',))
c1 = threading.Thread(target=customer, args=('B君',))
c2 = threading.Thread(target=customer, args=('C君',))
c3 = threading.Thread(target=customer, args=('D君',))

p1.start()
c1.start()
c2.start()
c3.start()
