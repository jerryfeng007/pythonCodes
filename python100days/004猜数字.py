import random
a = random.randint(1, 100)
# print(a)

counter = 0
while True:
    counter += 1
    b = int(input('请猜这个数是多少：'))
    if b == a:
        print('恭喜你，猜对了')
        print('您总共猜了%d次' % counter)
        break
    elif b > a:
        print('大了')
        continue
    else:
        print('小了')
        continue
