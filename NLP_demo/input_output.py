import re

# 1.读取文件
# with open('input_file1', 'r') as f:
#     con = f.read()  # 一次性读取所有，内容多时不要这么用
#     # print(con)

# 方式4
with open('input_file1', 'r') as f:
    con = ''
    while True:
        con_temp = f.read(100)
        con += con_temp
        if len(con_temp) == 0:
            break
    # print(con)

# 2.去除所有的标点符号和换行符，并把所有大写变成小写
# 去除所有标点符号
punctuation = '!,.;:?"\''
con = re.sub(r'[{}]+'.format(punctuation), ' ', con)

# 去除换行符
con = con.replace('\n', '')
# print(con)

# 所有大写变为小写
con = con.lower()
# print(con)

# 3.合并相同的词，统计每个词出现的频率，并按照词频从大到小排序
# 生成所有单词的列表
con = con.split(' ')
# print(con)

# 去除空白单词
while True:
    if '' in con:
        con.remove('')
    else:
        # print(con)
        break

# 生成单词和词频的字典
d = {}.fromkeys(con)
# print(d)

for key in d:
    d[key] = con.count(key)
# print(d)

# 按照词频从大到小排序
d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(d1)

# 4.将结果按行输出到文件
with open('input_file2', 'w') as f:
    for k, v in d1:
        print(k, v, file=f)  # 这里使用了 print函数中的 file 写入文件了 哈哈哈哈哈
