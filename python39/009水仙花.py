# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

for i in range(1, 100000):
    l = len(str(i))
    sum = 0
    for j in str(i):
        sum += int(j) ** l
    if sum == i:
        print(i)


# 方法2
for i in range(100, 1000):
    bai = i // 100
    shi = i // 10 % 10
    ge = i % 10
    if bai ** 3 + shi ** 3 + ge ** 3 == i:
        print(i)

