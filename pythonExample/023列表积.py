# 列表积

# 方法1
import functools

l = [2, 3, 4, 5]

ji = functools.reduce(lambda x, y: x*y, l)
print(ji)


# 方法2
ji2 = l[0]
for i in l[1:]:
    ji2 = ji2 * i
print(ji2)
