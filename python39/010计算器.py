# 简单计算器


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


choice = eval(input('选择运算序号，1.相加 2.相减 3.相乘 4.相除：'))

if choice not in [1, 2, 3, 4]:
    print('选择错误！')
    exit()

x = eval(input('请输入第一个数：'))
y = eval(input('请输入第二个数：'))

if choice == 1:
    print(add(x, y))
elif choice == 2:
    print(sub(x, y))
elif choice == 3:
    print(multi(x, y))
elif choice == 4:
    print(div(x, y))
