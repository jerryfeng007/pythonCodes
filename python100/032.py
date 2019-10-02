# 按相反的顺序输出列表的值。


def bbb(l):
    # return l[::-1]
    l.reverse()
    return l


for i in bbb([2, 5, 7]):
    print(i)
