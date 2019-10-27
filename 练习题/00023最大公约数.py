# 该函数返回两个数的最大公约数


def gongyueshu(x, y):
    temp = 0
    small = min(x, y)
    for i in range(1, small+1):
        if x % i == 0 and y % i == 0:
            temp = i
    return temp


print(gongyueshu(54, 24))

# 方法2
from math import gcd

print(gcd(54, 24))
