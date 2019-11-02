# 给定一个字典，然后计算它们所有数字值的和。

d = {'a': 100, 'b': 200, 'c': 300}


# 方法1
def sum1(d):
    sum = 0
    for i in d:
        sum += d[i]
    return sum


print(sum1(d))


# 方法2
def sum2(d):
    l = []
    for i in d:
        l.append(d[i])
    return sum(l)


print(sum2(d))
