# requests库+pyquery：拉销网，保存到mongodb
import requests
from pyquery import PyQuery
import threading
import time
from pymongo import MongoClient


def pyquery_laxiao_mongo(j):
    client = MongoClient('localhost', connect=False)
    db = client['laxiao']
    url = 'https://www.laxiao.com/company/index_' + str(j) + '.html'
    print(url)
    res = requests.get(url)
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

    info = {'名称': list_info[0], '资本': list_info[1], '类型': list_info[2],
            '联系人': list_info[3], '手机': list_info[4], '电话': list_info[5],
            '传真': list_info[6], '地址': list_info[7], '邮编': list_info[8],
            '行业': list_info[9], '网址': list_info[10], '人数': list_info[11]}
    db['laxiao'].insert(info)
    print('success')


start_time = time.time()
for j in range(2, 100):
    t = threading.Thread(target=pyquery_laxiao_mongo, args=(j, ))
    t.start()
end_time = time.time()
print('cost time:', end_time - start_time)
