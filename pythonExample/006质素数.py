# 判断质数

# a = 11

for a in range(2, 100):
    for i in range(2, a):
        if a % i == 0:
            # print('不是质数')
            break
    else:
        print('质数', a)
