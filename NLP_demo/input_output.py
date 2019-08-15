import re

# 1.读取文件

# # 方式1：一次性读取所有内容（内容多时不要这么用）
# with open('input_file1', 'r') as f:
#     con = f.read()
#     # print(con)

# # 方式2：一次性读取了所有行（内容多时不要这么用）
# with open('input_file1', 'r') as f:
#     con = ''
#     cons = f.readlines()  # 行列表
#     for i in cons:
#         con += i
#     # print(con)

# # 方式3：每次读取一定长度的内容
with open('input_file1', 'r') as f:
    con = ''
    while True:
        con_temp = f.read(100)
        con += con_temp
        if len(con_temp) == 0:
            break
#     # print(con)

# # 方式4：每次读取一行
# with open('input_file1', 'r') as f:
#     con = ''
#     while True:
#         con_temp = f.readline()
#         con += con_temp
#         if not con_temp:
#             break
#     # print(con)

# # 方式5：for循环遍历f
# with open('input_file1', 'r') as f:
#     con = ''
#     for i in f:
#         con += i
#     # print(con)


def parse(con):
    # 使用正则表达式去除所有标点符号和换行
    con = re.sub(r'[^\w]', ' ', con)
    # print(con)

    # 所有大写变为小写
    con = con.lower()
    # print(con)

    # 生成所有单词的列表
    con = con.split(' ')
    # print(con)

    # 去除空白单词
    con = list(filter(None, con))  # 可以过滤0、None、空列表等，注意别过滤多了
    # print(con)

    # 或者用这几句过滤
    # while True:
    #     if '' in con:
    #         con.remove('')
    #     else:
    #         print(con)
    #         break

    # 生成单词和词频的字典
    d = {}.fromkeys(con)
    # print(d)
    for key in d:
        d[key] = con.count(key)
    # print(d)

    # 按照词频从大到小排序
    d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print(d1)

    return d1


# 处理读取的数据
d2 = parse(con)

# 将结果按行输出到文件
with open('input_file2', 'w') as f:
    for k, v in d2:
        print(k, v, file=f)  # 这里使用了 print函数中的 file 写入文件了 哈哈哈哈哈
        # f.write(f'{k} {v}\n') 也可以使用这句
