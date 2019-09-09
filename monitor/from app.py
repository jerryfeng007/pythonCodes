import requests

# 从金融界手机APP获取智头条最新一条新闻的标题
url = 'http://mapi.itougu.jrj.com.cn/wireless/information/getMajorInfoList.jspa?pn=1&ps=1&'
res = requests.get(url).json()
data = res['data'][0]

# 获取title
title_app = data['title']
print(title_app)

# 获取time
time_app = data['listdate'][11:]
print(time_app)
