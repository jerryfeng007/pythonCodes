# 面试官让我现场写的一个笔试题

d = {}
with open('面试官让我现场写的一个笔试题', 'r', encoding='utf8') as f:
    for i in f:
        k = i.split('，')[0]

        # 第一
        # if k not in d:
        #     d[k] = 1
        # else:
        #     d[k] += 1

        # 第二
        if k not in d:
            d[k] = 0
        d[k] += 1

print(d)
