"""
定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
"""

l = [1, 2, 3, 4, 5]

# 把 1 2 两个数翻转到尾部，变为 [3, 4, ,5, 1, 2]


def fanzhuan(l, d):
    return l[d:] + l[:d]


print(fanzhuan(l, 1))
print(fanzhuan(l, 2))
print(fanzhuan(l, 3))
print(fanzhuan(l, 4))
print('--------------------------------------------------')


# 方法2
def fanzhuan2(l, d):
    for i in range(d):
        l.append(l.pop(0))
    return l


# print(fanzhuan2(l, 1))
# print(fanzhuan2(l, 2))
print(fanzhuan2(l, 3))
# print(fanzhuan2(l, 4))
print('--------------------------------------------------')


# 方法3
def fanzhuan3(l, d):
    s1 = l[:d]
    s2 = l[d:]
    s2.extend(s1)
    return s2


l = [1, 2, 3, 4, 5]
print(fanzhuan3(l, 3))
