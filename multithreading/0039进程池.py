# 进程池内部维护一个进程序列，当使用时，去进程池中获取一个进程，
# 如果进程池没有可供使用的进程，那么程序就会等待，直到进程池中有可用的进程为止
# 进程池有2个方法
# apply 同步，不用
# apply_async 异步，用这个
import time
import os
import multiprocessing


def Foo(i):
    time.sleep(1)
    print(i)
    print('foo:', os.getpid())  # 子进程的id
    print('parent', os.getppid())
    return 'hello %s' % i  # 这里return给了回调函数Bar中的参数
                             # 如果把这里的return语句省略，那么其实是return None
                             # 所以，Bar函数一定要有参数来接收return的值，即便这个值是None


def Bar(arg):  # 必须得有arg，即便Foo函数中没有return语句
               # （没有return语句，其实是return None，那么arg的值为None，打印logger:None）
    print('hello')
    print('bar:', os.getpid())  # 进程id为主进程的id，因为是主进程在调用回调函数Bar
    print('logger:', arg)  # Foo函数没有return语句时，这里打印logger:None


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)  # 如果不写，默认是按电脑默认的cpu核数，
                                    # 这样也可以检验自己的电脑是几核的
    print('main:', os.getpid())  # 主进程id

    for i in range(20):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        # 回调函数：某个动作或函数执行成功后，再去执行的函数
        # 在这里，其实是主进程apply_async调用的回调函数，而不是func调用的，可以打印进程id看一下
        # 为啥要让回调函数在主进程调用，而不是子进程调用？有啥好处?
        # pool.apply_async(func=Foo,args=(i,))
        # pool.apply(func=Foo, args=(i,)) 基本上不用，因为是同步，需要等

    pool.close()  # 在进程池里，close必须放在join前面
    pool.join()  # close和join顺序是固定的，记住就行
    print('end')
