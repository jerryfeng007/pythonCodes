# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

l = []
for i in range(1, 6):
    s = input(f'输入第{i}个：')
    l.append(s)
print(l)

m = max(l)
i = l.index(m)

l[0], l[i] = l[i], l[0]

n = min(l)
j = l.index(n)
l[-1], l[j] = l[j], l[-1]

print(l)
