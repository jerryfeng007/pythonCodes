# requests库+beautifulsoup：博客标题、博客链接、博客时间，存储在excel
import requests
from bs4 import BeautifulSoup
import time
import openpyxl
import threading


def bs_blog_excel(i, lock, table):
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
        title = results[j].a.get_text()
        time = results1[j*3].get_text()
        link = 'http://www.xqtesting.com' + results[j].a['href']
        info = [title, time, link]
        with lock:
            table.append(info)


# 多线程，4.5秒
if __name__ == '__main__':
    start_time = time.time()
    wb = openpyxl.load_workbook('0009bs_blog_excel.xlsx')
    table = wb['Sheet1']
    table.append(['标题', '时间', '链接'])

    lock = threading.Lock()
    list1 = []
    for i in range(1, 32):
        t = threading.Thread(target=bs_blog_excel, args=(i, lock, table))
        list1.append(t)
        t.start()

    for t in list1:
        t.join()

    wb.save('0009bs_blog_excel.xlsx')

    end_time = time.time()
    print('cost time:', end_time-start_time)
