# 计算数组元素之和
from functools import reduce

l = [1, 2, 3, 4, 5]


# 方法1
def sum1(l):
    return sum(l)


print(sum1(l))


# 方法2
def sum2(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print(sum2(l))


# 方法3
sum3 = reduce(lambda x, y: x+y, l)
print(sum3)
