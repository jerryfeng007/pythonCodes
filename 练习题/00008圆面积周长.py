from math import pi


def zc_area(r):
    return '%.2f' % (2 * pi * r), '%.2f' % (pi * (r**2))


r = eval(input('请输入圆的半径：'))
zc, area = zc_area(r)
print(zc, area)
