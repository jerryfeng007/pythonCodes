# 斐波那契数列
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ......

# 递归实现


def aa(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return aa(n-1) + aa(n-2)


print(aa(1))
print(aa(2))
print(aa(3))
print(aa(4))
print(aa(5))
print(aa(20))
