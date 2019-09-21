# requests库+正则表达式：博客标题、博客链接、博客时间，存储在excel
import requests
import re
import time
from xlrd import open_workbook
from xlutils.copy import copy


def regular_blog_excel(i):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://www.xqtesting.com/blog/p' + str(i) + '.html'
    # print(url)
    res = requests.get(url, headers=headers)
    res = res.text
    pattern = '<h4.*?class.*?card-heading.*?>.*?<a.*?href.*?(.*?).html.*?style.*?color:.*?>(.*?)</a>.*?</h4>.*?<i class="icon-time"></i>(.*?)</span>'
    results = re.findall(pattern, res, re.S)
    # print(results)

    rexcel = open_workbook('0020regular_blog_excel.xlsx')  # 用wlrd提供的方法读取一个excel文件
    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
    row = rows
    for j in range(len(results)):
        # table.write(row, 0, j+1)  # xlwt对象的写方法，参数分别是行、列、值
        table.write(row, 1, results[j][1])
        table.write(row, 2, 'http://www.xqtesting.com' + results[j][0][2:] + '.html')
        table.write(row, 3, results[j][2])
        row += 1
    excel.save('0020regular_blog_excel.xlsx')  # xlwt对象的保存方法，这时便覆盖掉了原来的excel


start_time = time.time()
for i in range(1, 32):
    regular_blog_excel(i)
end_time = time.time()
print('cost time:', end_time-start_time)
