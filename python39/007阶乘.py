# n!=1×2×3×...×n。


def jie(n):
    if n == 1:
        return 1
    return n * jie(n-1)


print(jie(998))  # 如果是大于998会报错！

# 方法2：
from math import factorial  # 阶乘函数

print(factorial(1000))
