# 定义一个列表，并将列表中的头尾两个元素对调。


def duidiao(l):
    l[0], l[-1] = l[-1], l[0]
    return l


print(duidiao([1, 2, 3, 4, 5]))
