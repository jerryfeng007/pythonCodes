# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13
# 特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。


def feibo(n):  # n代表第几项的值
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return feibo(n-1) + feibo(n-2)


num = eval(input('返回几项：'))
for i in range(1, num+1):
    print(feibo(i), end=',')
