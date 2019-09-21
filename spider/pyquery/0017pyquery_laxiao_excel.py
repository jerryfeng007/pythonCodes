# requests库+pyquery：拉销网，保存到excel
import requests
from pyquery import PyQuery
import time
from xlrd import open_workbook
from xlutils.copy import copy


def pyquery_laxiao_excel(i):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'https://www.laxiao.com/company/index_' + str(i) + '.html'
    # print(url)
    res = requests.get(url, headers=headers, verify=False)
    res = res.text
    # print(res)
    doc = PyQuery(res)
    content = doc('table[class="table table-bordered table-striped"] td:odd')
    # print(content, type(content))
    list_info = []
    for info in content:
        res = PyQuery(info).text()
        # print(res)
        list_info.append(res)
    # print(list_info)

    rexcel = open_workbook('0017pyquery_laxiao_excel.xlsx')  # 用wlrd提供的方法读取一个excel文件
    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
    row = rows

    table.write(row, 0, i-1)  # xlwt对象的写方法，参数分别是行、列、值
    table.write(row, 1, list_info[0])
    table.write(row, 2, list_info[1])
    table.write(row, 3, list_info[2])
    table.write(row, 4, list_info[3])
    table.write(row, 5, list_info[4])
    table.write(row, 6, list_info[5])
    table.write(row, 7, list_info[6])
    table.write(row, 8, list_info[7])
    table.write(row, 9, list_info[8])
    table.write(row, 10, list_info[9])
    table.write(row, 11, list_info[10])
    table.write(row, 12, list_info[11])
    excel.save('0017pyquery_laxiao_excel.xlsx')  # xlwt对象的保存方法，这时便覆盖掉了原来的excel


start_time = time.time()
for i in range(2, 100):
    pyquery_laxiao_excel(i)
end_time = time.time()
print('cost time:', end_time - start_time)
