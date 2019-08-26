"""
https://time.geekbang.org/column/article/103358

Asyncio
和其他 Python 程序一样，asyncio是单线程的，它只有一个主线程，但是可以进行多个不同的任务（task）
这些不同的任务，被一个叫做 event loop(事件循环) 的对象所控制

对于 Asyncio 来说，它的任务在运行时不会被外部的一些因素打断，
因此 Asyncio 内的操作不会出现 race condition 的情况，这样你就不需要担心线程安全的问题

requests 库并不兼容 Asyncio，但是 aiohttp库兼容

如果你需要 await 一系列的操作，就得使用 asyncio.gather()；
如果只是单个的 future，或许只用asyncio.wait() 就可以了

"""
print('-------------------------------使用aiohttp-----非常快------------------------------')
import asyncio
import aiohttp
import time


async def download_one(url):
    async with aiohttp.ClientSession() as session:                     # 注意这里的写法
        async with session.get(url) as resp:                           # 注意这里的写法
            print('Read {} from {}'.format(resp.content_length, url))  # 注意这里


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        'http://pic33.nipic.com/20131007/13639685_123501617185_2.jpg',
        'http://pic1.win4000.com/wallpaper/c/53cdd1f7c1f21.jpg',
        'http://pic16.nipic.com/20111006/6239936_092702973000_2.jpg',
        'http://pic25.nipic.com/20121112/9252150_150552938000_2.jpg',
        'http://pic26.nipic.com/20121221/9252150_142515375000_2.jpg',
        'http://pic68.nipic.com/file/20150601/8164280_104301508000_2.jpg',
        'http://pic51.nipic.com/file/20141025/8649940_220505558734_2.jpg',
        'http://pic26.nipic.com/20130121/9252150_101440518391_2.jpg',
        'http://pic30.nipic.com/20130619/9885883_210838271000_2.jpg',
        'http://pic38.nipic.com/20140228/2457331_083845176000_2.jpg',
        'http://pic39.nipic.com/20140321/18063302_210604412116_2.jpg',
        'http://pic13.nipic.com/20110409/7119492_114440620000_2.jpg',
        'http://photocdn.sohu.com/20120708/Img347586981.jpg',
        'http://img.redocn.com/sheying/20140731/qinghaihuyuanjing_2820969.jpg',
        'http://b-ssl.duitang.com/uploads/item/201509/02/20150902213128_f58GY.jpeg',
        'http://img4.cache.netease.com/photo/0001/2010-04-17/64EFS71V05RQ0001.jpg',
        'http://i2.w.yun.hjfile.cn/doc/201303/78ebff0b-3b4b-4695-93b7-4b5f62312ce6_03.jpg',
        'http://img4q.duitang.com/uploads/item/201404/12/20140412153248_VE8BM.jpeg',
        'http://photocdn.sohu.com/20150625/Img415614733.jpg',
        'http://k.zol-img.com.cn/dcbbs/22000/a21999018_01000.jpg',
        'http://pic33.nipic.com/20131007/13639685_123501617185_2.jpg',
        'http://pic1.win4000.com/wallpaper/c/53cdd1f7c1f21.jpg',
        'http://pic16.nipic.com/20111006/6239936_092702973000_2.jpg',
        'http://pic25.nipic.com/20121112/9252150_150552938000_2.jpg',
        'http://pic26.nipic.com/20121221/9252150_142515375000_2.jpg',
        'http://pic68.nipic.com/file/20150601/8164280_104301508000_2.jpg',
        'http://pic51.nipic.com/file/20141025/8649940_220505558734_2.jpg',
        'http://pic26.nipic.com/20130121/9252150_101440518391_2.jpg',
        'http://pic30.nipic.com/20130619/9885883_210838271000_2.jpg',
        'http://pic38.nipic.com/20140228/2457331_083845176000_2.jpg',
        'http://pic39.nipic.com/20140321/18063302_210604412116_2.jpg',
        'http://pic13.nipic.com/20110409/7119492_114440620000_2.jpg',
        'http://photocdn.sohu.com/20120708/Img347586981.jpg',
        'http://img.redocn.com/sheying/20140731/qinghaihuyuanjing_2820969.jpg',
        'http://b-ssl.duitang.com/uploads/item/201509/02/20150902213128_f58GY.jpeg',
        'http://img4.cache.netease.com/photo/0001/2010-04-17/64EFS71V05RQ0001.jpg',
        'http://i2.w.yun.hjfile.cn/doc/201303/78ebff0b-3b4b-4695-93b7-4b5f62312ce6_03.jpg',
        'http://img4q.duitang.com/uploads/item/201404/12/20140412153248_VE8BM.jpeg',
        'http://photocdn.sohu.com/20150625/Img415614733.jpg',
        'http://k.zol-img.com.cn/dcbbs/22000/a21999018_01000.jpg'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
