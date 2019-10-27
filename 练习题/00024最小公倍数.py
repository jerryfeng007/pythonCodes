# 求两个数之间的最小公倍数相对简单，用两个数的乘积对两个之间的最大公约数求商即可:
from math import gcd

x = 54
y = 24
c = int(x * y / gcd(x, y))
print(c)
