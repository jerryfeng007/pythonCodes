# requests库+beautifulsoup：7x24新闻标题、新闻链接、新闻时间，存储在mongodb
import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient


def bs_jrj7x24_mongo():
    client = MongoClient('localhost', connect=False)
    db = client['bs_jrj7x24']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://finance.jrj.com.cn/yaowen'
    res = requests.get(url, headers=headers)
    res = res.text
    # print(res)
    soup = BeautifulSoup(res, 'lxml')
    results = soup.find_all('strong')
    results1 = soup.find_all('div', {'class': 'timeleft'})
    for i in range(len(results)):
        # print(results[i].b)
        # print(results[i].b.a['href'])
        # print(results[i].b.a.get_text())
        info = {'新闻时间': results1[i].i.get_text(), '新闻标题': results[i].b.a.get_text(), '新闻链接': results[i].b.a['href']}
        db['bs_jrj7x24'].insert(info)
        print('success')


start_time = time.time()
bs_jrj7x24_mongo()
end_time = time.time()
print('cost time:', end_time-start_time)
