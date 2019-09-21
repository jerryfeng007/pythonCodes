# yield是最底层的
# 进一步封装，这里使用了greenlet
# 再进一步封装，这里使用了Gevent

import gevent
import requests
import time
start = time.time()


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://www.baidu.com/'),
    gevent.spawn(f, 'https://www.sina.com.cn/')
])

'''如果数量多的话，对比比较明显
f('https://www.python.org/')
f('https://www.yahoo.com/')
f('https://www.baidu.com/')
f('https://www.sina.com.cn/')
'''
print('cost time:', time.time()-start)

# 协程的控制权，在用户级别上
