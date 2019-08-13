print('----------------------------------流程控制三兄弟：if for while------------------------------------------------')

# if语句
# 方式1----互斥
'''
if xxx:
    xxxx
elif xxx:
    xxxx
else:
    xxxx
'''

# 方式2----每个if都会判断
'''
if xxx:
    xxxx
if xxxxx:
    xxxxxx
if xxxxx:
    xxxxxxx
'''

print('----------------------------------for循环------------------------------------------------')

# 使用range
for i in range(3):
    print(i)

for i in range(1, 4):
    print(i)

# 不使用range
for i in [1, 2, 3]:
    print(i, end=' ')  # 不换行

print()

# 特殊的for循环
a = [(1, 2), (3, 4)]
# 方式1
for i in a:
    print(i[0], i[1])

# 方式2
for i, j in a:
    print(i, j)

# 嵌套循环
for i in range(3):
    for j in range(2):
        print(i, j)

print('----------------------------------while循环------------------------------------------------')

'''
while循环是深度循环，只要条件满足就会一直执行下去，直到不满足
for循环是广度循环
如果while循环一直满足条件，那么就成了死循环
'''
# 普通循环
i = 0
while i < 5:
    print(i)
    i += 1

print('--------------------------------------流程控制词：pass  continue   break---------------------------------------')

# pass
for i in range(3):
    pass

# break 跳出最近的一层循环
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
