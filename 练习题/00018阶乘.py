# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n

# 利用math库的函数
from math import factorial


def jie_cheng2(n):
    return factorial(n)


print(jie_cheng2(5))


# 利用递归
# 如果是大于998会报错！
def jie_cheng(n):
    if n == 1 or n == 0:
        return 1
    return n * jie_cheng(n-1)


print(jie_cheng(5))


# 其他
def jie(n):
    ji = 1
    for i in range(1, n+1):
        ji *= i
    return ji


print(jie(5))
