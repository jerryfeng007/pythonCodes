# 流程控制三兄弟：if for while ---------------------------------------------------------------------------------------------
# if语句：注意，要减少不必要的判断，比如以下：
a = 5
if a > 4:
    print('a大于4')
elif a > 3:
    print('a大于3')
else:
    print('a大于2')

# 第一种方式，满足if条件之后，就不会再判断elif和else了
'''
if xxx:
    xxxx
elif xxx:
    xxxx
else:
    xxxx
'''

# 第二种方式，每一个if都会判断
'''
if xxx:
    xxxx
if xxxxx:
    xxxxxx
if xxxxx:
    xxxxxxx
'''

# for循环
# 使用range
for i in range(3):
    print(i)

for i in range(2, 10):
    print(i, end='_')  # print函数，使用了end

print()  # 换行

# 不使用range
for i in [1, 2, 3]:
    print(i, end=' ')

print()   # 换行

# 可迭代对象
# 字符串、列表、元组、集合

# 特殊的for循环
a = [(1, 2), (3, 4)]
# 方式1
for i in a:
    print(i[0])

# 方式2  类似序列解包赋值？ a, b = 1, 2
for i, j in a:
    print('i=', i, 'j=', j)

# 嵌套循环
for i in range(3):
    for j in range(2):
        print(i, j)

# while循环---------------------------------------------------------------------------------------------------------------
'''
while循环是深度循环，只要条件满足就会一直执行下去，直到不满足；for循环是广度循环
如果while循环一直满足条件，那么就成了死循环
'''
# 死循环
# while True:
#     print('111111111111')

# 普通循环
i = 0
while i < 5:
    print(i)
    i += 1

# 流程控制词：pass  continue   break--------------------------------------------------------------------------------------------
# pass  占位
for i in range(3):
    pass

# break 跳出循环
name = 'jerry'
for i in name:
    if i == 'e':
        break
    print(i)

a = 0
while a < 5:
    a += 1
    if a == 3:
        break
    print(a)

# continue # 结束本次循环，继续进行下一次循环
name = 'jerry'
for i in name:
    if i == 'e':
        continue
    print(i)

a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)