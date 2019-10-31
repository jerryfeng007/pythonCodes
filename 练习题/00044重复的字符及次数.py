# 给定一个列表，找出列表中有重复的字符，并打印出他们的次数

l = ['abc', 'ab', 'bc', 'abc', 'dd', 'bc', 'ee', 'bc', 'ss', 'bc']

# 方法1
s = set(l)
for i in s:
    if l.count(i) != 1:
        print(i, l.count(i))

print('-------------------------------')

# 方法2 ---- 不可取，有重复的
for i in l:
    if l.count(i) != 1:
        print(i, l.count(i))


print('--------------------------------')

# 方法3
d = {}
for i in l:
    if l.count(i) != 1:
        if i not in d:
            d[i] = 0
        d[i] += 1
print(d)
