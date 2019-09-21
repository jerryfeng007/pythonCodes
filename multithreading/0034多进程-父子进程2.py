# Process类
import time
import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self, i):
        super(MyProcess, self).__init__()  # 继承父类的init方法
        # multiprocessing.Process.__init__(self)
        self.i = i

    def run(self):
        time.sleep(1)
        print(self.is_alive())
        print(self.i)
        print(self.pid)
        time.sleep(1)


if __name__ == '__main__':
    p_list = []
    for i in range(2):
        p = MyProcess(i)
        p_list.append(p)
        p.start()

    print('main process end')
