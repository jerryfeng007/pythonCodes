# 列表排序及连接。
a = [1, 3, 2]
b = [3, 4, 5]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

c = a + b
print(c)

a.extend(b)
print(a)
