import re

print('--------------------------------遍历f---每次读取一行--------------------------------------------')


def parse(line, word_list):
    # 使用正则表达式去除所有标点符号和换行
    con = re.sub(r'[^\w]', ' ', line)
    # print(con)

    # 所有大写变为小写
    con = con.lower()
    # print(con)

    # 生成所有单词的列表
    con = con.split(' ')
    # print(con)

    # 去除空白单词
    con = list(filter(None, con))
    # print(con)

    # 保存到最终的word_list
    word_list += con


# 读取数据
with open('file1.txt', 'r') as f:
    word_list = []
    for line in f:
        if line != '\n':  # 如果是空行，就不执行parse函数
            parse(line, word_list)

# 生成单词和词频的字典
d = {}
for key in word_list:
    if key not in d:
        d[key] = word_list.count(key)

# 按照词频从大到小排序
d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)

# 将结果按行输出到文件
with open('file2.txt', 'w') as f1:
    for k, v in d1:
        f1.write(f'{k} {v}\n')
