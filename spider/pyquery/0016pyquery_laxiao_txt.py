# requests库+pyquery：拉销网，保存到记事本
import requests
from pyquery import PyQuery
import time


def pyquery_laxiao_txt(j):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'https://www.laxiao.com/company/index_' + str(j) + '.html'
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

    with open('0016pyquery_laxiao.txt', 'a', encoding='utf8') as f:
        f.write('名称：' + list_info[0] + '\n' +
                '资本：' + list_info[1] + '\n' +
                '类型：' + list_info[2] + '\n' +
                '联系人：' + list_info[3] + '\n' +
                '手机：' + list_info[4] + '\n' +
                '电话：' + list_info[5] + '\n' +
                '传真：' + list_info[6] + '\n' +
                '地址：' + list_info[7] + '\n' +
                '邮编：' + list_info[8] + '\n' +
                '行业：' + list_info[9] + '\n' +
                '网址：' + list_info[10] + '\n' +
                '人数：' + list_info[11] + '\n\n')


start_time = time.time()

for j in range(2, 100):
    pyquery_laxiao_txt(j)

end_time = time.time()
print('cost time:', end_time - start_time)
