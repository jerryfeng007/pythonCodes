import requests
from bs4 import BeautifulSoup
import openpyxl
import time


def job51():
    wb = openpyxl.load_workbook('0005bs_51job_excel.xlsx')
    table = wb['Sheet1']
    table.append(['职位','公司','地址','薪水','日期'])

    for i in range(1, 37):
        url = 'https://search.51job.com/list/070200,000000,0000,00,9,99,java%25E5%25BC%2580%25E5%258F%2591,2,'+str(i)+'.html'
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
            info = [title,company,address,salary,time]
            # info = (title,company,address,salary,time)
            # info = {'职位':title, '公司':company, '地址':address, '薪水':salary, '时间':time}
            # list.append(info)
            table.append(info)
        # print(list)
    wb.save('0005bs_51job_excel.xlsx')


# 串行 21秒
st = time.time()
job51()
et = time.time()
print(et - st)
