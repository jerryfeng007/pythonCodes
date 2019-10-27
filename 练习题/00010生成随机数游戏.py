import random

r = random.randint(1, 10)
print(r)

r2 = random.randrange(50)
print(r2)

# 随机数游戏
while True:
    num = eval(input('请输入一个数：'))
    if num == r:
        print('您猜对了')
        break
    elif num < r:
        print('再猜大一点')
        continue
    else:
        print('再猜小一点')
        continue
