# 设计一个函数返回传入的列表中最大和第二大的元素的值。


def aa(l):
    l.sort(reverse=True)
    return l[:2]


print(aa([1, 30, -3, 40, 100, -50]))
