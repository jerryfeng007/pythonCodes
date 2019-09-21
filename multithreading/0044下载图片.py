# 练习2
import requests
import threading

with open('0044.txt', 'r') as f:
    contents = f.readlines()
    print(contents)


def pics(i):
    res = requests.get(contents[i].strip())
    res = res.content
    with open(str(i)+'.jpg', 'wb') as f:
        f.write(res)
        print('下载'+contents[i].strip()+'完成')


for i in range(len(contents)):
    t = threading.Thread(target=pics, args=(i,))
    t.start()
