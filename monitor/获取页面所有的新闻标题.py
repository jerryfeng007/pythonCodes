import requests
from bs4 import BeautifulSoup

# 备注：只抓取了当天从0点开始的所有标题，即：未点击“加载更多”

url = 'http://finance.jrj.com.cn/yaowen'
r = requests.get(url).text
# print(r)

soup = BeautifulSoup(r, 'html.parser')
b = soup.find_all('b')

with open('存储新闻标题.txt', 'w') as f:
    for bb in b:
        if bb.a:
            f.write(bb.a.text + '\n')
