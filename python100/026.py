# 求1+2!+3!+...+20!的和。


def aaa(n):
    if n == 1:
        return 1
    return n * aaa(n-1)


print(aaa(5))
