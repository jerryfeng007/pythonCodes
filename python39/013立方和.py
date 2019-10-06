# 计算 n 个自然数的立方和
# 比如n=5： 1**3 + 2**3 + 3**3 + 4**3 + 5**3


def aa(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    return sum


print(aa(7))
