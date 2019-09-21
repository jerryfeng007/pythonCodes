# requests库+正则表达式：7x24新闻标题、新闻链接、新闻时间，存储在mongodb
import requests
import re
import time
from pymongo import MongoClient


def regular_jrj7x24_mongo():
    client = MongoClient('localhost', connect=False)
    db = client['jrj7x24']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://finance.jrj.com.cn/yaowen'
    res = requests.get(url, headers=headers)
    res = res.text
    # print(res)
    pattern = '<i>(.*?)</i>.*?</div>.*?<div class="textright">.*?<strong><i class="icon"><a href=.*?>.*?</a></i><b><a href="(.*?)">(.*?)</a></b></strong>'
    results = re.findall(pattern, res, re.S)
    for result in results:
        # print(result)
        # print(result[0])
        # print(result[1])
        # print(result[2])
        info = {'新闻时间': result[0], '新闻标题': result[2], '新闻链接': result[1]}
        db['jrj7x24'].insert(info)
        print('success')


start_time = time.time()
regular_jrj7x24_mongo()
end_time = time.time()
print('cost time:', end_time-start_time)
