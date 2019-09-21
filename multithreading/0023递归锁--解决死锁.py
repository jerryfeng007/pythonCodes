# 解决死锁，把原来的A、B两把锁换为了rlock一把锁，完美解决
import threading
import time


class MyThread(threading.Thread):
    def actionA(self):
        rlock.acquire()   # 内部的计数器等于1，每次acquire一次就会加1
        print(self.name, 'gotA', time.ctime())
        time.sleep(2)

        rlock.acquire()  # 内部的计数器等于2
        print(self.name, 'gotB', time.ctime())
        time.sleep(1)

        rlock.release()  # 内部的计数器等于1，每次release一次就会减1
        rlock.release()  # 内部的计数器等于0

    def actionB(self):
        rlock.acquire()  # 内部的计数器等于1
        print(self.name, 'gotB', time.ctime())
        time.sleep(2)

        rlock.acquire()  # 内部的计数器等于2
        print(self.name, 'gotA', time.ctime())
        time.sleep(1)

        rlock.release()  # 内部的计数器等于1
        rlock.release()  # 内部的计数器等于0

    def run(self):
        self.actionA()
        self.actionB()


rlock = threading.RLock()
l = []

for i in range(5):
    t = MyThread()
    t.start()
    l.append(t)

for i in l:
    i.join()

print('ending.......')
