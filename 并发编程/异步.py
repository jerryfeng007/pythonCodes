import time
import asyncio
import aiohttp

# 比非异步快6倍


async def get_data(stock):
    url1 = 'http://hq.sinajs.cn/list=' + stock
    async with aiohttp.ClientSession() as session:
        async with session.get(url1) as res:
            print(await res.text())  # --------------注意这里，一定要有一个 await


async def get_all(stocks):
    tasks = [asyncio.create_task(get_data(stock)) for stock in stocks]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    s = time.time()
    stocks = ['sz000001', 'sz000002', 'sz000333', 'sz000858', 'sz000651', 'sz002415', 'sz002236', 'sh600276', 'sz300122',
              'sz300059', 'sz300015', 'sh600570', 'sh300012', 'sz300347', 'sz300033', 'sh688019', 'sh688006', 'sh688029',
              'sz300792', 'sz002504', 'sz002699', 'sz002581', 'sz002152', 'sz002326', 'sz300576', 'sz300380', 'sz002751',
              'sz002961', 'sz300458', 'sz300290', 'sz300752', 'sz002873', 'sz300081', 'sz002962', 'sz300790', 'sz300713',
              'sz300510', 'sz300362', 'sz300264', 'sz002942', 'sz002777', 'sz000636', 'sz000564', 'sz300782', 'sz300659',
              'sz300729', 'sz002241', 'sz002362', 'sz300315', 'sz002730', 'sz300466', 'sz002655', 'sz300611', 'sz300152',
              'sz002877', 'sz300593', 'sz300725', 'sz300566', 'sz300526', 'sz300459', 'sz300182', 'sz000536', 'sz300307',
              'sz000815', 'sz300537', 'sz002036', 'sz300057', 'sz002957', 'sz300451', 'sz002714', 'sz300417', 'sz002273',
              'sz002117', 'sz002351', 'sz000829', 'sz002205', 'sz300316', 'sz300555', 'sz300702', 'sz300322', 'sz002414']
    asyncio.run(get_all(stocks))
    e = time.time()
    print(e - s)
