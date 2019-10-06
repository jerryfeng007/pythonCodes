# 给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。
n = 2

s = 'Runoob'
s1 = s[n:] + s[:n]
print(s1)


s = 'Runoob'
s2 = s[-n:] + s[:-n]
print(s2)
