print('----------------------------协程和线程的具体区别------------------------------------------')

import asyncio
# import time


# async def worker_1():
#     print('worker_1 start')
#     await asyncio.sleep(1)
#     print('worker_1 done')
#
#
# async def worker_2():
#     print('worker_2 start')
#     await asyncio.sleep(2)
#     print('worker_2 done')
#
#
# async def main():
#     print('before await')
#     await worker_1()
#     print('awaited worker_1')
#     await worker_2()
#     print('awaited worker_2')
#
# s = time.time()
# asyncio.run(main())
# e = time.time()
# print(e-s)  # 总共3秒


import asyncio
import time


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)   # 从当前任务切出，事件调度器开始调度 worker_2
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)   # 从当前任务切出
    print('worker_2 done')


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1  # 用户选择从当前的主任务中切出，事件调度器开始调度 worker1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')       # 总共2秒

s = time.time()
asyncio.run(main())
e = time.time()
print(e-s)
