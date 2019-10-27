# 求100之内的素数/质数

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


# 判断给定的数是质数
b = eval(input('输入一个数：'))
if not b >= 2:
    raise Exception('必须大于等于2')
for k in range(2, b):
    if b % k == 0:
        print('不是质数')
        break
else:
    print('是质数')
