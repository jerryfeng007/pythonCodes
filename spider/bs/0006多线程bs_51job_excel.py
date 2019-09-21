import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import threading


def job51(num, lock):
    url = 'https://search.51job.com/list/070200,000000,0000,00,9,99,java%25E5%25BC%2580%25E5%258F%2591,2,'+str(num)+'.html'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        res = res.content
        res = str(res, encoding='gbk')
        # print(res)
    # list = []
    bs = BeautifulSoup(res, 'html.parser')
    divs = bs.select('.dw_table .el')
    for div in divs[1:]:
        title = div.select('.t1')[0].get_text(strip=True)
        company = div.select('.t2')[0].get_text(strip=True)
        address = div.select('.t3')[0].get_text(strip=True)
        salary = div.select('.t4')[0].get_text(strip=True)
        time = div.select('.t5')[0].get_text(strip=True)
        # print(title, company, address, salary, time)
        info = [title, company, address, salary, time]
        # info = (title,company,address,salary,time)
        # info = {'职位':title, '公司':company, '地址':address, '薪水':salary, '时间':time}
        # list.append(info)
        with lock:  # 这里加了一把锁；with可替代lock.acquire()和lock.release()，类似with open() as f
            table.append(info)
    # print(list)


# 多线程，8秒
if __name__ == '__main__':
    st = time.time()
    wb = openpyxl.load_workbook('0006bs_51job_excel.xlsx')
    table = wb['Sheet1']
    table.append(['职位', '公司', '地址', '薪水', '日期'])

    lock = threading.Lock()
    list1 = []
    for i in range(1, 37):
        t = threading.Thread(target=job51, args=(i, lock))
        list1.append(t)
        t.start()

    for t in list1:
        t.join()

    wb.save('0006bs_51job_excel.xlsx')

    et = time.time()
    print(et - st)
