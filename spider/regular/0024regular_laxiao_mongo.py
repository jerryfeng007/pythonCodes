# requests库+正则表达式：拉销网，保存到mongodb
import requests
import threading
import time
import re
from pymongo import MongoClient


def regular_laxiao_mongo(j):
    client = MongoClient('localhost', connect=False)
    db = client['regular_laxiao']
    url = 'https://www.laxiao.com/company/index_' + str(j) + '.html'
    # print(url)
    res = requests.get(url)
    res = res.text
    # print(res)
    pattern = ('<div class="zx_td">(.*?)</div>.*?<a href=.*?>(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>')
    results = re.findall(pattern, res, re.S)
    results[0] = list(results[0])  # 把元组转换成了列表
    # print(results[0])

    info = {results[0][0]: results[0][1], results[0][2]: results[0][3], results[0][4]: results[0][5]}
    db['regular_laxiao'].insert(info)
    print('success')


start_time = time.time()
for j in range(2, 100):
    t = threading.Thread(target=regular_laxiao_mongo, args=(j, ))
    t.start()
end_time = time.time()
print('cost time:', end_time - start_time)
