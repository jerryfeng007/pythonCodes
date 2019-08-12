# 元组的定义
# 方式1
tuple1 = (1, 2, 3, 4)

# 方式2，把字符串转化为元组
tuple2 = tuple('abcde')
print(tuple2)

# 把元组转化为字符串，跟列表转化为字符串一样，也是用''.join()函数
s = ''.join(tuple2)
print(s)

# 元组的连接
tuple10 = (1, 2, 3, 4)
tuple2 = (5, 6, 7)
tuple3 = tuple10 + tuple2
print(tuple3)

# 元组的索引
tuple3 = tuple('hello')
print(tuple3[0])
print(tuple3[-1])
print(tuple3[:])
print(tuple3[::])
print(tuple3[::2])
print(tuple3[::-1])  # 反转
print(tuple3[4:1:-1])
print(tuple3[-1:-4:-1])
print(tuple3[4:1:1])
'''
列表的索引，和字符串的索引不完全一样，因为可以通过列表的索引来修改列表
元组的索引，和字符串的索引完全一样，因为字符串和元组都是不可修改的
'''
# 元组的排序 sorted()
tuple9 = (3, 1, 0, -4, 6)
print(sorted(tuple9))
print(tuple9)

# 元组的特性
# 不加括号，默认是元组
a = 1, 2
print(a)

# 如果元组只有一个元素，也需要加逗号
b = 1
c = 1,
e = (1,)
print(b, c, e)

# max min sum
tuple8 = (1, 2, 3)
print(max(tuple8))
print(min(tuple8))
print(sum(tuple8))

# 元组的方法
tuple4 = ('a', 'b', 'c', 'a', 'e')
print(tuple4.count('a'))
print(tuple4.index('a'))  # 返回索引，如果不存在则报错

'''
字符串有index和find方法，列表和元组只有index
index如果找不到会报错，find找不到返回-1
'''