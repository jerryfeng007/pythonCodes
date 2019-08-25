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

print('------------------------------多线程---------------------------------------------------')
from concurrent import futures


def download_one1(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all1(sites):
    with futures.ThreadPoolExecutor(max_workers=5) as t:  # 改了这里
        t.map(download_one1, sites)


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
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))  # 5秒


if __name__ == '__main__':
    main1()

print('------------------------多进程------有问题--为啥没执行download_one2--------------------------')
#
#
# def download_one2(url):
#     resp = requests.get(url)
#     print('Read {} from {}'.format(len(resp.content), url))
#
#
# def download_all2(sites):
#     with futures.ProcessPoolExecutor() as executor:   # 这两句是区别所在
#         executor.map(download_one2, sites)
#
#
# def main2():
#     sites = [
#         'http://pic33.nipic.com/20131007/13639685_123501617185_2.jpg',
#         'http://pic1.win4000.com/wallpaper/c/53cdd1f7c1f21.jpg',
#         'http://pic16.nipic.com/20111006/6239936_092702973000_2.jpg',
#         'http://pic25.nipic.com/20121112/9252150_150552938000_2.jpg',
#         'http://pic26.nipic.com/20121221/9252150_142515375000_2.jpg',
#         'http://pic68.nipic.com/file/20150601/8164280_104301508000_2.jpg',
#         'http://pic51.nipic.com/file/20141025/8649940_220505558734_2.jpg',
#         'http://pic26.nipic.com/20130121/9252150_101440518391_2.jpg',
#         'http://pic30.nipic.com/20130619/9885883_210838271000_2.jpg',
#         'http://pic38.nipic.com/20140228/2457331_083845176000_2.jpg',
#         'http://pic39.nipic.com/20140321/18063302_210604412116_2.jpg',
#         'http://pic13.nipic.com/20110409/7119492_114440620000_2.jpg',
#         'http://photocdn.sohu.com/20120708/Img347586981.jpg',
#         'http://img.redocn.com/sheying/20140731/qinghaihuyuanjing_2820969.jpg',
#         'http://b-ssl.duitang.com/uploads/item/201509/02/20150902213128_f58GY.jpeg',
#         'http://img4.cache.netease.com/photo/0001/2010-04-17/64EFS71V05RQ0001.jpg',
#         'http://i2.w.yun.hjfile.cn/doc/201303/78ebff0b-3b4b-4695-93b7-4b5f62312ce6_03.jpg',
#         'http://img4q.duitang.com/uploads/item/201404/12/20140412153248_VE8BM.jpeg',
#         'http://photocdn.sohu.com/20150625/Img415614733.jpg',
#         'http://k.zol-img.com.cn/dcbbs/22000/a21999018_01000.jpg',
#         'http://pic33.nipic.com/20131007/13639685_123501617185_2.jpg',
#         'http://pic1.win4000.com/wallpaper/c/53cdd1f7c1f21.jpg',
#         'http://pic16.nipic.com/20111006/6239936_092702973000_2.jpg',
#         'http://pic25.nipic.com/20121112/9252150_150552938000_2.jpg',
#         'http://pic26.nipic.com/20121221/9252150_142515375000_2.jpg',
#         'http://pic68.nipic.com/file/20150601/8164280_104301508000_2.jpg',
#         'http://pic51.nipic.com/file/20141025/8649940_220505558734_2.jpg',
#         'http://pic26.nipic.com/20130121/9252150_101440518391_2.jpg',
#         'http://pic30.nipic.com/20130619/9885883_210838271000_2.jpg',
#         'http://pic38.nipic.com/20140228/2457331_083845176000_2.jpg',
#         'http://pic39.nipic.com/20140321/18063302_210604412116_2.jpg',
#         'http://pic13.nipic.com/20110409/7119492_114440620000_2.jpg',
#         'http://photocdn.sohu.com/20120708/Img347586981.jpg',
#         'http://img.redocn.com/sheying/20140731/qinghaihuyuanjing_2820969.jpg',
#         'http://b-ssl.duitang.com/uploads/item/201509/02/20150902213128_f58GY.jpeg',
#         'http://img4.cache.netease.com/photo/0001/2010-04-17/64EFS71V05RQ0001.jpg',
#         'http://i2.w.yun.hjfile.cn/doc/201303/78ebff0b-3b4b-4695-93b7-4b5f62312ce6_03.jpg',
#         'http://img4q.duitang.com/uploads/item/201404/12/20140412153248_VE8BM.jpeg',
#         'http://photocdn.sohu.com/20150625/Img415614733.jpg',
#         'http://k.zol-img.com.cn/dcbbs/22000/a21999018_01000.jpg'
#     ]
#     start_time = time.perf_counter()
#     download_all2(sites)
#     end_time = time.perf_counter()
#     print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
#
#
# if __name__ == '__main__':
#     main2()

print('------------------------------异步---------------------------------------------------')
import asyncio


async def download_one3(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


async def download_all3(sites):
    tasks = [asyncio.create_task(download_one3(url)) for url in sites]
    # await asyncio.gather(*tasks)
    for task in tasks:
        await task


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
    asyncio.run(download_all3(sites))  # 改了这里
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))  # 8秒


if __name__ == '__main__':
    main3()
