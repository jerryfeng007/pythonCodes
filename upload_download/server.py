import os
import shutil

BASE_DIR = 'server/'
NET_DIR = 'net/'

l = os.listdir(BASE_DIR)

while True:
    if len(l) == 0:
        break
    l1 = os.listdir(NET_DIR)
    if not l1:
        for index, i in enumerate(l):
            shutil.copy(BASE_DIR + i, NET_DIR + i)
            print(f'从server上传文件到网盘：{index+1}/{len(l)} {i}')
            l.remove(i)
            break
