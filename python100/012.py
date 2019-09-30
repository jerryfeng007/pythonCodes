# 判断101-200之间有多少个素数，并输出所有素数。
l1 = []
for i in range(101, 200):
    for j in range(2, i):
        if i % j == 0:
            l1.append(i)

print(list(set(l1)))

l2 = list(range(101, 200))
print(l2)

l3 = []
for i in l2:
    if i not in l1:
      l3.append(i)

print(l3)
print(len(l3))
