# 定义一个列表，并将它翻转。


def fanzhuan(l):
    return l[::-1]


print(fanzhuan([1, 2, 3, 4, 5]))


# 方法2：
def fanzhuan2(l):
    l.reverse()
    return l


print(fanzhuan2([1, 2, 3, 4, 5]))
