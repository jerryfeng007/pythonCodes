# 定义一个数字列表，并计算列表元素之积。
from functools import reduce


# 方式一
def ji(l):
    return reduce(lambda x, y: x * y, l)


print(ji([1, 2, 3, 4]))


# 方式一中列表的另一种写法
def ji2(n):
    return reduce(lambda x, y: x * y, list(range(1, n+1)))


print(ji2(4))


# 方法3
def ji3(l):
    ji4 = 1
    for i in l:
        ji4 *= i
    return ji4


print(ji3([1, 2, 3, 4]))
