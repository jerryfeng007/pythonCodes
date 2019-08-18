import os
import shutil
import time

BASE_DIR = 'client/'
NET_DIR = 'net/'

l1 = os.listdir(NET_DIR)

j = 0
while True:
    time.sleep(15)
    if l1 is not []:
        for i in l1:
            if os.path.exists(BASE_DIR + i):
                print(f'不下载，因为本地已经有：{i}')
                os.remove(NET_DIR + i)
                continue
            shutil.move(NET_DIR + i, BASE_DIR + i)
            j += 1
            print(f'从网盘下载文件到本地：{j} {i}')
            time.sleep(15)
        l1 = os.listdir(NET_DIR)
