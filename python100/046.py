# 求输入数字的平方，如果平方运算后小于 50 则退出。

while True:
    a = eval(input('请输入一个数字：'))
    s = a ** 2
    print(s)
    if s < 50:
        exit()
