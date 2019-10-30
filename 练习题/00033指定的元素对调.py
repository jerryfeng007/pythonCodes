# 定义一个列表，并将列表中的指定位置的两个元素对调。


def duidiao(l, m, n):
    l[m-1], l[n-1] = l[n-1], l[m-1]
    return l


print(duidiao([23, 65, 19, 90], 1, 3))
