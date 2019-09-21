# requests库+正则表达式：拉销网，保存到excel
import requests
import threading
import time
import re
from xlrd import open_workbook
from xlutils.copy import copy


def regular_laxiao_excel(j):
    url = 'https://www.laxiao.com/company/index_' + str(j) + '.html'
    # print(url)
    res = requests.get(url)
    res = res.text
    # print(res)
    pattern = ('<div class="zx_td">(.*?)</div>.*?<a href=.*?>(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>')
    results = re.findall(pattern, res, re.S)
    results[0] = list(results[0])  # 把元组转换成了列表
    # print(results[0])

    rexcel = open_workbook('0026regular_laxiao_excel.xlsx')  # 用wlrd提供的方法读取一个excel文件
    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
    row = rows

    table.write(row, 0, j - 1)  # xlwt对象的写方法，参数分别是行、列、值
    table.write(row, 1, results[0][0])
    table.write(row, 2, results[0][1])
    table.write(row, 3, results[0][2])
    table.write(row, 4, results[0][3])
    table.write(row, 5, results[0][4])
    table.write(row, 6, results[0][5])
    excel.save('0026regular_laxiao_excel.xlsx')  # xlwt对象的保存方法，这时便覆盖掉了原来的excel


start_time = time.time()
for j in range(2, 100):
    regular_laxiao_excel(j)
end_time = time.time()
print('cost time:', end_time - start_time)
