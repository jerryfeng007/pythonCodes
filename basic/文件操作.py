print('--------------------------------------------------文件基础------------------------------')

# 文件内容
# 1.文本文件：txt doc xls
# 2.二进制文件：图片 视频 音乐

# 文件操作模式
# 一般：   r, w, a
# 二进制： rb, wb, ab
# 其他：   r+, rb+, w+, wb+, a+, ab+ （r+ 除了读，还能写）

print('----------------------------------------------二进制读写图片------------------------------')

# 文件操作----视频、音频、图像，需要用二进制读写，加一个b
# 读取
f = open('ccc.JPG', 'rb')
content = f.read()
print(content)
f.close()

# # 写入
f1 = open('ddd.JPG', 'wb')
f1.write(content[0:(len(content)//2)])
f1.close()

print('-------------------------------------读取方法的选取---------------------------------------')

# read         一次性读取全部内容，加载到内存，所以会耗内存，不适合数据太大的文件；但加载到内存，性能高
# readline     一次读取一行，适合读取内容庞大的文件
# readlines    一次性读取全部行，加载到内存，所以会耗内存，不适合数据太大的文件；但加载到内存，性能高
# for in       遍历，适合读取内容庞大的文件
# 注意，有的文件没有换行，如果读取一行，那就全部读取了。所以可以使用：f.read(长度)

# read
f = open('eee.txt', 'r', encoding='utf8')
con = f.read()
print(con)

# readline
f = open('eee.txt', 'r', encoding='utf8')
con = f.readline()
print(con)

# readlines
f = open('eee.txt', 'r', encoding='utf8')
con = f.readlines()
print(con)
for i in con:  # 遍历行列表
    print(i, end='')

print('-------------------------------------遍历文件中的内容---------------------------------------')

# 一、可以遍历 f
f = open('eee.txt', 'r', encoding='utf8')
for i in f:
    print(i, end='')

# 二、也可以遍历行列表
f = open('eee.txt', 'r', encoding='utf8')
content = f.readlines()  # 行列表
for j in content:
    print(j, end='')

# 三、循环读取行
f = open('ggg.txt', 'r', encoding='utf8')
for i in range(3):  # 要读取几行？
    con = f.readline()
    print(con, end='')

print('-------------------------------------判断文件是否可读、可写---------------------------------------')

# 判断文件是否可读
f = open('eee.txt', 'r', encoding='utf8')
if f.readable():
    print('文件可读')
    content = f.read()
    print(content)
else:
    print('不可读')

# 判断文件是否可写
f = open('fff.txt', 'w', encoding='utf8')
if f.writable():
    print('文件可写')
    f.write('嘿嘿嘿\n哈哈哈\n呼呼呼')
else:
    print('不可写')

print('-------------------------------------重命名、删除、创建---------------------------------------')

import os
# 重命名（文件、目录）
# os.rename('fff.txt', 'ffff.txt')
# os.renames('ffff.txt', 'fff.txt')

# os.rename('AA', 'BB')
# os.renames('BB', 'AA')

# os.renames('AA/a.txt', 'BB/b.txt')
# os.renames('BB/b.txt', 'AA/a.txt')

# 删除文件、目录
# os.remove('CC/cc.txt')
# os.rmdir('CC/CCC')      　  #　不能递归删除
# os.removedirs('CC/CCC')     #  可以递归删除

# 创建目录
# os.mkdir('DD')

print('-------------------------------------获取、改变目录，获取当前目录的文件----------------------------------')

# 获取当前目录
d = os.getcwd()
print(d)

# 改变目录
os.chdir('AA')
d = os.getcwd()
print(d)

# 获取目录列表
l = os.listdir(d)
print(l)

os.chdir('..')  # 上级目录
print(os.getcwd())

l = os.listdir('./')  # 当前目录
print(l)

print('-------------------------------------文件内容复制---------------------------------------')
# 如果文件内容不多
# source_file = open('fff.txt', 'r', encoding='utf8')
# dst_file = open('fff_bat.txt', 'w', encoding='utf8')
#
# content = source_file.read()
# dst_file.write(content)
#
# source_file.close()
# dst_file.close()

# 如果是大文件
source_file = open('ggg.txt', 'r', encoding='utf8')
dst_file = open('ggg_bat.txt', 'w', encoding='utf8')

while True:
    content = source_file.read(1024)
    if len(content) == 0:
        break
    dst_file.write(content)

source_file.close()
dst_file.close()

print('-------------------------------------文件分类，并生成文件清单---------------------------------------')
import os
import shutil

if not os.path.exists('归类练习'):
    raise Exception('目录不存在')
os.chdir('归类练习')
p = os.getcwd()

l2 = os.listdir(p)
for i in l2:
    if os.path.isdir(i):
        continue
    item = i.split('.')[-1]
    if not os.path.exists(item):
        os.mkdir(item)
    shutil.move(i, item)

print('-------------------------------------递归展示目录下的文件---------------------------------------')
os.chdir('../归类练习2')
p = os.getcwd()


def show(p, f):
        l2 = os.listdir(p)
        for i in l2:
            new_p = os.path.join(p, i)
            if os.path.isdir(new_p):
                show(new_p, f)
            f.write(new_p + '\n')


with open('../write_path.txt', 'w', encoding='utf8') as f:
    show(p, f)
