# 按逗号分隔列表。


def aa(l):
    return ','.join([str(n) for n in l])


l = [1, 2, 3, 4]

print(aa(l))
