# 实现简单计算器实现，包括两个数基本的加减乘除运输：
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    if y == 0:
        raise Exception('除数不能为0')
    return x / y


n = input('输入加法(1)，减法(2)，乘法(3)，除法(4)：')
if n not in ['1', '2', '3', '4']:
    raise Exception('必须为1234中的数')

x, y = eval(input('输入两个数：'))
if n == '1':
    print(add(x, y))
elif n == '2':
    print(sub(x, y))
elif n == '3':
    print(multi(x, y))
else:
    print(div(x, y))
