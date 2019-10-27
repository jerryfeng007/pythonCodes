# 通过用户输入一个数字，并计算这个数字的平方根


def the_ping(num):
    return '%.2f' % num ** (1/2)  # 立方根是1/3，以此类推


num = eval(input('输入一个数：'))
print(the_ping(num))
