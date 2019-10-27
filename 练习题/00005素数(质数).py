# 求100之内的素数/质数

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
