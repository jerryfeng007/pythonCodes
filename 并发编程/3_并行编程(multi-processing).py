"""
-------------------------------------多进程------------------------------------------------
计算密集型场景(cpu bound)，cpu heavy，可以使用多进程

如果想使用多进程，得首先知道电脑有几核(os.cpu_count)

with futures.ProcessPoolExecutor(max_workers=3) as e:  (可以不写max_workers)
    e.map(func, 可迭代)                                (可以return)

通常省略参数 workers，系统会自动返回CPU的数量作为可以调用的进程数

如果使用多进程，必须要使用if __name__ == '__main__':  否则报错
"""

print('-------------------------------多进程--1----------------------------------------')
from concurrent import futures
import time


def suan(i):
    return sum(j*j for j in range(i))


def deal(l1):                                               # 可以不写max_workers，但发现等于3时间最短
    with futures.ProcessPoolExecutor(max_workers=3) as e:  # 主要是这两句
        return e.map(suan, l1)                              # 可以return


if __name__ == '__main__':                    # 必须要有if __name__ == '__main__'，否则报错
    start = time.perf_counter()
    l = [10000000 + x for x in range(20)]
    result = deal(l)
    print(list(result))                       # 需要list()
    end = time.perf_counter()
    print(end - start)

print('-----------------------多进程--2---有问题，为啥没执行download_one2----------------')
# import concurrent.futures
# import time
# import requests
#
#
# def download_one(url):
#     print(1111111111111111111111111)
#     resp = requests.get(url)
#     print(2222222222222222222222222)
#     print('Read {} from {}'.format(len(resp.content), url))
#     print(3333333333333333333333333)
#
#
# def download_all(sites):
#     with concurrent.futures.ProcessPoolExecutor() as p:
#         p.map(download_one, sites)
#
#
# if __name__ == '__main__':
#     sites = [
#         'https://www.baidu.com/',
#         'https://pypi.org/',
#         'https://www.sina.com.cn/',
#         'https://www.163.com/',
#         'https://news.qq.com/',
#         'http://www.ifeng.com/',
#         'http://www.ce.cn/',
#         'https://news.baidu.com/',
#         'http://www.people.com.cn/',
#         'http://www.ce.cn/',
#         'https://news.163.com/',
#         'http://news.sohu.com/'
#     ]
#     start_time = time.perf_counter()
#     try:
#         download_all(sites)
#     except Exception as e:
#         print('啥问题？', str(e))
#     end_time = time.perf_counter()
#     print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
