# 从文本中取出ip，并计算每个ip的次数

d = {}
with open('00003文本取IP存字典', 'r', encoding='utf8') as f:
    for line in f:
        ip = line.split('，')[0]
        if ip not in d:
            d[ip] = 1
        else:
            d[ip] += 1
print(d)
