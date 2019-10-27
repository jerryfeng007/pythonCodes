while True:
    a, b, c = eval(input('输入三角形的三条边，以英文逗号分隔：'))
    if not (a + b > c and a + c > b and b + c > a):
        print('输入的三边不可能构成三角形，请重新输入！')
        continue

    # 计算
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('%.2f' % area)
    break
