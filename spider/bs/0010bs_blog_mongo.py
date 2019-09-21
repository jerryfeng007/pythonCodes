# requests库+beautifulsoup：博客标题、博客链接、博客时间，存储在mongodb
import requests
from bs4 import BeautifulSoup
import time
import threading
from pymongo import MongoClient


def bs_blog_mongo(i):
    client = MongoClient('localhost', connect=False)
    db = client['bs_blog']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://www.xqtesting.com/blog/p' + str(i) + '.html'
    # print(url)
    res = requests.get(url, headers=headers)
    res = res.text
    # print(res)
    soup = BeautifulSoup(res, 'lxml')
    results = soup.find_all('h4', {'class': 'card-heading'})
    results1 = soup.find_all('span', attrs={'data-toggle': 'tooltip'})
    # print(results1)
    # print(results)
    for j in range(len(results)):
        # print(results[j].a)
        # print(results[j].a.get_text())
        # print(results[j].a['href'])
        # print(results1[j*3].get_text())
        lianjie = 'http://www.xqtesting.com' + results[j].a['href']
        info = {'博客标题': results[j].a.get_text(), '博客时间': results1[j*3].get_text(), '博客链接': lianjie}
        db['bs_blog'].insert(info)
        print('success')


start_time = time.time()
for i in range(1, 32):
    t = threading.Thread(target=bs_blog_mongo, args=(i,))
    t.start()
end_time = time.time()
print('cost time:', end_time-start_time)
