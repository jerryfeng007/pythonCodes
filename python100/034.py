# 练习函数调用


def a(m):
    if m == 1:
        return True
    else:
        return False


def b(m):
    check = a(m)
    if check:
        print('对')
    else:
        print('错')


b(1)
b(3)
