print('----------------------------------流程控制三兄弟：if for while------------------------------------------------')

print('----------------------------------if语句------------------------------------------------')

# 互斥
'''
if xxx:
elif xxx:
else:
'''

# 每个if都会判断
'''
if xxx:
if xxx:
if xxx:
'''

# 判断条件的省略用法：
'''
if a:
    print(True)
else:
    print(False)

如果a是以下类型： 
string: 空string---false
int:    0----------false
bool:   false------false
list:   []---------false
tuple:  ()---------false
dict:   {}---------false
set:    set()------false
object: None-------false
'''

print('----------------------------------for循环------------------------------------------------')

# 使用range
for i in range(3):
    print(i)

for i in range(1, 4):
    print(i)

l = [1, 2, 3]
for i in range(len(l)):
    print(i, l[i])

# 不使用range
for i in [1, 2, 3]:
    print(i)

# for循环 + if判断
l = [1, 2, 3]
for i in range(len(l)):
    if i < 2:
        print(i, l[i])

print('----------------------------------enumerate()函数-----------------------------------------------')

# 使用内置函数enumerate，上面的例子也可以写成：
for index, item in enumerate(l):
    if index < 2:
        print(index, item)

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

print('--------------------------------------条件与循环的复用---------------------------------------')

# 例1
# 有if，有else
i = 5
if i >= 3:
    print('大于等于3')
else:
    print('小于3')

# 将条件与循环并作一行
print('大于等于3') if i >= 3 else print('小于3')

# 例2
# 有if，有else，有循环
l = [1, 2, 3]
for i in l:
    if i >= 2:
        print('大于等于2')
    else:
        print('小于2')

# 将条件与循环并作一行
[print('大于等于2') if i >= 2 else print('小于2') for i in l]  # 注意要有中括号

# 例3
# 有if，没有else，有循环
l = [1, 2]
for i in l:
    if i > 1:
        print('大于1')

# 将条件与循环并作一行
[print('大于1') for i in l if i > 1]  # 注意要有中括号

# 例4
# 普通写法
l = [1, 2, 3, 4]
l1 = []
for i in l:
    if i > 2:
        l1.append(i)
    else:
        l1.append(i * 3)
print(l1)

# 将条件与循环并作一行
l2 = [i if i > 2 else i * 3 for i in l]  # 这就成了列表推导式
print(l2)
