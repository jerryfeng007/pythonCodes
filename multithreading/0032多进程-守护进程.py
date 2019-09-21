# 守护进程
import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def run(self):
        time.sleep(2)
        print('hello', self.name, time.ctime())  # 这里的self.name是进程名


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = MyProcess()
        p.daemon = True  # 守护进程，守护主进程，一定要在start方法之前设置
        p.start()
        p_list.append(p)

    time.sleep(1)  # 这里设置了时间，比上面的2秒要短，所以子进程跟随主进程退出，直接打印ending
    print('ending..........')
