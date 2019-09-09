import pymongo
import threading
import aiohttp
import smtplib
import requests

url1 = 'https://www.baidu.com'

# ---------------------------------------with的几个使用场景-------------------------------------------------

# 1.打开文件
with open('./file_read_write/file1.txt', 'r') as f:
    con = f.read()

# 2.连接数据库
with pymongo.MongoClient('localhost', 27017) as client:
    db = client['database']

# 3.锁
some_lock = threading.Lock()
some_lock.acquire()
# ----------------------------> 改为：
with threading.Lock() as some_lock:
    pass


# 4.并发编程 - asyncio
async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(f'read {resp.content_length} from {url}')

# 5.session
with requests.session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

# 6.发邮件
    with smtplib.SMTP_SSL('smtp.qq.com', '465') as smtp:
        smtp.set_debuglevel(0)
        smtp.login('267009633', 'yzb')
