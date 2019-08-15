import re

# 1.读取文件

# # 方式1：一次性读取所有内容（内容多时不要这么用）
# with open('input_file1', 'r') as f:
#     con = f.read()
#     # print(con)

# # 方式2：for循环遍历，一次性读取了所有行（同方式一，内容多时不要这么用）
# with open('input_file1', 'r') as f:
#     con = ''
#     cons = f.readlines()
#     for i in cons:
#         con += i
#     # print(con)

# # 方式3：while循环，每次读取一定长度的内容
with open('input_file1', 'r') as f:
    con = ''
    while True:
        con_temp = f.read(100)
        con += con_temp
        if len(con_temp) == 0:
            break
    # print(con)

# # 方式4：for循环，每次读取一行，需要提前知道行数
# with open('input_file1', 'r') as f:
#     con = ''
#     for i in range(9):  # 经过查看文件有9行
#         con_temp = f.readline()
#         con += con_temp
#     # print(con)

# # 方式5：for循环遍历f，每次也是读取一行，但无需知道行数
# with open('input_file1', 'r') as f:
#     # print(len(list(f)))  # 把f转换为列表，可以看到他的长度是9行
#     con = ''
#     for i in f:
#         con += i
#     # print(con)

# 2.去除所有的标点符号和换行符，并把所有大写变成小写
# 去除所有标点符号
con = re.sub(r'[^\w]', ' ', con)
# print(con)

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
