# requests库+beautifulsoup：博客标题、博客链接、博客时间，存储在记事本
import requests
from bs4 import BeautifulSoup
import time


def bs_blog_text(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://www.xqtesting.com/blog/p' + str(page) + '.html'
    # print(url)
    res = requests.get(url, headers=headers)
    res = res.text
    # print(res)
    soup = BeautifulSoup(res, 'lxml')
    results = soup.find_all('h4', {'class': 'card-heading'})
    results1 = soup.find_all('span', attrs={'data-toggle': 'tooltip'})
    # print(results1)
    # print(results)
    with open('0001bs_blog_text.txt', 'a', encoding='utf-8') as f:
        for j in range(len(results)):
            # print(results[j].a)
            # print(results[j].a.get_text())
            # print(results[j].a['href'])
            # print(results1[j*3].get_text())
            f.write('博客标题：' + results[j].a.get_text() + '\n' +
                    '博客时间：' + results1[j*3].get_text() + '\n' +
                    '博客链接：' + 'http://www.xqtesting.com' + results[j].a['href'] + '\n\n')


# 串行，大概需要13秒
start_time = time.time()
for i in range(1, 32):
    bs_blog_text(i)
end_time = time.time()
print('cost time:', end_time - start_time)
