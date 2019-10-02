# 求100之内的素数。

l1 = []  # 非素数
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            l1.append(i)
            break
print(l1)

l = [i for i in range(2, 100) if i not in l1]
print(l)


# 方法2：
for a in range(2, 100):
    for i in range(2, a):
        if a % i == 0:
            break
    else:
        print(a)
