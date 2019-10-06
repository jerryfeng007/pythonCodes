# 定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
# 例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。


# 方法1
def aa(l, d):
    return l[d:] + l[:d]


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(aa(l, 1))


# 方法2
def bb(l, d):
    for i in range(d):
        l.append(l.pop(0))  # 注意，这里必须是pop，因为l.pop()有返回值，如果是l.remove()返回值是None
    return l


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bb(l, 1))
