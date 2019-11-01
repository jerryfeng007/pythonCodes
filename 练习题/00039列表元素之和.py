# 定义一个数字列表，并计算列表元素之和。


# 方法1
from functools import reduce


def sum1(l):
    return sum(l)


print(sum1([11, 5, 17, 18, 23]))


# 方法2
def sum2(l):
    return reduce(lambda x, y: x + y, l)


print(sum2([11, 5, 17, 18, 23]))


# 方法2中列表的另一种写法
def sum3(n):
    return reduce(lambda x, y: x + y, list(range(1, n+1)))


print(sum3(5))


# 方法4 递归
def sum4(n):
    if n == 1:
        return 1
    return n + sum4(n-1)


print(sum4(5))
