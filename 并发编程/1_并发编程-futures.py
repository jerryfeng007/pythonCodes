"""
https://time.geekbang.org/column/article/102562

concurrent和asyncio中都有futures：
from concurrent import futures  ------多线程、多进程用的是这个
from asyncio import futures

在download_one() 函数中，我们使用的 requests.get() 方法是线程安全的（thread-safe)
因此在多线程的环境下，它也可以安全使用，并不会出现 race condition

虽然线程的数量可以自己定义，但是线程数并不是越多越好，因为线程的创建、维护和删除也会有一定的开销
所以如果你设置的很大，反而可能会导致速度变慢，需要根据实际的需求做一些测试，寻找最优的线程数量
"""
print('------------------------------不使用多线程---------------------------------------------------')
import requests
import time


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    for site in sites:
        download_one(site)


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
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))  # 10秒


if __name__ == '__main__':
    main()


print('------------------------------多线程--map()-------------------------------------------------')
from concurrent import futures
import time
import requests


def download_one1(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all1(sites):
    with futures.ThreadPoolExecutor(max_workers=5) as t:   # 这两句是关键
        t.map(download_one1, sites)  # 对sites中的每一个元素，并发地调用函数download_one


def main1():
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
    download_all1(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main1()

print('-------------第二种写法---submit()----as_completed()----result()--------------------------')

# 首先调用 executor.submit()，将下载每一个网站的内容都放进 future 队列 to_do，等待执行。
# 然后是 as_completed() 函数，在 future完成后，便输出结果


def download_one3(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all3(sites):
    with futures.ThreadPoolExecutor(max_workers=5) as e:
        to_do = []                                         # 这里做了改动
        for site in sites:
            future = e.submit(download_one3, site)
            to_do.append(future)

        for future in futures.as_completed(to_do):
            future.result()


def main3():
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
    download_all3(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main3()
