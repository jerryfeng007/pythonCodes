# 输入三个整数x,y,z，请把这三个数由小到大输出。

a = eval(input('请输入三个整数：'))

b = sorted(a)

for i in b:
    print(i)
