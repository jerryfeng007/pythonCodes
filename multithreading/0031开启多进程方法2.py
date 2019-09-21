# 使用继承
import multiprocessing
import time


class MyProcess(multiprocessing.Process):  # 继承进程类
    def __init__(self, name):  # 如果没有参数，可以没有这几句话
        multiprocessing.Process.__init__(self)
        self.name = name

    def run(self):
        time.sleep(2)
        print('hello', self.name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = MyProcess('jerry')  # 这里可以传参数
        p.start()
        p_list.append(p)

    for p in p_list:
       p.join()

    print('ending..........')
