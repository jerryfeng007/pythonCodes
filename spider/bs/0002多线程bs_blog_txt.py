# requests库+beautifulsoup：博客标题、博客链接、博客时间，存储在记事本
import requests
from bs4 import BeautifulSoup
import time
import threading


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
    with open('0002bs_blog_text.txt', 'a', encoding='utf-8') as f:
        for j in range(len(results)):
            # print(results[j].a)
            # print(results[j].a.get_text())
            # print(results[j].a['href'])
            # print(results1[j*3].get_text())
            f.write('博客标题：' + results[j].a.get_text() + '\n' +
                    '博客时间：' + results1[j*3].get_text() + '\n' +
                    '博客链接：' + 'http://www.xqtesting.com' + results[j].a['href'] + '\n\n')


# 使用多线程，大概需要4.5秒
list1 = []

start_time = time.time()
print(start_time)

for i in range(1, 32):  # 开启31个子线程
    t = threading.Thread(target=bs_blog_text, args=(i,))
    list1.append(t)
    t.start()

for t in list1:
    t.join()  # 所有线程都执行完毕，才打印下面的结束时间

# 如果上面不加join，那么主线程跟子线程会同时执行，end_time会立马打印，那么cost time就不准了
end_time = time.time()
print(end_time)

print('cost time:', end_time - start_time)
