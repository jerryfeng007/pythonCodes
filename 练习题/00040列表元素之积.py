# 定义一个数字列表，并计算列表元素之积。
from functools import reduce


def ji(l):
    return reduce(lambda x, y: x * y, l)


print(ji([1, 2, 3, 4]))


# 方法2
def ji2(l):
    ji3 = 1
    for i in l:
        ji3 *= i
    return ji3


print(ji2([1, 2, 3, 4]))
