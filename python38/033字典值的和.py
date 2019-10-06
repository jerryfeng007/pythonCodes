# 给定一个字典，然后计算它们所有数字值的和。
d = {'a': 100, 'b': 200, 'c': 300}

l = []
for i in d:
    l.append(d[i])

print(sum(l))
