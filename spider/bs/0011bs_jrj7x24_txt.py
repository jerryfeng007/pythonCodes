# requests库+beautifulsoup：7x24新闻标题、新闻链接、新闻时间，存储在记事本
import requests
from bs4 import BeautifulSoup
import time


def bs_jrj7x24_txt():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://finance.jrj.com.cn/yaowen'
    res = requests.get(url, headers=headers)
    res = res.text
    # print(res)
    soup = BeautifulSoup(res, 'lxml')
    results = soup.find_all('strong')
    results1 = soup.find_all('div', {'class': 'timeleft'})
    with open('0011bs_jrj7x24_txt.txt', 'a', encoding='utf-8') as f:
        for i in range(len(results)):
            # print(results[i].b)
            # print(results[i].b.a['href'])
            # print(results[i].b.a.get_text())
            f.write('新闻时间：' + results1[i].i.get_text() + '\n' + '新闻标题：' + results[i].b.a.get_text() + '\n' + '新闻链接：' + results[i].b.a['href'] + '\n\n')


# 串行 0.23秒
start_time = time.time()
bs_jrj7x24_txt()
end_time = time.time()
print('cost time:', end_time-start_time)
