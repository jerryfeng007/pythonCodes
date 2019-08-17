import re

print('---------------------------------一次性读取全部数据--------------------------------------------')

with open('file1.txt', 'r') as f:
    content = f.read()
    # print(content)


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

    # 方式2
    # while True:
    #     if '' in con:
    #         con.remove('')
    #     else:
    #         print(con)
    #         break

    # 生成单词和词频的字典
    d = {}
    for key in con:
        if key not in d:
            d[key] = con.count(key)
    # print(d)

    # 方式2
    # d = {}
    # for key in con:
    #     if key not in d:
    #         d[key] = 0
    #     d[key] += 1
    # # print(d)

    # 按照词频从大到小排序
    d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print(d1)

    return d1


# 处理读取的数据
d2 = parse(content)

# 将结果按行输出到文件
with open('file2.txt', 'w') as f:
    for k, v in d2:
        print(k, v, file=f)  # 这里使用了 print函数中的 file 写入文件了 哈哈哈哈哈
        # f.write(f'{k} {v}\n') 也可以使用这句
