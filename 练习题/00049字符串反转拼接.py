# 给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。

s = 'Runoob'


def fan(s, n):
    return s[n:] + s[:n], s[-n:] + s[:-n]


print(fan(s, 2))
