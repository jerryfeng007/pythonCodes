# 定义一个列表，并将该列表元素复制到另外一个列表上。

import copy

l = [1, 2, [3, 4, 5]]

l2 = l.copy()
print(l2)

l3 = copy.deepcopy(l)
print(l3)

l4 = l
print(l4)

l5 = [i for i in l]
print(l5)

l6 = list(l)
print(l6)

l7 = l[::]
print(l7)

l8 = []
l8.extend(l)
print(l8)
