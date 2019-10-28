# Python 计算 n 个自然数的立方和
# 如果n=5， 那么计算 1**3 + 2**3 + 3**3 + 4**3 + 5**3

from functools import reduce

n = eval(input('输入一个数：'))


# 方法1
def sum(n):
    if n == 1:
        return 1
    return n ** 3 + sum(n-1)


print(sum(n))


# 方法2
def sum2(n):
    sum3 = 0
    for i in range(1, n+1):
        sum3 += i ** 3
    return sum3


print(sum2(n))
