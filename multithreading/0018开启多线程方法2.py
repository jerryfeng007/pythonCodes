import threading
# 调用方法2，继承threading.Thread，然后重写他的run方法，不建议使用


class MyThread(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):  # 这个必须是run这个方法，名字不为run是不可以的，因为是重写的这个run方法
        print('aaa', self.index)


thread1 = MyThread(10)
thread1.start()   # start，其实是去执行run方法！！！！！！

thread2 = MyThread(20)
thread2.start()   # start，其实是去执行run方法！！！！！！

print('ending..........')      # 上面的子线程，跟主线程同时运行
