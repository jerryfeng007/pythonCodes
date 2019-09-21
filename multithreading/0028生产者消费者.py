# 生产者消费者模式，是通过一个容器来解决生产者和消费者的强耦合问题
# 生产者和消费者之间不直接通讯，而是通过阻塞队列来通讯
# 所以生产者生产完之后不用等消费者处理，直接给阻塞队列
# 消费者不找生成者要数据，而是直接从阻队列里取
# 阻塞队列相当于一个缓冲区，平衡了生产者和消费者的处理能力
import threading
import queue
import time
import random
q = queue.Queue()


def producer(name):
    count = 0
    while count < 10:
        print('making......')   # 制作包子
        time.sleep(random.randrange(3))  # 制作包子需要时间，1或2秒
        q.put(count)
        print('生产者 %s has produced %s 包子' % (name, count))
        count += 1
        q.task_done()  # 通知队列，放了一个包子
        print('ok......')


def customer(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(2))  # 吃包子需要时间
        if not q.empty():   # 注意，这里最初使用了 if  q.not_empty()，不会执行else语句
            data = q.get()
            q.join()  # 收到队列放包子的信号
            print('顾客 %s has eaten %s 包子' % (name, data))
        else:
            print('没有包子')
        count += 1


p1 = threading.Thread(target=producer, args=('A君',))
c1 = threading.Thread(target=customer, args=('B君',))
c2 = threading.Thread(target=customer, args=('C君',))
c3 = threading.Thread(target=customer, args=('D君',))

p1.start()
c1.start()
c2.start()
c3.start()
