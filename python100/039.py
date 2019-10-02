# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# l = [1, 3, 5, 7, 9]
# l = [3, 2, 1]
l = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]

a = 7

# for i, v in enumerate(l):
#     if l[0] > l[-1]:
#         if a >= v:
#             l.insert(i, a)
#             break
#     else:
#         if a <= v:
#             l.insert(i, a)
#             break
# else:
#     l.append(a)
# print(l)

# 方法2
l.append(a)
l.sort()
print(l)
