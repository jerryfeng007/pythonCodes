"""
案例：
输入一个列表，对于列表中的每个元素，计算0到这个元素的所有整数的平方和

分析：
本题属于计算密集型场景(cpu bound)，可以使用多进程
"""

print('-------------------------------不使用多进程------------------------------------------')
import time


def suan(i):
    print(sum(j*j for j in range(i)))


def deal(l):
    for i in l:
        suan(i)


if __name__ == '__main__':
    start = time.perf_counter()
    l = [10000000 + x for x in range(20)]
    deal(l)
    end = time.perf_counter()
    print(end - start)  # 27秒左右

print('-------------------------------使用多进程------------------------------------------')
from concurrent import futures


def suan1(i):
    return sum(j*j for j in range(i))


def deal1(l):                                              # 发现max_workers=3时间最短
    with futures.ProcessPoolExecutor(max_workers=3) as e:  # 改变了这两句,可以不写max_workers
        return e.map(suan1, l)                             # 可以return


if __name__ == '__main__':                    # 多进程必须要使用if __name__ == '__main__'
    start = time.perf_counter()
    l = [10000000 + x for x in range(20)]
    result = deal1(l)
    print(list(result))                       # 需要list()
    end = time.perf_counter()
    print(end - start)                        # 18秒左右

print('-------------------------------使用多线程------------------------------------------')


def suan2(i):
    return sum(j*j for j in range(i))


def deal2(l):
    with futures.ThreadPoolExecutor(max_workers=5) as e:  # 只改了这里
        return e.map(suan2, l)


if __name__ == '__main__':
    start = time.perf_counter()
    l = [10000000 + x for x in range(20)]
    result = deal2(l)
    print(list(result))
    end = time.perf_counter()
    print(end - start)                        # 27秒左右

print('-------------------------------使用异步------------------------------------------')
import asyncio


async def suan3(i):
    return sum(j*j for j in range(i))


async def deal3(l):
    tasks = [asyncio.create_task(suan3(i)) for i in l]  # 调用方式2
    # await asyncio.gather(*tasks)                      # 两种写法都可以
    for task in tasks:
        await task


if __name__ == '__main__':
    start = time.perf_counter()
    l = [10000000 + x for x in range(20)]
    asyncio.run(deal3(l))                          # 调用方式1
    end = time.perf_counter()
    print(end - start)                            # 27秒左右
