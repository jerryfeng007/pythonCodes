import threading
import time


class MyThread(threading.Thread):
    def actionA(self):
        A.acquire()
        print(self.name, 'gotA', time.ctime())
        time.sleep(2)

        B.acquire()
        print(self.name, 'gotB', time.ctime())
        time.sleep(1)

        B.release()
        A.release()

    def actionB(self):
        B.acquire()
        print(self.name, 'gotB', time.ctime())
        time.sleep(2)

        A.acquire()
        print(self.name, 'gotA', time.ctime())
        time.sleep(1)

        A.release()
        B.release()

    def run(self):
        self.actionA()
        self.actionB()


A = threading.Lock()
B = threading.Lock()
l = []

for i in range(5):
    t = MyThread()
    t.start()
    l.append(t)

for i in l:
    i.join()

print('ending.......')
