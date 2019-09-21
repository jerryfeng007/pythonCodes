import requests
from datetime import datetime, timedelta


def maoyan_pinglun(url):
    # url = 'http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset=15&startTime=2018-11-20%2022%3A10%3A55'
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Mobile Safari/537.36'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        res = res.json()  # 转换为了字典类型的数据
        # print(res)  # 注意：第一次运行，显示cmts， 第二次运行，就显示了hcmts， 有可能是做了这样的限制
        list = []
        datas = res['cmts']
        for data in datas:
            # print(data['cityName'], data['score'], data['nickName'], data['content'])
            info = {'startTime': data['startTime'],
                    'id': data['id'],
                    'cityName': data['cityName'] if 'cityName' in data else '',  # 处理城市名为空
                    'score': data['score'],
                    'nickName': data['nickName'],
                    'content': data['content'].replace('\n', ' ')}  # 处理评论换行
            # print(info)
            list.append(info)
        return list


start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
end_time = '2018-08-10 00:00:00'  # 定义结束时间为电影上映的时间

while start_time > end_time:
    url = 'http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset=0&startTime=' + start_time.replace(' ', '%20')
    # print(url)
    list = maoyan_pinglun(url)

    start_time = list[14]['startTime']  # 末尾评论时间；字符串类型
    # 先转化为日期类型才能加减；向前减1秒，防止获取到重复数据
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')-timedelta(seconds=1)
    # 再次把start_time转换为字符串
    start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')
    print(start_time)
    for item in list:
        with open('aaa.txt', 'a', encoding='utf8') as f:
            f.write(item['startTime'] + ' ' +
                    str(item['id']) + ' ' +
                    item['cityName'] + ' ' +
                    str(item['score']) + ' ' +
                    item['nickName'] + ' ' +
                    item['content'] + '\n')
