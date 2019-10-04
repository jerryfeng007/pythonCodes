# 猜数字
import time
import random

times = 0

while True:
    if times != 0:
        print('开始吧！')
    else:
        play = input('想玩游戏吗？y/n')
        if play.lower() not in ('y', 'n'):
            print('必须输入y或者n')
            continue
        if play.lower() == 'n':
            print('好吧，你不想玩就退出了。')
            break

    a = random.randint(0, 100)
    print(a)

    s = time.time()
    print('开始时间：', s)

    while True:
        b = eval(input('输入一个数：'))

        if b > a:
            print('输入的大了，请再次输入')
            continue
        elif b < a:
            print('输入的小了，请再次输入')
            continue
        else:
            print(f'猜对了，这个数就是{b}')
            break

    e = time.time()
    print('结束时间：', e)
    t = e - s
    print('这一局耗时为：', t)

    if t < 15:
        print('你很聪明哦！')
    elif t < 25:
        print('你很一般哦！')
    else:
        print('你很笨笨哦！')

    play = input('再来一局？y/n')

    if play.lower() not in ('y', 'n'):
        print('没诚意就别玩了吧！')
        break
    if play.lower() == 'n':
        print('好吧，你不想玩就退出了。')
        break

    times += 1
