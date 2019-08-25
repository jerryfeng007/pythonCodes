"""
协程(coroutine)，是实现并发编程的一种方式
一说并发，会想到多线程/多进程，他们是解决并发问题的经典模型之一

协程和多线程的区别，主要在于两点：
一是协程为单线程
二是协程由用户决定，在哪些地方交出控制权，切换到下一个任务。

协程的写法更加简洁清晰，把 async / await 语法和 create_task 结合来用，对于中小级别的并发需求已经毫无压力

写协程程序的时候，你的脑海中要有清晰的事件循环概念，
知道程序在什么时候需要暂停、等待 I/O，
什么时候需要一并执行到底。
"""

print('----------------------------------------爬虫例子-----------------------------------------')

import time


# def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('OK {}'.format(url))
#
#
# def main(urls):
#     for url in urls:
#         crawl_page(url)  # 五个页面分别用了1秒到4秒，加起来一共用了10秒
#
#
# time_s = time.time()
# main(['url_1', 'url_2', 'url_3', 'url_4'])
# time_e = time.time()
# print(time_e - time_s)

# 这种爬取操作，完全可以并发化。我们就来看看使用协程怎么写。

print('----------------------------------------使用协程写异步程序-----------------------------------------')

'''
asyncio  实现协程需要导入这个库
async    声明异步函数
调用异步函数，得到的是一个协程对象(coroutine object)，并不会执行这个函数

协程的执行，有多种方法：
1.通过await来调用：和python正常执行是一样的，程序会阻塞在这里，进入被调用的协程函数，执行完毕返回后再继续
                    await是同步调用
2.通过asyncio.create_task()
3.需要asyncio.run()来触发运行  python3.7之后才有

一个非常好的编程规范是，
asyncio.run(main())作为主程序的入口函数，在程序运行周期内，只调用一次asyncio.run
'''

# import asyncio
#
#
# async def crawl_page1(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))
#
#
# async def main(urls):
#     for url in urls:
#         await crawl_page1(url)
#
# time_s = time.time()
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# time_e = time.time()
# print(time_e - time_s)  # 还是10秒？

'''
运行以上程序，发现时间仍然是10秒，为啥?
因为await是同步调用，上面相当于用异步接口写了个同步代码

接下来怎么办呢？

协程中的一个概念 --- 任务（task）
'''

print('------------------------------利用asyncio.create_task()执行协程-----------------------------')

import asyncio


async def crawl_page2(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)      # 这里的await会交出控制权，会切出
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page2(url)) for url in urls]
    for task in tasks:
        await task       # 运行总时长等于运行时间最长的爬虫


s = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
e = time.time()
print(e-s)

'''
有了协程对象（调用异步函数，得到协程对象），便可以通过 asyncio.create_task 来创建任务
任务创建后很快就会被调度执行，这样，我们的代码也不会阻塞在任务这里。
所以，我们要等所有任务都结束才行，用：for task in tasks: await task
'''

print('------------------------------task的另一种执行方法--------------------------------------')

import asyncio


async def crawl_page3(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page3(url)) for url in urls]
    await asyncio.gather(*tasks)  # 注意这里

s = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
e = time.time()
print(e-s)

'''
*tasks 解包列表，将列表变成了函数的参数；与之对应的是， ** dict 将字典变成了函数的参数
'''
