import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 从网站获取7x24小时最新一条新闻的标题
url = 'http://finance.jrj.com.cn/yaowen'
# res = requests.get(url).content.decode('gbk', 'ignore').encode('utf8', 'ignore')
# res = requests.get(url).content
res = requests.get(url).text
# print(res)

# 创建对象，以python内置的标准库
soup = BeautifulSoup(res, 'html.parser')

# find_all方法搜索所有满足条件的tag
# 获取标题
b = soup.find_all('b', {})
# print(b)
title_web = b[0].a.get_text()
print(title_web)

# 获取时间
i = soup.find_all('i', {})
# print(i)
time_web = i[1].get_text()
print(time_web)

# 从数据库查询出7x24小时的最新一条新闻的标题
# Mongo数据库配置和连接
try:
    with MongoClient('108.9.91.76', 3306) as client:
        db = client['z3']
        db.authenticate('z3dad', 'd')
        print('连接数据库成功!')

        # 查询7x24小时最新的一条
        collection = db['Z3_NEWS']
        for latest in collection.find({"is_7_24hour": True}).sort([("declare_date", -1)]).limit(1):
            print('从表Z3_NEWS中查询出7x24小时最新一条数据=', latest)

        # 查询title字段
        title_mongo = latest['title']
        print('查询出7x24小时字段title=', title_mongo)

        # 查询declare_date字段
        time_mongo = latest['declare_date']
        time_mongo = str(time_mongo)[11:]
        print('查询出7x24小时字段declare_date=', time_mongo)
except Exception as e:
    print('查询mongo数据库异常', str(e))

# 当网站上的最新新闻的时间大于客户端最新新闻的时间时，给数据人员发消息
if time_web > time_mongo:
    params = {'action': 'send_msg', 'users': 'xxx|yyy', 'content':
              '智胜生产环境7x24小时新闻监控：' + '\n' +
              'mongo库Z3_NEWS表查询出来的7x24小时最新新闻与网站获取到的不一致！' + '\n' +
              '从数据库查询到的最新新闻为：' + title_mongo + '，时间为：' + time_mongo + '\n' +
              '金融界网站获取的最新新闻为：' + title_web + '，时间为：' + time_web}
    requests.get('http://wx.nn.com.cn/api/weixin.jsp', params=params)
