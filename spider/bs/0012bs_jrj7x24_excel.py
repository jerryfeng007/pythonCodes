# requests库+beautifulsoup：7x24新闻标题、新闻链接、新闻时间，存储在excel
import requests
from bs4 import BeautifulSoup
import time
from xlrd import open_workbook
from xlutils.copy import copy


def bs_jrj7x24_excel():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://finance.jrj.com.cn/yaowen'
    res = requests.get(url, headers=headers)
    res = res.text
    # print(res)
    soup = BeautifulSoup(res, 'lxml')
    results = soup.find_all('strong')
    results1 = soup.find_all('div', {'class': 'timeleft'})
    # print(results)
    rexcel = open_workbook('0012bs_jrj7x24_excel.xlsx')  # 用wlrd提供的方法读取一个excel文件
    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
    row = rows
    for j in range(len(results)):
        # table.write(row, 0, j)  # xlwt对象的写方法，参数分别是行、列、值
        table.write(row, 0, results1[j].i.get_text())
        table.write(row, 1, results[j].b.a['href'])
        table.write(row, 2, results[j].b.a.get_text())
        row += 1
    excel.save('0012bs_jrj7x24_excel.xlsx')  # xlwt对象的保存方法，这时便覆盖掉了原来的excel


start_time = time.time()
bs_jrj7x24_excel()
end_time = time.time()
print('cost time:', end_time-start_time)
