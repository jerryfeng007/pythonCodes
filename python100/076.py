# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n


def ou(n):
    if n == 1:
        return 0
    if n == 2:
        return 1/2
    return 1/n + ou(n-2)


def ji(n):
    if n == 1:
        return 1
    if n == 3:
        return 1/3
    return 1 + 1/n + ji(n-2)


if __name__ == '__main__':
    n = 5
    if n % 2 == 0:
        print(ou(n))
    else:
        print(ji(n))
