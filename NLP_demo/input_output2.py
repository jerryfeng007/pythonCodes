import re

print('---------------------------------每次读取一定长度的数据--------------------------------------------')


def parse(con, last_word, word_list):
    # 使用正则表达式去除所有标点符号和换行
    con = re.sub(r'[^\w]', ' ', last_word+con)
    # print(con)

    # 所有大写变为小写
    con = con.lower()
    # print(con)

    # 生成所有单词的列表
    con = con.split(' ')
    # print(con)

    # 对于边界的处理
    # 获取最后一个元素
    last_word = con[-1]

    # 去除最后一个元素，因为最后一个元素有可能是不完整的单词
    con1 = con[:-1]
    # print(con1)

    # 去除空白单词
    con1 = list(filter(None, con1))
    # print(con1)

    # 保存到最终的word_list
    word_list += con1
    return last_word


# 读取数据
with open('file1.txt', 'r') as f:
    word_list = []
    last_word = ''
    while True:
        content = f.read(100)
        if not content:
            break
        last_word = parse(content, last_word, word_list)
        # 这里返回了last_word，所以改变了最初的值，虽然没有返回列表，但是列表的值本身已改变

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
